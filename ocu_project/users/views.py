from django.http.response import JsonResponse
from ocu.libs import validate_email
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from .models import User
import json
from django.contrib import auth
from rest_framework.authtoken.models import Token


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    response = {}
    request_body = json.loads(request.body)
    email = request_body["email"]
    password = request_body["password"]
    if not validate_email(email):
        print("Enter a valid email.")
    user = None
    try:
        user = auth.authenticate(email=email.lower(), password=password)
        if user is not None:
            auth.login(request, user)
            print("user login successful.")
            token = Token.objects.get_or_create(user=user)[0].key
            print("Token: %s" % token)
        else:
            print("user login failed.")
    except BaseException as e:
        raise ValidationError({"400": f"{str(e)}"})
