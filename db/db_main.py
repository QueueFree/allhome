import sqlite3
from allhome.db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('база данных создана')

    cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)

    db.commit()


async def sql_insert_products(collection, product_id, name_products, info_products, size_products, price_products, photo):
    cursor.execute(queries.INSERT_COLLECTION_PRODUCTS_QUERY, (
        collection,
        product_id,
        name_products,
        info_products,
        size_products,
        price_products,
        photo
    ))

    db.commit()

