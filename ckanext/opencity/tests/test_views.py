"""Tests for views.py."""

import pytest

import ckanext.opencity.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "opencity")
@pytest.mark.usefixtures("with_plugins")
def test_opencity_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("opencity.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, opencity!"
