"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.opencity.logic import validators


def test_opencity_reauired_with_valid_value():
    assert validators.opencity_required("value") == "value"


def test_opencity_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.opencity_required(None)
