import React, { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import SearchBar from '../components/SearchBar'
import ProductCard from '../components/ProductCard'
import axios from 'axios'
import { ProductType } from '../type'


function HomePage() {
    const [searchParams, setSearchParams] = useSearchParams()
    const [key, setKey] = useState<string>("")
    const [products, setProducts] = useState<ProductType[]>([])
    const [loading, setLoading] = useState<boolean>(true)

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setKey(e.target.value)
        setSearchParams({ key: e.target.value })
    }

    const getProducts = ({ key }: { key: string }) => (
        axios.get(import.meta.env.VITE_API_PRODUCT_SEARCH + key)
    )

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
            if (!key) return
            setLoading(true)
            const { data } = await getProducts({ key })
            setProducts(data)
            setKey("")
            setLoading(false)
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(() => {
        const fetchApi = async () => {
            const { data } = await getProducts({ key: searchParams.get('key') || '' })
            setProducts(data)
            setLoading(false)
        }
        fetchApi()
    }, [])


    return (
        <div className='app'>
            <SearchBar
                handleChange={handleChange}
                handleSubmit={handleSubmit}
                value={key} />
            <p className='product_count'>{products.length} sản phẩm</p>
            {loading && <h2 className='loading_text'>Đang tải...</h2>}
            {
                !products?.length && !loading
                    ? <h2 className='loading_text'>Không có kết quả phù hợp!</h2>
                    : <div className='product_cards'>
                        {
                            products?.map(p => (
                                <ProductCard {...p} />
                            ))
                        }
                    </div>
            }
        </div>
    )
}

export default HomePage
