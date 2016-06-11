from django.contrib import admin
from registration.models import *

class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TestAdmin(admin.ModelAdmin):
   pass
admin.site.register(Test,TestAdmin)


class TechTestAdmin(admin.ModelAdmin):
 pass
admin.site.register(TechTest, TechTestAdmin)
#class HRTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(HRTest, HRTestAdmin)
#class QuantTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(QuantTest, QuantTestAdmin)
#class VerbTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(VerbTest, VerbTestAdmin)
#class ReasonTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(ReasonTest, ReasonTestAdmin)
#class EligTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(EligTest, EligTestAdmin)
#class AptitudeTestAdmin(admin.ModelAdmin):
 #pass
#admin.site.register(AptitudeTest, AptitudeTestAdmin)