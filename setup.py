# -*- coding: utf-8 -*-
"""
setup.py script
"""

import io
from collections import OrderedDict
from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding='utf8') as f:
    README = f.read()

setup(
    name='SampleModule',
    version='1.0.0',
    url='http://github.com/giovannicuriel/python-project',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/giovannicuriel/python-project.git'),
        ('Issue tracker', 'https://github.com/giovannicuriel/python-project/issues'),
    )),
    license='BSD-3-Clause',
    author='Giovanni Curiel dos Santos',
    author_email='giovannicuriel@gmail.com',
    maintainer='dojot team',
    description='Sample project structure for Python modules',
    long_description=README,
    packages=["sample_package"],
    include_package_data=True,
    zip_safe=False,
    platforms=[any],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'super_package==1.0.0'
    ],
    extras_require={
        "dev": [
            "pytest==4.0.0",
            "pytest-cov==2.6.0"
        ]
    }
)
