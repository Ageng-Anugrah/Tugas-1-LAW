from django.contrib import admin
from .models import Oauth

# Register your models here.
class OauthAdmin(admin.ModelAdmin):
    readonly_fields = ('last_hit',)

admin.site.register(Oauth,OauthAdmin)