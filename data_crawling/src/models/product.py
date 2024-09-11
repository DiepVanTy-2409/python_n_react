import httpx
from ..constants import FPT_SHOP_API_KEY,\
      NUMBER_OF_PRODUCTS_PER_PAGE, API_KEY_GET_PRODUCT_IDS
from ..utils.logger import logging_info
class Product:
    def __init__(self, id, name, image_src, brand_name, price, price_online):
        self.id = id
        self.name = name
        self.brand_name = brand_name
        self.image_src = image_src
        self.price = price
        self.price_online = price_online

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_src": self.image_src,
            "brand_name": self.brand_name,
            "price": self.price,
            "price_online": self.price_online,
         }
    
    @staticmethod
    async def get_products_ids():
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(API_KEY_GET_PRODUCT_IDS)
                return response.json()
        except Exception as e:
            raise e

    @staticmethod
    async def get_products_by_page(page_index = 1):
        '''Get products per page'''
        try:
            url = f"{FPT_SHOP_API_KEY}{page_index}" 
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = response.json()
                products = data['datas']['filterModel']['listDefault']['list']
                return [ Product(
                        id= p['productVariant']['id'],
                        name=p['name'],
                        brand_name=p['brandName'],
                        image_src=p['urlPicture'], 
                        price=p['productVariant']['price'],
                        price_online=p["productVariant"]['priceOnline'])
                    for p in products ]
        except Exception as e:
            raise e
        
    @staticmethod
    async def get_new_products():
        '''Get new products'''
        try:
            ids_exists = await Product.get_products_ids()
            products = []
            products_current_page = []
            page_index = 1
            isFirst = True
            new_ids = []

            while (isFirst or len(products_current_page) >= NUMBER_OF_PRODUCTS_PER_PAGE):
                products_current_page = await Product.get_products_by_page(page_index)
                _pcp = [p for p in products_current_page]
                # Xuất hiện một sp ở hai page cần loại bỏ bớt 763299
                for p in products_current_page:
                    if p.id not in new_ids:
                        new_ids.append(p.id)
                    else:
                        _pcp.remove(p)
                products.extend(_pcp)
                page_index += 1
                isFirst = False
                logging_info('products_current_page',
                             f'{len(products_current_page)}')

            newProducts = list(filter(lambda x: x.id not in ids_exists, products))
            # print('Product::get_new_products: new ids: ')
            # [print(x.id) for x in newProducts]
            return newProducts
        except Exception as e:
            print(e)
            return []