def modify_json_values(json_data, key, value):
    if key in json_data:
        json_data[key] = value


def remove_json_values(json_data, key):
    if key in json_data:
        del json_data[key]


def remove_property_object(json_data, key_to_remove):
    if key_to_remove in json_data:
        del json_data[key_to_remove]


def remove_items_within_list_property(json_data, key, index, target):
    if key in json_data:
        if target in json_data[key][index]:
            del json_data[key][index][target]


def modify_dict_value(json_data, dict_key, second_key, value):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        if second_key in json_data[dict_key]:
            json_data[dict_key][second_key] = value


def clear_dict_nested_value(json_data, dict_key, second_key):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        if second_key in json_data[dict_key]:
            json_data[dict_key][second_key] = {}


def remove_items_dict_nested_value(json_data, dict_key, second_key):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        if second_key in json_data[dict_key]:
            del json_data[dict_key][second_key]


def clear_dict_value(json_data, dict_key):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        json_data[dict_key] = {}


def set_empty_nested_dict_value(json_data, dict_key, second_key, target, value):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        if second_key in json_data[dict_key]:
            if target in json_data[dict_key][second_key]:
                json_data[dict_key][second_key][target] = value


def set_null_nested_dict_value(json_data, dict_key, second_key, target):
    if dict_key in json_data and isinstance(json_data[dict_key], dict):
        if second_key in json_data[dict_key]:
            if target in json_data[dict_key][second_key]:
                del json_data[dict_key][second_key][target]


def remove_property_object_within_object(json_data, key_to_remove, index, second_key, second_index=None):
    if key_to_remove in json_data and isinstance(json_data[key_to_remove], list):
        target_list = json_data[key_to_remove]

        if index < len(target_list):
            target_dict = target_list[index]

            if second_key in target_dict and isinstance(target_dict[second_key], list):
                target_sublist = target_dict[second_key]

                if second_index is not None and second_index < len(target_sublist):
                    del target_sublist[second_index]
                    return True
                elif second_index is None:
                    del target_dict[second_key]
                    return True

    return False


def turn_empty_list_in_json(json_data, key):
    if key in json_data and isinstance(json_data[key], list):
        json_data[key] = []


def modify_items_within_object_property(json_data, primary_key, index, second_key, value):
    if primary_key in json_data and isinstance(json_data[primary_key], list):
        if second_key in json_data[primary_key][index] and isinstance(json_data[primary_key][index], dict):
            json_data[primary_key][index][second_key] = value


def update_attribute_in_nested_object(json_data, keys_and_indices, attribute, new_value):
    current = json_data
    for key, index in keys_and_indices:
        if key in current and isinstance(current[key], list) and index < len(current[key]):
            current = current[key][index]
        else:
            return False

    if attribute in current:
        current[attribute] = new_value
        return True
    else:
        return False


def delete_attribute_in_nested_object(json_data, keys_and_indices, attribute):
    current = json_data
    for key, index in keys_and_indices:
        if key in current and isinstance(current[key], list) and index < len(current[key]):
            current = current[key][index]
        else:
            return False

    if attribute in current:
        del current[attribute]
        return True
    else:
        return False

# def clear_dict_in_nested_object(json_data, primary_key, target):
#     if primary_key in json_data and isinstance(json_data[primary_key], list):
#         campaigns = json_data[primary_key]
#
#         for campaign in campaigns:
#             if target in campaign and isinstance(campaign[target], list):
#                 campaign[target] = []
#
#     return json_data
