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


class DirectLineChannelProperties(Model):
    """The parameters to provide for the Direct Line channel.

    :param sites: The list of Direct Line sites
    :type sites: list[~azure.mgmt.botservice.models.DirectLineSite]
    """

    _attribute_map = {
        'sites': {'key': 'sites', 'type': '[DirectLineSite]'},
    }

    def __init__(self, **kwargs):
        super(DirectLineChannelProperties, self).__init__(**kwargs)
        self.sites = kwargs.get('sites', None)