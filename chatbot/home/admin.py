from django.contrib import admin
from home.models import account,appointment,sleephrs,lastemail
#,sleephrs,lastemail
# Register your models here.
admin.site.register(account)
admin.site.register(appointment)
admin.site.register(sleephrs)
admin.site.register(lastemail)