from asyncio.windows_events import NULL
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None

data = pd.read_csv("data/Справочник пром производства.csv", sep=";")
data = data.fillna(NULL)

have_price = data[data["price"] > data["price"].min()]
none_price = data[data["price"] == data["price"].isnull()]

without_nds = data[data["product_vat_rate"] == "Без НДС"]
with_nds = data[data["product_vat_rate"] != "Без НДС"]

by_country_643 = data[data["country_code"] == 643]
not_country_643 = data[data["country_code"] == 0]