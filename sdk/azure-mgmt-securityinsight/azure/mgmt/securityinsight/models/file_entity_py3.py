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

from .entity_py3 import Entity


class FileEntity(Entity):
    """Represents a file entity.

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
    :ivar directory: The full path to the file.
    :vartype directory: str
    :ivar file_name: The file name without path (some alerts might not include
     path).
    :vartype file_name: str
    :ivar host_entity_id: The Host entity id which the file belongs to
    :vartype host_entity_id: str
    :ivar file_hash_entity_ids: The file hash entity identifiers associated
     with this file
    :vartype file_hash_entity_ids: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'friendly_name': {'readonly': True},
        'additional_data': {'readonly': True},
        'directory': {'readonly': True},
        'file_name': {'readonly': True},
        'host_entity_id': {'readonly': True},
        'file_hash_entity_ids': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'directory': {'key': 'properties.directory', 'type': 'str'},
        'file_name': {'key': 'properties.fileName', 'type': 'str'},
        'host_entity_id': {'key': 'properties.hostEntityId', 'type': 'str'},
        'file_hash_entity_ids': {'key': 'properties.fileHashEntityIds', 'type': '[str]'},
    }

    def __init__(self, **kwargs) -> None:
        super(FileEntity, self).__init__(**kwargs)
        self.friendly_name = None
        self.additional_data = None
        self.directory = None
        self.file_name = None
        self.host_entity_id = None
        self.file_hash_entity_ids = None
        self.kind = 'File'