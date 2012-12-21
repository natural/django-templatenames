#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='templatenames',
    version='0.1',
    description="""
    Provides template tags for template name, plus corresponding CSS and JS.
    """,
    author='Troy Melhase',
    author_email='troy@troy.io',
    url='https://github.com/natural/django-templatenames',
    packages = ['templatenames'],
    package_data={},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=False,
    zip_safe=True,
    install_requires=['setuptools'],
)
