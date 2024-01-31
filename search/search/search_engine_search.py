from dataclasses import replace
import json
import os
import elasticsearch


search_engine = elasticsearch.Elasticsearch("http://localhost:9200")

# search_query = {
#         'size' : 10000,
#         'query': {
#             'match_all' : {
#                 "product_name" : "локи"
#             }
#         }
#     }

# res = search_engine.search(
#         index="contracts44fz",
#         body={
#             "query": {
#                 "query_string": {
#                     "default_field": "for_search_engine",
#                     "query": "*яблоки* ",
#                 }
#             }
#         },
#     )

# res2 = []

# res2.append( search_engine.search(
#         index="contracts44fz",
#         body={
#   "query": {
#     "fuzzy" : { "for_search_engine" : "масляный" }
#   }
# }
#     )
# )

# res2.append( search_engine.search(
#         index="contracts44fz",
#         body={
#   "query": {
#     "fuzzy" : { "for_search_engine" : "фильтр" }
#   }
# }
#     )
# )

# res2.append( search_engine.search(
#         index="contracts44fz",
#         body={
#   "query": {
#     "fuzzy" : { "for_search_engine" : "авто" }
#   }
# }
#     )
# )
# res2 = search_engine.search(
#         index="contracts44fz",
#         body={
#   "query": {
#     "fuzzy": {
#       "for_search_engine": {
#         "value": "хлеб пшеничный ",
#         "fuzziness": 5,
#         "max_expansions": 50,
#         "prefix_length": 0,
#         "transpositions": True,
#         "rewrite": "constant_score"
#       }
#     }
#   }
# }
#     )


# while(1):

#     serch = str(input())
#     os.system("clear")
#     serch = serch.replace("  ", " ")
#     serch = serch.replace(" ", "~")
#     serch = serch.replace("~", "~ ")
#     if serch[-1] == ' ':
#         serch = serch[:len(serch) - 1]
#     if serch[-1] != '~':
#         serch += '~'
#     print(serch)
#     res2 = search_engine.search(
#             index="contracts44fz_medium_data",
#             body={
#     "query": {
#         "query_string": {
#         "query": serch,
#         "default_field": "for_search_engine"
#         }
#     }
#     }
#         )


#     for data in res2["hits"]["hits"]:

#         print(  '\n',
#             data["_source"]['product_name']

#         )

serch = "бур"

while "  " in serch:
    serch = serch.replace("  ", " ")

check_id = 0
while check_id < len(serch):
    print(serch[check_id], serch[check_id] == "/")
    if serch[check_id] in [
        "+",
        "-",
        "=",
        "&&",
        "||",
        ">",
        "<",
        "!",
        "(",
        ")",
        "{",
        "}",
        "[",
        "]",
        "^",
        '"',
        "~",
        "*",
        "?",
        ":",
        "\\",
        "/",
    ]:

        serch = serch[:check_id] + "\\" + serch[check_id:]

        check_id += 3

    else:
        check_id += 1

serch = serch.strip()
serch = serch.replace(" ", "~")
serch = serch.replace("~", "~ ")


if serch[-1] != "~":
    serch += "~"

print(serch)

res2 = search_engine.search(
    index="contracts44fz_small_data",
    body={
        "query": {
            "query_string": {"query": serch, "default_field": "product_name"}
            
        },
        "size": 30,
    },
)
id = 0
for data in res2["hits"]["hits"]:
    print(id)
    id += 1
    print("\n", data["_source"]["product_name"])
