# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Book(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, previous_work=None, dcc=None, coden=None, isbn=None, cover_artist=None, translator=None, alternative_title=None, description=None, subsequent_work=None, chief_editor=None, music_composer=None, last_publication_date=None, type=None, lcc=None, non_fiction_subject=None, lccn=None, main_character=None, number_of_pages=None, id=None, literary_genre=None, based_on=None, first_publisher=None, first_publication_date=None, film_version=None, release_date=None, number_of_volumes=None, composer=None, author=None, preface_by=None, runtime=None, media_type=None, production_company=None, label=None, original_language=None, license=None, subject_term=None, original_title=None, circulation=None, oclc=None, producer=None, starring=None, completion_date=None, writer=None, magazine=None, illustrator=None):  # noqa: E501
        """Book - a model defined in OpenAPI

        :param previous_work: The previous_work of this Book.  # noqa: E501
        :type previous_work: List[object]
        :param dcc: The dcc of this Book.  # noqa: E501
        :type dcc: List[str]
        :param coden: The coden of this Book.  # noqa: E501
        :type coden: List[str]
        :param isbn: The isbn of this Book.  # noqa: E501
        :type isbn: List[str]
        :param cover_artist: The cover_artist of this Book.  # noqa: E501
        :type cover_artist: List[object]
        :param translator: The translator of this Book.  # noqa: E501
        :type translator: List[object]
        :param alternative_title: The alternative_title of this Book.  # noqa: E501
        :type alternative_title: List[str]
        :param description: The description of this Book.  # noqa: E501
        :type description: List[str]
        :param subsequent_work: The subsequent_work of this Book.  # noqa: E501
        :type subsequent_work: List[object]
        :param chief_editor: The chief_editor of this Book.  # noqa: E501
        :type chief_editor: List[object]
        :param music_composer: The music_composer of this Book.  # noqa: E501
        :type music_composer: List[object]
        :param last_publication_date: The last_publication_date of this Book.  # noqa: E501
        :type last_publication_date: List[str]
        :param type: The type of this Book.  # noqa: E501
        :type type: List[str]
        :param lcc: The lcc of this Book.  # noqa: E501
        :type lcc: List[str]
        :param non_fiction_subject: The non_fiction_subject of this Book.  # noqa: E501
        :type non_fiction_subject: List[object]
        :param lccn: The lccn of this Book.  # noqa: E501
        :type lccn: List[str]
        :param main_character: The main_character of this Book.  # noqa: E501
        :type main_character: List[object]
        :param number_of_pages: The number_of_pages of this Book.  # noqa: E501
        :type number_of_pages: List[int]
        :param id: The id of this Book.  # noqa: E501
        :type id: str
        :param literary_genre: The literary_genre of this Book.  # noqa: E501
        :type literary_genre: List[object]
        :param based_on: The based_on of this Book.  # noqa: E501
        :type based_on: List[object]
        :param first_publisher: The first_publisher of this Book.  # noqa: E501
        :type first_publisher: List[object]
        :param first_publication_date: The first_publication_date of this Book.  # noqa: E501
        :type first_publication_date: List[str]
        :param film_version: The film_version of this Book.  # noqa: E501
        :type film_version: List[object]
        :param release_date: The release_date of this Book.  # noqa: E501
        :type release_date: List[str]
        :param number_of_volumes: The number_of_volumes of this Book.  # noqa: E501
        :type number_of_volumes: List[int]
        :param composer: The composer of this Book.  # noqa: E501
        :type composer: List[object]
        :param author: The author of this Book.  # noqa: E501
        :type author: List[object]
        :param preface_by: The preface_by of this Book.  # noqa: E501
        :type preface_by: List[object]
        :param runtime: The runtime of this Book.  # noqa: E501
        :type runtime: List[object]
        :param media_type: The media_type of this Book.  # noqa: E501
        :type media_type: List[object]
        :param production_company: The production_company of this Book.  # noqa: E501
        :type production_company: List[object]
        :param label: The label of this Book.  # noqa: E501
        :type label: List[str]
        :param original_language: The original_language of this Book.  # noqa: E501
        :type original_language: List[object]
        :param license: The license of this Book.  # noqa: E501
        :type license: List[object]
        :param subject_term: The subject_term of this Book.  # noqa: E501
        :type subject_term: List[str]
        :param original_title: The original_title of this Book.  # noqa: E501
        :type original_title: List[str]
        :param circulation: The circulation of this Book.  # noqa: E501
        :type circulation: List[int]
        :param oclc: The oclc of this Book.  # noqa: E501
        :type oclc: List[str]
        :param producer: The producer of this Book.  # noqa: E501
        :type producer: List[object]
        :param starring: The starring of this Book.  # noqa: E501
        :type starring: List[object]
        :param completion_date: The completion_date of this Book.  # noqa: E501
        :type completion_date: List[str]
        :param writer: The writer of this Book.  # noqa: E501
        :type writer: List[object]
        :param magazine: The magazine of this Book.  # noqa: E501
        :type magazine: List[object]
        :param illustrator: The illustrator of this Book.  # noqa: E501
        :type illustrator: List[object]
        """


        self.openapi_types = {
            'previous_work': List[object],
            'dcc': List[str],
            'coden': List[str],
            'isbn': List[str],
            'cover_artist': List[object],
            'translator': List[object],
            'alternative_title': List[str],
            'description': List[str],
            'subsequent_work': List[object],
            'chief_editor': List[object],
            'music_composer': List[object],
            'last_publication_date': List[str],
            'type': List[str],
            'lcc': List[str],
            'non_fiction_subject': List[object],
            'lccn': List[str],
            'main_character': List[object],
            'number_of_pages': List[int],
            'id': str,
            'literary_genre': List[object],
            'based_on': List[object],
            'first_publisher': List[object],
            'first_publication_date': List[str],
            'film_version': List[object],
            'release_date': List[str],
            'number_of_volumes': List[int],
            'composer': List[object],
            'author': List[object],
            'preface_by': List[object],
            'runtime': List[object],
            'media_type': List[object],
            'production_company': List[object],
            'label': List[str],
            'original_language': List[object],
            'license': List[object],
            'subject_term': List[str],
            'original_title': List[str],
            'circulation': List[int],
            'oclc': List[str],
            'producer': List[object],
            'starring': List[object],
            'completion_date': List[str],
            'writer': List[object],
            'magazine': List[object],
            'illustrator': List[object]
        }

        self.attribute_map = {
            'previous_work': 'previousWork',
            'dcc': 'dcc',
            'coden': 'coden',
            'isbn': 'isbn',
            'cover_artist': 'coverArtist',
            'translator': 'translator',
            'alternative_title': 'alternativeTitle',
            'description': 'description',
            'subsequent_work': 'subsequentWork',
            'chief_editor': 'chiefEditor',
            'music_composer': 'musicComposer',
            'last_publication_date': 'lastPublicationDate',
            'type': 'type',
            'lcc': 'lcc',
            'non_fiction_subject': 'nonFictionSubject',
            'lccn': 'lccn',
            'main_character': 'mainCharacter',
            'number_of_pages': 'numberOfPages',
            'id': 'id',
            'literary_genre': 'literaryGenre',
            'based_on': 'basedOn',
            'first_publisher': 'firstPublisher',
            'first_publication_date': 'firstPublicationDate',
            'film_version': 'filmVersion',
            'release_date': 'releaseDate',
            'number_of_volumes': 'numberOfVolumes',
            'composer': 'composer',
            'author': 'author',
            'preface_by': 'prefaceBy',
            'runtime': 'runtime',
            'media_type': 'mediaType',
            'production_company': 'productionCompany',
            'label': 'label',
            'original_language': 'originalLanguage',
            'license': 'license',
            'subject_term': 'subjectTerm',
            'original_title': 'originalTitle',
            'circulation': 'circulation',
            'oclc': 'oclc',
            'producer': 'producer',
            'starring': 'starring',
            'completion_date': 'completionDate',
            'writer': 'writer',
            'magazine': 'magazine',
            'illustrator': 'illustrator'
        }

        self._previous_work = previous_work
        self._dcc = dcc
        self._coden = coden
        self._isbn = isbn
        self._cover_artist = cover_artist
        self._translator = translator
        self._alternative_title = alternative_title
        self._description = description
        self._subsequent_work = subsequent_work
        self._chief_editor = chief_editor
        self._music_composer = music_composer
        self._last_publication_date = last_publication_date
        self._type = type
        self._lcc = lcc
        self._non_fiction_subject = non_fiction_subject
        self._lccn = lccn
        self._main_character = main_character
        self._number_of_pages = number_of_pages
        self._id = id
        self._literary_genre = literary_genre
        self._based_on = based_on
        self._first_publisher = first_publisher
        self._first_publication_date = first_publication_date
        self._film_version = film_version
        self._release_date = release_date
        self._number_of_volumes = number_of_volumes
        self._composer = composer
        self._author = author
        self._preface_by = preface_by
        self._runtime = runtime
        self._media_type = media_type
        self._production_company = production_company
        self._label = label
        self._original_language = original_language
        self._license = license
        self._subject_term = subject_term
        self._original_title = original_title
        self._circulation = circulation
        self._oclc = oclc
        self._producer = producer
        self._starring = starring
        self._completion_date = completion_date
        self._writer = writer
        self._magazine = magazine
        self._illustrator = illustrator

    @classmethod
    def from_dict(cls, dikt) -> 'Book':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Book of this Book.  # noqa: E501
        :rtype: Book
        """
        return util.deserialize_model(dikt, cls)

    @property
    def previous_work(self):
        """Gets the previous_work of this Book.

        Description not available  # noqa: E501

        :return: The previous_work of this Book.
        :rtype: List[object]
        """
        return self._previous_work

    @previous_work.setter
    def previous_work(self, previous_work):
        """Sets the previous_work of this Book.

        Description not available  # noqa: E501

        :param previous_work: The previous_work of this Book.
        :type previous_work: List[object]
        """

        self._previous_work = previous_work

    @property
    def dcc(self):
        """Gets the dcc of this Book.

        The Dewey Decimal Classification is a proprietary system of library classification developed by Melvil Dewey in 1876.  # noqa: E501

        :return: The dcc of this Book.
        :rtype: List[str]
        """
        return self._dcc

    @dcc.setter
    def dcc(self, dcc):
        """Sets the dcc of this Book.

        The Dewey Decimal Classification is a proprietary system of library classification developed by Melvil Dewey in 1876.  # noqa: E501

        :param dcc: The dcc of this Book.
        :type dcc: List[str]
        """

        self._dcc = dcc

    @property
    def coden(self):
        """Gets the coden of this Book.

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :return: The coden of this Book.
        :rtype: List[str]
        """
        return self._coden

    @coden.setter
    def coden(self, coden):
        """Sets the coden of this Book.

        CODEN is a six character, alphanumeric bibliographic code, that provides concise, unique and unambiguous identification of the titles of serials and non-serial publications from all subject areas.  # noqa: E501

        :param coden: The coden of this Book.
        :type coden: List[str]
        """

        self._coden = coden

    @property
    def isbn(self):
        """Gets the isbn of this Book.

        The International Standard Book Number (ISBN) is a unique numeric commercial book identifier based upon the 9-digit Standard Book Numbering (SBN) code.  # noqa: E501

        :return: The isbn of this Book.
        :rtype: List[str]
        """
        return self._isbn

    @isbn.setter
    def isbn(self, isbn):
        """Sets the isbn of this Book.

        The International Standard Book Number (ISBN) is a unique numeric commercial book identifier based upon the 9-digit Standard Book Numbering (SBN) code.  # noqa: E501

        :param isbn: The isbn of this Book.
        :type isbn: List[str]
        """

        self._isbn = isbn

    @property
    def cover_artist(self):
        """Gets the cover_artist of this Book.

        Cover artist  # noqa: E501

        :return: The cover_artist of this Book.
        :rtype: List[object]
        """
        return self._cover_artist

    @cover_artist.setter
    def cover_artist(self, cover_artist):
        """Sets the cover_artist of this Book.

        Cover artist  # noqa: E501

        :param cover_artist: The cover_artist of this Book.
        :type cover_artist: List[object]
        """

        self._cover_artist = cover_artist

    @property
    def translator(self):
        """Gets the translator of this Book.

        Translator(s), if original not in English  # noqa: E501

        :return: The translator of this Book.
        :rtype: List[object]
        """
        return self._translator

    @translator.setter
    def translator(self, translator):
        """Sets the translator of this Book.

        Translator(s), if original not in English  # noqa: E501

        :param translator: The translator of this Book.
        :type translator: List[object]
        """

        self._translator = translator

    @property
    def alternative_title(self):
        """Gets the alternative_title of this Book.

        The alternative title attributed to a work  # noqa: E501

        :return: The alternative_title of this Book.
        :rtype: List[str]
        """
        return self._alternative_title

    @alternative_title.setter
    def alternative_title(self, alternative_title):
        """Sets the alternative_title of this Book.

        The alternative title attributed to a work  # noqa: E501

        :param alternative_title: The alternative_title of this Book.
        :type alternative_title: List[str]
        """

        self._alternative_title = alternative_title

    @property
    def description(self):
        """Gets the description of this Book.

        small description  # noqa: E501

        :return: The description of this Book.
        :rtype: List[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Book.

        small description  # noqa: E501

        :param description: The description of this Book.
        :type description: List[str]
        """

        self._description = description

    @property
    def subsequent_work(self):
        """Gets the subsequent_work of this Book.

        Description not available  # noqa: E501

        :return: The subsequent_work of this Book.
        :rtype: List[object]
        """
        return self._subsequent_work

    @subsequent_work.setter
    def subsequent_work(self, subsequent_work):
        """Sets the subsequent_work of this Book.

        Description not available  # noqa: E501

        :param subsequent_work: The subsequent_work of this Book.
        :type subsequent_work: List[object]
        """

        self._subsequent_work = subsequent_work

    @property
    def chief_editor(self):
        """Gets the chief_editor of this Book.

        Description not available  # noqa: E501

        :return: The chief_editor of this Book.
        :rtype: List[object]
        """
        return self._chief_editor

    @chief_editor.setter
    def chief_editor(self, chief_editor):
        """Sets the chief_editor of this Book.

        Description not available  # noqa: E501

        :param chief_editor: The chief_editor of this Book.
        :type chief_editor: List[object]
        """

        self._chief_editor = chief_editor

    @property
    def music_composer(self):
        """Gets the music_composer of this Book.

        Description not available  # noqa: E501

        :return: The music_composer of this Book.
        :rtype: List[object]
        """
        return self._music_composer

    @music_composer.setter
    def music_composer(self, music_composer):
        """Sets the music_composer of this Book.

        Description not available  # noqa: E501

        :param music_composer: The music_composer of this Book.
        :type music_composer: List[object]
        """

        self._music_composer = music_composer

    @property
    def last_publication_date(self):
        """Gets the last_publication_date of this Book.

        Date of the last publication.  # noqa: E501

        :return: The last_publication_date of this Book.
        :rtype: List[str]
        """
        return self._last_publication_date

    @last_publication_date.setter
    def last_publication_date(self, last_publication_date):
        """Sets the last_publication_date of this Book.

        Date of the last publication.  # noqa: E501

        :param last_publication_date: The last_publication_date of this Book.
        :type last_publication_date: List[str]
        """

        self._last_publication_date = last_publication_date

    @property
    def type(self):
        """Gets the type of this Book.

        type of the resource  # noqa: E501

        :return: The type of this Book.
        :rtype: List[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Book.

        type of the resource  # noqa: E501

        :param type: The type of this Book.
        :type type: List[str]
        """

        self._type = type

    @property
    def lcc(self):
        """Gets the lcc of this Book.

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :return: The lcc of this Book.
        :rtype: List[str]
        """
        return self._lcc

    @lcc.setter
    def lcc(self, lcc):
        """Sets the lcc of this Book.

        The Library of Congress Classification (LCC) is a system of library classification developed by the Library of Congress.  # noqa: E501

        :param lcc: The lcc of this Book.
        :type lcc: List[str]
        """

        self._lcc = lcc

    @property
    def non_fiction_subject(self):
        """Gets the non_fiction_subject of this Book.

        The subject of a non-fiction book (e.g.: History, Biography, Cookbook, Climate change, ...).  # noqa: E501

        :return: The non_fiction_subject of this Book.
        :rtype: List[object]
        """
        return self._non_fiction_subject

    @non_fiction_subject.setter
    def non_fiction_subject(self, non_fiction_subject):
        """Sets the non_fiction_subject of this Book.

        The subject of a non-fiction book (e.g.: History, Biography, Cookbook, Climate change, ...).  # noqa: E501

        :param non_fiction_subject: The non_fiction_subject of this Book.
        :type non_fiction_subject: List[object]
        """

        self._non_fiction_subject = non_fiction_subject

    @property
    def lccn(self):
        """Gets the lccn of this Book.

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :return: The lccn of this Book.
        :rtype: List[str]
        """
        return self._lccn

    @lccn.setter
    def lccn(self, lccn):
        """Sets the lccn of this Book.

        The Library of Congress Control Number or LCCN is a serially based system of numbering cataloging records in the Library of Congress in the United States. It has nothing to do with the contents of any book, and should not be confused with Library of Congress Classification.  # noqa: E501

        :param lccn: The lccn of this Book.
        :type lccn: List[str]
        """

        self._lccn = lccn

    @property
    def main_character(self):
        """Gets the main_character of this Book.

        Description not available  # noqa: E501

        :return: The main_character of this Book.
        :rtype: List[object]
        """
        return self._main_character

    @main_character.setter
    def main_character(self, main_character):
        """Sets the main_character of this Book.

        Description not available  # noqa: E501

        :param main_character: The main_character of this Book.
        :type main_character: List[object]
        """

        self._main_character = main_character

    @property
    def number_of_pages(self):
        """Gets the number_of_pages of this Book.

        The books number of pages.  # noqa: E501

        :return: The number_of_pages of this Book.
        :rtype: List[int]
        """
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages):
        """Sets the number_of_pages of this Book.

        The books number of pages.  # noqa: E501

        :param number_of_pages: The number_of_pages of this Book.
        :type number_of_pages: List[int]
        """

        self._number_of_pages = number_of_pages

    @property
    def id(self):
        """Gets the id of this Book.

        identifier  # noqa: E501

        :return: The id of this Book.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Book.

        identifier  # noqa: E501

        :param id: The id of this Book.
        :type id: str
        """

        self._id = id

    @property
    def literary_genre(self):
        """Gets the literary_genre of this Book.

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :return: The literary_genre of this Book.
        :rtype: List[object]
        """
        return self._literary_genre

    @literary_genre.setter
    def literary_genre(self, literary_genre):
        """Sets the literary_genre of this Book.

        A literary genre is a category of literary composition. Genres may be determined by literary technique, tone, content, or even (as in the case of fiction) length.  # noqa: E501

        :param literary_genre: The literary_genre of this Book.
        :type literary_genre: List[object]
        """

        self._literary_genre = literary_genre

    @property
    def based_on(self):
        """Gets the based_on of this Book.

        Description not available  # noqa: E501

        :return: The based_on of this Book.
        :rtype: List[object]
        """
        return self._based_on

    @based_on.setter
    def based_on(self, based_on):
        """Sets the based_on of this Book.

        Description not available  # noqa: E501

        :param based_on: The based_on of this Book.
        :type based_on: List[object]
        """

        self._based_on = based_on

    @property
    def first_publisher(self):
        """Gets the first_publisher of this Book.

        Description not available  # noqa: E501

        :return: The first_publisher of this Book.
        :rtype: List[object]
        """
        return self._first_publisher

    @first_publisher.setter
    def first_publisher(self, first_publisher):
        """Sets the first_publisher of this Book.

        Description not available  # noqa: E501

        :param first_publisher: The first_publisher of this Book.
        :type first_publisher: List[object]
        """

        self._first_publisher = first_publisher

    @property
    def first_publication_date(self):
        """Gets the first_publication_date of this Book.

        Date of the first publication.  # noqa: E501

        :return: The first_publication_date of this Book.
        :rtype: List[str]
        """
        return self._first_publication_date

    @first_publication_date.setter
    def first_publication_date(self, first_publication_date):
        """Sets the first_publication_date of this Book.

        Date of the first publication.  # noqa: E501

        :param first_publication_date: The first_publication_date of this Book.
        :type first_publication_date: List[str]
        """

        self._first_publication_date = first_publication_date

    @property
    def film_version(self):
        """Gets the film_version of this Book.

        Description not available  # noqa: E501

        :return: The film_version of this Book.
        :rtype: List[object]
        """
        return self._film_version

    @film_version.setter
    def film_version(self, film_version):
        """Sets the film_version of this Book.

        Description not available  # noqa: E501

        :param film_version: The film_version of this Book.
        :type film_version: List[object]
        """

        self._film_version = film_version

    @property
    def release_date(self):
        """Gets the release_date of this Book.

        Description not available  # noqa: E501

        :return: The release_date of this Book.
        :rtype: List[str]
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this Book.

        Description not available  # noqa: E501

        :param release_date: The release_date of this Book.
        :type release_date: List[str]
        """

        self._release_date = release_date

    @property
    def number_of_volumes(self):
        """Gets the number_of_volumes of this Book.

        Description not available  # noqa: E501

        :return: The number_of_volumes of this Book.
        :rtype: List[int]
        """
        return self._number_of_volumes

    @number_of_volumes.setter
    def number_of_volumes(self, number_of_volumes):
        """Sets the number_of_volumes of this Book.

        Description not available  # noqa: E501

        :param number_of_volumes: The number_of_volumes of this Book.
        :type number_of_volumes: List[int]
        """

        self._number_of_volumes = number_of_volumes

    @property
    def composer(self):
        """Gets the composer of this Book.

        Description not available  # noqa: E501

        :return: The composer of this Book.
        :rtype: List[object]
        """
        return self._composer

    @composer.setter
    def composer(self, composer):
        """Sets the composer of this Book.

        Description not available  # noqa: E501

        :param composer: The composer of this Book.
        :type composer: List[object]
        """

        self._composer = composer

    @property
    def author(self):
        """Gets the author of this Book.

        Description not available  # noqa: E501

        :return: The author of this Book.
        :rtype: List[object]
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this Book.

        Description not available  # noqa: E501

        :param author: The author of this Book.
        :type author: List[object]
        """

        self._author = author

    @property
    def preface_by(self):
        """Gets the preface_by of this Book.

        Description not available  # noqa: E501

        :return: The preface_by of this Book.
        :rtype: List[object]
        """
        return self._preface_by

    @preface_by.setter
    def preface_by(self, preface_by):
        """Sets the preface_by of this Book.

        Description not available  # noqa: E501

        :param preface_by: The preface_by of this Book.
        :type preface_by: List[object]
        """

        self._preface_by = preface_by

    @property
    def runtime(self):
        """Gets the runtime of this Book.

        Description not available  # noqa: E501

        :return: The runtime of this Book.
        :rtype: List[object]
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Book.

        Description not available  # noqa: E501

        :param runtime: The runtime of this Book.
        :type runtime: List[object]
        """

        self._runtime = runtime

    @property
    def media_type(self):
        """Gets the media_type of this Book.

        Print / On-line (then binding types etc. if relevant)  # noqa: E501

        :return: The media_type of this Book.
        :rtype: List[object]
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this Book.

        Print / On-line (then binding types etc. if relevant)  # noqa: E501

        :param media_type: The media_type of this Book.
        :type media_type: List[object]
        """

        self._media_type = media_type

    @property
    def production_company(self):
        """Gets the production_company of this Book.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :return: The production_company of this Book.
        :rtype: List[object]
        """
        return self._production_company

    @production_company.setter
    def production_company(self, production_company):
        """Sets the production_company of this Book.

        the company that produced the work e.g. Film, MusicalWork, Software  # noqa: E501

        :param production_company: The production_company of this Book.
        :type production_company: List[object]
        """

        self._production_company = production_company

    @property
    def label(self):
        """Gets the label of this Book.

        short description of the resource  # noqa: E501

        :return: The label of this Book.
        :rtype: List[str]
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Book.

        short description of the resource  # noqa: E501

        :param label: The label of this Book.
        :type label: List[str]
        """

        self._label = label

    @property
    def original_language(self):
        """Gets the original_language of this Book.

        The original language of the work.  # noqa: E501

        :return: The original_language of this Book.
        :rtype: List[object]
        """
        return self._original_language

    @original_language.setter
    def original_language(self, original_language):
        """Sets the original_language of this Book.

        The original language of the work.  # noqa: E501

        :param original_language: The original_language of this Book.
        :type original_language: List[object]
        """

        self._original_language = original_language

    @property
    def license(self):
        """Gets the license of this Book.

        Description not available  # noqa: E501

        :return: The license of this Book.
        :rtype: List[object]
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Book.

        Description not available  # noqa: E501

        :param license: The license of this Book.
        :type license: List[object]
        """

        self._license = license

    @property
    def subject_term(self):
        """Gets the subject_term of this Book.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :return: The subject_term of this Book.
        :rtype: List[str]
        """
        return self._subject_term

    @subject_term.setter
    def subject_term(self, subject_term):
        """Sets the subject_term of this Book.

        The subject as a term, possibly a term from a formal classification  # noqa: E501

        :param subject_term: The subject_term of this Book.
        :type subject_term: List[str]
        """

        self._subject_term = subject_term

    @property
    def original_title(self):
        """Gets the original_title of this Book.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :return: The original_title of this Book.
        :rtype: List[str]
        """
        return self._original_title

    @original_title.setter
    def original_title(self, original_title):
        """Sets the original_title of this Book.

        The original title of the work, most of the time in the original language as well  # noqa: E501

        :param original_title: The original_title of this Book.
        :type original_title: List[str]
        """

        self._original_title = original_title

    @property
    def circulation(self):
        """Gets the circulation of this Book.

        Description not available  # noqa: E501

        :return: The circulation of this Book.
        :rtype: List[int]
        """
        return self._circulation

    @circulation.setter
    def circulation(self, circulation):
        """Sets the circulation of this Book.

        Description not available  # noqa: E501

        :param circulation: The circulation of this Book.
        :type circulation: List[int]
        """

        self._circulation = circulation

    @property
    def oclc(self):
        """Gets the oclc of this Book.

        Online Computer Library Center number  # noqa: E501

        :return: The oclc of this Book.
        :rtype: List[str]
        """
        return self._oclc

    @oclc.setter
    def oclc(self, oclc):
        """Sets the oclc of this Book.

        Online Computer Library Center number  # noqa: E501

        :param oclc: The oclc of this Book.
        :type oclc: List[str]
        """

        self._oclc = oclc

    @property
    def producer(self):
        """Gets the producer of this Book.

        The producer of the creative work.  # noqa: E501

        :return: The producer of this Book.
        :rtype: List[object]
        """
        return self._producer

    @producer.setter
    def producer(self, producer):
        """Sets the producer of this Book.

        The producer of the creative work.  # noqa: E501

        :param producer: The producer of this Book.
        :type producer: List[object]
        """

        self._producer = producer

    @property
    def starring(self):
        """Gets the starring of this Book.

        Description not available  # noqa: E501

        :return: The starring of this Book.
        :rtype: List[object]
        """
        return self._starring

    @starring.setter
    def starring(self, starring):
        """Sets the starring of this Book.

        Description not available  # noqa: E501

        :param starring: The starring of this Book.
        :type starring: List[object]
        """

        self._starring = starring

    @property
    def completion_date(self):
        """Gets the completion_date of this Book.

        Description not available  # noqa: E501

        :return: The completion_date of this Book.
        :rtype: List[str]
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this Book.

        Description not available  # noqa: E501

        :param completion_date: The completion_date of this Book.
        :type completion_date: List[str]
        """

        self._completion_date = completion_date

    @property
    def writer(self):
        """Gets the writer of this Book.

        Description not available  # noqa: E501

        :return: The writer of this Book.
        :rtype: List[object]
        """
        return self._writer

    @writer.setter
    def writer(self, writer):
        """Sets the writer of this Book.

        Description not available  # noqa: E501

        :param writer: The writer of this Book.
        :type writer: List[object]
        """

        self._writer = writer

    @property
    def magazine(self):
        """Gets the magazine of this Book.

        Description not available  # noqa: E501

        :return: The magazine of this Book.
        :rtype: List[object]
        """
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        """Sets the magazine of this Book.

        Description not available  # noqa: E501

        :param magazine: The magazine of this Book.
        :type magazine: List[object]
        """

        self._magazine = magazine

    @property
    def illustrator(self):
        """Gets the illustrator of this Book.

        Illustrator (where used throughout and a major feature)  # noqa: E501

        :return: The illustrator of this Book.
        :rtype: List[object]
        """
        return self._illustrator

    @illustrator.setter
    def illustrator(self, illustrator):
        """Sets the illustrator of this Book.

        Illustrator (where used throughout and a major feature)  # noqa: E501

        :param illustrator: The illustrator of this Book.
        :type illustrator: List[object]
        """

        self._illustrator = illustrator