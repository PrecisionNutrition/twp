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

from .workbook import convert


__title__ = 'twp'
__version__ = '2.0.0'
__author__ = 'Levi Kanwischer, Alaina Hardie'
__copyright__ = 'Copyright (c) 2016 Levi Kanwischer, (c) 2021 Alaina Hardie'
__license__ = 'MIT'
__all__ = ['convert']
