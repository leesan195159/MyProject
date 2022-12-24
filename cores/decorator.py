import jwt

from django.http import JsonResponse
from django.conf import settings
from users.models import User


def login_authorization(func):
    def wrapper(self, request, *args, **kargs):
        try:
            access_token = request.headers.get('Authorization')
            payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['id'])
            return func(self, request, *args, **kargs)

        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "Expired_Token"}, status=408)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'Invalid_Token'}, status=409)

        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid_User'}, status=407)

    return wrapper
