import elasticsearch

from parse_database_data import (
    parse_contracts44fz_for_search_engine,
    parse_directory_for_search_engine,
    parse_price_offer_for_search_engine,
)


search_engine = elasticsearch.Elasticsearch("http://localhost:9200")


contracts44fz_data = parse_contracts44fz_for_search_engine()
for data in contracts44fz_data:
    search_engine.index(index="contracts44fz_medium_data", body=data)

print("dir ")
directory_data = parse_directory_for_search_engine()
for data in directory_data:
    search_engine.index(index="directory_medium_data", body=data)

print("priceofer")

price_offer_data = parse_price_offer_for_search_engine()
for data in price_offer_data:

    search_engine.index(index="price_offer_medium_data", body=data)
