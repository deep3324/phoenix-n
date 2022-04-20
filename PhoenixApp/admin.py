from django.contrib import admin
from PhoenixApp.models import ArtCraft, Card, ChooseATechField, Git, Membership,  Review, Contact, PreviousEvent, UpComingEvent, Result, Blog, Gallery, appDevelopment, backendDevelopment, gswcw, pythonDevelopment, quizomania, gswcpM, robonixIntro, webDevelopment
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Review)
admin.site.register(Git)
admin.site.register(Contact)
admin.site.register(PreviousEvent)
admin.site.register(UpComingEvent)
admin.site.register(Result)
admin.site.register(Gallery)
admin.site.register(ArtCraft)
admin.site.register(quizomania)
admin.site.register(Membership)
admin.site.register(Card)
admin.site.register(ChooseATechField)


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)


class gswcpResource(resources.ModelResource):
    class Meta:
        model = gswcpM

@admin.register(gswcpM)
class gswcpAdmin(ImportExportModelAdmin):
    resource_class = gswcpResource
    list_display = ("name", "department", "college",
                    "session", "contact",)
    search_fields = ['name',]

class gswcwResource(resources.ModelResource):
    class Meta:
        model = gswcw

@admin.register(gswcw)
class gswcwAdmin(ImportExportModelAdmin):
    resource_class = gswcwResource
    list_display = ("name", "email","department", "college",
                    "session", "contact",)
    search_fields = ['name','email']

class robonixIntroResource(resources.ModelResource):
    class Meta:
        model = robonixIntro

@admin.register(robonixIntro)
class robonixIntroAdmin(ImportExportModelAdmin):
    resource_class = robonixIntroResource
    list_display = ("name", "email","department", "college",
                    "session", "contact",)
    search_fields = ['name','email']

class appDevelopmentResource(resources.ModelResource):
    class Meta:
        model = appDevelopment

@admin.register(appDevelopment)
class appDevelopmentAdmin(ImportExportModelAdmin):
    resource_class = appDevelopmentResource
    list_display = ("name", "email","department", "college",
                    "session", "contact","prior")
    search_fields = ['name','email']
class webDevelopmentResource(resources.ModelResource):
    class Meta:
        model = webDevelopment

@admin.register(webDevelopment)
class webDevelopmentAdmin(ImportExportModelAdmin):
    resource_class = webDevelopmentResource
    list_display = ("name", "email","department", "college",
                    "session", "contact","prior")
    search_fields = ['name','email']


class pythonDevelopmentResource(resources.ModelResource):
    class Meta:
        model = pythonDevelopment

@admin.register(pythonDevelopment)
class pythonDevelopmentAdmin(ImportExportModelAdmin):
    resource_class = pythonDevelopmentResource
    list_display = ("name", "email","department", "college",
                    "session", "contact","prior")
    search_fields = ['name','email']

class backendDevelopmentResource(resources.ModelResource):
    class Meta:
        model = backendDevelopment

@admin.register(backendDevelopment)
class backendDevelopmentAdmin(ImportExportModelAdmin):
    resource_class = backendDevelopmentResource
    list_display = ("name", "email","department", "college",
                    "session", "contact","prior")
    search_fields = ['name','email']
