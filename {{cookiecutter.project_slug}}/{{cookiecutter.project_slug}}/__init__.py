try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version('{{ cookiecutter.project_slug }}')
except PackageNotFoundError:
    # package is not installed
    message = 'Unable to find a version number for "{{ cookiecutter.project_slug }}"; This is likely indicates the installation of this library failed. Please try re-installing it.'
    print(message)

__author__ = '''{{ cookiecutter.full_name }}'''
__email__ = '{{ cookiecutter.email }}'
