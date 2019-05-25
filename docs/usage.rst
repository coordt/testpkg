=====
Usage
=====

To use Django Testpkg in a project, add it to your `INSTALLED_APPS`:

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
