"""{{cookiecutter.project_name}} CLI interface."""

import click

from .__init__ import __version__ as VERSION


@click.command()
@click.option('--version', is_flag=True, help='Print the version of the package')
def main(version):
    """CLI interface for {{cookiecutter.project_slug}}"""
    if version:
        print(f'{{ cookiecutter.project_slug }} version: {VERSION}')


if __name__ == "__main__":
    main()
