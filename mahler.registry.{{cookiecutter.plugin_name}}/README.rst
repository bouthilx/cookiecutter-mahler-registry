{%- from "macros/rst" import doc_title, doc_subtitle -%}

{{ doc_title('mahler.registry.' + cookiecutter.plugin_name) }}


.. |pypi| image:: https://img.shields.io/pypi/v/mahler.registry.{{cookiecutter.plugin_name}}
    :target: https://pypi.python.org/pypi/mahler.registry.{{cookiecutter.plugin_name}}
    :alt: Current PyPi Version

.. |py_versions| image:: https://img.shields.io/pypi/pyversions/mahler.registry.{{cookiecutter.plugin_name}}.svg
    :target: https://pypi.python.org/pypi/mahler.registry.{{cookiecutter.plugin_name}}
    :alt: Supported Python Versions

.. |license| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0
    :alt: GPL v3 license

.. |rtfd| image:: https://readthedocs.org/projects/mahler.registry.{{cookiecutter.plugin_name}}/badge/?version=latest
    :target: https://mahler-registry-{{cookiecutter.plugin_name}}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |codecov| image:: https://codecov.io/gh/Epistimio/mahler.registry.{{cookiecutter.plugin_name}}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Epistimio/mahler.registry.{{cookiecutter.plugin_name}}
    :alt: Codecov Report

.. |travis| image:: https://travis-ci.org/bouthilx/mahler.registry.{{cookiecutter.plugin_name}}.svg?branch=master
    :target: https://travis-ci.org/bouthilx/mahler.registry.{{cookiecutter.plugin_name}}
    :alt: Travis tests


{{cookiecutter.short_description}}


----

This `mahler.registry`_ plugin was generated with `Cookiecutter`_ along with `@bouthilx`_'s `cookiecutter-mahler-registry`_ template.


Features
--------

* TODO


Requirements
------------

* TODO


Installation
------------

You can install "mahler.registry.{{cookiecutter.plugin_name}}" via `pip`_ from `PyPI`_::

    $ pip install git+https://github.com/{{ cookiecutter.github_username }}/mahler.registry.{{cookiecutter.plugin_name}}.git


Usage
-----

* TODO

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the GPL v3 license,
"mahler.registry.{{cookiecutter.plugin_name}}" is free and open source software.


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@bouthilx`: https://github.com/bouthilx
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`cookiecutter-mahler-registry`: https://github.com/bouthilx/cookiecutter-mahler.registry
.. _`file an issue`: https://github.com/{{cookiecutter.github_username}}/cookiecutter-mahler.registry.{{cookiecutter.plugin_name}}/issues
.. _`mahler`: https://github.com/bouthilx/mahler
