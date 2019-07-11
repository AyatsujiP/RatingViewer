from django.contrib import admin

# Register your models here.
from .models import Members, Ratings

admin.site.register([Members,Ratings])
