#!/usr/bin/python3
"""Setup
"""
from setuptools import find_packages
from distutils.core import setup

version = "0.1.3"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-be-bnp',
      version=version,
      author="Benoit Frisque",
      author_email="benoitfrisque@gmail.com",
      url="https://github.com/bfrisque/ofxstatement-be-bnp",
      description=("ofxstatement plugin for parsing Belgian BNP Paribas Fortis bank's CSV statements to OFX"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement", "bnp", "csv"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 3',
          'Natural Language :: English',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['bnp = ofxstatement.plugins.bnp:bnpPlugin']
          },
      install_requires=['ofxstatement'],
      include_package_data=True,
      zip_safe=True
      )
