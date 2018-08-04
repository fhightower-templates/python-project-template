#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `{{ cookiecutter.project_slug }}` module."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import sys
import unittest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
import docopt
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


{% if cookiecutter.use_pytest == 'y' -%}
@pytest.fixture
def absolute_path():
    """Return an absolute path (which is useful for running tests)."""
    # return os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(absolute_path, response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


{%- if cookiecutter.command_line_interface|lower == 'docopt' %}
@pytest.fixture
def command_line_args():
    """Function to simulate command line arguments using docopt."""
    args = dict()

    # TODO: Add command line arguments here (see: https://github.com/docopt/docopt#api)

    return args


def test_command_line_interface(command_line_args):
    """Test the command line usage of this project."""
    # TODO: Add more robust testing here
    with pytest.raises(docopt.DocoptExit) as exc_info:
        cli.main()

    # get the error message
    error_message = exc_info.value
    # make sure the error message contains the expected usage output
    assert "Usage:" in str(error_message)

{%- endif %}
{% else %}
class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass
{% if cookiecutter.command_line_interface|lower == 'docopt' %}
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert '{{ cookiecutter.project_slug }}.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
{%- endif %}