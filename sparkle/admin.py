from django.contrib import admin
from .conf import SYSTEM_PROFILES_VISIBLE
from .models import (
    Application, Version, SystemProfileReport, SystemProfileReportRecord,
)
from .forms import VersionAdminForm


class ApplicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = ('name', 'slug',)
    list_display_links = list_display


class VersionAdmin(admin.ModelAdmin):
    form = VersionAdminForm
    list_display = (
        'title', 'version', 'short_version', 'application', 'publish_at',
    )
    list_display_links = ('title',)
    list_filter = ('application', 'publish_at',)
    readonly_fields = ('created_at',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Version, VersionAdmin)


if SYSTEM_PROFILES_VISIBLE:
    class SystemProfileReportRecordInline(admin.TabularInline):
        model = SystemProfileReportRecord
        extra = 0
        max_num = 0
        readonly_fields = ('key', 'value')
        can_delete = False

    class SystemProfileReportAdmin(admin.ModelAdmin):
        inlines = (SystemProfileReportRecordInline,)

    class SystemProfileReportRecordAdmin(admin.ModelAdmin):
        list_display = ('key', 'value')
        list_filter = ('key',)

    admin.site.register(SystemProfileReport, SystemProfileReportAdmin)
    admin.site.register(
        SystemProfileReportRecord, SystemProfileReportRecordAdmin,
    )
