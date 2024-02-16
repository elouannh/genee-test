import Divider from '@mui/material/Divider';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import "./App.css";
import { useEffect, useState } from 'react';

export default function Place({ place, index, setPlaces, multi }) {
    const [departement, setDepartement] = useState(place.departement)
    const [commune, setCommune] = useState(place.commune)
    const [desc, setDesc] = useState(place.desc)
    const [autoDep, setAutoDep] = useState([{label: "..."}])
    const [autoCom, setAutoCom] = useState([{label: "..."}])
    
    useEffect(() => {
        setPlaces((prev) => {
            prev[index] = {departement, commune, desc}
            return (prev)
        })
    }, [departement, commune, desc])

    // useEffect(async () => {
    //    const response = await fetch("localhost:5001/api/place", {method: "POST", body: JSON.stringify({dep_name: departement})})
    //     console.log(response)
    // }, [departement])

    return (
        <div className='place_container'>
            <div>
                <Autocomplete
                disablePortal
                options={autoDep}
                sx={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Departement" />}
                value={departement}
                onChange={(e, value) => setDepartement(value)}
                />
            </div>
            <div>
                <Autocomplete
                    disablePortal
                    options={autoCom}
                    sx={{ width: 300 }}
                    renderInput={(params) => <TextField {...params} label="Commune" />}
                    value={commune}
                    onChange={(e, value) => setCommune(value)}
                />
            </div>
            <div className='text_case'>
                <TextField
                id="outlined-required"
                sx={{ width: 300}}
                onChange={(e, value) => setDesc(value)}
                value={desc}
                />
                <Button sx={{margin: 1}} variant="contained" color="error" disabled={!multi}>
                    X
                </Button>
            </div>
            <Divider/>
        </div>
    )
}
