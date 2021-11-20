from django.contrib import admin
from .models import Contract, Sponsor, Student, University


admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(Contract)
admin.site.register(University)

