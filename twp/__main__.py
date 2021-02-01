# -*- coding: utf-8 -*-

"""
Tableau Workbook SQL Extract Tool

twp is a command line tool for parsing sql queries & related
information out of tableau workbooks (.twb & .twbx files). It works by
taking a tableau workbook, parsing the xml, and formatting information
about worksheets, connections to those worksheets, their connection(db)
details, and the corresponding custom sql (assuming it exists) in a
valid sql & human readable format.

    USAGE:
    $ twp input.twb(x) > output.sql


See the README for further details.
"""

import sys

import click

import twp


@click.command()
@click.argument('filename')
def cli(filename):
    """Tableau Workbook Parser

    twp is a command line tool for parsing sql queries & related
    information out of tableau workbooks (.twb & .twbx files). It works by
    taking a tableau workbook, parsing the xml, and formatting information
    about worksheets, connections to those worksheets, their connection(db)
    details, and the corresponding custom sql (assuming it exists) in a
    valid sql & human readable format.

        USAGE:

            $ twp input.twb(x) > output.sql

    See the README for further details.
    """
    sys.stdout.write(twp.convert(filename))
