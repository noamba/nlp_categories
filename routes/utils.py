from nlp.prepare_data import prepare_data
from nlp.setup_phrase_match import (
    get_categories,
    output_categories_df,
    get_match_dict,
    get_phrase_matcher,
)
from nlp.utils import save_object_to_disk, load_objects_from_disk
from settings import (
    CATEGORIES_FILE,
    DEBUG,
    PERSIST_MATCH_OBJECTS,
    MATCH_DICT_PICKLE_FILE,
    PHRASE_MATCHER_PICKLE_FILE,
)


def create_match_objects(
    categories_file,
    persist_match_objects,
    match_dict_pickle_file,
    phrase_matcher_pickle_file,
):
    print("Creating match objects from scratch...")
    # set up required objects for matching categories to a phrase
    categories = get_categories(categories_file)
    prepared_data = prepare_data(categories)

    if DEBUG == "Full":
        output_categories_df(prepared_data)

    match_dict = get_match_dict(prepared_data)
    phrase_matcher = get_phrase_matcher(match_dict)

    if persist_match_objects:
        save_object_to_disk(object_to_save=match_dict, path=match_dict_pickle_file)
        save_object_to_disk(
            object_to_save=phrase_matcher, path=phrase_matcher_pickle_file
        )

    return match_dict, phrase_matcher


def setup_match_objects(
        categories_file=CATEGORIES_FILE,
        persist_match_objects=PERSIST_MATCH_OBJECTS,
        match_dict_pickle_file=MATCH_DICT_PICKLE_FILE,
        phrase_matcher_pickle_file=PHRASE_MATCHER_PICKLE_FILE,
):
    match_dict = phrase_matcher = None

    if persist_match_objects:
        print("Trying to Load match objects from disk...")
        try:
            match_dict = load_objects_from_disk(match_dict_pickle_file)
            phrase_matcher = load_objects_from_disk(phrase_matcher_pickle_file)
        except FileNotFoundError:
            print("Can't find match object/s on disk...")

    if not (match_dict and phrase_matcher):
        match_dict, phrase_matcher = create_match_objects(
            categories_file,
            persist_match_objects,
            match_dict_pickle_file,
            phrase_matcher_pickle_file,
        )

    return match_dict, phrase_matcher
