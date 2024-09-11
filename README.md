>[!NOTE]
> * Dùng lệnh sau để chạy dự án
> ```bash
> docker-compose up -d 
>```

Project
|-- data_crawling/
|-- mysql/
|-- mysql_api/
|-- search_webpage/
|-- docker-compose.yml 
    
data_crawling
|-- src/
|   |-- models/
|   |   |-- product.py
|   |   
|   |-- utils/
|   |   |-- logger.py
|   |
|   |-- contants.py
|   |-- main.py
|   |-- requirements.txt
|   |-- .env
|   
|-- Dockerfile

mysql
|-- init_db/
|   |-- create_user.sql
|   |-- init.sql
|   
|-- Dockerfile


mysql_api
|-- app/
|   |-- config/
|   |   |-- db.py
|   |   
|   |-- models/
|   |   |-- product.py
|   |   
|   |-- routers/
|   |   |-- product_router.py
|   |
|   |-- services/
|   |   |-- product_service.py
|   |
|   |-- utils/
|   |   |-- logger.py
|   |
|   |-- main.py
|   |-- requirements.txt
|   |-- .env
|   
|-- Dockerfile



search_webpage
|-- node_modules/
|   
|-- public/
|
|-- src/
|   |-- components
|   |   |-- ProdcuctCard.tsx
|   |   |-- SearchBar.tsx
|   |
|   |-- pages
|   |   |-- Homepage.tsx
|   |
|   |-- App.tsx
|   |-- main.tsx
|   
|-- index.html
|-- Dockerfile
|-- package.json
|-- .dockerignore
|-- .env
|-- ...