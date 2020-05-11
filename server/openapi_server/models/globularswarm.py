# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Globularswarm(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, v_hb=None, radius_ly=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """Globularswarm - a model defined in OpenAPI

        :param v_hb: The v_hb of this Globularswarm.  # noqa: E501
        :type v_hb: List[int]
        :param radius_ly: The radius_ly of this Globularswarm.  # noqa: E501
        :type radius_ly: List[int]
        :param description: The description of this Globularswarm.  # noqa: E501
        :type description: List[str]
        :param id: The id of this Globularswarm.  # noqa: E501
        :type id: str
        :param label: The label of this Globularswarm.  # noqa: E501
        :type label: List[str]
        :param type: The type of this Globularswarm.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'v_hb': List[int],
            'radius_ly': List[int],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'v_hb': 'v_hb',
            'radius_ly': 'radius_ly',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._v_hb = v_hb
        self._radius_ly = radius_ly
        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'Globularswarm':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Globularswarm of this Globularswarm.  # noqa: E501
        :rtype: Globularswarm
        """
        return util.deserialize_model(dikt, cls)

    @property
    def v_hb(self):
        """Gets the v_hb of this Globularswarm.

        Description not available  # noqa: E501

        :return: The v_hb of this Globularswarm.
        :rtype: List[int]
        """
        return self._v_hb

    @v_hb.setter
    def v_hb(self, v_hb):
        """Sets the v_hb of this Globularswarm.

        Description not available  # noqa: E501

        :param v_hb: The v_hb of this Globularswarm.
        :type v_hb: List[int]
        """

        self._v_hb = v_hb

    @property
    def radius_ly(self):
        """Gets the radius_ly of this Globularswarm.

        Description not available  # noqa: E501

        :return: The radius_ly of this Globularswarm.
        :rtype: List[int]
        """
        return self._radius_ly

    @radius_ly.setter
    def radius_ly(self, radius_ly):
        """Sets the radius_ly of this Globularswarm.

        Description not available  # noqa: E501

        :param radius_ly: The radius_ly of this Globularswarm.
        :type radius_ly: List[int]
        """

        self._radius_ly = radius_ly

    @property
    def description(self):
        """Gets the description of this Globularswarm.

        small description  # noqa: E501

        :return: The description of this Globularswarm.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Globularswarm.

        small description  # noqa: E501

        :param description: The description of this Globularswarm.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Globularswarm.

        identifier  # noqa: E501

        :return: The id of this Globularswarm.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Globularswarm.

        identifier  # noqa: E501

        :param id: The id of this Globularswarm.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Globularswarm.

        short description of the resource  # noqa: E501

        :return: The label of this Globularswarm.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Globularswarm.

        short description of the resource  # noqa: E501

        :param label: The label of this Globularswarm.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this Globularswarm.

        type of the resource  # noqa: E501

        :return: The type of this Globularswarm.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Globularswarm.

        type of the resource  # noqa: E501

        :param type: The type of this Globularswarm.
        :type type: List[str]
        """

        self._type = type