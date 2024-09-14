CREATE_TABLE_PRODUCTS_DETAILS = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    info_product VARCHAR(255),
    category VARCHAR(255),
    product_id VARCHAR(255)
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products_details (info_product, product_id, category)
    VALUES (?, ?, ?)
"""
