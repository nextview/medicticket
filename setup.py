#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Noah Kantrowitz
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.


import os

from setuptools import setup

setup(
    name = 'TracTxomonTickets',
    version = '0.0.1',
    packages = ['ticket'],

    author = 'Javier Domingo',
    author_email = 'javierdo1@gmail.com',
    description = 'Modified ticket system to provide privacy for Trac.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    license = 'GPLv3',
    keywords = 'trac plugin ticket privacy permissions security',
    url = '',
    download_url = '',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac'],

    entry_points = """
        [trac.plugins]
        txomon.ticket.admin = txomon.ticket.admin
        txomon.ticket.batch = txomon.ticket.batch
        txomon.ticket.query = txomon.ticket.query
        txomon.ticket.report = txomon.ticket.report
        txomon.ticket.roadmap = txomon.ticket.roadmap
        txomon.ticket.web_ui = txomon.ticket.web_ui
    """,
)
