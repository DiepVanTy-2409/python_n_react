'''API routing for products'''

from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import List

from ..models.product import Product
from ..services.product_service import ProductService
from ..utils.logger import logging_info

router = APIRouter()

@router.post('/api/product/save')
def save_new_products(products: List[Product], bg_tasks: BackgroundTasks):
    # [print(p) for p in products] 
    logging_info("product_router::save_new_products",
                 f"{len(products)} new products")
    try:
        bg_tasks.add_task(ProductService.insert_many, products=products)
        return {
            "new_products": len(products),
            "new_product_ids": [p.id for p in products]
        }
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail={"error": "Đã xảy ra lỗi!"}
        )

@router.get('/api/product/get-ids')
def get_product_ids(): 
    try:
        return ProductService.get_ids()
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail={"error": "Đã xảy ra lỗi!"}
        )

@router.get('/api/product')
def get_product(key: str = ""):
    logging_info("product_router::get_product", f"search with key: {key}")
    try:
        # return {"_key_search": key}
        return ProductService.find(key)
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, 
            detail={"error": "Đã xảy ra lỗi!"}
        )