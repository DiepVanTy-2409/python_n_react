import React from "react"
import SearchIcon from "../assets/search_icon.svg";

type PropType = { 
    handleChange: React.ChangeEventHandler<HTMLInputElement> 
    handleSubmit: React.FormEventHandler<HTMLFormElement>
    value: string
}

const SearchBar = ({ handleChange, handleSubmit, value }: PropType) => {
    return (
        <form onSubmit={handleSubmit} className="search_bar">
            <input autoFocus onChange={handleChange} value={value} type="text" placeholder="Tìm kiếm..." />
            <button className="search_bar__btn" type="submit">
                <img src={SearchIcon} alt="" />    
                Tìm kiếm
            </button>
        </form>
    )
}

export default SearchBar