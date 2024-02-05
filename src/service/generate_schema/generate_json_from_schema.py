from src.service.generate_schema.generate_data_for_user_creation import generate_password, generate_random_user


def generate_user_data_json(schema):
    data = {}

    for prop, prop_schema in schema.items():
        if isinstance(prop_schema, str):
            if prop_schema == "user-email":
                data[prop] = "eve.holt@reqres.in"
            if prop_schema == "user-name":
                data[prop] = generate_random_user()[0]
            if prop_schema == "user-job":
                data[prop] = generate_random_user()[1]
            elif prop_schema == "user-password":
                data[prop] = generate_password()
        elif isinstance(prop_schema, list):
            data[prop] = []
            for _ in range(len(prop_schema)):
                item_data = generate_user_data_json(prop_schema[0])
                data[prop].append(item_data)
        elif isinstance(prop_schema, dict):
            data[prop] = generate_user_data_json(prop_schema)

    return data


# loaded_schema = file_reader(filename='../service/generate_schema/create_user_schema.json')
# body = generate_user_data_json(loaded_schema)
# json_string = json.dumps(body, indent=4)
# print(json_string)
