from django.contrib import admin

# Register your models here.
from space.models import Space, Host, Location, SpaceCategory, SpacePackage, SpacePackageSpecialPrice


class ListDisplayHost(admin.ModelAdmin):
    list_display = ("name", "phone")


class ListDisplayLocation(admin.ModelAdmin):
    list_display = ("city", "district", "name")


class ListDisplaySpaceCategory(admin.ModelAdmin):
    list_display = ("title",)


class ListDisplaySpace(admin.ModelAdmin):
    list_display = ("host", "name", "location", "activate")


class ListDisplaySpacePackage(admin.ModelAdmin):
    list_display = ("space", "name", "price")


class ListDisplaySpacePackageSpecialPrice(admin.ModelAdmin):
    list_display = ("package", "start_date", "end_date", "special_price")


admin.site.register(Host, ListDisplayHost)
admin.site.register(Location, ListDisplayLocation)
admin.site.register(SpaceCategory, ListDisplaySpaceCategory)
admin.site.register(Space, ListDisplaySpace)
admin.site.register(SpacePackage, ListDisplaySpacePackage)
admin.site.register(SpacePackageSpecialPrice, ListDisplaySpacePackageSpecialPrice)
