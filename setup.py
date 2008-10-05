#!/usr/bin/env python

from setuptools import setup, find_packages

import lunardate

setup(name='lunardate',
      version='0.1.2',
      py_modules = ['lunardate'],
      description = 'A Chinese Calendar Library in Pure Python',
      long_description = lunardate.__doc__,
      author = 'LI Daobing',
      author_email = 'lidaobing@gmail.com',
      url = 'http://code.google.com/p/python-lunardate',
      license = 'GPLv3',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python',
                     'License :: OSI Approved :: GNU General Public License (GPL)',
                     'Operating System :: OS Independent',
                     'Topic :: Software Development :: Libraries :: Python Modules'
                     ]
      )
