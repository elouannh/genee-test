import { useState } from 'react'
import './App.css'
// import { ICase } from "./interface"

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className='global_container'>
      <div>
        onglet here
      </div>
      <div>
        Vite + React
      </div>
    </div>
  )
}

export default App
