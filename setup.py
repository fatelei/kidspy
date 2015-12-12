# -*- coding: utf8 -*-

from setuptools import setup

from kids import __version__

setup(
    name="kids",
    version=__version__,
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="Kids Python Client",
    install_requires=["redis"],
    packages=["kids"],
    zip_safe=False,
    url="https://github.com/fatelei/kidspy",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Logging"
    ],
    license="BSD License"
)
