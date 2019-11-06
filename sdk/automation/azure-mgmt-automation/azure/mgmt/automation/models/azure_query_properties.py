# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureQueryProperties(Model):
    """Azure query for the update configuration.

    :param scope: List of Subscription or Resource Group ARM IDs.
    :type scope: list[str]
    :param locations: List of locations to scope the query to.
    :type locations: list[str]
    :param tag_settings: Tag settings for the VM.
    :type tag_settings: ~azure.mgmt.automation.models.TagSettingsProperties
    """

    _attribute_map = {
        'scope': {'key': 'scope', 'type': '[str]'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'tag_settings': {'key': 'tagSettings', 'type': 'TagSettingsProperties'},
    }

    def __init__(self, **kwargs):
        super(AzureQueryProperties, self).__init__(**kwargs)
        self.scope = kwargs.get('scope', None)
        self.locations = kwargs.get('locations', None)
        self.tag_settings = kwargs.get('tag_settings', None)
