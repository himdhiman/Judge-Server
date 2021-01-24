from django.contrib import admin
from problem import models
# Register your models here.

admin.site.register([models.Tags, models.Problem, models.UploadTC])