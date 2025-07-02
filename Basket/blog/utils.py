import random
from django.core.mail import send_mail
from .models import EmailVerificationCode

def send_verification_email(email):
    # Random 6 rəqəmli kod yaradılır
    code = str(random.randint(100000, 999999))

    EmailVerificationCode.objects.update_or_create(
        email=email,
        defaults={'code': code}
    )

    send_mail(
        subject='Email Doğrulama Kodu',
        message=f'Sənin doğrulama kodun: {code}',
        from_email='ttanriverdiyev02@gmail.com',
        recipient_list=[email],
        fail_silently=False,
    )