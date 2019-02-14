#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
# from ..models import UserProfile


__author__ = "Alan Viars"


def save_profile(backend, user, response, *args, **kwargs):
    # print("BACKEND!!!!!", backend.name)
    if backend.name == 'verifymyidentity-openidconnect':
        id_token = response.get('id_token', "")
        print("IDTOKEN", id_token)
        # profile, g_o_c = UserProfile.objects.get_or_create(user=user)
        # profile.patient_fhir_id = response.get('patient', "")
    # profile.save()
