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

from .entity import Entity


class ProcessEntity(Entity):
    """Represents a process entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :ivar friendly_name: The graph item display name which is a short humanly
     readable description of the graph item instance. This property is optional
     and might be system generated.
    :vartype friendly_name: str
    :ivar additional_data: A bag of custom fields that should be part of the
     entity and will be presented to the user.
    :vartype additional_data: dict[str, object]
    :ivar process_id: The process ID
    :vartype process_id: str
    :ivar command_line: The command line used to create the process
    :vartype command_line: str
    :param elevation_token: The elevation token associated with the process.
     Possible values include: 'Default', 'Full', 'Limited'
    :type elevation_token: str or
     ~azure.mgmt.securityinsight.models.ElevationToken
    :ivar creation_time_utc: The time when the process started to run
    :vartype creation_time_utc: datetime
    :ivar image_file_entity_id: Image file entity id
    :vartype image_file_entity_id: str
    :ivar account_entity_id: The account entity id running the processes.
    :vartype account_entity_id: str
    :ivar parent_process_entity_id: The parent process entity id.
    :vartype parent_process_entity_id: str
    :ivar host_entity_id: The host entity id on which the process was running
    :vartype host_entity_id: str
    :ivar host_logon_session_entity_id: The session entity id in which the
     process was running
    :vartype host_logon_session_entity_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'friendly_name': {'readonly': True},
        'additional_data': {'readonly': True},
        'process_id': {'readonly': True},
        'command_line': {'readonly': True},
        'creation_time_utc': {'readonly': True},
        'image_file_entity_id': {'readonly': True},
        'account_entity_id': {'readonly': True},
        'parent_process_entity_id': {'readonly': True},
        'host_entity_id': {'readonly': True},
        'host_logon_session_entity_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'process_id': {'key': 'properties.processId', 'type': 'str'},
        'command_line': {'key': 'properties.commandLine', 'type': 'str'},
        'elevation_token': {'key': 'properties.elevationToken', 'type': 'ElevationToken'},
        'creation_time_utc': {'key': 'properties.creationTimeUtc', 'type': 'iso-8601'},
        'image_file_entity_id': {'key': 'properties.imageFileEntityId', 'type': 'str'},
        'account_entity_id': {'key': 'properties.accountEntityId', 'type': 'str'},
        'parent_process_entity_id': {'key': 'properties.parentProcessEntityId', 'type': 'str'},
        'host_entity_id': {'key': 'properties.hostEntityId', 'type': 'str'},
        'host_logon_session_entity_id': {'key': 'properties.hostLogonSessionEntityId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProcessEntity, self).__init__(**kwargs)
        self.friendly_name = None
        self.additional_data = None
        self.process_id = None
        self.command_line = None
        self.elevation_token = kwargs.get('elevation_token', None)
        self.creation_time_utc = None
        self.image_file_entity_id = None
        self.account_entity_id = None
        self.parent_process_entity_id = None
        self.host_entity_id = None
        self.host_logon_session_entity_id = None
        self.kind = 'Process'