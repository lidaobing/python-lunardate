#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import re

def get_version():
    with open(
        os.path.join(os.path.dirname(__file__), "lunardate.py"),
        "r",
        encoding="utf-8",
    ) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(name='lunardate',
      version=get_version(),
      py_modules = ['lunardate'],
      description = 'A Chinese Calendar Library in Pure Python',
      long_description = open("README.md", "r", encoding="utf-8").read(),
      author = 'LI Daobing',
      author_email = 'lidaobing@gmail.com',
      url = 'https://github.com/lidaobing/python-lunardate',
      license = 'GPLv3',
      python_requires='>=3.7',
      classifiers = [
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                     'Programming Language :: Python :: 3.11',
                     'License :: OSI Approved :: GNU General Public License (GPL)',
                     'Operating System :: OS Independent',
                     'Topic :: Software Development :: Libraries :: Python Modules'
                     ]
      )
