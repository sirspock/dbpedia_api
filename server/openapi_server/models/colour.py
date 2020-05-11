# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Colour(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, hsv_coordinate_saturation=None, wavelength=None, rgb_coordinate_red=None, description=None, label=None, hsv_coordinate_hue=None, type=None, rgb_coordinate_blue=None, cmyk_coordinate_cyanic=None, hsv_coordinate_value=None, id=None, cmyk_coordinate_black=None, cmyk_coordinate_yellow=None, cmyk_coordinate_magenta=None, rgb_coordinate_green=None):  # noqa: E501
        """Colour - a model defined in OpenAPI

        :param hsv_coordinate_saturation: The hsv_coordinate_saturation of this Colour.  # noqa: E501
        :type hsv_coordinate_saturation: List[int]
        :param wavelength: The wavelength of this Colour.  # noqa: E501
        :type wavelength: List[float]
        :param rgb_coordinate_red: The rgb_coordinate_red of this Colour.  # noqa: E501
        :type rgb_coordinate_red: List[int]
        :param description: The description of this Colour.  # noqa: E501
        :type description: List[str]
        :param label: The label of this Colour.  # noqa: E501
        :type label: List[str]
        :param hsv_coordinate_hue: The hsv_coordinate_hue of this Colour.  # noqa: E501
        :type hsv_coordinate_hue: List[int]
        :param type: The type of this Colour.  # noqa: E501
        :type type: List[str]
        :param rgb_coordinate_blue: The rgb_coordinate_blue of this Colour.  # noqa: E501
        :type rgb_coordinate_blue: List[int]
        :param cmyk_coordinate_cyanic: The cmyk_coordinate_cyanic of this Colour.  # noqa: E501
        :type cmyk_coordinate_cyanic: List[int]
        :param hsv_coordinate_value: The hsv_coordinate_value of this Colour.  # noqa: E501
        :type hsv_coordinate_value: List[int]
        :param id: The id of this Colour.  # noqa: E501
        :type id: str
        :param cmyk_coordinate_black: The cmyk_coordinate_black of this Colour.  # noqa: E501
        :type cmyk_coordinate_black: List[int]
        :param cmyk_coordinate_yellow: The cmyk_coordinate_yellow of this Colour.  # noqa: E501
        :type cmyk_coordinate_yellow: List[int]
        :param cmyk_coordinate_magenta: The cmyk_coordinate_magenta of this Colour.  # noqa: E501
        :type cmyk_coordinate_magenta: List[int]
        :param rgb_coordinate_green: The rgb_coordinate_green of this Colour.  # noqa: E501
        :type rgb_coordinate_green: List[int]
        """


        self.openapi_types = {
            'hsv_coordinate_saturation': List[int],
            'wavelength': List[float],
            'rgb_coordinate_red': List[int],
            'description': List[str],
            'label': List[str],
            'hsv_coordinate_hue': List[int],
            'type': List[str],
            'rgb_coordinate_blue': List[int],
            'cmyk_coordinate_cyanic': List[int],
            'hsv_coordinate_value': List[int],
            'id': str,
            'cmyk_coordinate_black': List[int],
            'cmyk_coordinate_yellow': List[int],
            'cmyk_coordinate_magenta': List[int],
            'rgb_coordinate_green': List[int]
        }

        self.attribute_map = {
            'hsv_coordinate_saturation': 'hsvCoordinateSaturation',
            'wavelength': 'wavelength',
            'rgb_coordinate_red': 'rgbCoordinateRed',
            'description': 'description',
            'label': 'label',
            'hsv_coordinate_hue': 'hsvCoordinateHue',
            'type': 'type',
            'rgb_coordinate_blue': 'rgbCoordinateBlue',
            'cmyk_coordinate_cyanic': 'cmykCoordinateCyanic',
            'hsv_coordinate_value': 'hsvCoordinateValue',
            'id': 'id',
            'cmyk_coordinate_black': 'cmykCoordinateBlack',
            'cmyk_coordinate_yellow': 'cmykCoordinateYellow',
            'cmyk_coordinate_magenta': 'cmykCoordinateMagenta',
            'rgb_coordinate_green': 'rgbCoordinateGreen'
        }

        self._hsv_coordinate_saturation = hsv_coordinate_saturation
        self._wavelength = wavelength
        self._rgb_coordinate_red = rgb_coordinate_red
        self._description = description
        self._label = label
        self._hsv_coordinate_hue = hsv_coordinate_hue
        self._type = type
        self._rgb_coordinate_blue = rgb_coordinate_blue
        self._cmyk_coordinate_cyanic = cmyk_coordinate_cyanic
        self._hsv_coordinate_value = hsv_coordinate_value
        self._id = id
        self._cmyk_coordinate_black = cmyk_coordinate_black
        self._cmyk_coordinate_yellow = cmyk_coordinate_yellow
        self._cmyk_coordinate_magenta = cmyk_coordinate_magenta
        self._rgb_coordinate_green = rgb_coordinate_green

    @classmethod
    def from_dict(cls, dikt) -> 'Colour':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Colour of this Colour.  # noqa: E501
        :rtype: Colour
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hsv_coordinate_saturation(self):
        """Gets the hsv_coordinate_saturation of this Colour.

        Description not available  # noqa: E501

        :return: The hsv_coordinate_saturation of this Colour.
        :rtype: List[int]
        """
        return self._hsv_coordinate_saturation

    @hsv_coordinate_saturation.setter
    def hsv_coordinate_saturation(self, hsv_coordinate_saturation):
        """Sets the hsv_coordinate_saturation of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_saturation: The hsv_coordinate_saturation of this Colour.
        :type hsv_coordinate_saturation: List[int]
        """

        self._hsv_coordinate_saturation = hsv_coordinate_saturation

    @property
    def wavelength(self):
        """Gets the wavelength of this Colour.

        Description not available  # noqa: E501

        :return: The wavelength of this Colour.
        :rtype: List[float]
        """
        return self._wavelength

    @wavelength.setter
    def wavelength(self, wavelength):
        """Sets the wavelength of this Colour.

        Description not available  # noqa: E501

        :param wavelength: The wavelength of this Colour.
        :type wavelength: List[float]
        """

        self._wavelength = wavelength

    @property
    def rgb_coordinate_red(self):
        """Gets the rgb_coordinate_red of this Colour.

        Description not available  # noqa: E501

        :return: The rgb_coordinate_red of this Colour.
        :rtype: List[int]
        """
        return self._rgb_coordinate_red

    @rgb_coordinate_red.setter
    def rgb_coordinate_red(self, rgb_coordinate_red):
        """Sets the rgb_coordinate_red of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_red: The rgb_coordinate_red of this Colour.
        :type rgb_coordinate_red: List[int]
        """

        self._rgb_coordinate_red = rgb_coordinate_red

    @property
    def description(self):
        """Gets the description of this Colour.

        small description  # noqa: E501

        :return: The description of this Colour.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Colour.

        small description  # noqa: E501

        :param description: The description of this Colour.
        :type description: List[str]
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this Colour.

        short description of the resource  # noqa: E501

        :return: The label of this Colour.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Colour.

        short description of the resource  # noqa: E501

        :param label: The label of this Colour.
        :type label: List[str]
        """

        self._label = label

    @property
    def hsv_coordinate_hue(self):
        """Gets the hsv_coordinate_hue of this Colour.

        Description not available  # noqa: E501

        :return: The hsv_coordinate_hue of this Colour.
        :rtype: List[int]
        """
        return self._hsv_coordinate_hue

    @hsv_coordinate_hue.setter
    def hsv_coordinate_hue(self, hsv_coordinate_hue):
        """Sets the hsv_coordinate_hue of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_hue: The hsv_coordinate_hue of this Colour.
        :type hsv_coordinate_hue: List[int]
        """

        self._hsv_coordinate_hue = hsv_coordinate_hue

    @property
    def type(self):
        """Gets the type of this Colour.

        type of the resource  # noqa: E501

        :return: The type of this Colour.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Colour.

        type of the resource  # noqa: E501

        :param type: The type of this Colour.
        :type type: List[str]
        """

        self._type = type

    @property
    def rgb_coordinate_blue(self):
        """Gets the rgb_coordinate_blue of this Colour.

        Description not available  # noqa: E501

        :return: The rgb_coordinate_blue of this Colour.
        :rtype: List[int]
        """
        return self._rgb_coordinate_blue

    @rgb_coordinate_blue.setter
    def rgb_coordinate_blue(self, rgb_coordinate_blue):
        """Sets the rgb_coordinate_blue of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_blue: The rgb_coordinate_blue of this Colour.
        :type rgb_coordinate_blue: List[int]
        """

        self._rgb_coordinate_blue = rgb_coordinate_blue

    @property
    def cmyk_coordinate_cyanic(self):
        """Gets the cmyk_coordinate_cyanic of this Colour.

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_cyanic of this Colour.
        :rtype: List[int]
        """
        return self._cmyk_coordinate_cyanic

    @cmyk_coordinate_cyanic.setter
    def cmyk_coordinate_cyanic(self, cmyk_coordinate_cyanic):
        """Sets the cmyk_coordinate_cyanic of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_cyanic: The cmyk_coordinate_cyanic of this Colour.
        :type cmyk_coordinate_cyanic: List[int]
        """

        self._cmyk_coordinate_cyanic = cmyk_coordinate_cyanic

    @property
    def hsv_coordinate_value(self):
        """Gets the hsv_coordinate_value of this Colour.

        Description not available  # noqa: E501

        :return: The hsv_coordinate_value of this Colour.
        :rtype: List[int]
        """
        return self._hsv_coordinate_value

    @hsv_coordinate_value.setter
    def hsv_coordinate_value(self, hsv_coordinate_value):
        """Sets the hsv_coordinate_value of this Colour.

        Description not available  # noqa: E501

        :param hsv_coordinate_value: The hsv_coordinate_value of this Colour.
        :type hsv_coordinate_value: List[int]
        """

        self._hsv_coordinate_value = hsv_coordinate_value

    @property
    def id(self):
        """Gets the id of this Colour.

        identifier  # noqa: E501

        :return: The id of this Colour.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Colour.

        identifier  # noqa: E501

        :param id: The id of this Colour.
        :type id: str
        """

        self._id = id

    @property
    def cmyk_coordinate_black(self):
        """Gets the cmyk_coordinate_black of this Colour.

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_black of this Colour.
        :rtype: List[int]
        """
        return self._cmyk_coordinate_black

    @cmyk_coordinate_black.setter
    def cmyk_coordinate_black(self, cmyk_coordinate_black):
        """Sets the cmyk_coordinate_black of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_black: The cmyk_coordinate_black of this Colour.
        :type cmyk_coordinate_black: List[int]
        """

        self._cmyk_coordinate_black = cmyk_coordinate_black

    @property
    def cmyk_coordinate_yellow(self):
        """Gets the cmyk_coordinate_yellow of this Colour.

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_yellow of this Colour.
        :rtype: List[int]
        """
        return self._cmyk_coordinate_yellow

    @cmyk_coordinate_yellow.setter
    def cmyk_coordinate_yellow(self, cmyk_coordinate_yellow):
        """Sets the cmyk_coordinate_yellow of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_yellow: The cmyk_coordinate_yellow of this Colour.
        :type cmyk_coordinate_yellow: List[int]
        """

        self._cmyk_coordinate_yellow = cmyk_coordinate_yellow

    @property
    def cmyk_coordinate_magenta(self):
        """Gets the cmyk_coordinate_magenta of this Colour.

        Description not available  # noqa: E501

        :return: The cmyk_coordinate_magenta of this Colour.
        :rtype: List[int]
        """
        return self._cmyk_coordinate_magenta

    @cmyk_coordinate_magenta.setter
    def cmyk_coordinate_magenta(self, cmyk_coordinate_magenta):
        """Sets the cmyk_coordinate_magenta of this Colour.

        Description not available  # noqa: E501

        :param cmyk_coordinate_magenta: The cmyk_coordinate_magenta of this Colour.
        :type cmyk_coordinate_magenta: List[int]
        """

        self._cmyk_coordinate_magenta = cmyk_coordinate_magenta

    @property
    def rgb_coordinate_green(self):
        """Gets the rgb_coordinate_green of this Colour.

        Description not available  # noqa: E501

        :return: The rgb_coordinate_green of this Colour.
        :rtype: List[int]
        """
        return self._rgb_coordinate_green

    @rgb_coordinate_green.setter
    def rgb_coordinate_green(self, rgb_coordinate_green):
        """Sets the rgb_coordinate_green of this Colour.

        Description not available  # noqa: E501

        :param rgb_coordinate_green: The rgb_coordinate_green of this Colour.
        :type rgb_coordinate_green: List[int]
        """

        self._rgb_coordinate_green = rgb_coordinate_green