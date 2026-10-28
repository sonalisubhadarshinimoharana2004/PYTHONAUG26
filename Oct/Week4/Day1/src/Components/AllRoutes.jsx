import React from 'react'
import { Route, Routes } from 'react-router'
import Register from './components/Register'
import Home from './components/Home'

function AllRoutes() {
  return (
    <div>
        {/* Path declaration */}
        <Routes>
            <Route path='/' element={<Home/>}></Route>
            <Route path='/register' element={<Register/>}></Route>
        </Routes>
    </div>
  )
}

export default AllRoutes
