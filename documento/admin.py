from django.contrib import admin

from documento.models import Documento, Pessoa


# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Documento)