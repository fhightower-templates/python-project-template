"""Tests for `{{ cookiecutter.project_slug }}` CLI."""

{%- if 'Click' in cookiecutter.command_line_interface %}
import click
from click.testing import CliRunner
{%- endif %}

{% if 'Click' in cookiecutter.command_line_interface -%}
from {{ cookiecutter.project_slug }} import cli
{%- endif %}


def test_{{ cookiecutter.project_slug }}_cli():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}.cli.main' in result.output

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
