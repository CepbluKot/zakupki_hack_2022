import json
import get_data.get_json_data as get_database_data


def parse_one_spec(specs: str):
    if ":" in specs:

        divide_index = specs.index(":")
        spec_name = specs[:divide_index]
        spec_value = specs[divide_index + 1 :]
        return spec_name, spec_value
    return specs


def parse_item_specs(data: str):
    if "||" in data:

        all_specs = []
        data = data.split("||")
        for one_spec in data:
            one_spec_json = {}
            one_spec = parse_one_spec(one_spec)

            one_spec_json["parameter"] = one_spec[0]
            one_spec_json["value"] = one_spec[1]
            all_specs.append(one_spec_json)
        return all_specs

    return data


def parse_item_specs_for_search_engine(data: str):
    if "||" in data:

        all_specs = {}
        data = data.split("||")
        for one_spec in data:
            one_spec = parse_one_spec(one_spec)
            all_specs[one_spec[0]] = one_spec[1]
        return json.dumps(all_specs)

    return data


def parse_contracts44fz():
    full_json = []
    for data in get_database_data.get_contracts44fz_data():
        formatted_json = {}

        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs(data[4])

        formatted_json["okpd2_code"] = data[5]
        formatted_json["okpd2_name"] = data[6]
        formatted_json["inn"] = data[7]
        formatted_json["country_code"] = data[8]
        full_json.append(formatted_json)

    return full_json


def parse_directory():
    full_json = []
    for data in get_database_data.get_directory_data():
        formatted_json = {}

        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs(data[4])
        formatted_json["okpd2_code"] = data[5]
        formatted_json["okpd2_name"] = data[6]
        formatted_json["inn"] = data[7]
        formatted_json["country_code"] = data[8]
        full_json.append(formatted_json)

    return full_json


def parse_price_offer():
    full_json = []
    for data in get_database_data.get_price_offer_data():
        formatted_json = {}

        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs(data[4])
        formatted_json["inn"] = data[5]
        formatted_json["country_code"] = data[6]
        full_json.append(formatted_json)

    return full_json


def parse_country_directory():
    full_json = []
    for data in get_database_data.get_country_directory_data():
        formatted_json = {}

        formatted_json["country_name"] = data[0]
        formatted_json["country_code"] = data[1]

        full_json.append(formatted_json)
    return full_json


def parse_contracts44fz_for_search_engine():
    full_json = []
    for data in get_database_data.get_contracts44fz_data():
        formatted_json = {}

        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs_for_search_engine(
            data[4]
        )

        formatted_json["okpd2_code"] = data[5]
        formatted_json["okpd2_name"] = data[6]

        formatted_json["inn"] = data[7]
        formatted_json["country_code"] = data[8]

        formatted_json["for_search_engine"] = data[0] + " " + data[4]

        full_json.append(formatted_json)

    return full_json


def parse_directory_for_search_engine():
    full_json = []
    for data in get_database_data.get_directory_data():
        formatted_json = {}

        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs_for_search_engine(
            data[4]
        )
        formatted_json["okpd2_code"] = data[5]
        formatted_json["okpd2_name"] = data[6]
        formatted_json["inn"] = data[7]
        formatted_json["country_code"] = data[8]

        formatted_json["for_search_engine"] = data[0] + " " + data[4]

        full_json.append(formatted_json)

    return full_json


def parse_price_offer_for_search_engine():
    full_json = []
    for data in get_database_data.get_price_offer_data():
        formatted_json = {}
        print(data)
        formatted_json["product_name"] = data[0]
        formatted_json["price"] = data[1]
        formatted_json["product_vat_rate"] = data[2]
        formatted_json["product_msr"] = data[3]
        formatted_json["product_characteristics"] = parse_item_specs_for_search_engine(
            data[4]
        )

        formatted_json["okpd2_code"] = data[5]
        formatted_json["okpd2_name"] = data[6]

        formatted_json["inn"] = data[7]
        formatted_json["country_code"] = data[8]

        formatted_json["for_search_engine"] = data[0] + " " + data[4]

        full_json.append(formatted_json)

    return full_json


# f = open('example.txt', 'w')
# f.write(str(parse_country_directory()))
