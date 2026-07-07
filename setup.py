#!/usr/bin/env python

from setuptools import setup, find_packages

import lunardate

setup(name='lunardate',
      version=lunardate.__version__,
      py_modules = ['lunardate'],
      description = 'A Chinese Calendar Library in Pure Python',
      long_description = lunardate.__doc__,
      author = 'LI Daobing',
      author_email = 'lidaobing@gmail.com',
      url = 'https://github.com/lidaobing/python-lunardate',
      license = 'GPL-3.0-or-later',
      python_requires='>=3.7',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                     'Programming Language :: Python :: 3.11',
                     'Operating System :: OS Independent',
                     'Topic :: Software Development :: Libraries :: Python Modules'
                     ]
      )
