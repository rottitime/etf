from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Evaluation)
admin.site.register(models.Intervention)
admin.site.register(models.OutcomeMeasure)
admin.site.register(models.OtherMeasure)
