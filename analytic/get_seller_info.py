import pandas as pd
from pydantic import BaseModel
from typing import List
from statistics import median, mean
import numpy as np
import json

class FloatFromStr(str):
    @classmethod
    def validate(cls, v: str):
        return float(v)

    @classmethod
    def get_validators(cls):
        yield cls.validate

class DictFromStr(str):
    @classmethod
    def validate(cls, v: str):
        try:
            res = v.replace("\'", "\"")
            # res = json.loads(res)
            # res = json.dumps(res, ensure_ascii=False).encode('utf-8')

            res = json.loads(res)
            return res
        except json.decoder.JSONDecodeError:
            return {}

    @classmethod
    def get_validators(cls):
        yield cls.validate


class OnePoint(BaseModel):
    price: FloatFromStr
    okpd2_code: int
    product_vat_rate: str
    product_name: str
    okpd2_name: str
    product_msr: str
    country_code: FloatFromStr
    inn: str
    product_characteristics: DictFromStr

class ItemListInfo(BaseModel):
    inn: str
    count_sale: int
    products: List[OnePoint]

class Item(BaseModel):
    upper_price: float
    lower_price: float
    average_price: float
    mediana_price: float
    count_seller: int
    count_sale: int
    sellers_info: List[ItemListInfo]

class ItemList(BaseModel):
    __root__: List[Item]

def return_inn_dict_product(unique_inn, df_sale):
    inn = []
    for i in range(len(df_sale)):
        element_of_dict = df_sale["products"].iloc[i]
        if element_of_dict["inn"] == unique_inn:
            inn.append(df_sale.products[i])
    return inn

def get_sellers_info(json_sales):
    df_sale = pd.read_json(json_sales.json())

    prices = []
    inn = []
    for i in range(len(df_sale)):
        element_of_dict = df_sale["products"].iloc[i]
        prices.append(float(element_of_dict["price"]))
        inn.append(element_of_dict["inn"])
    unique_inn = np.unique(np.array(inn))

    upper_price = max(prices)
    lower_price = min(prices)
    average_price = mean(prices)
    mediana_price = median(prices)
    count_seller = len(unique_inn)
    count_sale = len(df_sale)

    sellers_info = []
    for i in range(len(unique_inn)):
        seller_inf = {}
        seller_inf["inn"] = unique_inn[i]
        seller_inf["count_sale"] = inn.count(unique_inn[i])
        seller_inf["products"] = return_inn_dict_product(unique_inn, df_sale)
        sellers_info.append(seller_inf)

    info_to_pydantic_list = [{
        "upper_price": upper_price,
        "lower_price": lower_price,
        "average_price": average_price,
        "mediana_price": mediana_price,
        "count_seller": count_seller,
        "count_sale": count_sale,
        "sellers_info": sellers_info
    }]

    full_info = ItemList(__root__= info_to_pydantic_list)
    return full_info