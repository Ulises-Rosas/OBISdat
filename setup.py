#!/usr/bin/env python3

import setuptools
from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()


setup(name="OBISdat",
      version='1.3',
      long_description = readme,
      long_description_content_type='text/markdown',
      author='Ulises Rosas',
      author_email='ulisesfrosasp@gmail.com',
      url='https://github.com/Ulises-Rosas/OBISdat',
      packages = ['OBISdat'],
      package_dir = {'OBISdat': 'src'},
      entry_points = {
           'console_scripts': [
                 'obis = OBISdat.obis:main'
            ]
      },
      classifiers=[
             'Programming Language :: Python :: 3',
             'License :: OSI Approved :: MIT License'
             ]
      )
