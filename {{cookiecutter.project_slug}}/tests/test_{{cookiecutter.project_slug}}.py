#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `{{ cookiecutter.project_slug }}` module."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def test_{{ cookiecutter.project_slug }}_initialization():
    assert 1 == 1
