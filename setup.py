#!/usr/bin/env/python
"""Installation script
Version handling borrowed from geopandas project.
"""

from setuptools import setup
LONG_DESCRIPTION = ''' Ipython notifyer is dependent on pync package and
meant as a tiny decorator for your heavy long functions. It is especially
useful in the Ipython, as web browser can lead to the massive destruction :-)
'''

setup(name='inotifyer',
      version='0.48.b',
      description='timer included',
      license='BSD',
      author='Philipp Kats',
      author_email='casyfill@gmail.com',
      url='https://github.com/Casyfill/ipython_notifier',
      long_description=LONG_DESCRIPTION,
      packages=['ipynotifyer'],
      install_requires=('pync'))
