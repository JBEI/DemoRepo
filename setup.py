#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="DemoRepo",
    version="0.1",
    description="An example repository that describes how to set up basic tools for good code health.",
    author="Bret Peterson",
    author_email="bretpeterson@lbl.gov",
    url="https://github.com/JBEI/DemoRemo",
    packages=setuptools.find_packages(),
    install_requires=[
        "ipython",
        "mock",
        "pytest",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research/Development",
        "Intended Audience :: Scientific Engineering",
        "Intended Audience :: Application",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
)
