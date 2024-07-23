# from mozilla_django_oidc.auth import OIDCAuthenticationBackend
# from django.shortcuts import redirect
# from .models import Users

# class CustomOIDCBackend(OIDCAuthenticationBackend):
#     def create_user(self, claims):
#         email = claims.get('email')
#         if not Users.objects.filter(email=email).exists():
#             return redirect('/register')
#         return super().create_user(claims)
