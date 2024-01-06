from django.contrib import admin

from sistema.models import Team, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Team)