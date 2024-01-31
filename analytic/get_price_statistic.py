import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional, List
import json
from statistics import mean
from get_seller_info import get_sellers_info


class Item(BaseModel):
    lower_price: float = None
    higher_price: float = None
    average_price: float = None
    status: str = None


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
    #name: str
    #name_seller: str
    price: FloatFromStr
    #okpd2_code: int
    product_vat_rate: str
    product_name: str
    #okpd2_name: str
    product_msr: str
    country_code: FloatFromStr
    inn: str
    product_characteristics: DictFromStr
    alnalize: Optional[Item] = Item()

    class Config:
        exclude = {'for_search_engine'}


class ListFromOnePoint(list):
    @classmethod
    def validate(cls, v: list):
        all_element = []
        for one_el in v:
            all_element.append(OnePoint(**one_el["_source"]))
        return all_element

    @classmethod
    def get_validators(cls):
        yield cls.validate

class AllProduct(BaseModel):
    products: ListFromOnePoint = Field(List[OnePoint])

def get_item_list_price(json_with_prices):
    df_price = pd.read_json(json_with_prices.json())

    prices = []
    for i in range(len(df_price)):
        element_of_dict = df_price["products"].iloc[i]
        prices.append(float(element_of_dict["price"]))

    for i in range(len(df_price)):
        price_item = Item()
        if len(prices) == 0:
            continue
        elif not len(prices) == 0:
            average_arifmetic_price = mean(prices)
            percentage = average_arifmetic_price / 100
            price_item.lower_price = min(prices)
            price_item.higher_price = max(prices)
            price_item.average_price = average_arifmetic_price
            if prices[i] < average_arifmetic_price - percentage*10:
                price_item.status = "ниже рыночной цены"
            elif prices[i] > average_arifmetic_price + percentage*10:
                price_item.status = "выше рыночной цены"
            elif (prices[i] < average_arifmetic_price + percentage*10) & (prices[i] > average_arifmetic_price - percentage*10):
                price_item.status = "рыночная цена"
            if type(price_item) is Item:
                json_with_prices.products[i].alnalize = price_item

    return json_with_prices, price_item