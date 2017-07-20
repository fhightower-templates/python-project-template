# -*- coding: utf-8 -*-
"""{{cookiecutter.project_name}}.

Usage:
  # TODO: Add usage instructions here
  {{cookiecutter.project_slug}}.py ship new <name>...
  {{cookiecutter.project_slug}}.py ship <name> move <x> <y> [--speed=<kn>]
  {{cookiecutter.project_slug}}.py ship shoot <x> <y>
  {{cookiecutter.project_slug}}.py mine (set|remove) <x> <y> [--moored | --drifting]
  {{cookiecutter.project_slug}}.py (-h | --help)
  {{cookiecutter.project_slug}}.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  # TODO: Add options here
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""

from docopt import docopt

from .__init__ import __version__ as VERSION


def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    arguments = docopt(__doc__, version=VERSION)
    print(arguments)
    print("You can modify the output of the CLI by making changes to {{cookiecutter.project_slug}}.cli.main .")


if __name__ == "__main__":
    main()