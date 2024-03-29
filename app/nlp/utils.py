import pickle
from pprint import pprint
from time import perf_counter, sleep

from settings import DEBUG


def timeit(func):
    """Time func execution if in DEBUG mode. Used as decorator"""
    if not DEBUG:
        return func

    def timed(*args, **kw):
        start = perf_counter()
        result = func(*args, **kw)
        end = perf_counter()

        elapsed_time = end - start
        print(
            f"{'>>> ' if elapsed_time > 2 else ''}"
            f"{func.__name__} process time: {elapsed_time}\n"
        )

        return result

    return timed


@timeit
def save_object_to_disk(object_to_save, path):
    """Save (pickle) an object to disk"""
    print(f"Trying to save pickled object to {path}...")

    with open(path, "wb") as f:
        pickle.dump(object_to_save, f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?


@timeit
def load_objects_from_disk(path):
    """Load (unpickle) an object from disk"""
    print(f"Trying to open and load pickled object from: {path}")
    with open(path, "rb") as f:
        loaded_object = pickle.load(f)

    sleep(1)  # TODO: This may be needed to avoid a save/load issue with docker?

    return loaded_object


def output_matches(phrase, matched_original_categories):
    """Send data to output"""
    print("Phrase:", phrase)
    print("Matched categories:")
    pprint(matched_original_categories)
    print("\n")
