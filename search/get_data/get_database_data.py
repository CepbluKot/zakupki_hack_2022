import sqlalchemy


engine = sqlalchemy.create_engine(
    "postgresql+psycopg2://postgres:752505@localhost/zakupki_hack_big"
)
engine.connect()

metadata = sqlalchemy.MetaData()


contracts44fz = sqlalchemy.Table(
    "table_1",
    metadata,
    sqlalchemy.Column("product_name", sqlalchemy.Text()),
    sqlalchemy.Column(
        "price",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_vat_rate",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_msr",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_characteristics",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "okpd2_code",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "okpd2_name",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column("inn", sqlalchemy.Text()),
    sqlalchemy.Column("country_code", sqlalchemy.Text()),
)


directory = sqlalchemy.Table(
    "table_2",
    metadata,
    sqlalchemy.Column("product_name", sqlalchemy.Text()),
    sqlalchemy.Column(
        "price",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_vat_rate",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_msr",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_characteristics",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column("okpd2_code", sqlalchemy.Text()),
    sqlalchemy.Column("okpd2_name", sqlalchemy.Text()),
    sqlalchemy.Column("inn", sqlalchemy.Text()),
    sqlalchemy.Column("country_code", sqlalchemy.Text()),
)


price_offer = sqlalchemy.Table(
    "table_3",
    metadata,
    sqlalchemy.Column("product_name", sqlalchemy.Text()),
    sqlalchemy.Column(
        "price",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_vat_rate",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_msr",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column(
        "product_characteristics",
        sqlalchemy.Text(),
    ),
    sqlalchemy.Column("inn", sqlalchemy.Text()),
    sqlalchemy.Column("okpd2_code", sqlalchemy.Text()),
    sqlalchemy.Column("okpd2_name", sqlalchemy.Text()),
    sqlalchemy.Column("country_code", sqlalchemy.Text()),
)


country_directory = sqlalchemy.Table(
    "country_dir",
    metadata,
    sqlalchemy.Column("country_name", sqlalchemy.Text()),
    sqlalchemy.Column(
        "country_code",
        sqlalchemy.Text(),
    ),
)


def get_contracts44fz_data():
    query = sqlalchemy.select([contracts44fz]).limit(10000)
    return engine.execute(query).fetchall()


def get_directory_data():
    query = sqlalchemy.select([directory]).limit(10000)
    return engine.execute(query).fetchall()


def get_price_offer_data():
    query = sqlalchemy.select([price_offer]).limit(10000)
    return engine.execute(query).fetchall()


def get_country_directory_data():
    query = sqlalchemy.select([country_directory])
    return engine.execute(query).fetchall()
