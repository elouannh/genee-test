import { useState } from 'react'
import { Button } from '@mui/material';
import './App.css'
import TextField from '@mui/material/TextField';
import Place from './Place';
import Divider from '@mui/material/Divider';
import Switch from '@mui/material/Switch';


function App() {
  const excase = {
    id: 1,
    name: "case1",
    places: [
      {
        departement: "rhone",
        commune: "lyon",
        desc: "c'est la description"
      }
    ]
  }
  const [multi, setMulti] = useState(false);
  const [places, setPlaces] = useState([{
    departement: "",
    commune: "",
    desc: ""
  }])

  return (
    <div className='global_container'>

      <div className='case_header'>
        <div className='case_item'>
          <Switch checked={multi} onChange={(e)=>setMulti(e.target.checked)} />
        </div>
        <div className='case_item'>
          <TextField
            id="outlined-required"
            label="Nom de l'affaire"
          />
        </div>
        <div className='case_item'>
          <Button variant="contained">send</Button>
        </div>
      </div>

      <Divider />
      { 
        places.map((place, index) => {
          if (!multi && index != 0)
            return (<></>);
          return (
            <div key={index}>
              <Place place={place} index={index} setPlaces={setPlaces} multi={multi}/>
            </div>
          );
        }
        )
      }
      <div>
        <Button sx={{margin: 1}} variant="contained" disabled={!multi}>ajouter</Button>
      </div>
      
    </div>
  )
}

export default App
