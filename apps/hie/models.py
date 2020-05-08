from django.db import models
from django.contrib.auth import get_user_model
from ..accounts.models import UserProfile
from .fhir_requests import get_converted_fhir_resource
from django.conf import settings
import json
# Copyright Videntity Systems Inc.
__author__ = "Alan Viars"


class HIEProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                db_index=True, null=False)
    organization_name = models.CharField(max_length=64, default=settings.APPLICATION_TITLE,
                                         blank=True)
    mrn = models.CharField(max_length=64, default='',
                           blank=True, db_index=True)
    stageuser_password = models.CharField(
        max_length=64, default='', blank=True)
    stageuser_token = models.CharField(max_length=64, default='', blank=True)
    data_requestor = models.CharField(max_length=64, default='ActualCBOUser', blank=True)
    terms_accepted = models.TextField(default='', blank=True)
    terms_string = models.TextField(default='', blank=True)
    user_accept = models.BooleanField(default=False, blank=True)
    terms_of_service = models.CharField(max_length=64, default='', blank=True)
    cda_content = models.TextField(default='', blank=True)
    cda_content_md5hash = models.CharField(max_length=64, default='', blank=True)
    consumer_directive_response = models.TextField(default='', blank=True)
    consumer_directive_response_code = models.TextField(default='', blank=True)
    activate_staged_user_response = models.TextField(default='', blank=True)
    activate_staged_user_response_code = models.TextField(default='', blank=True)
    patient_search_response = models.TextField(default='', blank=True)
    patient_search_response_code = models.TextField(default='', blank=True)
    get_cda_response = models.TextField(default='', blank=True)
    get_cda_response_code = models.TextField(default='', blank=True)
    cda2fhir_response = models.TextField(default='', blank=True)
    cda2fhir_response_code = models.TextField(default='', blank=True)
    fhir_content = models.TextField(default='', blank=True)
    fhir_content_embellish = models.TextField(default='', blank=True, help_text='Reserved for future use.')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        display = '%s %s (%s)' % (self.user.first_name,
                                  self.user.last_name,
                                  self.user.username)
        return display

    @property
    def flag_dont_connect(self):
        boundary = '0' * 64  # a zero-filled string the max length of the mrn
        return self.mrn and self.mrn <= boundary  # don't connect if mrn <= boundary

    @property
    def consent_to_share_data(self):
        if self.user_accept is True:
            return 1
        return 0

    @property
    def name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    @property
    def subject(self):
        up, g_or_c = UserProfile.objects.get_or_create(user=self.user)
        return up.subject

    @property
    def terms_string_stripped(self):
        return self.terms_string.strip('\\n').strip('\\t')

    @property
    def get_fhir_resource(self, fhir_resource_name):
        jc = json.loads(self.fhir_content)
        cv = get_converted_fhir_resource(jc, fhir_resource_name)
        print(cv)
        return cv
