import sys
import json
import math
import numbers


def build_flattened_key(prefix, key):
    """This function builds the key of the flattened object using the prefix 
       and the key

    Args:
        prefix (String): Correspond to the prefix of the key it is empty if 
        the current JSON object is not nested. If it nested it will corres-
        pond to all the keys before the current objects separated by dots.

        key (String): Correspond to the key of the current object that we are
        flattening

    Returns:
        String: Prefix.key if prefix not empty else key
    """
    return key if not prefix else prefix + "." + key


def flatten_json(object_json, prefix="", flatten_result={}):
    """Method that call itself recursively to flatten the object object_json
       This function currently does not support the arrays as it was not a 
       necessary.

    Args:
        object_json (dict): The JSON object that we flatten

        prefix (str, optional): The multiple keys (separated by ".") of the 
        parents of the JSON object to nest. Defaults to ""

        flatten_result (dict, optional): The Dictionnary that correspond to
        the current flatten JSON we are creating. Defaults to {}

    Returns:
        dict: The JSON object flattened with the method required (The keys 
        of the nested objects are concatenated using a dot)
    """
    assert(type(object_json) is dict)
    for (key, value) in object_json.items():
        # Because the arrays are not supported the only special case is the
        # nested object
        if type(value) is dict:
            flatten_json(value, build_flattened_key(
                prefix, key), flatten_result)
        else:
            # Treat the values that are specific number cases (Necessary to
            # return a valid json object)
            if value == float("inf"):
                value = "Infinity"
            elif value == float("-inf"):
                value = "-Infinity"

            flatten_result[build_flattened_key(prefix, key)] = value

    return flatten_result


def main():
    """ This method will read the JSON file given as stdin and flatten the 
        object.
        The object needs to be a valid JSON object.
        The program can be used using a UNIX terminal like this: 
        "cat json_file_to_flatten.json | ptyhon3 program_mongo_db_json.py"
    """

    json_str = sys.stdin.read()

    try:
        object_json = json.loads(json_str)

    except json.JSONDecodeError:
        print("Error with the JSON input. Please check your JSON file.")
        sys.exit(1)

    final_object = flatten_json(object_json, prefix="")
    object_json_output = json.dumps(final_object, indent=4)

    print(object_json_output)


if __name__ == "__main__":
    main()
