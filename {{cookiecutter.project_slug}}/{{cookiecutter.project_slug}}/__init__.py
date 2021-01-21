try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version('{{ cookiecutter.project_slug }}')
except PackageNotFoundError:
    message = 'Unable to find a version number for "{{ cookiecutter.project_slug }}". This likely means the library was not installed properly. Please try re-installing it.'
    print(message)

__author__ = '''{{ cookiecutter.full_name }}'''
__email__ = '{{ cookiecutter.email }}'

from {{cookiecutter.project_slug}} import *
