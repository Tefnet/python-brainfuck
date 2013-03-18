#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'brainfuck',
    version = '0.1',
    url = 'http://github.com/Tefnet/python-brainfuck',
    license = 'GPL',
    description = 'Brainfuck parser and server',
    author = 'Tomasz Jezierski',
    author_email = 'tomasz.jezierski@tefnet.pl',
    packages = ['brainfuck'],
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [ 'brainfuck_server = brainfuck.server:main' ]
    }
)
