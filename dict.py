from flask import make_response, abort

def matching_strings(strings, queries):
    res = [0] * len(queries)
    strings = strings.split(',')
    queries = queries.split(',')

    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                res[i] += 1

    nb_occurrence = {}
    for i in range(len(queries)):
        nb_occurrence[queries[i]] = res[i]

    return nb_occurrence


# Data to serve with our API
DICT = {
    "ab,bd": {
        "strings": "ab,bc,cd",
        "queries": "ab,bd",
        "nb_occurrence": matching_strings("ab,bc,cd", "ab,bd"),
    },
    "ab,bc,cd": {
        "strings": "ab,ab,cd,bc,cd",
        "queries": "ab,bc,cd",
        "nb_occurrence": matching_strings("ab,ab,cd,bc,cd", "ab,bc,cd"),
    },
}


def read_all():
    # Create the list of DICT from our data
    return [DICT[key] for key in sorted(DICT.keys())]


def read_one(queries):

    if queries in DICT:
        dict = DICT.get(queries)

    # otherwise, nope, not found
    else:
        abort(
            404, "Dictionary with query {queries} not found".format(queries=queries)
        )
    return dict


def create(dictionary):
    queries = dictionary.get("queries", None)
    strings = dictionary.get("strings", None)

    if queries not in DICT and queries is not None:
        DICT[queries] = {
            "queries": queries,
            "strings": strings,
            "nb_occurrence": matching_strings(strings, queries),
        }
        return make_response(
            "{queries} successfully created".format(queries=queries), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Dictionary with query {queries} already exists".format(queries=queries),
        )


def update(queries, dictionary):

    if queries in DICT:

        strings = dictionary.get("strings")

        DICT[queries]["strings"] = strings
        DICT[queries]["nb_occurrence"] = matching_strings(strings, queries)

        return DICT[queries]

    # otherwise, nope, that's an error
    else:
        abort(
            404, "Dictionary with query {queries} not found".format(queries=queries)
        )


def delete(queries):
    if queries in DICT:
        del DICT[queries]
        return make_response(
            "{queries} successfully deleted".format(queries=queries), 200
        )

    else:
        abort(
            404, "Dictionary with query {queries} not found".format(queries=queries)
        )
