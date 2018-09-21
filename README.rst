===============================================================================
installer: A library for installing python packages.
===============================================================================

.. image:: https://img.shields.io/pypi/v/installer.svg
    :target: https://pypi.org/project/installer

.. image:: https://img.shields.io/pypi/l/installer.svg
    :target: https://pypi.org/project/installer

.. image:: https://api.travis-ci.com/sarugaku/installer.svg?branch=master
    :target: https://travis-ci.com/sarugaku/installer

.. image:: https://ci.appveyor.com/api/projects/status/y9kpdaqy4di5nhyk/branch/master?svg=true
    :target: https://ci.appveyor.com/project/sarugaku/installer

.. image:: https://img.shields.io/pypi/pyversions/installer.svg
    :target: https://pypi.org/project/installer

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/techalchemy

.. image:: https://readthedocs.org/projects/installer/badge/?version=latest
    :target: https://installer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Summary
=======

Installer_ is a library designed for installing python packages built using packagebuilder_.
It is targeted as a lightweight library for synchronizing Pipfile_ formatted projects with
their respective environments (but provides no interface through virtual environments,
see mork_ for that!).  Its goal is to provide a small but functional interface to take a
set of requirementslib_ compatible requirements (preferrably from a `Pipfile.lock`) and
install them into an environment, optionally removing packages not present in the lockfile.

Ultimately this project will back installation in Pipenv_.

  ::

    >>> import installer
    >>> from passa.cli.options import Project
    >>> project = Project(root="/some/root/directory")
    >>> syncer = installer.synchronizer.Synchronizer(
        project, default=True, develop=True,
        clean_unneeded=True
    )
    >>> installer.operations.sync(syncer)


.. _packagebuilder: https://github.com/sarugaku/packagebuilder
.. _requirementslib: https://github.com/sarugaku/requirementslib
.. _mork: https://github.com/sarugaku/mork
.. _pipfile: https://github.com/pypa/pipfile
.. _pipenv: https://github.com/pypa/pipenv

`Read the documentation <https://installer.readthedocs.io/>`__.
