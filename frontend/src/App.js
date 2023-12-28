
import React, { useState, useEffect } from 'react';
import './css/App.css';
import { MyButtons, Pestaña, import_data } from './comps/Tools';
import { okaidia } from '@uiw/codemirror-theme-okaidia';
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { saveAs} from 'file-saver';

import Sidebar from './comps/Sidebar';


function App() {

  const [code1, setCode1] = useState('');
  const [code2, setCode2] = useState('');

  const [selectedFile, setSelectedFile] = useState(null);


  const [items, setItems] = useState({ListConsole: [], ListError: [], ListSymbol: []});

  const [select_items, set_select_items] = useState({ListSelect: []});


  const handleChange1 = (value) => {
    setCode1(value);
  }

  const handleChange2 = (value) => {
    setCode2(value);
  }

  const handleSave = () => {
    const a = document.createElement("a");
    
    // Definir las variables blob y url con let o const
    const blob = new Blob([code1], { type: "octet/stream" });
    const url = window.URL.createObjectURL(blob);
    
    a.href = url;
    a.download = 'default.sql';
    
    a.click();
    
    window.URL.revokeObjectURL(url);
  };


  const impport_data = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setCode1(e.target.result);
        
      };
      reader.readAsText(file);
    }
    setSelectedFile(file);
    console.log(code1)
  }

  const traducir = () => {
    fetch ('http://localhost:5000/traduccion', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {setCode2(data.res)})
    .catch(err => console.log(err))
  }
  
  const selects = () => {
    fetch ('http://localhost:5000/selects', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      set_select_items(data)
    })
    .catch(err => console.log(err))
  }

  const ejecutar = () => {
    fetch ('http://localhost:5000/datas', {
      method: 'POST',
      body: code1,
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {setItems(data)})
    .catch(err => console.log(err))
  }

  const [imageSrc, setImageSrc] = useState('');

  const imges = () => {
    fetch('http://localhost:5000/get_image')
      .then(response => response.blob())
      .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        setImageSrc(imageUrl);
      })
      .catch(error => console.error('Error fetching image:', error));
  }

  return (
    <div className="App">
      <div>
        <div className="navbar">
          <h1>XSQL-IDE</h1>
          <div className="file-input-wrapper">
            <input className="file-input" type="file" id="fileInput" onChange={impport_data} />
            <label className="file-input-label" htmlFor="fileInput"> Importar </label>
            <button className="buttons" onClick={handleSave}>Guardar</button>
          </div>
        </div>
      </div>

      <div style={{ display: 'flex' }}>
        <div>
          {Sidebar()}
        </div>
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', alignItems: 'flex-start' }}>
            <div className='codemirror-style'>
              <CodeMirror
                value={code1}
                height='400px'
                width='900px'
                theme={okaidia}
                extensions={[javascript({ jsx: true })]}
                onChange={handleChange1}
              />
            </div>

            <div className='c3d-codemirror-style'>
              <div >
                <CodeMirror
                  value={code2}
                  height='360px'
                  width='390px'
                  theme={okaidia}
                  extensions={[javascript({ jsx: true })]}
                  onChange={handleChange2}
                />
              </div>

              <div>
                <button className="buttons" type="button" onClick={ejecutar}>Ejecutar</button>
                <button className="buttons" type="button" onClick={imges}>ast</button>
                <button className="buttons" type="button" onClick={traducir}>Traducir</button>
                <button className="buttons" type="button" onClick={selects}>select</button>
              </div>
            </div>

          </div>

          <div className="paneles">
            <Pestaña items={items.ListError} env={items.ListSymbol} terminal={items.ListConsole} ast={imageSrc} select={select_items}/>
          </div>

        </div>

      </div>

    </div>

  );
}

export default App;
