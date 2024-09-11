import { ProductType } from '../type'

const ProductCard = ({
    id, name, image_src, brand_name, price, price_online
}: ProductType) => {
    return (
        <div data-id={String(id)} className='product_card'>
            <div className="product_card__image_contaier">
                <img src={import.meta.env.VITE_IMAGE_BASE_URL + image_src} />
            </div>
            <h5>{name}</h5>
            <p className='text-small'>Thương hiệu: {brand_name}</p>
            <div className='product_card__prices'>
                <span className='text-small product_card__price'>{price_online} vnd</span>
                <del className='text-small'>{price} vnd</del>
            </div>
        </div>
    )
}

export default ProductCard