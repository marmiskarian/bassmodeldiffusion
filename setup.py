#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy==1.24.3', 'pandas==2.0.1', 'matplotlib==3.7.1', 'statsmodels==0.14.0']

setup(
    author="Maria Miskaryan",
    author_email='mar.miskaryan@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10.9',
    ],
    description="The Python implementation of the Bass Model",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='bassmodel',
    name='bassmodel',
    packages=find_packages(include=['bassmodel', 'bassmodel.*']),
    url='https://github.com/ilynmark/bassmodel',
    version='0.1.0',
    zip_safe=False,
)
