# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Planet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, mean_radius=None, orbital_period=None, discovered=None, surface_area=None, orbital_eccentricity=None, mass=None, description=None, epoch=None, type=None, max_absolute_magnitude=None, mean_temperature=None, escape_velocity=None, von_klitzing_constant=None, maximum_temperature=None, temperature=None, apparent_magnitude=None, satellite=None, id=None, albedo=None, periapsis=None, absolute_magnitude=None, density=None, detection_method=None, average_speed=None, label=None, apoapsis=None, volume=None, surface_gravity=None, rotation_period=None, messier_name=None, max_apparent_magnitude=None, minimum_temperature=None, ngc_name=None):  # noqa: E501
        """Planet - a model defined in OpenAPI

        :param mean_radius: The mean_radius of this Planet.  # noqa: E501
        :type mean_radius: List[object]
        :param orbital_period: The orbital_period of this Planet.  # noqa: E501
        :type orbital_period: List[object]
        :param discovered: The discovered of this Planet.  # noqa: E501
        :type discovered: List[str]
        :param surface_area: The surface_area of this Planet.  # noqa: E501
        :type surface_area: List[object]
        :param orbital_eccentricity: The orbital_eccentricity of this Planet.  # noqa: E501
        :type orbital_eccentricity: List[float]
        :param mass: The mass of this Planet.  # noqa: E501
        :type mass: List[object]
        :param description: The description of this Planet.  # noqa: E501
        :type description: List[str]
        :param epoch: The epoch of this Planet.  # noqa: E501
        :type epoch: List[str]
        :param type: The type of this Planet.  # noqa: E501
        :type type: List[str]
        :param max_absolute_magnitude: The max_absolute_magnitude of this Planet.  # noqa: E501
        :type max_absolute_magnitude: List[float]
        :param mean_temperature: The mean_temperature of this Planet.  # noqa: E501
        :type mean_temperature: List[object]
        :param escape_velocity: The escape_velocity of this Planet.  # noqa: E501
        :type escape_velocity: List[float]
        :param von_klitzing_constant: The von_klitzing_constant of this Planet.  # noqa: E501
        :type von_klitzing_constant: List[float]
        :param maximum_temperature: The maximum_temperature of this Planet.  # noqa: E501
        :type maximum_temperature: List[object]
        :param temperature: The temperature of this Planet.  # noqa: E501
        :type temperature: List[object]
        :param apparent_magnitude: The apparent_magnitude of this Planet.  # noqa: E501
        :type apparent_magnitude: List[float]
        :param satellite: The satellite of this Planet.  # noqa: E501
        :type satellite: List[str]
        :param id: The id of this Planet.  # noqa: E501
        :type id: str
        :param albedo: The albedo of this Planet.  # noqa: E501
        :type albedo: List[float]
        :param periapsis: The periapsis of this Planet.  # noqa: E501
        :type periapsis: List[object]
        :param absolute_magnitude: The absolute_magnitude of this Planet.  # noqa: E501
        :type absolute_magnitude: List[float]
        :param density: The density of this Planet.  # noqa: E501
        :type density: List[object]
        :param detection_method: The detection_method of this Planet.  # noqa: E501
        :type detection_method: List[str]
        :param average_speed: The average_speed of this Planet.  # noqa: E501
        :type average_speed: List[object]
        :param label: The label of this Planet.  # noqa: E501
        :type label: List[str]
        :param apoapsis: The apoapsis of this Planet.  # noqa: E501
        :type apoapsis: List[object]
        :param volume: The volume of this Planet.  # noqa: E501
        :type volume: List[object]
        :param surface_gravity: The surface_gravity of this Planet.  # noqa: E501
        :type surface_gravity: List[float]
        :param rotation_period: The rotation_period of this Planet.  # noqa: E501
        :type rotation_period: List[float]
        :param messier_name: The messier_name of this Planet.  # noqa: E501
        :type messier_name: List[str]
        :param max_apparent_magnitude: The max_apparent_magnitude of this Planet.  # noqa: E501
        :type max_apparent_magnitude: List[float]
        :param minimum_temperature: The minimum_temperature of this Planet.  # noqa: E501
        :type minimum_temperature: List[object]
        :param ngc_name: The ngc_name of this Planet.  # noqa: E501
        :type ngc_name: List[str]
        """


        self.openapi_types = {
            'mean_radius': List[object],
            'orbital_period': List[object],
            'discovered': List[str],
            'surface_area': List[object],
            'orbital_eccentricity': List[float],
            'mass': List[object],
            'description': List[str],
            'epoch': List[str],
            'type': List[str],
            'max_absolute_magnitude': List[float],
            'mean_temperature': List[object],
            'escape_velocity': List[float],
            'von_klitzing_constant': List[float],
            'maximum_temperature': List[object],
            'temperature': List[object],
            'apparent_magnitude': List[float],
            'satellite': List[str],
            'id': str,
            'albedo': List[float],
            'periapsis': List[object],
            'absolute_magnitude': List[float],
            'density': List[object],
            'detection_method': List[str],
            'average_speed': List[object],
            'label': List[str],
            'apoapsis': List[object],
            'volume': List[object],
            'surface_gravity': List[float],
            'rotation_period': List[float],
            'messier_name': List[str],
            'max_apparent_magnitude': List[float],
            'minimum_temperature': List[object],
            'ngc_name': List[str]
        }

        self.attribute_map = {
            'mean_radius': 'meanRadius',
            'orbital_period': 'orbitalPeriod',
            'discovered': 'discovered',
            'surface_area': 'surfaceArea',
            'orbital_eccentricity': 'orbitalEccentricity',
            'mass': 'mass',
            'description': 'description',
            'epoch': 'epoch',
            'type': 'type',
            'max_absolute_magnitude': 'maxAbsoluteMagnitude',
            'mean_temperature': 'meanTemperature',
            'escape_velocity': 'escapeVelocity',
            'von_klitzing_constant': 'vonKlitzingConstant',
            'maximum_temperature': 'maximumTemperature',
            'temperature': 'temperature',
            'apparent_magnitude': 'apparentMagnitude',
            'satellite': 'satellite',
            'id': 'id',
            'albedo': 'albedo',
            'periapsis': 'periapsis',
            'absolute_magnitude': 'absoluteMagnitude',
            'density': 'density',
            'detection_method': 'detectionMethod',
            'average_speed': 'averageSpeed',
            'label': 'label',
            'apoapsis': 'apoapsis',
            'volume': 'volume',
            'surface_gravity': 'surfaceGravity',
            'rotation_period': 'rotationPeriod',
            'messier_name': 'messierName',
            'max_apparent_magnitude': 'maxApparentMagnitude',
            'minimum_temperature': 'minimumTemperature',
            'ngc_name': 'ngcName'
        }

        self._mean_radius = mean_radius
        self._orbital_period = orbital_period
        self._discovered = discovered
        self._surface_area = surface_area
        self._orbital_eccentricity = orbital_eccentricity
        self._mass = mass
        self._description = description
        self._epoch = epoch
        self._type = type
        self._max_absolute_magnitude = max_absolute_magnitude
        self._mean_temperature = mean_temperature
        self._escape_velocity = escape_velocity
        self._von_klitzing_constant = von_klitzing_constant
        self._maximum_temperature = maximum_temperature
        self._temperature = temperature
        self._apparent_magnitude = apparent_magnitude
        self._satellite = satellite
        self._id = id
        self._albedo = albedo
        self._periapsis = periapsis
        self._absolute_magnitude = absolute_magnitude
        self._density = density
        self._detection_method = detection_method
        self._average_speed = average_speed
        self._label = label
        self._apoapsis = apoapsis
        self._volume = volume
        self._surface_gravity = surface_gravity
        self._rotation_period = rotation_period
        self._messier_name = messier_name
        self._max_apparent_magnitude = max_apparent_magnitude
        self._minimum_temperature = minimum_temperature
        self._ngc_name = ngc_name

    @classmethod
    def from_dict(cls, dikt) -> 'Planet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Planet of this Planet.  # noqa: E501
        :rtype: Planet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mean_radius(self):
        """Gets the mean_radius of this Planet.

        Description not available  # noqa: E501

        :return: The mean_radius of this Planet.
        :rtype: List[object]
        """
        return self._mean_radius

    @mean_radius.setter
    def mean_radius(self, mean_radius):
        """Sets the mean_radius of this Planet.

        Description not available  # noqa: E501

        :param mean_radius: The mean_radius of this Planet.
        :type mean_radius: List[object]
        """

        self._mean_radius = mean_radius

    @property
    def orbital_period(self):
        """Gets the orbital_period of this Planet.

        Description not available  # noqa: E501

        :return: The orbital_period of this Planet.
        :rtype: List[object]
        """
        return self._orbital_period

    @orbital_period.setter
    def orbital_period(self, orbital_period):
        """Sets the orbital_period of this Planet.

        Description not available  # noqa: E501

        :param orbital_period: The orbital_period of this Planet.
        :type orbital_period: List[object]
        """

        self._orbital_period = orbital_period

    @property
    def discovered(self):
        """Gets the discovered of this Planet.

        Description not available  # noqa: E501

        :return: The discovered of this Planet.
        :rtype: List[str]
        """
        return self._discovered

    @discovered.setter
    def discovered(self, discovered):
        """Sets the discovered of this Planet.

        Description not available  # noqa: E501

        :param discovered: The discovered of this Planet.
        :type discovered: List[str]
        """

        self._discovered = discovered

    @property
    def surface_area(self):
        """Gets the surface_area of this Planet.

        Description not available  # noqa: E501

        :return: The surface_area of this Planet.
        :rtype: List[object]
        """
        return self._surface_area

    @surface_area.setter
    def surface_area(self, surface_area):
        """Sets the surface_area of this Planet.

        Description not available  # noqa: E501

        :param surface_area: The surface_area of this Planet.
        :type surface_area: List[object]
        """

        self._surface_area = surface_area

    @property
    def orbital_eccentricity(self):
        """Gets the orbital_eccentricity of this Planet.

        Description not available  # noqa: E501

        :return: The orbital_eccentricity of this Planet.
        :rtype: List[float]
        """
        return self._orbital_eccentricity

    @orbital_eccentricity.setter
    def orbital_eccentricity(self, orbital_eccentricity):
        """Sets the orbital_eccentricity of this Planet.

        Description not available  # noqa: E501

        :param orbital_eccentricity: The orbital_eccentricity of this Planet.
        :type orbital_eccentricity: List[float]
        """

        self._orbital_eccentricity = orbital_eccentricity

    @property
    def mass(self):
        """Gets the mass of this Planet.

        Description not available  # noqa: E501

        :return: The mass of this Planet.
        :rtype: List[object]
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        """Sets the mass of this Planet.

        Description not available  # noqa: E501

        :param mass: The mass of this Planet.
        :type mass: List[object]
        """

        self._mass = mass

    @property
    def description(self):
        """Gets the description of this Planet.

        small description  # noqa: E501

        :return: The description of this Planet.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Planet.

        small description  # noqa: E501

        :param description: The description of this Planet.
        :type description: List[str]
        """

        self._description = description

    @property
    def epoch(self):
        """Gets the epoch of this Planet.

        moment in time used as a referrence point for some time-vaying astronomical quantity  # noqa: E501

        :return: The epoch of this Planet.
        :rtype: List[str]
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this Planet.

        moment in time used as a referrence point for some time-vaying astronomical quantity  # noqa: E501

        :param epoch: The epoch of this Planet.
        :type epoch: List[str]
        """

        self._epoch = epoch

    @property
    def type(self):
        """Gets the type of this Planet.

        type of the resource  # noqa: E501

        :return: The type of this Planet.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Planet.

        type of the resource  # noqa: E501

        :param type: The type of this Planet.
        :type type: List[str]
        """

        self._type = type

    @property
    def max_absolute_magnitude(self):
        """Gets the max_absolute_magnitude of this Planet.

        Description not available  # noqa: E501

        :return: The max_absolute_magnitude of this Planet.
        :rtype: List[float]
        """
        return self._max_absolute_magnitude

    @max_absolute_magnitude.setter
    def max_absolute_magnitude(self, max_absolute_magnitude):
        """Sets the max_absolute_magnitude of this Planet.

        Description not available  # noqa: E501

        :param max_absolute_magnitude: The max_absolute_magnitude of this Planet.
        :type max_absolute_magnitude: List[float]
        """

        self._max_absolute_magnitude = max_absolute_magnitude

    @property
    def mean_temperature(self):
        """Gets the mean_temperature of this Planet.

        Description not available  # noqa: E501

        :return: The mean_temperature of this Planet.
        :rtype: List[object]
        """
        return self._mean_temperature

    @mean_temperature.setter
    def mean_temperature(self, mean_temperature):
        """Sets the mean_temperature of this Planet.

        Description not available  # noqa: E501

        :param mean_temperature: The mean_temperature of this Planet.
        :type mean_temperature: List[object]
        """

        self._mean_temperature = mean_temperature

    @property
    def escape_velocity(self):
        """Gets the escape_velocity of this Planet.

        Description not available  # noqa: E501

        :return: The escape_velocity of this Planet.
        :rtype: List[float]
        """
        return self._escape_velocity

    @escape_velocity.setter
    def escape_velocity(self, escape_velocity):
        """Sets the escape_velocity of this Planet.

        Description not available  # noqa: E501

        :param escape_velocity: The escape_velocity of this Planet.
        :type escape_velocity: List[float]
        """

        self._escape_velocity = escape_velocity

    @property
    def von_klitzing_constant(self):
        """Gets the von_klitzing_constant of this Planet.

        Description not available  # noqa: E501

        :return: The von_klitzing_constant of this Planet.
        :rtype: List[float]
        """
        return self._von_klitzing_constant

    @von_klitzing_constant.setter
    def von_klitzing_constant(self, von_klitzing_constant):
        """Sets the von_klitzing_constant of this Planet.

        Description not available  # noqa: E501

        :param von_klitzing_constant: The von_klitzing_constant of this Planet.
        :type von_klitzing_constant: List[float]
        """

        self._von_klitzing_constant = von_klitzing_constant

    @property
    def maximum_temperature(self):
        """Gets the maximum_temperature of this Planet.

        Description not available  # noqa: E501

        :return: The maximum_temperature of this Planet.
        :rtype: List[object]
        """
        return self._maximum_temperature

    @maximum_temperature.setter
    def maximum_temperature(self, maximum_temperature):
        """Sets the maximum_temperature of this Planet.

        Description not available  # noqa: E501

        :param maximum_temperature: The maximum_temperature of this Planet.
        :type maximum_temperature: List[object]
        """

        self._maximum_temperature = maximum_temperature

    @property
    def temperature(self):
        """Gets the temperature of this Planet.

        Description not available  # noqa: E501

        :return: The temperature of this Planet.
        :rtype: List[object]
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this Planet.

        Description not available  # noqa: E501

        :param temperature: The temperature of this Planet.
        :type temperature: List[object]
        """

        self._temperature = temperature

    @property
    def apparent_magnitude(self):
        """Gets the apparent_magnitude of this Planet.

        Description not available  # noqa: E501

        :return: The apparent_magnitude of this Planet.
        :rtype: List[float]
        """
        return self._apparent_magnitude

    @apparent_magnitude.setter
    def apparent_magnitude(self, apparent_magnitude):
        """Sets the apparent_magnitude of this Planet.

        Description not available  # noqa: E501

        :param apparent_magnitude: The apparent_magnitude of this Planet.
        :type apparent_magnitude: List[float]
        """

        self._apparent_magnitude = apparent_magnitude

    @property
    def satellite(self):
        """Gets the satellite of this Planet.

        Description not available  # noqa: E501

        :return: The satellite of this Planet.
        :rtype: List[str]
        """
        return self._satellite

    @satellite.setter
    def satellite(self, satellite):
        """Sets the satellite of this Planet.

        Description not available  # noqa: E501

        :param satellite: The satellite of this Planet.
        :type satellite: List[str]
        """

        self._satellite = satellite

    @property
    def id(self):
        """Gets the id of this Planet.

        identifier  # noqa: E501

        :return: The id of this Planet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Planet.

        identifier  # noqa: E501

        :param id: The id of this Planet.
        :type id: str
        """

        self._id = id

    @property
    def albedo(self):
        """Gets the albedo of this Planet.

        reflection coefficient  # noqa: E501

        :return: The albedo of this Planet.
        :rtype: List[float]
        """
        return self._albedo

    @albedo.setter
    def albedo(self, albedo):
        """Sets the albedo of this Planet.

        reflection coefficient  # noqa: E501

        :param albedo: The albedo of this Planet.
        :type albedo: List[float]
        """

        self._albedo = albedo

    @property
    def periapsis(self):
        """Gets the periapsis of this Planet.

        Description not available  # noqa: E501

        :return: The periapsis of this Planet.
        :rtype: List[object]
        """
        return self._periapsis

    @periapsis.setter
    def periapsis(self, periapsis):
        """Sets the periapsis of this Planet.

        Description not available  # noqa: E501

        :param periapsis: The periapsis of this Planet.
        :type periapsis: List[object]
        """

        self._periapsis = periapsis

    @property
    def absolute_magnitude(self):
        """Gets the absolute_magnitude of this Planet.

        Description not available  # noqa: E501

        :return: The absolute_magnitude of this Planet.
        :rtype: List[float]
        """
        return self._absolute_magnitude

    @absolute_magnitude.setter
    def absolute_magnitude(self, absolute_magnitude):
        """Sets the absolute_magnitude of this Planet.

        Description not available  # noqa: E501

        :param absolute_magnitude: The absolute_magnitude of this Planet.
        :type absolute_magnitude: List[float]
        """

        self._absolute_magnitude = absolute_magnitude

    @property
    def density(self):
        """Gets the density of this Planet.

        Description not available  # noqa: E501

        :return: The density of this Planet.
        :rtype: List[object]
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this Planet.

        Description not available  # noqa: E501

        :param density: The density of this Planet.
        :type density: List[object]
        """

        self._density = density

    @property
    def detection_method(self):
        """Gets the detection_method of this Planet.

        Description not available  # noqa: E501

        :return: The detection_method of this Planet.
        :rtype: List[str]
        """
        return self._detection_method

    @detection_method.setter
    def detection_method(self, detection_method):
        """Sets the detection_method of this Planet.

        Description not available  # noqa: E501

        :param detection_method: The detection_method of this Planet.
        :type detection_method: List[str]
        """

        self._detection_method = detection_method

    @property
    def average_speed(self):
        """Gets the average_speed of this Planet.

        The average speed of a thing.  # noqa: E501

        :return: The average_speed of this Planet.
        :rtype: List[object]
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        """Sets the average_speed of this Planet.

        The average speed of a thing.  # noqa: E501

        :param average_speed: The average_speed of this Planet.
        :type average_speed: List[object]
        """

        self._average_speed = average_speed

    @property
    def label(self):
        """Gets the label of this Planet.

        short description of the resource  # noqa: E501

        :return: The label of this Planet.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Planet.

        short description of the resource  # noqa: E501

        :param label: The label of this Planet.
        :type label: List[str]
        """

        self._label = label

    @property
    def apoapsis(self):
        """Gets the apoapsis of this Planet.

        Description not available  # noqa: E501

        :return: The apoapsis of this Planet.
        :rtype: List[object]
        """
        return self._apoapsis

    @apoapsis.setter
    def apoapsis(self, apoapsis):
        """Sets the apoapsis of this Planet.

        Description not available  # noqa: E501

        :param apoapsis: The apoapsis of this Planet.
        :type apoapsis: List[object]
        """

        self._apoapsis = apoapsis

    @property
    def volume(self):
        """Gets the volume of this Planet.

        Description not available  # noqa: E501

        :return: The volume of this Planet.
        :rtype: List[object]
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Planet.

        Description not available  # noqa: E501

        :param volume: The volume of this Planet.
        :type volume: List[object]
        """

        self._volume = volume

    @property
    def surface_gravity(self):
        """Gets the surface_gravity of this Planet.

        Description not available  # noqa: E501

        :return: The surface_gravity of this Planet.
        :rtype: List[float]
        """
        return self._surface_gravity

    @surface_gravity.setter
    def surface_gravity(self, surface_gravity):
        """Sets the surface_gravity of this Planet.

        Description not available  # noqa: E501

        :param surface_gravity: The surface_gravity of this Planet.
        :type surface_gravity: List[float]
        """

        self._surface_gravity = surface_gravity

    @property
    def rotation_period(self):
        """Gets the rotation_period of this Planet.

        Description not available  # noqa: E501

        :return: The rotation_period of this Planet.
        :rtype: List[float]
        """
        return self._rotation_period

    @rotation_period.setter
    def rotation_period(self, rotation_period):
        """Sets the rotation_period of this Planet.

        Description not available  # noqa: E501

        :param rotation_period: The rotation_period of this Planet.
        :type rotation_period: List[float]
        """

        self._rotation_period = rotation_period

    @property
    def messier_name(self):
        """Gets the messier_name of this Planet.

        Name for Messier objects  # noqa: E501

        :return: The messier_name of this Planet.
        :rtype: List[str]
        """
        return self._messier_name

    @messier_name.setter
    def messier_name(self, messier_name):
        """Sets the messier_name of this Planet.

        Name for Messier objects  # noqa: E501

        :param messier_name: The messier_name of this Planet.
        :type messier_name: List[str]
        """

        self._messier_name = messier_name

    @property
    def max_apparent_magnitude(self):
        """Gets the max_apparent_magnitude of this Planet.

        Description not available  # noqa: E501

        :return: The max_apparent_magnitude of this Planet.
        :rtype: List[float]
        """
        return self._max_apparent_magnitude

    @max_apparent_magnitude.setter
    def max_apparent_magnitude(self, max_apparent_magnitude):
        """Sets the max_apparent_magnitude of this Planet.

        Description not available  # noqa: E501

        :param max_apparent_magnitude: The max_apparent_magnitude of this Planet.
        :type max_apparent_magnitude: List[float]
        """

        self._max_apparent_magnitude = max_apparent_magnitude

    @property
    def minimum_temperature(self):
        """Gets the minimum_temperature of this Planet.

        Description not available  # noqa: E501

        :return: The minimum_temperature of this Planet.
        :rtype: List[object]
        """
        return self._minimum_temperature

    @minimum_temperature.setter
    def minimum_temperature(self, minimum_temperature):
        """Sets the minimum_temperature of this Planet.

        Description not available  # noqa: E501

        :param minimum_temperature: The minimum_temperature of this Planet.
        :type minimum_temperature: List[object]
        """

        self._minimum_temperature = minimum_temperature

    @property
    def ngc_name(self):
        """Gets the ngc_name of this Planet.

        Name for NGC objects  # noqa: E501

        :return: The ngc_name of this Planet.
        :rtype: List[str]
        """
        return self._ngc_name

    @ngc_name.setter
    def ngc_name(self, ngc_name):
        """Sets the ngc_name of this Planet.

        Name for NGC objects  # noqa: E501

        :param ngc_name: The ngc_name of this Planet.
        :type ngc_name: List[str]
        """

        self._ngc_name = ngc_name