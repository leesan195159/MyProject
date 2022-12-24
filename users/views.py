import json
import jwt
import bcrypt

from django.views import View
from django.http  import JsonResponse
from django.forms import ValidationError
from datetime     import datetime, timedelta

from django.conf       import settings
from cores.validations import validate_email, validate_password
from users.models      import User


class SignIn(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            name     = data['user_name']
            email    = data['email']
            password = data['password']

            validate_email(email)
            validate_password(password)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Already_Exist_Email'}, status=402)

            User.objects.create(
                name     = name,
                email    = email,
                password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode(('utf-8'))
            )
            return JsonResponse({'message': 'Success'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'Key_Error'}, status=401)
        except ValidationError:
            return JsonResponse({'message': 'Validation_Error'}, status=403)


class LogIn(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)

            validate_email(email)
            validate_password(password)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'Invalid_Password'}, status=401)

            token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(days=1)},
                             settings.SECRET_KEY,
                             settings.ALGORITHM)
            return JsonResponse({'message': 'Success', 'token': token}, status=200)

        except KeyError:
            return JsonResponse({'message': 'Key_Error'}, status=401)
        except ValidationError:
            return JsonResponse({'message': 'Validation_Error'}, status=403)
        except User.DoesNotExist:
            return JsonResponse({'message': 'Does_Not_Exist_Error'}, status=407)
