# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class GermanSettlement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, licence_letter=None, number_of_neighbourhood=None, description=None, id=None, label=None, type=None):  # noqa: E501
        """GermanSettlement - a model defined in OpenAPI

        :param licence_letter: The licence_letter of this GermanSettlement.  # noqa: E501
        :type licence_letter: List[str]
        :param number_of_neighbourhood: The number_of_neighbourhood of this GermanSettlement.  # noqa: E501
        :type number_of_neighbourhood: List[int]
        :param description: The description of this GermanSettlement.  # noqa: E501
        :type description: List[str]
        :param id: The id of this GermanSettlement.  # noqa: E501
        :type id: str
        :param label: The label of this GermanSettlement.  # noqa: E501
        :type label: List[str]
        :param type: The type of this GermanSettlement.  # noqa: E501
        :type type: List[str]
        """


        self.openapi_types = {
            'licence_letter': List[str],
            'number_of_neighbourhood': List[int],
            'description': List[str],
            'id': str,
            'label': List[str],
            'type': List[str]
        }

        self.attribute_map = {
            'licence_letter': 'licenceLetter',
            'number_of_neighbourhood': 'numberOfNeighbourhood',
            'description': 'description',
            'id': 'id',
            'label': 'label',
            'type': 'type'
        }

        self._licence_letter = licence_letter
        self._number_of_neighbourhood = number_of_neighbourhood
        self._description = description
        self._id = id
        self._label = label
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'GermanSettlement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GermanSettlement of this GermanSettlement.  # noqa: E501
        :rtype: GermanSettlement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def licence_letter(self):
        """Gets the licence_letter of this GermanSettlement.

        Description not available  # noqa: E501

        :return: The licence_letter of this GermanSettlement.
        :rtype: List[str]
        """
        return self._licence_letter

    @licence_letter.setter
    def licence_letter(self, licence_letter):
        """Sets the licence_letter of this GermanSettlement.

        Description not available  # noqa: E501

        :param licence_letter: The licence_letter of this GermanSettlement.
        :type licence_letter: List[str]
        """

        self._licence_letter = licence_letter

    @property
    def number_of_neighbourhood(self):
        """Gets the number_of_neighbourhood of this GermanSettlement.

        Description not available  # noqa: E501

        :return: The number_of_neighbourhood of this GermanSettlement.
        :rtype: List[int]
        """
        return self._number_of_neighbourhood

    @number_of_neighbourhood.setter
    def number_of_neighbourhood(self, number_of_neighbourhood):
        """Sets the number_of_neighbourhood of this GermanSettlement.

        Description not available  # noqa: E501

        :param number_of_neighbourhood: The number_of_neighbourhood of this GermanSettlement.
        :type number_of_neighbourhood: List[int]
        """

        self._number_of_neighbourhood = number_of_neighbourhood

    @property
    def description(self):
        """Gets the description of this GermanSettlement.

        small description  # noqa: E501

        :return: The description of this GermanSettlement.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GermanSettlement.

        small description  # noqa: E501

        :param description: The description of this GermanSettlement.
        :type description: List[str]
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GermanSettlement.

        identifier  # noqa: E501

        :return: The id of this GermanSettlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GermanSettlement.

        identifier  # noqa: E501

        :param id: The id of this GermanSettlement.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this GermanSettlement.

        short description of the resource  # noqa: E501

        :return: The label of this GermanSettlement.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GermanSettlement.

        short description of the resource  # noqa: E501

        :param label: The label of this GermanSettlement.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this GermanSettlement.

        type of the resource  # noqa: E501

        :return: The type of this GermanSettlement.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GermanSettlement.

        type of the resource  # noqa: E501

        :param type: The type of this GermanSettlement.
        :type type: List[str]
        """

        self._type = type