import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)
        remove_file(os.path.join('tests', 'test_cli.py'))

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if '{{ cookiecutter.repo_location }}' == 'gitlab.com':
        remove_file('.travis.yml')

    if '{{ cookiecutter.repo_location }}' != 'gitlab.com':
        remove_file('.gitlab-ci.yml')
