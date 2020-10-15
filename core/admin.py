from django.contrib import admin
from core.models import School, Wihda, Exercise, Summary_wihda, Order_name, Modakira, Tadaroj, Year


class WihdaAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    list_filter = ('name', 'school')
    list_editable = ('name',)
    list_display_links = ('school',)
    search_fields = ('name',)


class Summary_wihdaAdmin(admin.ModelAdmin):
    list_display = ('name', 'wihda', 'order_name')
    list_filter = ('name', 'wihda')
    list_editable = ('name',)
    list_display_links = ('wihda',)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'wihda')
    list_filter = ('wihda', 'name', 'order_name')
    list_editable = ('name', 'short_name')
    list_display_links = ('wihda',)
    search_fields = ('name',)


admin.site.register(School)
admin.site.register(Wihda, WihdaAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Summary_wihda, Summary_wihdaAdmin)
admin.site.register(Order_name)
admin.site.register(Modakira)
admin.site.register(Tadaroj)
admin.site.register(Year)
