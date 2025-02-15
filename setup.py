#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-helpscout',
      version='1.1.0',
      description='Singer.io tap for extracting data from the HelpScout Mailbox API 2.0',
      author='jeff.huth@bytecode.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_helpscout'],
      install_requires=[
          'backoff==1.8.0',
          'requests==2.23.0',
          'singer-python==5.13.0'
      ],
      entry_points='''
          [console_scripts]
          tap-helpscout=tap_helpscout:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_helpscout': [
              'schemas/*.json'
          ]
      })
