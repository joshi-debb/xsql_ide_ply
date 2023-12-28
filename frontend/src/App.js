
import React, { useState } from 'react';
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

  const [getTrad, setTrad] = useState('');

  const [selectedFile, setSelectedFile] = useState(null);


  const [items, setItems] = useState({ ListSymbol: [], ListError: [], ListConsole: [] });

  const traduccion = {
    adsf: '1a'
  }

  const data = {
    ListSymbol: [1, 2, 3],
    ListError: ['a', 'b', 'c'],
    ListConsole: ['1a', '2b', '3c']
  }


  const handleChange1 = (value) => {
    setCode1(value);
  }

  const handleChange2 = (value) => {
    setCode2(value);
  }

  const ejecutar_ins = () => {
    setItems(data)
    // console.log(data.ListConsole)
  }

  const traducir_ins = () => {
    setCode2('SELECT * FROM persona;')
    console.log('oli')

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

                <button className="buttons" type="button" onClick={ejecutar_ins}>Ejecutar</button>

                

                <button className="buttons" type="button" onClick={traducir_ins}>Traducir</button>

              </div>
            </div>

          </div>

          <div className="paneles">
            <Pestaña items={items.ListError} env={items.ListSymbol} terminal={items.ListConsole} />
          </div>

        </div>

      </div>

    </div>

  );
}

export default App;
