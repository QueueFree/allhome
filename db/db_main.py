import sqlite3
from allhome.db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('база данных создана')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
    db.commit()


async def sql_insert_products(info_product, category, product_id):
    cursor.execute(queries.INSERT_PRODUCTS_QUERY(
        info_product,
        category,
        product_id
    ))
