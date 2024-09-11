import httpx
from fastapi import FastAPI, HTTPException, BackgroundTasks
from .models.product import Product
from .constants import API_KEY_SAVE_NEW_PRODUCTS
from .utils.logger import logging_info

app = FastAPI()

# Hàm này sẽ thực hiện công việc của cả hai hàm trước đó và chạy như một background task
async def refresh_and_post_products():
    try:
        # Lấy dữ liệu sản phẩm mới
        new_products = await Product.get_new_products()
        if new_products:
            async with httpx.AsyncClient() as client:
                # Gửi dữ liệu sản phẩm mới đến server 
                response = await client.post(
                    API_KEY_SAVE_NEW_PRODUCTS,
                    json=[p.to_dict() for p in new_products])
                logging_info("Background task::post_new_products",
                    f"{len(new_products)} new products"
                )
                # print(f"Background task::post_new_products: {response.json()}")
        else:
            logging_info("Background task::post_new_products","No new products")
    except Exception as ex:
        # Ném lỗi để hàm refresh_data bên dưới sử lý
        raise ex

@app.get('/')
def greeting():
    return "Data crawling!"

# Endpoint chính để kích hoạt làm mới dữ liệu
@app.get('/api/data/crawl')
async def refresh_data(background_tasks: BackgroundTasks):
    try:
        # Đặt refresh_and_post_products vào background để thực thi
        background_tasks.add_task(refresh_and_post_products)
        return {"message": "Refresh process started, running in background"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An error occurred")
