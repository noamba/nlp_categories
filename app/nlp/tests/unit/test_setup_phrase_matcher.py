"""This module includes unit-tests for the setup_phrase_match module"""

import collections

import pandas as pd
from spacy.matcher import PhraseMatcher

from settings import CATEGORIES_FILE
from nlp.setup_phrase_match import get_categories, get_match_dict, get_phrase_matcher


def test_get_categories():
    """test get_categories function"""
    categories = get_categories(CATEGORIES_FILE)

    assert type(categories) == pd.Series
    assert not categories.empty


def test_get_match_dict(prepared_data_fixture, categories_series_fixture):
    """test get_match_dict function"""
    match_dict = get_match_dict(prepared_data_fixture)

    assert type(match_dict) == collections.defaultdict
    assert len(match_dict) >= len(prepared_data_fixture) > 0

    # check that a representative match_dict value is one of the
    # original categories
    assert list(match_dict.values())[0].pop() in categories_series_fixture.to_list()


def test_get_phrase_matcher_returns_PhraseMatcher(match_dict_fixture):
    """test get_phrase_matcher returns a PhraseMatcher"""
    phrase_matcher = get_phrase_matcher(match_dict_fixture)

    assert type(phrase_matcher) == PhraseMatcher
