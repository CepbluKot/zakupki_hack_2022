import json


def get_contracts44fz_data():
    file = open('./small_data/contracts44fz.json')
    file = file.read()
    return json.loads(file)


def get_directory_data():
    file = open('./small_data/directory.json')
    file = file.read()
    return json.loads(file)


def get_price_offer_data():
    file = open('./small_data/price_offer.json')
    file = file.read()
    return json.loads(file)


def get_country_directory_data():
    file = open('./small_data/country_directory.json')
    file = file.read()
    return json.loads(file)
