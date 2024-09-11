CREATE DATABASE fpt_shop_db;

USE fpt_shop_db;

CREATE TABLE
    products (
        id int (10) NOT NULL,
        name nvarchar(500) DEFAULT '',
        image_src varchar(100),
        brand_name nvarchar(100),
        price int (10),
        price_online int (10),
        PRIMARY KEY (id)
    );