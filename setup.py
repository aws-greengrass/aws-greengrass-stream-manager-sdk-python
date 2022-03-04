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
    "cbor2~=5.4.2"
]


def get_version():
    init = open(os.path.join(ROOT,'stream_manager','streammanagerclient.py')).read()
    version = VERSION_RE.search(init).group(1)
    if os.getenv("PYPI_TEST", False) == "True":
        import time
        return version + "." + str(int(time.time()))
    return version


setup(
    name='stream_manager',
    version=get_version(),
    description='The AWS IoT Greengrass Stream Manager SDK for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
