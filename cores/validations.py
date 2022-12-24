import re

from django.forms import ValidationError

# 이메일  - 이메일 형식
# 비밀번호 - 최소 한개의 영문자 + 최소 한개의 숫자 + 최소 8자
EMAIL_REGEX    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PASSWORD_REGEX = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*_+])[A-Za-z\d!@#$%^&*()_+?&]{8,}$"


def validate_email(email):
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError('Invalid_Email')


def validate_password(password):
    if not re.match(PASSWORD_REGEX, password):
        raise ValidationError('Invalid_Password')
