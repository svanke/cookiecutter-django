# -*- coding: utf-8 -*-

"""
This module is called after project is created.

It does the following:
1. Generates and saves random secret key
2. Removes docker files if it is not used

A portion of this code was adopted from Django's standard crypto functions and
utilities, specifically:
https://github.com/django/django/blob/master/django/utils/crypto.py
# Copy entrypoint.sh

# Adds our application code to the image
And from pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import secrets
import shutil
import string

# CHANGEME mark
CHANGEME = '__CHANGEME__'

# Get the root project directory
PROJECT_NAME = 'src'
REPO_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_DIRECTORY = os.path.join(REPO_DIRECTORY, PROJECT_NAME)

print(PROJECT_DIRECTORY)


def _get_random_string(length=50):
    """
    Returns a securely generated random string.

    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits

    >>> secret = _get_random_string()
    >>> len(secret)
    50

    """
    punctuation = string.punctuation.replace(
        '"', '',
    ).replace(
        "'", '',
    ).replace(
        '\\', '',
    ).replace(
        '$', '',  # see issue-271
    )

    chars = string.digits + string.ascii_letters + punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def _create_secret_key(config_path):
    # Generate a SECRET_KEY that matches the Django standard
    secret_key = _get_random_string()

    with open(config_path, 'r+') as config_file:
        # Replace CHANGEME with SECRET_KEY
        file_contents = config_file.read().replace(CHANGEME, secret_key, 1)

        # Write the results to the file:
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def print_futher_instuctions():
    """Shows user what to do next after project creation."""
    print()
    print('Your project {0} is created.'.format(PROJECT_NAME))
    print('Now you can start working on it:')
    print()
    print('    cd {0}'.format(PROJECT_NAME))


def copy_local_configuration():
    """
    Handler to copy local configurat# Copy entrypoint.sh

# Adds our application code to the image

    It is copied from ``.template`` files to the actual files.
    """
    secret_template = os.path.join(
        PROJECT_DIRECTORY, 'config', 'settings', '.env.template',
    )
    secret_config = os.path.join(
        # PROJECT_DIRECTORY, 'config', 'settings', '.env.dev',
        PROJECT_DIRECTORY,
    )
    shutil.move(secret_template, secret_config)
    _create_secret_key(secret_config)


copy_local_configuration()
print_futher_instuctions()
