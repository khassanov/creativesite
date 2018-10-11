from django.contrib import admin

from services.models import Service, About_us, Contact, Contact_form
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

class About_usAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}

class ContactFormAdmin(admin.ModelAdmin):
	list_filter = ('name', 'data')
	list_display = ('name', 'email', 'data')

admin.site.register(Service, ServiceAdmin)
admin.site.register(About_us, About_usAdmin)
admin.site.register(Contact)
admin.site.register(Contact_form, ContactFormAdmin)