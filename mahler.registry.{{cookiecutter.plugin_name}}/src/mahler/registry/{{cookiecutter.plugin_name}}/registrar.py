# -*- coding: utf-8 -*-
"""
:mod:`mahler.registry.{{ cookiecutter.plugin_name }}.registrar -- TODO 
======================{{ '=' * cookiecutter.plugin_name|length }}==================

.. module:: {{ cookiecutter.plugin_name }}
    :platform: Unix
    :synopsis: {{ cookiecutter.synopsis }}

TODO: Write long description
"""
from mahler.core.registrar import RegistrarDB


class {{ cookiecutter.registrardb_classname }}(RegistrarDB):
    """
    """

    def __init__(self):
        """
        """
        pass

    def register_task(self, task):
        """
        """
        raise NotImplementedError()

    def retrieve_tasks(self, tags, status=None):
        """
        """
        raise NotImplementedError()

    def add_event(self, event_type, event_object):
        """
        """
        raise NotImplementedError()

    def retrieve_events(self, event_type, task):
        """
        """
        raise NotImplementedError()

    def set_output(self, task, output):
        """
        """
        raise NotImplementedError()

    def set_volume(self, task, volume):
        """
        """
        raise NotImplementedError()

    def retrieve_output(self, task):
        """
        """
        raise NotImplementedError()
