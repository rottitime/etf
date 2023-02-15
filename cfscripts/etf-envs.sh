#!/bin/bash

if [ $1 ]; then
    CF_SPACE=$1
fi

### What environments need SENTRY
sentry_envs=(
    prod
    develop
    staging
    pentest
)

### What environments need GOV NOTIFY
govuk_email_backend=(
    sandbox
)

live_notify_api=(
    staging
)


###############################################################################################
if [[ " ${sentry_envs[*]} " =~ " ${CF_SPACE} " ]]; then
  sentry=true
fi

if [[ " ${govuk_email_backend[*]} " =~ " ${CF_SPACE} " ]]; then
    gov_notify=true
fi
echo "GOV NOTIFY= ${gov_notify}"

if [[ " ${live_notify_api[*]} " =~ " ${CF_SPACE} " ]]; then
    live_api_key=true
fi

while read -r line; do
apps=$(echo $line | head -n1 | cut -d " " -f1)
if [ "$apps" != "Getting" ] && [ "$apps" != "name" ] && [ "$apps" ]; then
    cfapps+=($apps)
fi
done < <(./cf apps)

#remove proxy apps from list
for value in "${cfapps[@]}"
do
    if grep -q "proxy" <<< "$value"; then
        cfapps=("${cfapps[@]/$value}")
    fi
done

#Apply required variables
for value in "${cfapps[@]}"
do
    if grep -q "etf" <<< "$value"; then
        echo "Adding envs to: ${value}..........."
        if [ "$value" == "etf" ]; then
            $(./cf set-env ${value} DJANGO_SECRET_KEY ${PROD_DJANGO_SECRET_KEY} &> /dev/null)
        else
            $(./cf set-env ${value} DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY} &> /dev/null)
        fi
        if [ $gov_notify ] || [ "$value" == "etf" ]; then
            if [ $live_api_key ] || [ "$value" == "etf" ]; then
                $(./cf set-env ${value} GOVUK_NOTIFY_API_KEY ${LIVE_NOTIFY_API_KEY} &> /dev/null)
            else
                $(./cf set-env ${value} GOVUK_NOTIFY_API_KEY ${TEAM_NOTIFY_API_KEY} &> /dev/null)
            fi

            $(./cf set-env ${value} EMAIL_BACKEND_TYPE GOVUKNOTIFY &> /dev/null)
            $(./cf set-env ${value} GOVUK_NOTIFY_PLAIN_EMAIL_TEMPLATE_ID ${NOTIFY_PLAIN_EMAIL_TEMPLATE_ID} &> /dev/null)
        else
            $(./cf set-env ${value} EMAIL_BACKEND_TYPE CONSOLE &> /dev/null)
        fi

        if [ $sentry ]; then
            $(./cf set-env ${value} SENTRY_DSN ${SENTRY_DSN}  &> /dev/null)
            $(./cf set-env ${value} SENTRY_ENVIRONMENT ${CF_SPACE} &> /dev/null)
        fi
    fi
done


# for value in "${cfapps[@]}"
# do
#     if grep -q "etf" <<< "$value"; then
#         echo "Starting ${value}....."
#         $(./cf restage ${value} &> /dev/null)
#     fi
# done
