import json

from flask import request

from nlp.match_categories import get_matched_categories_in_phrase


def validate(text):
    if not text:
        return (
            "No relevant data given. Please provide a text parameter e.g. "
            "?text=I+love+concentrated+apricot+juice"
        )


def configure_routes(app, match_dict, phrase_matcher):
    @app.route("/")
    def find_categories_in_phrase():
        text = request.args.get("text", type=str)

        error_message = validate(text)
        if error_message:
            return json.dumps({"error": error_message})

        # TODO: The result is neater but, it may be safer to have
        #   ensure_ascii=True.
        #   see https://stackoverflow.com/questions/40412714/using-json-dumps-with-ensure-ascii-true
        return json.dumps(
            list(get_matched_categories_in_phrase(match_dict, phrase_matcher, text)),
            ensure_ascii=False,
        )
