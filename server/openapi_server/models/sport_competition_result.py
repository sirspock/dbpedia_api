# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SportCompetitionResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number_of_bronze_medals_won=None, description=None, number_of_silver_medals_won=None, competition=None, id=None, label=None, type=None, number_of_gold_medals_won=None):  # noqa: E501
        """SportCompetitionResult - a model defined in OpenAPI

        :param number_of_bronze_medals_won: The number_of_bronze_medals_won of this SportCompetitionResult.  # noqa: E501
        :type number_of_bronze_medals_won: List[int]
        :param description: The description of this SportCompetitionResult.  # noqa: E501
        :type description: List[str]
        :param number_of_silver_medals_won: The number_of_silver_medals_won of this SportCompetitionResult.  # noqa: E501
        :type number_of_silver_medals_won: List[int]
        :param competition: The competition of this SportCompetitionResult.  # noqa: E501
        :type competition: List[object]
        :param id: The id of this SportCompetitionResult.  # noqa: E501
        :type id: str
        :param label: The label of this SportCompetitionResult.  # noqa: E501
        :type label: List[str]
        :param type: The type of this SportCompetitionResult.  # noqa: E501
        :type type: List[str]
        :param number_of_gold_medals_won: The number_of_gold_medals_won of this SportCompetitionResult.  # noqa: E501
        :type number_of_gold_medals_won: List[int]
        """


        self.openapi_types = {
            'number_of_bronze_medals_won': List[int],
            'description': List[str],
            'number_of_silver_medals_won': List[int],
            'competition': List[object],
            'id': str,
            'label': List[str],
            'type': List[str],
            'number_of_gold_medals_won': List[int]
        }

        self.attribute_map = {
            'number_of_bronze_medals_won': 'numberOfBronzeMedalsWon',
            'description': 'description',
            'number_of_silver_medals_won': 'numberOfSilverMedalsWon',
            'competition': 'competition',
            'id': 'id',
            'label': 'label',
            'type': 'type',
            'number_of_gold_medals_won': 'numberOfGoldMedalsWon'
        }

        self._number_of_bronze_medals_won = number_of_bronze_medals_won
        self._description = description
        self._number_of_silver_medals_won = number_of_silver_medals_won
        self._competition = competition
        self._id = id
        self._label = label
        self._type = type
        self._number_of_gold_medals_won = number_of_gold_medals_won

    @classmethod
    def from_dict(cls, dikt) -> 'SportCompetitionResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SportCompetitionResult of this SportCompetitionResult.  # noqa: E501
        :rtype: SportCompetitionResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number_of_bronze_medals_won(self):
        """Gets the number_of_bronze_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :return: The number_of_bronze_medals_won of this SportCompetitionResult.
        :rtype: List[int]
        """
        return self._number_of_bronze_medals_won

    @number_of_bronze_medals_won.setter
    def number_of_bronze_medals_won(self, number_of_bronze_medals_won):
        """Sets the number_of_bronze_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :param number_of_bronze_medals_won: The number_of_bronze_medals_won of this SportCompetitionResult.
        :type number_of_bronze_medals_won: List[int]
        """

        self._number_of_bronze_medals_won = number_of_bronze_medals_won

    @property
    def description(self):
        """Gets the description of this SportCompetitionResult.

        small description  # noqa: E501

        :return: The description of this SportCompetitionResult.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SportCompetitionResult.

        small description  # noqa: E501

        :param description: The description of this SportCompetitionResult.
        :type description: List[str]
        """

        self._description = description

    @property
    def number_of_silver_medals_won(self):
        """Gets the number_of_silver_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :return: The number_of_silver_medals_won of this SportCompetitionResult.
        :rtype: List[int]
        """
        return self._number_of_silver_medals_won

    @number_of_silver_medals_won.setter
    def number_of_silver_medals_won(self, number_of_silver_medals_won):
        """Sets the number_of_silver_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :param number_of_silver_medals_won: The number_of_silver_medals_won of this SportCompetitionResult.
        :type number_of_silver_medals_won: List[int]
        """

        self._number_of_silver_medals_won = number_of_silver_medals_won

    @property
    def competition(self):
        """Gets the competition of this SportCompetitionResult.

        Description not available  # noqa: E501

        :return: The competition of this SportCompetitionResult.
        :rtype: List[object]
        """
        return self._competition

    @competition.setter
    def competition(self, competition):
        """Sets the competition of this SportCompetitionResult.

        Description not available  # noqa: E501

        :param competition: The competition of this SportCompetitionResult.
        :type competition: List[object]
        """

        self._competition = competition

    @property
    def id(self):
        """Gets the id of this SportCompetitionResult.

        identifier  # noqa: E501

        :return: The id of this SportCompetitionResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SportCompetitionResult.

        identifier  # noqa: E501

        :param id: The id of this SportCompetitionResult.
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this SportCompetitionResult.

        short description of the resource  # noqa: E501

        :return: The label of this SportCompetitionResult.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SportCompetitionResult.

        short description of the resource  # noqa: E501

        :param label: The label of this SportCompetitionResult.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this SportCompetitionResult.

        type of the resource  # noqa: E501

        :return: The type of this SportCompetitionResult.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SportCompetitionResult.

        type of the resource  # noqa: E501

        :param type: The type of this SportCompetitionResult.
        :type type: List[str]
        """

        self._type = type

    @property
    def number_of_gold_medals_won(self):
        """Gets the number_of_gold_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :return: The number_of_gold_medals_won of this SportCompetitionResult.
        :rtype: List[int]
        """
        return self._number_of_gold_medals_won

    @number_of_gold_medals_won.setter
    def number_of_gold_medals_won(self, number_of_gold_medals_won):
        """Sets the number_of_gold_medals_won of this SportCompetitionResult.

        Description not available  # noqa: E501

        :param number_of_gold_medals_won: The number_of_gold_medals_won of this SportCompetitionResult.
        :type number_of_gold_medals_won: List[int]
        """

        self._number_of_gold_medals_won = number_of_gold_medals_won