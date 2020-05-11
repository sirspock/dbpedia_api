# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LiechtensteinSettlement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, council=None, description=None, ward=None, id=None, label=None, type=None):  # noqa: E501
        """LiechtensteinSettlement - a model defined in OpenAPI

        :param council: The council of this LiechtensteinSettlement.  # noqa: E501
        :type council: List[str]
        :param description: The description of this LiechtensteinSettlement.  # noqa: E501
        :type description: List[str]
        :param ward: The ward of this LiechtensteinSettlement.  # noqa: E501
        :type ward: List[str]
        :param id: The id of this LiechtensteinSettlement.  # noqa: E501
        :type id: str
        :param label: The label of this LiechtensteinSettlement.  # noqa: E501
        :type label: List[str]
        :param type: The type of this LiechtensteinSettlement.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'council': List[str],
            'description': List[str],
            'ward': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'council': 'council',
            'description': 'description',
            'ward': 'ward',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._council = council
        self._description = description
        self._ward = ward
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'LiechtensteinSettlement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LiechtensteinSettlement of this LiechtensteinSettlement.  # noqa: E501
        :rtype: LiechtensteinSettlement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def council(self):
        """Gets the council of this LiechtensteinSettlement.

        Description not available  # noqa: E501

        :return: The council of this LiechtensteinSettlement.
        :rtype: List[str]
        """
        return self._council

    @council.setter
    def council(self, council):
        """Sets the council of this LiechtensteinSettlement.

        Description not available  # noqa: E501

        :param council: The council of this LiechtensteinSettlement.
        :type council: List[str]
        """

        self._council = council

    @property
    def description(self):
        """Gets the description of this LiechtensteinSettlement.

        small description  # noqa: E501

        :return: The description of this LiechtensteinSettlement.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LiechtensteinSettlement.

        small description  # noqa: E501

        :param description: The description of this LiechtensteinSettlement.
        :type description: List[str]
        """

        self._description = description

    @property
    def ward(self):
        """Gets the ward of this LiechtensteinSettlement.

        Description not available  # noqa: E501

        :return: The ward of this LiechtensteinSettlement.
        :rtype: List[str]
        """
        return self._ward

    @ward.setter
    def ward(self, ward):
        """Sets the ward of this LiechtensteinSettlement.

        Description not available  # noqa: E501

        :param ward: The ward of this LiechtensteinSettlement.
        :type ward: List[str]
        """

        self._ward = ward

    @property
    def id(self):
        """Gets the id of this LiechtensteinSettlement.

        identifier  # noqa: E501

        :return: The id of this LiechtensteinSettlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LiechtensteinSettlement.

        identifier  # noqa: E501

        :param id: The id of this LiechtensteinSettlement.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this LiechtensteinSettlement.

        short description of the resource  # noqa: E501

        :return: The label of this LiechtensteinSettlement.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LiechtensteinSettlement.

        short description of the resource  # noqa: E501

        :param label: The label of this LiechtensteinSettlement.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this LiechtensteinSettlement.

        type of the resource  # noqa: E501

        :return: The type of this LiechtensteinSettlement.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LiechtensteinSettlement.

        type of the resource  # noqa: E501

        :param type: The type of this LiechtensteinSettlement.
        :type type: List[str]
        """

        self._type = type