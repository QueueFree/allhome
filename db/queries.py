CREATE_TABLE_COLLECTION_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    collection VARCHAR(255) NOT NULL,
    product_id INTEGER VARCHAR(255) NOT NULL
    )
"""


INSERT_COLLECTION_PRODUCTS_QUERY = """
    INSERT INTO collection_products (collection, product_id)
    VALUES (?, ?)
"""
