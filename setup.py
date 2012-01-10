#!/usr/bin/env python

from setuptools import setup

PROJECT = 'virtualenvwrapper.locodev'
VERSION = '0.0.1'

setup(
        name=PROJECT,
        version=VERSION,

        description='',

        author='',
        author_email='',

        url = '',
        download_url='' ,

        classifiers=[
            'Development Status :: 4 - Beta',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Intended Audience :: Developers',
            'Environment :: Console',
            ],

        platforms=[
            'Any',
            ],

        namespace_packages=[
            'virtualenvwrapper',
            ],

        packages=[
            'virtualenvwrapper',
            ],

        install_requires=[
            'virtualenv',
            'virtualenvwrapper>=2.9',
            ],

        entry_points={
            'virtualenvwrapper.project.template': [
                'locodev = virtualenvwrapper.locodev:template',
                ]
            },

        zip_safe=False,
        )
