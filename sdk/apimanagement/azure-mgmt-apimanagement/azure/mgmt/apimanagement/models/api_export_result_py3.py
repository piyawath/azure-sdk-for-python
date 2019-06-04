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


class ApiExportResult(Model):
    """API Export result.

    :param id: ResourceId of the API which was exported.
    :type id: str
    :param export_result_format: Format in which the Api Details are exported
     to the Storage Blob with Sas Key valid for 5 minutes. Possible values
     include: 'Swagger', 'Wsdl', 'Wadl', 'OpenApi'
    :type export_result_format: str or
     ~azure.mgmt.apimanagement.models.ExportResultFormat
    :param value: The object defining the schema of the exported Api Detail
    :type value: ~azure.mgmt.apimanagement.models.ApiExportResultValue
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'export_result_format': {'key': 'format', 'type': 'str'},
        'value': {'key': 'value', 'type': 'ApiExportResultValue'},
    }

    def __init__(self, *, id: str=None, export_result_format=None, value=None, **kwargs) -> None:
        super(ApiExportResult, self).__init__(**kwargs)
        self.id = id
        self.export_result_format = export_result_format
        self.value = value