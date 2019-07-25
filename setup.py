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
      license = 'GPLv3',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'License :: OSI Approved :: GNU General Public License (GPL)',
                     'Operating System :: OS Independent',
                     'Topic :: Software Development :: Libraries :: Python Modules'
                     ]
      )
