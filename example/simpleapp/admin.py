from django.contrib import admin

from .models import SimpleModel, LookupModel, TabularModel, StackedModel, NoInlineModel


class LookupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_per_page = 5

admin.site.register(LookupModel, LookupAdmin)


class TabularModelInline(admin.TabularInline):
    model = TabularModel


class StackedModelInline(admin.StackedInline):
    model = StackedModel


class NoInlineModelInline(admin.StackedInline):
    model = NoInlineModel
    extra = 0


class SimpleModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_field': ('char_field',)}
    search_fields = ('char_field',)
    list_display = ('char_field', 'integer_field', 'decimal_field', 'float_field', 'boolean_field')
    list_display_links = ('char_field', 'integer_field', )
    fieldsets = (
        (None, {
            'fields': ('char_field', 'slug_field', 'email_field', 'text_field'),
            'classes': ('wide', )
        }),
        ("Numerical Fields", {
            'description': "These fields are numerical in nature.",
            'fields': ('biginteger_field', 'integer_field', 'positiveinteger_field', 'smallinteger_field', 'possmallinteger_field', 'decimal_field', 'float_field', 'csi_field'),
        }),
        ("Boolean Fields", {
            'fields': ('boolean_field', 'nullboolean_field')
        }),
        ("Temporal Fields", {
            'fields': ('date_field', 'time_field', 'datetime_field'),
        }),
        ("File-based Fields", {
            'fields': ('file_field', 'filepath_field', 'image_field'),
        }),
        ("Misc Fields", {
            'fields': ('ipaddress_field', 'genericipaddress_field', 'url_field'),
            'classes': ('collapse', ),
        }),
        ("Related Fields", {
            'fields': ('foreignkey_field', 'manytomany_horiz', 'manytomany_vert')
        })
    )
    raw_id_fields = ("foreignkey_field", )
    filter_vertical = ("manytomany_vert", )
    filter_horizontal = ("manytomany_horiz", )
    inlines = (TabularModelInline, StackedModelInline, NoInlineModelInline)


admin.site.register(SimpleModel, SimpleModelAdmin)
