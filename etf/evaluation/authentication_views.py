from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from etf.evaluation.views import MethodDispatcher
from . import models
from .email_handler import send_password_reset_email, verify_token, send_verification_email


@require_http_methods(["GET", "POST"])
class CustomLoginView(MethodDispatcher):
    def get(self, request):
        return render(request, "account/login.html")

    def post(self, request):
        password = request.POST.get("password", None)
        email = request.POST.get("login", None)
        print(password)
        print(email)
        if not password or not email:
            messages.error(request, "Please enter an email and password.")
            return render(request, "account/login.html", {})
        else:
            user = authenticate(request, email=email, password=password)
            if not user.verified:
                messages.error(request, "Please check your emails for a verification email, then try again.")
                return render(request, "account/login.html", {})
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "The email address or password you entered is incorrect.")
                return render(request, "account/login.html", {})


class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            try:
                validate_password(password1)
            except ValidationError as exc:
                for errors in exc.error_list:
                    for error in errors:
                        messages.error(request, error)
                return render(request, self.template_name)
            if password1 != password2:
                messages.error(request, "Passwords must match.")
                return render(request, self.template_name)
            if models.User.objects.filter(email=email).exists():
                messages.error(request, "Registration was unsuccessful.")
                return render(request, self.template_name)
            user = models.User.objects.create_user(email=email, password=password1)
            user.save()
            send_verification_email(user)
            response = render(request, "account/verify_email_sent.html", {})
            return response
        response = super().dispatch(request, *args, **kwargs)
        return response


@require_http_methods(["GET"])
class CustomVerifyUserEmail(MethodDispatcher):
    def get(self, request):
        user_id = request.GET.get("user_id")
        token = request.GET.get("code")
        if not models.User.objects.filter(pk=user_id).exists():
            return render(request, "account/verify_email_from_token.html", {"verify_result": False})
        verify_result = verify_token(user_id, token, "email-verification")
        if verify_result:
            user = models.User.objects.get(pk=user_id)
            user.verified = True
            user.save()
        return render(request, "account/verify_email_from_token.html", {"verify_result": verify_result})


@require_http_methods(["GET", "POST"])
class PasswordReset(MethodDispatcher):
    def get(self, request):
        return render(request, "account/password_reset.html", {})

    def post(self, request):
        email = request.POST.get("email")
        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            return render(request, "account/password_reset_done.html", {})
        send_password_reset_email(user)
        return render(request, "account/password_reset_done.html", {})


@require_http_methods(["GET", "POST"])
class PasswordChange(MethodDispatcher):
    password_reset_error_message = (
        "This link is not valid. It may have expired or have already been used. Please try again."
    )

    def get_token_request_args(self, request):
        user_id = request.GET.get("user_id", None)
        token = request.GET.get("code", None)
        valid_request = False
        if not user_id or not token:
            messages.error(request, self.password_reset_error_message)
        else:
            result = verify_token(user_id, token, "password_reset")
            if not result:
                messages.error(request, self.password_reset_error_message)
            else:
                valid_request = True
        return user_id, token, valid_request

    def get(self, request):
        user_id, token, valid_request = self.get_token_request_args(request)
        return render(request, "account/password_reset_from_key.html", {"valid": valid_request})

    def post(self, request):
        user_id, token, valid_request = self.get_token_request_args(request)
        pwd1 = request.POST.get("password1", None)
        pwd2 = request.POST.get("password2", None)
        if pwd1 != pwd2:
            messages.error(request, "Passwords must match.")
            return render(request, "account/password_reset_from_key.html", {"valid": valid_request})
        if not valid_request:
            messages.error(request, self.password_reset_error_message)
            return render(request, "account/password_reset_from_key.html", {"valid": valid_request})
        user = models.User.objects.get(pk=user_id)
        try:
            validate_password(pwd1, user)
        except ValidationError as e:
            for msg in e:
                messages.error(request, str(msg))
            return render(request, "account/password_reset_from_key.html", {"valid": valid_request})
        user.set_password(pwd1)
        user.save()
        return render(request, "account/password_reset_from_key_done.html", {})
