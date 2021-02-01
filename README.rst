# twp - tableau workbook parser

.. image:: https://img.shields.io/pypi/v/twp.svg
    :target: https://pypi.python.org/pypi/twp


OVERVIEW
''''''''
twp is a command line tool for parsing sql queries & related
information out of tableau workbooks (.twb & .twbx files). It works by
taking a tableau workbook, parsing the xml, and formatting information
about worksheets, connections to those worksheets, their connection(db)
details, and the corresponding custom sql (assuming it exists) in a
valid sql & human readable format.


USAGE
'''''
.. code-block:: bash

    $ twp input.twb(x) > output.sql


INSTALL
'''''''
.. code-block:: bash

    $ python -m pip install twp

CREDITS
*******
Forked from (and based mostly on) https://github.com/levikanwischer/tabtosql, work (c) 2016 by Levi Kanwischer
