=============================
Django Testpkg
=============================

.. image:: https://badge.fury.io/py/django-testpkg.svg
    :target: https://badge.fury.io/py/django-testpkg

.. image:: https://travis-ci.org/coordt/django-testpkg.svg?branch=master
    :target: https://travis-ci.org/coordt/django-testpkg

.. image:: https://codecov.io/gh/coordt/django-testpkg/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/coordt/django-testpkg

Your project description goes here

Documentation
-------------

The full documentation is at https://django-testpkg.readthedocs.io.

Quickstart
----------

Install Django Testpkg::

    pip install django-testpkg

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'testpkg.apps.TestpkgConfig',
        ...
    )

Add Django Testpkg's URL patterns:

.. code-block:: python

    from testpkg import urls as testpkg_urls


    urlpatterns = [
        ...
        url(r'^', include(testpkg_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
