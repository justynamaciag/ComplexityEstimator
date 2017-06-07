#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_zad2_justynamaciag
----------------------------------

Tests for `zad2_justynamaciag` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from zad2_justynamaciag import zad2_justynamaciag
from zad2_justynamaciag import cli



class TestZad2_justynamaciag(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'zad2_justynamaciag.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output