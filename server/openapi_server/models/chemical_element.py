# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ChemicalElement(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lethal_on_mice=None, density=None, carcinogen=None, description=None, molecular_weight=None, label=None, type=None, melting_point=None, solvent_with_good_solubility=None, boiling_point=None, lethal_on_chickens=None, lethal_on_rats=None, flash_point=None, lethal_on_rabbits=None, solvent_with_mediocre_solubility=None, solubility=None, formula=None, id=None, solvent_with_bad_solubility=None, not_soluble_in=None):  # noqa: E501
        """ChemicalElement - a model defined in OpenAPI

        :param lethal_on_mice: The lethal_on_mice of this ChemicalElement.  # noqa: E501
        :type lethal_on_mice: List[str]
        :param density: The density of this ChemicalElement.  # noqa: E501
        :type density: List[object]
        :param carcinogen: The carcinogen of this ChemicalElement.  # noqa: E501
        :type carcinogen: List[str]
        :param description: The description of this ChemicalElement.  # noqa: E501
        :type description: List[str]
        :param molecular_weight: The molecular_weight of this ChemicalElement.  # noqa: E501
        :type molecular_weight: List[int]
        :param label: The label of this ChemicalElement.  # noqa: E501
        :type label: List[str]
        :param type: The type of this ChemicalElement.  # noqa: E501
        :type type: List[str]
        :param melting_point: The melting_point of this ChemicalElement.  # noqa: E501
        :type melting_point: List[object]
        :param solvent_with_good_solubility: The solvent_with_good_solubility of this ChemicalElement.  # noqa: E501
        :type solvent_with_good_solubility: List[object]
        :param boiling_point: The boiling_point of this ChemicalElement.  # noqa: E501
        :type boiling_point: List[object]
        :param lethal_on_chickens: The lethal_on_chickens of this ChemicalElement.  # noqa: E501
        :type lethal_on_chickens: List[str]
        :param lethal_on_rats: The lethal_on_rats of this ChemicalElement.  # noqa: E501
        :type lethal_on_rats: List[str]
        :param flash_point: The flash_point of this ChemicalElement.  # noqa: E501
        :type flash_point: List[int]
        :param lethal_on_rabbits: The lethal_on_rabbits of this ChemicalElement.  # noqa: E501
        :type lethal_on_rabbits: List[str]
        :param solvent_with_mediocre_solubility: The solvent_with_mediocre_solubility of this ChemicalElement.  # noqa: E501
        :type solvent_with_mediocre_solubility: List[object]
        :param solubility: The solubility of this ChemicalElement.  # noqa: E501
        :type solubility: List[int]
        :param formula: The formula of this ChemicalElement.  # noqa: E501
        :type formula: List[str]
        :param id: The id of this ChemicalElement.  # noqa: E501
        :type id: str
        :param solvent_with_bad_solubility: The solvent_with_bad_solubility of this ChemicalElement.  # noqa: E501
        :type solvent_with_bad_solubility: List[object]
        :param not_soluble_in: The not_soluble_in of this ChemicalElement.  # noqa: E501
        :type not_soluble_in: List[object]
        """


        self.openapi_types = {
            'lethal_on_mice': List[str],
            'density': List[object],
            'carcinogen': List[str],
            'description': List[str],
            'molecular_weight': List[int],
            'label': List[str],
            'type': List[str],
            'melting_point': List[object],
            'solvent_with_good_solubility': List[object],
            'boiling_point': List[object],
            'lethal_on_chickens': List[str],
            'lethal_on_rats': List[str],
            'flash_point': List[int],
            'lethal_on_rabbits': List[str],
            'solvent_with_mediocre_solubility': List[object],
            'solubility': List[int],
            'formula': List[str],
            'id': str,
            'solvent_with_bad_solubility': List[object],
            'not_soluble_in': List[object]
        }

        self.attribute_map = {
            'lethal_on_mice': 'lethalOnMice',
            'density': 'density',
            'carcinogen': 'carcinogen',
            'description': 'description',
            'molecular_weight': 'molecularWeight',
            'label': 'label',
            'type': 'type',
            'melting_point': 'meltingPoint',
            'solvent_with_good_solubility': 'solventWithGoodSolubility',
            'boiling_point': 'boilingPoint',
            'lethal_on_chickens': 'lethalOnChickens',
            'lethal_on_rats': 'lethalOnRats',
            'flash_point': 'flashPoint',
            'lethal_on_rabbits': 'lethalOnRabbits',
            'solvent_with_mediocre_solubility': 'solventWithMediocreSolubility',
            'solubility': 'solubility',
            'formula': 'formula',
            'id': 'id',
            'solvent_with_bad_solubility': 'solventWithBadSolubility',
            'not_soluble_in': 'notSolubleIn'
        }

        self._lethal_on_mice = lethal_on_mice
        self._density = density
        self._carcinogen = carcinogen
        self._description = description
        self._molecular_weight = molecular_weight
        self._label = label
        self._type = type
        self._melting_point = melting_point
        self._solvent_with_good_solubility = solvent_with_good_solubility
        self._boiling_point = boiling_point
        self._lethal_on_chickens = lethal_on_chickens
        self._lethal_on_rats = lethal_on_rats
        self._flash_point = flash_point
        self._lethal_on_rabbits = lethal_on_rabbits
        self._solvent_with_mediocre_solubility = solvent_with_mediocre_solubility
        self._solubility = solubility
        self._formula = formula
        self._id = id
        self._solvent_with_bad_solubility = solvent_with_bad_solubility
        self._not_soluble_in = not_soluble_in

    @classmethod
    def from_dict(cls, dikt) -> 'ChemicalElement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ChemicalElement of this ChemicalElement.  # noqa: E501
        :rtype: ChemicalElement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lethal_on_mice(self):
        """Gets the lethal_on_mice of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The lethal_on_mice of this ChemicalElement.
        :rtype: List[str]
        """
        return self._lethal_on_mice

    @lethal_on_mice.setter
    def lethal_on_mice(self, lethal_on_mice):
        """Sets the lethal_on_mice of this ChemicalElement.

        Description not available  # noqa: E501

        :param lethal_on_mice: The lethal_on_mice of this ChemicalElement.
        :type lethal_on_mice: List[str]
        """

        self._lethal_on_mice = lethal_on_mice

    @property
    def density(self):
        """Gets the density of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The density of this ChemicalElement.
        :rtype: List[object]
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this ChemicalElement.

        Description not available  # noqa: E501

        :param density: The density of this ChemicalElement.
        :type density: List[object]
        """

        self._density = density

    @property
    def carcinogen(self):
        """Gets the carcinogen of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The carcinogen of this ChemicalElement.
        :rtype: List[str]
        """
        return self._carcinogen

    @carcinogen.setter
    def carcinogen(self, carcinogen):
        """Sets the carcinogen of this ChemicalElement.

        Description not available  # noqa: E501

        :param carcinogen: The carcinogen of this ChemicalElement.
        :type carcinogen: List[str]
        """

        self._carcinogen = carcinogen

    @property
    def description(self):
        """Gets the description of this ChemicalElement.

        small description  # noqa: E501

        :return: The description of this ChemicalElement.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChemicalElement.

        small description  # noqa: E501

        :param description: The description of this ChemicalElement.
        :type description: List[str]
        """

        self._description = description

    @property
    def molecular_weight(self):
        """Gets the molecular_weight of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The molecular_weight of this ChemicalElement.
        :rtype: List[int]
        """
        return self._molecular_weight

    @molecular_weight.setter
    def molecular_weight(self, molecular_weight):
        """Sets the molecular_weight of this ChemicalElement.

        Description not available  # noqa: E501

        :param molecular_weight: The molecular_weight of this ChemicalElement.
        :type molecular_weight: List[int]
        """

        self._molecular_weight = molecular_weight

    @property
    def label(self):
        """Gets the label of this ChemicalElement.

        short description of the resource  # noqa: E501

        :return: The label of this ChemicalElement.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChemicalElement.

        short description of the resource  # noqa: E501

        :param label: The label of this ChemicalElement.
        :type label: List[str]
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this ChemicalElement.

        type of the resource  # noqa: E501

        :return: The type of this ChemicalElement.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChemicalElement.

        type of the resource  # noqa: E501

        :param type: The type of this ChemicalElement.
        :type type: List[str]
        """

        self._type = type

    @property
    def melting_point(self):
        """Gets the melting_point of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The melting_point of this ChemicalElement.
        :rtype: List[object]
        """
        return self._melting_point

    @melting_point.setter
    def melting_point(self, melting_point):
        """Sets the melting_point of this ChemicalElement.

        Description not available  # noqa: E501

        :param melting_point: The melting_point of this ChemicalElement.
        :type melting_point: List[object]
        """

        self._melting_point = melting_point

    @property
    def solvent_with_good_solubility(self):
        """Gets the solvent_with_good_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The solvent_with_good_solubility of this ChemicalElement.
        :rtype: List[object]
        """
        return self._solvent_with_good_solubility

    @solvent_with_good_solubility.setter
    def solvent_with_good_solubility(self, solvent_with_good_solubility):
        """Sets the solvent_with_good_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :param solvent_with_good_solubility: The solvent_with_good_solubility of this ChemicalElement.
        :type solvent_with_good_solubility: List[object]
        """

        self._solvent_with_good_solubility = solvent_with_good_solubility

    @property
    def boiling_point(self):
        """Gets the boiling_point of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The boiling_point of this ChemicalElement.
        :rtype: List[object]
        """
        return self._boiling_point

    @boiling_point.setter
    def boiling_point(self, boiling_point):
        """Sets the boiling_point of this ChemicalElement.

        Description not available  # noqa: E501

        :param boiling_point: The boiling_point of this ChemicalElement.
        :type boiling_point: List[object]
        """

        self._boiling_point = boiling_point

    @property
    def lethal_on_chickens(self):
        """Gets the lethal_on_chickens of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The lethal_on_chickens of this ChemicalElement.
        :rtype: List[str]
        """
        return self._lethal_on_chickens

    @lethal_on_chickens.setter
    def lethal_on_chickens(self, lethal_on_chickens):
        """Sets the lethal_on_chickens of this ChemicalElement.

        Description not available  # noqa: E501

        :param lethal_on_chickens: The lethal_on_chickens of this ChemicalElement.
        :type lethal_on_chickens: List[str]
        """

        self._lethal_on_chickens = lethal_on_chickens

    @property
    def lethal_on_rats(self):
        """Gets the lethal_on_rats of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The lethal_on_rats of this ChemicalElement.
        :rtype: List[str]
        """
        return self._lethal_on_rats

    @lethal_on_rats.setter
    def lethal_on_rats(self, lethal_on_rats):
        """Sets the lethal_on_rats of this ChemicalElement.

        Description not available  # noqa: E501

        :param lethal_on_rats: The lethal_on_rats of this ChemicalElement.
        :type lethal_on_rats: List[str]
        """

        self._lethal_on_rats = lethal_on_rats

    @property
    def flash_point(self):
        """Gets the flash_point of this ChemicalElement.

        lowest temperature at which a substance can vaporize and start burning  # noqa: E501

        :return: The flash_point of this ChemicalElement.
        :rtype: List[int]
        """
        return self._flash_point

    @flash_point.setter
    def flash_point(self, flash_point):
        """Sets the flash_point of this ChemicalElement.

        lowest temperature at which a substance can vaporize and start burning  # noqa: E501

        :param flash_point: The flash_point of this ChemicalElement.
        :type flash_point: List[int]
        """

        self._flash_point = flash_point

    @property
    def lethal_on_rabbits(self):
        """Gets the lethal_on_rabbits of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The lethal_on_rabbits of this ChemicalElement.
        :rtype: List[str]
        """
        return self._lethal_on_rabbits

    @lethal_on_rabbits.setter
    def lethal_on_rabbits(self, lethal_on_rabbits):
        """Sets the lethal_on_rabbits of this ChemicalElement.

        Description not available  # noqa: E501

        :param lethal_on_rabbits: The lethal_on_rabbits of this ChemicalElement.
        :type lethal_on_rabbits: List[str]
        """

        self._lethal_on_rabbits = lethal_on_rabbits

    @property
    def solvent_with_mediocre_solubility(self):
        """Gets the solvent_with_mediocre_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The solvent_with_mediocre_solubility of this ChemicalElement.
        :rtype: List[object]
        """
        return self._solvent_with_mediocre_solubility

    @solvent_with_mediocre_solubility.setter
    def solvent_with_mediocre_solubility(self, solvent_with_mediocre_solubility):
        """Sets the solvent_with_mediocre_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :param solvent_with_mediocre_solubility: The solvent_with_mediocre_solubility of this ChemicalElement.
        :type solvent_with_mediocre_solubility: List[object]
        """

        self._solvent_with_mediocre_solubility = solvent_with_mediocre_solubility

    @property
    def solubility(self):
        """Gets the solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The solubility of this ChemicalElement.
        :rtype: List[int]
        """
        return self._solubility

    @solubility.setter
    def solubility(self, solubility):
        """Sets the solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :param solubility: The solubility of this ChemicalElement.
        :type solubility: List[int]
        """

        self._solubility = solubility

    @property
    def formula(self):
        """Gets the formula of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The formula of this ChemicalElement.
        :rtype: List[str]
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this ChemicalElement.

        Description not available  # noqa: E501

        :param formula: The formula of this ChemicalElement.
        :type formula: List[str]
        """

        self._formula = formula

    @property
    def id(self):
        """Gets the id of this ChemicalElement.

        identifier  # noqa: E501

        :return: The id of this ChemicalElement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChemicalElement.

        identifier  # noqa: E501

        :param id: The id of this ChemicalElement.
        :type id: str
        """

        self._id = id

    @property
    def solvent_with_bad_solubility(self):
        """Gets the solvent_with_bad_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The solvent_with_bad_solubility of this ChemicalElement.
        :rtype: List[object]
        """
        return self._solvent_with_bad_solubility

    @solvent_with_bad_solubility.setter
    def solvent_with_bad_solubility(self, solvent_with_bad_solubility):
        """Sets the solvent_with_bad_solubility of this ChemicalElement.

        Description not available  # noqa: E501

        :param solvent_with_bad_solubility: The solvent_with_bad_solubility of this ChemicalElement.
        :type solvent_with_bad_solubility: List[object]
        """

        self._solvent_with_bad_solubility = solvent_with_bad_solubility

    @property
    def not_soluble_in(self):
        """Gets the not_soluble_in of this ChemicalElement.

        Description not available  # noqa: E501

        :return: The not_soluble_in of this ChemicalElement.
        :rtype: List[object]
        """
        return self._not_soluble_in

    @not_soluble_in.setter
    def not_soluble_in(self, not_soluble_in):
        """Sets the not_soluble_in of this ChemicalElement.

        Description not available  # noqa: E501

        :param not_soluble_in: The not_soluble_in of this ChemicalElement.
        :type not_soluble_in: List[object]
        """

        self._not_soluble_in = not_soluble_in