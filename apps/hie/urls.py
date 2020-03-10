from django.conf.urls import url
from django.contrib import admin
from .views import get_authorization, approve_authorization, refresh_patient_data, cda2fhir_patient_data
from .api_views import (get_cda_in_json, get_cda_raw,
                        get_cda_in_json_test, get_cda_raw_test,
                        get_patient_fhir_content,
                        get_patient_fhir_content_test,
                        get_fhir_resource_bundle_test,
                        get_fhir_resource_bundle,
                        get_fhir_vital_signs_bundle_test,
                        get_fhir_vital_signs_bundle,
                        get_fhir_lab_results_bundle_test,
                        get_fhir_lab_results_bundle,
                        )

admin.autodiscover()

urlpatterns = [


    url(r'api/fhir/stu3/VitalSigns/$', get_fhir_vital_signs_bundle,
        name='get_fhir_vital_signs_bundle'),

    url(r'api/test/fhir/stu3/VitalSigns/$', get_fhir_vital_signs_bundle_test,
        name='get_fhir_vital_signs_bundle_test'),

    url(r'api/fhir/stu3/LabResults/$', get_fhir_lab_results_bundle,
        name='get_fhir_lab_results_bundle'),

    url(r'api/test/fhir/stu3/LabResults/$', get_fhir_lab_results_bundle_test,
        name='get_fhir_lab_results_bundle_test'),


    url(r'api/fhir/stu3/(?P<fhir_resource_name>[^/]+)/$', get_fhir_resource_bundle,
        name='get_fhir_resource_bundle'),

    url(r'api/test/fhir/stu3/(?P<fhir_resource_name>[^/]+)/$', get_fhir_resource_bundle_test,
        name='get_fhir_resource_bundle_test'),

    url(r'cda2fhir$', cda2fhir_patient_data, name='cda2fhir_patient_data'),
    url(r'refresh-patient-data$', refresh_patient_data,
        name='hie_refresh_patient_data'),
    url(r'get-authorization$', get_authorization, name='hie_get_authorization'),
    url(r'approve-authorization$', approve_authorization,
        name='approve_authorization'),
    url(r'api/cda-in-json$', get_cda_in_json, name='get_cda_in_json'),
    url(r'api/cda$', get_cda_raw, name='get_cda_raw'),
    url(r'api/cda-in-json-test$', get_cda_in_json_test,
        name='get_cda_in_json_test'),
    url(r'api/cda-test$', get_cda_raw_test, name='get_cda_raw_test'),
    url(r'api/fhir/stu3/Patient/\$everything$',
        get_patient_fhir_content, name='get_patient_fhir_content'),
    url(r'api/test/fhir/stu3/Patient/\$everything$',
        get_patient_fhir_content_test, name='get_patient_fhir_content_test'),

]
