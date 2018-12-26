# {{ cookiecutter.project_name }}

{%- if cookiecutter.repo_location == 'github.com' %}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Build Status](https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }})
[![codecov](https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](http://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/)
{%- elif cookiecutter.repo_location == 'gitlab.com' %}
![Pipeline status](https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/badges/master/build.svg)
{%- endif %}

{{ cookiecutter.project_short_description }}

## Usage

Coming soon...

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://gitlab.com/fhightower-templates/python-project-template).
