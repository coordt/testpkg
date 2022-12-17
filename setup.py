#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from m2r import parse_from_file
from setuptools import setup, find_packages

def get_version(*file_paths):
    """Retrieves the version from testpkg/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    if version_match := re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    ):
        return version_match[1]
    raise RuntimeError('Unable to find version string.')


def parse_reqs(filepath):
    with open(filepath, 'r') as f:
        reqstr = f.read()
    requirements = []
    for line in reqstr.splitlines():
        line = line.strip()
        if line == '':
            continue
        elif not line or line.startswith('#'):
            # comments are lines that start with # only
            continue
        elif line.startswith('-r') or line.startswith('--requirement'):
            _, new_filename = line.split()
            new_file_path = os.path.join(os.path.dirname(filepath or '.'),
                                         new_filename)
            requirements.extend(parse_reqs(new_file_path))
        elif line.startswith('-f') or line.startswith('--find-links') or \
                line.startswith('-i') or line.startswith('--index-url') or \
                line.startswith('--extra-index-url') or \
                line.startswith('--no-index'):
            continue
        elif line.startswith('-Z') or line.startswith('--always-unzip'):
            continue
        else:
            requirements.append(line)
    return requirements

version = get_version("testpkg", "__init__.py")
readme = open('README.rst').read()
history = parse_from_file('CHANGELOG.md')

setup(
    name='django-testpkg',
    version=version,
    description="""Your project description goes here""",
    long_description=readme + '\n\n' + history,
    author='Corey Oordt',
    author_email='coreyoordt@gmail.com',
    url='https://github.com/coordt/django-testpkg',
    packages=find_packages(exclude=['example*', 'tests*', 'docs', 'build', ]),
    include_package_data=True,
    install_requires=parse_reqs('requirements.txt'),
    license="MIT",
    zip_safe=False,
    keywords='django-testpkg',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
