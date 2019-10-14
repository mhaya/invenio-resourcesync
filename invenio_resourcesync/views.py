# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 National Institute of Informatics.
#
# Invenio-ResourceSync is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that adds ResourceSync function to the platform."""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template, make_response, request, url_for
from flask_babelex import gettext as _

blueprint = Blueprint(
    'invenio_resourcesync',
    __name__,
    template_folder='templates',
    static_folder='static',
)

@blueprint.route("/.well-known/resourcesync")
def sourceDescription():
    template = render_template(
        "invenio_resourcesync/resourcesync.xml",
        request_url=url_for(request.url))
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response


@blueprint.route("/capabilitylist.xml")
def capabilitylist():
    template = render_template(
        "invenio_resourcesync/capabilitylist.xml",
        request_url=url_for(request.url))
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

@blueprint.route("/resourcelist.xml")
def resourcelist():
    template = render_template(
        "invenio_resourcesync/resourcelist.xml",
        request_url=url_for(request.url))
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response

@blueprint.route("/changelist.xml")
def changelist():
    template = render_template(
        "invenio_resourcesync/changelist.xml",
        request_url=url_for(request.url))
    response = make_response(template)
    response.headers['Content-Type'] = 'application/xml'
    return response