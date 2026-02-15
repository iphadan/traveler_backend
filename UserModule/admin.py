from django.contrib import admin
from .models import User, Account, Address, EmailVerification
 # Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Address)
admin.site.register(EmailVerification)