from pydantic import BaseModel


# Kế thừa BaseModel => https://fastapi.tiangolo.com/tutorial/body/
class Product(BaseModel):  
    id: int
    name: str
    image_src: str
    brand_name: str 
    price: int
    price_online: int

    def __init__(self, id, name, image_src, brand_name, 
                price, price_online):
        super().__init__(id=id, name=name, image_src=image_src, brand_name=brand_name,
                        price=price, price_online=price_online)