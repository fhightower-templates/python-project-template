{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
*******************************
{{ cookiecutter.project_name }}
*******************************

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}

.. image:: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}
        
.. image:: https://api.codacy.com/project/badge/Grade/6927955d30df40f395aa8adbd7b8bfe4
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

.. image:: https://pyup.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io
{% endif %}

Features
========

* TODO

Credits
=======

This package was created with Cookiecutter_ and fhightower's `Python project template`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Python project template`: https://github.com/fhightower-templates/python-project-template
