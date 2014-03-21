#!/usr/bin/env python
from setuptools import setup


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='asstosrt',
    version='0.1.3',
    description='A tool that convert ASS/SSA subtitle to SRT format',
    author='XiErCh',
    author_email='orz@sorz.org',
    url='https://github.com/bluen/asstosrt/',
    py_modules=['batch'],
    packages=['asstosrt'],
    data_files=[('', ['README.rst'])],
    install_requires=['setuptools'],
    entry_points="""
    [console_scripts]
    asstosrt = batch:main
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
    ],
    long_description=long_description
)
