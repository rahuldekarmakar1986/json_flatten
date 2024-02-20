import json

def flatten(json_filepath, keys, output_filepath):
    """
    :param json_file_path: Nested json input file (i.e. example.json)
    :param keys: A list of json key paths to be flattened
    :param output_file_path: the flatten json output file path
    :return True if json_flatten completed without error
    """
    try:
        # Load the nested JSON data from the file
        with open(json_filepath, 'r') as f:
            nested_data = json.load(f)

        # Initialize an empty dictionary to store flattened data
        flattened_data = {}

        # Iterate over each key in the selected keys list
        for key in keys:
            # Split the key by '.' to access nested levels
            nested_keys = key.split('.')
            value = nested_data
            # Traverse the nested data structure to access the value corresponding to the key
            for nested_key in nested_keys:
                if type(value) is dict:
                    if nested_key in value:
                        value = value[nested_key]
                else:
                    if nested_key in value[0]:
                        value = value[0][nested_key]
                    else:
                        # If any key is missing, break and return False indicating failure
                        return False
            # Add the key-value pair to the flattened data dictionary
            flattened_data[key] = value

        # Write the flattened data to the output JSON file
        with open(output_filepath, 'w') as f:
            json.dump(flattened_data, f, indent=4)

        # Return True indicating success
        return True

    except Exception as e:
        # If any error occurs during the process, print the error and return False
        print("An error occurred:", e)
        return False