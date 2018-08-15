#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `{{ cookiecutter.project_slug }}` CLI."""

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
from click.testing import CliRunner
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' -%}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


def test_{{ cookiecutter.project_slug }}_cli():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--version'])
    assert result.exit_code == 0
    assert result.output == '{{ cookiecutter.project_slug }} version: {{ cookiecutter.version }}\n'
