#!/usr/bin/env python3

import setuptools
from distutils.core import setup

setup(name="OBISdat",
      version='1.0',
      author='Ulises Rosas',
      author_email='ulisesfrosasp@gmail.com',
      url='https://github.com/Ulises-Rosas/OBISdat',
      packages = ['OBISdat'],
      package_dir = {'OBISdat': 'src'},
      scripts = ['src/obis.py']
      )

