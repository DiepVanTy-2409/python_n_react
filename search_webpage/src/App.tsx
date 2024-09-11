import { BrowserRouter, Routes, Route } from 'react-router-dom'
import './App.css'
import HomePage from './pages/HomePage'


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' Component={HomePage} />
      </Routes>
    </BrowserRouter>
  )
}

export default App