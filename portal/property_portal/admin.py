from django.contrib import admin
from .models import Rent, Buy, UserProfile

admin.site.register(Rent)
admin.site.register(Buy)
admin.site.register(UserProfile)
