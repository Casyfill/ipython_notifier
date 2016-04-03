#!/usr/bin/env/python
"""Installation script
Version handling borrowed from geopandas project.
"""

import sys
import os
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LONG_DESCRIPTION = """Simple notifier to decorate your long functions
"""

MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''
if os.environ.get('READTHEDOCS', False) == 'True':
    INSTALL_REQUIRES = []
else:
    INSTALL_REQUIRES = ['pync']

FULLVERSION = VERSION
if not ISRELEASED:
    FULLVERSION += '.dev'
    try:
        import subprocess
        try:
            pipe = subprocess.Popen(["git", "rev-parse", "--short", "HEAD"],
                                    stdout=subprocess.PIPE).stdout
        except OSError:
            # msysgit compatibility
            pipe = subprocess.Popen(
                ["git.cmd", "describe", "HEAD"],
                stdout=subprocess.PIPE).stdout
        rev = pipe.read().strip()
        # makes distutils blow up on Python 2.7
        if sys.version_info[0] >= 3:
            rev = rev.decode('ascii')

        FULLVERSION = '%d.%d.%d.dev-%s' % (MAJOR, MINOR, MICRO, rev)

    except:
        warnings.warn("WARNING: Couldn't get git revision")
else:
    FULLVERSION += QUALIFIER


def write_version_py(filename=None):
    cnt = """\
version = '%s'
short_version = '%s'
"""
    if not filename:
        filename = os.path.join(
            os.path.dirname(__file__), 'inotifyer', 'version.py')

    a = open(filename, 'w')
    try:
        a.write(cnt % (FULLVERSION, VERSION))
    finally:
        a.close()

write_version_py()

setup(name='inotifyer',
      version=FULLVERSION,
      description='simple notification decorator',
      license='BSD',
      author='Philipp Kats',
      author_email='casyfill@gmail.com',
      url='https://github.com/Casyfill/ipython_notifier',
      long_description=LONG_DESCRIPTION,
      packages=['ipynotifyer'],
      install_requires=INSTALL_REQUIRES)