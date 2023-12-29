
import React, { useState, useEffect } from 'react';
import './css/App.css';
import { Pestaña, side_bar } from './comps/Tools';
import { okaidia } from '@uiw/codemirror-theme-okaidia';
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';
import { saveAs } from 'file-saver';



function App() {

  const [code1, setCode1] = useState('');
  const [code2, setCode2] = useState('');

  const [selectedFile, setSelectedFile] = useState(null);



  const [items, setItems] = useState({ ListConsole: [], ListError: [], ListSymbol: [] });

  const [select_items, set_select_items] = useState({ ListSelect: [] });

  const [current_item, set_current_item] = useState({ xml_data: []});



  const handleChange1 = (value) => {
    setCode1(value);
  }

  const handleChange2 = (value) => {
    setCode2(value);
  }

  // boton de guardar
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
    fetch('http://localhost:5000/traduccion', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => { setCode2(data.res) })
      .catch(err => console.log(err))
  }

  const selects = () => {
    fetch('http://localhost:5000/selects', {
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

  const xml_datas = () => {
    fetch('http://localhost:5000/xml', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        set_current_item(data)

      })
      .catch(err => console.log(err))
  }

  const ejecutar = () => {
    fetch('http://localhost:5000/datas', {
      method: 'POST',
      body: code1,
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => { setItems(data) })
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
        <div className="navbar" >
          <h1 className="custom-color">XSQL-IDE</h1>
          <h1 className="custom-color">XSQL-IDE</h1>
          <h1 class="custom-color2">XSQL-IDE</h1>
          <h1 className="custom-color">XSQL-IDE</h1>

          <div className="file-input-wrapper" >
            <input className="file-input" type="file" id="fileInput" onChange={impport_data} />
            <label className="file-input-label" htmlFor="fileInput"> ABRIR </label>
            <button className="buttons" onClick={handleSave}> GUARDAR </button>
          </div>
        </div>
      </div>


      <div style={{ display: 'flex' }}>
        <div>
          {/* sidebar */}

          <div className="sidebar">
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <button className="buttons"> IMPORTAR </button>
              <button className="buttons"> EXPORTAR </button>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <button className="buttons"> SQL DUMP </button>
              <button className="buttons" onClick={xml_datas}> RECARGAR </button>
            </div>

            <hr />
            <div>
              <h4 style={{ display: 'flex', justifyContent: 'center' }}>DBMS</h4 >
              {/* {current_item.datas.database.map(item => {
                console.log(item)
              })} */}
              <h4 style={{ display: 'flex', justifyContent: 'center' }}></h4 >
            </div>
            {/* aqui se deben recorrer las bases de datos */}
            <hr />
            
            {console.log(current_item.xml_data)}
            {/* {current_item.xml_data.map(item => {
                console.log(item)
              })} */}
            <ul>
              <li> File
                <ul>
                  <li>Tablas</li>
                  <ul>
                    <li>tabla1</li>
                    <li>tabla2</li>
                  </ul>
                  <li>Vistas</li>
                  <li>Funciones</li>
                  <li>Procedimientos</li>
                </ul>
              </li>
            </ul>
            <hr />
            <hr />
            <ul>
              <li>File
                <ul>
                  <li>Tablas</li>
                  <ul>
                    <li>tabla1</li>
                    <li>tabla2</li>
                  </ul>
                  <li>Vistas</li>
                  <li>Funciones</li>
                  <li>Procedimientos</li>
                </ul>
              </li>
            </ul>
            <hr />



          </div>



          {/* sidebar */}
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

              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                <button className="buttons" type="button" onClick={ejecutar}> EJECUTAR </button>
                <button className="buttons" type="button" onClick={traducir}> TRADUCIR </button>
                <button className="buttons" type="button" onClick={imges}> ASTGDA </button>
                <button className="buttons" type="button" onClick={selects}> SELECT </button>
              </div>
            </div>

          </div>

          <div className="paneles">
            <Pestaña items={items.ListError} env={items.ListSymbol} terminal={items.ListConsole} ast={imageSrc} select={select_items} />
          </div>

        </div>

      </div>

    </div>

  );
}

export default App;
