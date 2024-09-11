'''interact with the database'''

from ..config.db import db_config
import mysql.connector
from ..models.product import Product


class ProductService:

    @staticmethod
    def insert_many(products=[]):
        '''Insert a array of products to db'''
        try:
            with mysql.connector.connect(**db_config) as connection:
                cursor = connection.cursor()
                query = f"""INSERT INTO products ( 
                        id, name, image_src, brand_name, price, price_online) 
                        VALUES (%s, %s, %s, %s, %s, %s)"""
                # return [Product(*row) for row in cursor.commit()]
                [cursor.execute(query, (
                        p.id, p.name, p.image_src, p.brand_name, p.price, p.price_online
                    )) for p in products]
                connection.commit()
        except Exception as ex:
            raise ex

    @staticmethod
    def get_ids():
        '''Get product ids'''
        try:
            with mysql.connector.connect(**db_config) as connection:
                cursor = connection.cursor()
                cursor.execute("select id from products")
                return [row[0] for row in cursor.fetchall()]
        except mysql.connector.Error as err:
            # print("Error fetching product IDs from the database:", err)
            # return []
            raise err

    @staticmethod
    def find(key):
        '''Search for a product by key'''
        try:
            with mysql.connector.connect(**db_config) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    f"""SELECT id, name, image_src, brand_name, price, price_online 
                    from products 
                    where id like '%{key}%' 
                          or name like '%{key}%' 
                          or brand_name like '%{key}%'"""
                    )
                return [Product(*row) for row in cursor.fetchall()]
        except Exception as ex:
            raise ex