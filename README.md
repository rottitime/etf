This purpose of this project is to create an "Evaluation Registry" for the Evaluation Task Force (ETF). This will allow researchers across government to register evaluations at an early stage, and will allow users to search the registry for evaluations in their chosen policy area.

## How to run

To run this project:

    docker-compose up --build --force-recreate web

open http://localhost:8010/

To populate the database with fake data:

    docker-compose run web python manage.py add_fake_data

or

    make add-fake-data

\*_Note: This requires at least one user to be created to run correctly_

To reset the database:

    make reset-db

To check for syntax errors:

    make check-python-code

To update the requirement lockfiles:

    make update-requirements

To run tests:

    make test

To update organisations data:

    python scripts/scrape_organisations.py

And move the formatted data to the `enums.py` file.

# Frontend development

Open the `web` folder for all the following

## How to run the project

```
npm ci
npm run dev
```

> Note: You will still need the previous steps to have ETF running on docker (http://localhost:8010/) to preview the site as you update any CSS and JS

## How to generate the static build

```
npm run build
```

## Uploading initial data

Data to initially populate the registry has been provided in a specified Excel format.

Run this locally to find errors before running in the development/testing/live environments.

Save the data file in the folder `etf/data` then run:

```
docker-compose run web python manage.py upload_rsm_data --filename <name-of-excel-file.xlsx>
```
