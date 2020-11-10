from django.contrib import admin
from .models import Categories, City,Country, Pictures, TransportType ,Trips,Packages, Logs, Status,Deals
# Register your models here.

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Categories)
admin.site.register(TransportType)
admin.site.register(Trips)
admin.site.register(Logs)
admin.site.register(Status)
admin.site.register(Deals)

class PicturesAdmin(admin.StackedInline):
    model = Pictures

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    inlines = [PicturesAdmin]

    class Meta:
       model = Pictures

@admin.register(Pictures)
class PicturesAdmin(admin.ModelAdmin):
    pass