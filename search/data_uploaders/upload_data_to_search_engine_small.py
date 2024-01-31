import elasticsearch
import get_data.get_json_data as get_database_data

from parser.parse_database_data import (
    parse_contracts44fz_for_search_engine,
    parse_directory_for_search_engine,
    parse_price_offer_for_search_engine,
)


search_engine = elasticsearch.Elasticsearch("http://localhost:9200")

def upload_to_search():
    print("contracts ")
    # contracts44fz_data = parse_contracts44fz_for_search_engine()
    contracts44fz_data = get_database_data.get_contracts44fz_data()
    for data in contracts44fz_data:
        print(data)
        search_engine.index(index="contracts44fz_small_data", body=data)

    print("dir ")
    # directory_data = parse_directory_for_search_engine()
    directory_data = get_database_data.get_directory_data()
    for data in directory_data:
        search_engine.index(index="directory_small_data", body=data)

    print("priceofer")

    # price_offer_data = parse_price_offer_for_search_engine()
    price_offer_data = get_database_data.get_price_offer_data()
    for data in price_offer_data:

        search_engine.index(index="price_offer_small_data", body=data)
