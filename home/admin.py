from django.contrib import admin
from .models import MissingPerson
from .models import FoundPerson

admin.site.register(MissingPerson)
admin.site.register(FoundPerson)
