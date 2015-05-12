#!/usr/bin/env python
"""
sentry-freight
==============

A Sentry extension which integrates with Freight release tracking.

:copyright: (c) 2015 by Sentry Team, see AUTHORS for more details.
:license: Apache 2.0, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    # 'sentry>=7.5.0',
]

setup(
    name='sentry-freight',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://github.com/getsentry/sentry-freight',
    description='A Sentry extension which integrates Freight release tracking.',
    long_description=open('README.rst').read(),
    license='Apache 2.0',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_freight = sentry_freight',
        ],
        'sentry.plugins': [
            'sentry_freight = sentry_freight.plugin:FreightPlugin',
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
