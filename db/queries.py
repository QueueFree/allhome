CREATE_TABLE_COLLECTION_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_products VARCHAR(255) NOT NULL,
    info_products VARCHAR(255) NOT NULL,
    size_products VARCHAR(255) NOT NULL,
    price_products INTEGER NOT NULL,
    collection VARCHAR(255) NOT NULL,
    product_id INTEGER VARCHAR(255) NOT NULL,
    photo VARCHAR(499) NOT NULL
    )
"""


INSERT_COLLECTION_PRODUCTS_QUERY = """
    INSERT INTO collection_products (collection, product_id, name_products, info_products, size_products, price_products, photo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""
