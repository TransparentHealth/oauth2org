from django.contrib import admin

from apps.fhir.bluebutton.models import (Crosswalk,
                                         FhirServer)


class CrosswalkAdmin(admin.ModelAdmin):
    list_display = ('user', 'fhir_id', 'fhir_source')
    search_fields = ('user', 'fhir_id', 'fhir_source')


class FhirServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'shard_by', 'fhir_url')
    search_fields = ('name', 'fhir_url')


admin.site.register(Crosswalk, CrosswalkAdmin)
admin.site.register(FhirServer, FhirServerAdmin)
