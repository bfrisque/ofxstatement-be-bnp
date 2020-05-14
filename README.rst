~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Belgian BNP Paribas Fortis Bank plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project provides an `ofxstatement`_ plugin for converting the Belgian BNP Paribas Fortis bank's CSV format statements to OFX.

`ofxstatement`_ is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugins for ofxstatement parse a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

Users of ofxstatement have developed several plugins for their banks. They are
listed on main `ofxstatement`_ site. If your bank is missing, you can develop
your own plugin.

.. _ofxstatement: https://github.com/kedder/ofxstatement


Installation
============
Either:

#. Download from `pypi <https://pypi.org/project/ofxstatement-be-bnp>`_ and run
   :code:`$ python setup.py install`
#. Install using pip: :code:`$ pip install ofxstatement-be-bnp`

Usage
=====
Basically: :code:`$ ofxstatement convert -t bnp input.csv output.ofx`

General usage of ofxstatement:

.. code-block::

   $ ofxstatement --help
   usage: ofxstatement [-h] [--version] [-d]
                    {convert,list-plugins,edit-config} ...

   Tool to convert proprietary bank statement to OFX format.

   optional arguments:
     -h, --help            show this help message and exit
     --version             show current version
     -d, --debug           show debugging information

   action:
     {convert,list-plugins,edit-config}
       convert             convert to OFX
       list-plugins        list available plugins
       edit-config         open configuration file in default editor

Usage of the convert command:

.. code-block::

   $ ofxstatement convert --help
   usage: ofxstatement convert [-h] -t TYPE input output

   positional arguments:
     input                 input file to process
     output                output (OFX) file to produce

   optional arguments:
     -h, --help            show this help message and exit
     -t TYPE, --type TYPE  input file type. This is a section in config file, or
                           plugin name if you have no config file.
