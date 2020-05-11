# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Grape(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, notable_wine=None, classis=None, sub_family=None, scientific_name=None, description=None, binomial_authority=None, cultivated_variety=None, type=None, sub_tribus=None, sub_classis=None, taxon=None, id=None, tribus=None, order=None, conservation_status=None, wine_region=None, super_family=None, binomial=None, label=None, conservation_status_system=None, kingdom=None, hybrid=None, phylum=None, species=None, genus=None, domain=None, super_tribus=None, family=None):  # noqa: E501
        """Grape - a model defined in OpenAPI

        :param notable_wine: The notable_wine of this Grape.  # noqa: E501
        :type notable_wine: List[object]
        :param classis: The classis of this Grape.  # noqa: E501
        :type classis: List[object]
        :param sub_family: The sub_family of this Grape.  # noqa: E501
        :type sub_family: List[object]
        :param scientific_name: The scientific_name of this Grape.  # noqa: E501
        :type scientific_name: List[str]
        :param description: The description of this Grape.  # noqa: E501
        :type description: List[str]
        :param binomial_authority: The binomial_authority of this Grape.  # noqa: E501
        :type binomial_authority: List[object]
        :param cultivated_variety: The cultivated_variety of this Grape.  # noqa: E501
        :type cultivated_variety: List[object]
        :param type: The type of this Grape.  # noqa: E501
        :type type: List[str]
        :param sub_tribus: The sub_tribus of this Grape.  # noqa: E501
        :type sub_tribus: List[object]
        :param sub_classis: The sub_classis of this Grape.  # noqa: E501
        :type sub_classis: List[object]
        :param taxon: The taxon of this Grape.  # noqa: E501
        :type taxon: List[object]
        :param id: The id of this Grape.  # noqa: E501
        :type id: str
        :param tribus: The tribus of this Grape.  # noqa: E501
        :type tribus: List[object]
        :param order: The order of this Grape.  # noqa: E501
        :type order: List[object]
        :param conservation_status: The conservation_status of this Grape.  # noqa: E501
        :type conservation_status: List[str]
        :param wine_region: The wine_region of this Grape.  # noqa: E501
        :type wine_region: List[object]
        :param super_family: The super_family of this Grape.  # noqa: E501
        :type super_family: List[object]
        :param binomial: The binomial of this Grape.  # noqa: E501
        :type binomial: List[object]
        :param label: The label of this Grape.  # noqa: E501
        :type label: List[str]
        :param conservation_status_system: The conservation_status_system of this Grape.  # noqa: E501
        :type conservation_status_system: List[str]
        :param kingdom: The kingdom of this Grape.  # noqa: E501
        :type kingdom: List[object]
        :param hybrid: The hybrid of this Grape.  # noqa: E501
        :type hybrid: List[object]
        :param phylum: The phylum of this Grape.  # noqa: E501
        :type phylum: List[object]
        :param species: The species of this Grape.  # noqa: E501
        :type species: List[object]
        :param genus: The genus of this Grape.  # noqa: E501
        :type genus: List[object]
        :param domain: The domain of this Grape.  # noqa: E501
        :type domain: List[object]
        :param super_tribus: The super_tribus of this Grape.  # noqa: E501
        :type super_tribus: List[object]
        :param family: The family of this Grape.  # noqa: E501
        :type family: List[object]
        """


        self.openapi_types = {
            'notable_wine': List[object],
            'classis': List[object],
            'sub_family': List[object],
            'scientific_name': List[str],
            'description': List[str],
            'binomial_authority': List[object],
            'cultivated_variety': List[object],
            'type': List[str],
            'sub_tribus': List[object],
            'sub_classis': List[object],
            'taxon': List[object],
            'id': str,
            'tribus': List[object],
            'order': List[object],
            'conservation_status': List[str],
            'wine_region': List[object],
            'super_family': List[object],
            'binomial': List[object],
            'label': List[str],
            'conservation_status_system': List[str],
            'kingdom': List[object],
            'hybrid': List[object],
            'phylum': List[object],
            'species': List[object],
            'genus': List[object],
            'domain': List[object],
            'super_tribus': List[object],
            'family': List[object]
        }

        self.attribute_map = {
            'notable_wine': 'notableWine',
            'classis': 'classis',
            'sub_family': 'subFamily',
            'scientific_name': 'scientificName',
            'description': 'description',
            'binomial_authority': 'binomialAuthority',
            'cultivated_variety': 'cultivatedVariety',
            'type': 'type',
            'sub_tribus': 'subTribus',
            'sub_classis': 'subClassis',
            'taxon': 'taxon',
            'id': 'id',
            'tribus': 'tribus',
            'order': 'order',
            'conservation_status': 'conservationStatus',
            'wine_region': 'wineRegion',
            'super_family': 'superFamily',
            'binomial': 'binomial',
            'label': 'label',
            'conservation_status_system': 'conservationStatusSystem',
            'kingdom': 'kingdom',
            'hybrid': 'hybrid',
            'phylum': 'phylum',
            'species': 'species',
            'genus': 'genus',
            'domain': 'domain',
            'super_tribus': 'superTribus',
            'family': 'family'
        }

        self._notable_wine = notable_wine
        self._classis = classis
        self._sub_family = sub_family
        self._scientific_name = scientific_name
        self._description = description
        self._binomial_authority = binomial_authority
        self._cultivated_variety = cultivated_variety
        self._type = type
        self._sub_tribus = sub_tribus
        self._sub_classis = sub_classis
        self._taxon = taxon
        self._id = id
        self._tribus = tribus
        self._order = order
        self._conservation_status = conservation_status
        self._wine_region = wine_region
        self._super_family = super_family
        self._binomial = binomial
        self._label = label
        self._conservation_status_system = conservation_status_system
        self._kingdom = kingdom
        self._hybrid = hybrid
        self._phylum = phylum
        self._species = species
        self._genus = genus
        self._domain = domain
        self._super_tribus = super_tribus
        self._family = family

    @classmethod
    def from_dict(cls, dikt) -> 'Grape':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Grape of this Grape.  # noqa: E501
        :rtype: Grape
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notable_wine(self):
        """Gets the notable_wine of this Grape.

        Description not available  # noqa: E501

        :return: The notable_wine of this Grape.
        :rtype: List[object]
        """
        return self._notable_wine

    @notable_wine.setter
    def notable_wine(self, notable_wine):
        """Sets the notable_wine of this Grape.

        Description not available  # noqa: E501

        :param notable_wine: The notable_wine of this Grape.
        :type notable_wine: List[object]
        """

        self._notable_wine = notable_wine

    @property
    def classis(self):
        """Gets the classis of this Grape.

        the living thing class (from the Latin \"classis\"), according to the biological taxonomy  # noqa: E501

        :return: The classis of this Grape.
        :rtype: List[object]
        """
        return self._classis

    @classis.setter
    def classis(self, classis):
        """Sets the classis of this Grape.

        the living thing class (from the Latin \"classis\"), according to the biological taxonomy  # noqa: E501

        :param classis: The classis of this Grape.
        :type classis: List[object]
        """

        self._classis = classis

    @property
    def sub_family(self):
        """Gets the sub_family of this Grape.

        Description not available  # noqa: E501

        :return: The sub_family of this Grape.
        :rtype: List[object]
        """
        return self._sub_family

    @sub_family.setter
    def sub_family(self, sub_family):
        """Sets the sub_family of this Grape.

        Description not available  # noqa: E501

        :param sub_family: The sub_family of this Grape.
        :type sub_family: List[object]
        """

        self._sub_family = sub_family

    @property
    def scientific_name(self):
        """Gets the scientific_name of this Grape.

        Description not available  # noqa: E501

        :return: The scientific_name of this Grape.
        :rtype: List[str]
        """
        return self._scientific_name

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        """Sets the scientific_name of this Grape.

        Description not available  # noqa: E501

        :param scientific_name: The scientific_name of this Grape.
        :type scientific_name: List[str]
        """

        self._scientific_name = scientific_name

    @property
    def description(self):
        """Gets the description of this Grape.

        small description  # noqa: E501

        :return: The description of this Grape.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Grape.

        small description  # noqa: E501

        :param description: The description of this Grape.
        :type description: List[str]
        """

        self._description = description

    @property
    def binomial_authority(self):
        """Gets the binomial_authority of this Grape.

        Description not available  # noqa: E501

        :return: The binomial_authority of this Grape.
        :rtype: List[object]
        """
        return self._binomial_authority

    @binomial_authority.setter
    def binomial_authority(self, binomial_authority):
        """Sets the binomial_authority of this Grape.

        Description not available  # noqa: E501

        :param binomial_authority: The binomial_authority of this Grape.
        :type binomial_authority: List[object]
        """

        self._binomial_authority = binomial_authority

    @property
    def cultivated_variety(self):
        """Gets the cultivated_variety of this Grape.

        Name of the cultivar (cultivated variety)  # noqa: E501

        :return: The cultivated_variety of this Grape.
        :rtype: List[object]
        """
        return self._cultivated_variety

    @cultivated_variety.setter
    def cultivated_variety(self, cultivated_variety):
        """Sets the cultivated_variety of this Grape.

        Name of the cultivar (cultivated variety)  # noqa: E501

        :param cultivated_variety: The cultivated_variety of this Grape.
        :type cultivated_variety: List[object]
        """

        self._cultivated_variety = cultivated_variety

    @property
    def type(self):
        """Gets the type of this Grape.

        type of the resource  # noqa: E501

        :return: The type of this Grape.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Grape.

        type of the resource  # noqa: E501

        :param type: The type of this Grape.
        :type type: List[str]
        """

        self._type = type

    @property
    def sub_tribus(self):
        """Gets the sub_tribus of this Grape.

        Description not available  # noqa: E501

        :return: The sub_tribus of this Grape.
        :rtype: List[object]
        """
        return self._sub_tribus

    @sub_tribus.setter
    def sub_tribus(self, sub_tribus):
        """Sets the sub_tribus of this Grape.

        Description not available  # noqa: E501

        :param sub_tribus: The sub_tribus of this Grape.
        :type sub_tribus: List[object]
        """

        self._sub_tribus = sub_tribus

    @property
    def sub_classis(self):
        """Gets the sub_classis of this Grape.

        a subdivision within a Species classis  # noqa: E501

        :return: The sub_classis of this Grape.
        :rtype: List[object]
        """
        return self._sub_classis

    @sub_classis.setter
    def sub_classis(self, sub_classis):
        """Sets the sub_classis of this Grape.

        a subdivision within a Species classis  # noqa: E501

        :param sub_classis: The sub_classis of this Grape.
        :type sub_classis: List[object]
        """

        self._sub_classis = sub_classis

    @property
    def taxon(self):
        """Gets the taxon of this Grape.

        Description not available  # noqa: E501

        :return: The taxon of this Grape.
        :rtype: List[object]
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this Grape.

        Description not available  # noqa: E501

        :param taxon: The taxon of this Grape.
        :type taxon: List[object]
        """

        self._taxon = taxon

    @property
    def id(self):
        """Gets the id of this Grape.

        identifier  # noqa: E501

        :return: The id of this Grape.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Grape.

        identifier  # noqa: E501

        :param id: The id of this Grape.
        :type id: str
        """

        self._id = id

    @property
    def tribus(self):
        """Gets the tribus of this Grape.

        Description not available  # noqa: E501

        :return: The tribus of this Grape.
        :rtype: List[object]
        """
        return self._tribus

    @tribus.setter
    def tribus(self, tribus):
        """Sets the tribus of this Grape.

        Description not available  # noqa: E501

        :param tribus: The tribus of this Grape.
        :type tribus: List[object]
        """

        self._tribus = tribus

    @property
    def order(self):
        """Gets the order of this Grape.

        Description not available  # noqa: E501

        :return: The order of this Grape.
        :rtype: List[object]
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Grape.

        Description not available  # noqa: E501

        :param order: The order of this Grape.
        :type order: List[object]
        """

        self._order = order

    @property
    def conservation_status(self):
        """Gets the conservation_status of this Grape.

        Description not available  # noqa: E501

        :return: The conservation_status of this Grape.
        :rtype: List[str]
        """
        return self._conservation_status

    @conservation_status.setter
    def conservation_status(self, conservation_status):
        """Sets the conservation_status of this Grape.

        Description not available  # noqa: E501

        :param conservation_status: The conservation_status of this Grape.
        :type conservation_status: List[str]
        """

        self._conservation_status = conservation_status

    @property
    def wine_region(self):
        """Gets the wine_region of this Grape.

        Description not available  # noqa: E501

        :return: The wine_region of this Grape.
        :rtype: List[object]
        """
        return self._wine_region

    @wine_region.setter
    def wine_region(self, wine_region):
        """Sets the wine_region of this Grape.

        Description not available  # noqa: E501

        :param wine_region: The wine_region of this Grape.
        :type wine_region: List[object]
        """

        self._wine_region = wine_region

    @property
    def super_family(self):
        """Gets the super_family of this Grape.

        Description not available  # noqa: E501

        :return: The super_family of this Grape.
        :rtype: List[object]
        """
        return self._super_family

    @super_family.setter
    def super_family(self, super_family):
        """Sets the super_family of this Grape.

        Description not available  # noqa: E501

        :param super_family: The super_family of this Grape.
        :type super_family: List[object]
        """

        self._super_family = super_family

    @property
    def binomial(self):
        """Gets the binomial of this Grape.

        Description not available  # noqa: E501

        :return: The binomial of this Grape.
        :rtype: List[object]
        """
        return self._binomial

    @binomial.setter
    def binomial(self, binomial):
        """Sets the binomial of this Grape.

        Description not available  # noqa: E501

        :param binomial: The binomial of this Grape.
        :type binomial: List[object]
        """

        self._binomial = binomial

    @property
    def label(self):
        """Gets the label of this Grape.

        short description of the resource  # noqa: E501

        :return: The label of this Grape.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Grape.

        short description of the resource  # noqa: E501

        :param label: The label of this Grape.
        :type label: List[str]
        """

        self._label = label

    @property
    def conservation_status_system(self):
        """Gets the conservation_status_system of this Grape.

        Description not available  # noqa: E501

        :return: The conservation_status_system of this Grape.
        :rtype: List[str]
        """
        return self._conservation_status_system

    @conservation_status_system.setter
    def conservation_status_system(self, conservation_status_system):
        """Sets the conservation_status_system of this Grape.

        Description not available  # noqa: E501

        :param conservation_status_system: The conservation_status_system of this Grape.
        :type conservation_status_system: List[str]
        """

        self._conservation_status_system = conservation_status_system

    @property
    def kingdom(self):
        """Gets the kingdom of this Grape.

        In biology, kingdom (Latin: regnum, pl. regna) is a taxonomic rank, which is either the highest rank or in the more recent three-domain system, the rank below domain.  # noqa: E501

        :return: The kingdom of this Grape.
        :rtype: List[object]
        """
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        """Sets the kingdom of this Grape.

        In biology, kingdom (Latin: regnum, pl. regna) is a taxonomic rank, which is either the highest rank or in the more recent three-domain system, the rank below domain.  # noqa: E501

        :param kingdom: The kingdom of this Grape.
        :type kingdom: List[object]
        """

        self._kingdom = kingdom

    @property
    def hybrid(self):
        """Gets the hybrid of this Grape.

        Plants from which another plant (or cultivar) has been developed from  # noqa: E501

        :return: The hybrid of this Grape.
        :rtype: List[object]
        """
        return self._hybrid

    @hybrid.setter
    def hybrid(self, hybrid):
        """Sets the hybrid of this Grape.

        Plants from which another plant (or cultivar) has been developed from  # noqa: E501

        :param hybrid: The hybrid of this Grape.
        :type hybrid: List[object]
        """

        self._hybrid = hybrid

    @property
    def phylum(self):
        """Gets the phylum of this Grape.

        A rank in the classification of organisms, below kingdom and above class; also called a division, especially in describing plants; a taxon at that rank.  # noqa: E501

        :return: The phylum of this Grape.
        :rtype: List[object]
        """
        return self._phylum

    @phylum.setter
    def phylum(self, phylum):
        """Sets the phylum of this Grape.

        A rank in the classification of organisms, below kingdom and above class; also called a division, especially in describing plants; a taxon at that rank.  # noqa: E501

        :param phylum: The phylum of this Grape.
        :type phylum: List[object]
        """

        self._phylum = phylum

    @property
    def species(self):
        """Gets the species of this Grape.

        Description not available  # noqa: E501

        :return: The species of this Grape.
        :rtype: List[object]
        """
        return self._species

    @species.setter
    def species(self, species):
        """Sets the species of this Grape.

        Description not available  # noqa: E501

        :param species: The species of this Grape.
        :type species: List[object]
        """

        self._species = species

    @property
    def genus(self):
        """Gets the genus of this Grape.

        A rank in the classification of organisms, below family and above species; a taxon at that rank  # noqa: E501

        :return: The genus of this Grape.
        :rtype: List[object]
        """
        return self._genus

    @genus.setter
    def genus(self, genus):
        """Sets the genus of this Grape.

        A rank in the classification of organisms, below family and above species; a taxon at that rank  # noqa: E501

        :param genus: The genus of this Grape.
        :type genus: List[object]
        """

        self._genus = genus

    @property
    def domain(self):
        """Gets the domain of this Grape.

        Description not available  # noqa: E501

        :return: The domain of this Grape.
        :rtype: List[object]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Grape.

        Description not available  # noqa: E501

        :param domain: The domain of this Grape.
        :type domain: List[object]
        """

        self._domain = domain

    @property
    def super_tribus(self):
        """Gets the super_tribus of this Grape.

        Description not available  # noqa: E501

        :return: The super_tribus of this Grape.
        :rtype: List[object]
        """
        return self._super_tribus

    @super_tribus.setter
    def super_tribus(self, super_tribus):
        """Sets the super_tribus of this Grape.

        Description not available  # noqa: E501

        :param super_tribus: The super_tribus of this Grape.
        :type super_tribus: List[object]
        """

        self._super_tribus = super_tribus

    @property
    def family(self):
        """Gets the family of this Grape.

        Description not available  # noqa: E501

        :return: The family of this Grape.
        :rtype: List[object]
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this Grape.

        Description not available  # noqa: E501

        :param family: The family of this Grape.
        :type family: List[object]
        """

        self._family = family