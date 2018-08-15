#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `{{ cookiecutter.project_slug }}` module."""

import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


@pytest.fixture
def response():
    return "foo bar"


def test_{{ cookiecutter.project_slug }}_initialization():
    assert 1 == 1
