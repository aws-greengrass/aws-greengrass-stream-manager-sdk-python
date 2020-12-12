#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''SDK_VERSION = ['"]([0-9.]+)['"]''')


requires = [
    "cbor2==4.1.2"
]


def get_version():
    init = open(os.path.join(ROOT,'stream_manager','streammanagerclient.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='stream_manager',
    version=get_version(),
    description='The AWS IoT Greengrass Stream Manager SDK for Python',
    long_description=open('README.md').read(),
    author='Amazon Web Services',
    url='',
    scripts=[],
    packages=find_packages(),
    package_data={
        'stream_manager': [
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
)
