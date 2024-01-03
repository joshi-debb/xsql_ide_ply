
import React, { useState } from 'react';
import './css/App.css';
import { Pestaña, DatabaseInfo } from './comps/Tools';
import { okaidia } from '@uiw/codemirror-theme-okaidia';
import CodeMirror from '@uiw/react-codemirror';
import { javascript } from '@codemirror/lang-javascript';


function App() {

  //variable que almacena la imagen del ast
  const [imageSrc, setImageSrc] = useState('');
  //variable que almacena el codigo 1
  const [code1, setCode1] = useState('');
  //variable que almacena el codigo 2
  const [code2, setCode2] = useState('');
  //variable que almacena el estado de la base de datos
  const [estado, setEstado] = useState(false);
  //variable que las listas de los errores, simbolos y consola
  const [items, setItems] = useState({ ListConsole: [], ListError: [], ListSymbol: [] });
  //variable que almacena las consultas de la base de datos
  const [select_items, set_select_items] = useState({ ListSelect: [] });
  //variable que almacena la base de datos actual
  const [current_item, set_current_item] = useState({ database: [] });



  const handleChange1 = (value) => {
    setCode1(value);
  }

  const handleChange2 = (value) => {
    setCode2(value);
  }

  //barra lateral de la base de datos
  const xml_datas =
    async () => {
      fetch('http://localhost:5000/xml', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(res => res.json())
        .then(data => {
          set_current_item(data)
          setEstado(true)
          // console.log(data)
        })
        .catch(err => console.log(err))
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

  //importar archivo
  const impport_data = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setCode1(e.target.result);

      };
      reader.readAsText(file);
    }
  }

  //importar tabla
  const import_table = (event) => {
    const file = event.target.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        fetch('http://localhost:5000/datas', {
          method: 'POST',
          body: e.target.result,
          headers: {
            'Content-Type': 'application/json'
          }
        })
          .then(res => res.json())
          .then(data => { setItems(data) })
          .catch(err => console.log(err))
      };
      reader.readAsText(file);
    }

  };

  //exportar tabla
  const export_table = () => {
    fetch('http://localhost:5000/export', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);

        // Array para almacenar los blobs individuales
        const blobArray = [];

        data.datas.forEach((item, index) => {
          // Agregar un salto de línea entre los registros, excepto para el último
          const separator = index < data.datas.length - 1 ? '\n' : '';
          const blobData = `${item}${separator}`;

          // Crear un Blob para cada elemento
          const blob = new Blob([blobData], { type: "octet/stream" });
          blobArray.push(blob);
        });

        // Crear un Blob que contenga todos los blobs
        const finalBlob = new Blob(blobArray, { type: "octet/stream" });

        const a = document.createElement("a");
        const url = window.URL.createObjectURL(finalBlob);

        a.href = url;
        a.download = 'export.sql';

        a.click();

        window.URL.revokeObjectURL(url);

      })
      .catch(err => console.log(err));
  }

  //exportar dump
  const export_dump = () => {
    fetch('http://localhost:5000/dump', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);

        // Array para almacenar los blobs individuales
        const blobArray = [];

        data.datas.forEach((item, index) => {
          // Agregar un salto de línea entre los registros, excepto para el último
          const separator = index < data.datas.length - 1 ? '\n' : '';
          const blobData = `${item}${separator}`;

          // Crear un Blob para cada elemento
          const blob = new Blob([blobData], { type: "octet/stream" });
          blobArray.push(blob);
        });

        // Crear un Blob que contenga todos los blobs
        const finalBlob = new Blob(blobArray, { type: "octet/stream" });

        const a = document.createElement("a");
        const url = window.URL.createObjectURL(finalBlob);

        a.href = url;
        a.download = 'dump.sql';

        a.click();

        window.URL.revokeObjectURL(url);

      })
      .catch(err => console.log(err));
  }

  //obtener imagen del ast
  const imges = () => {
    fetch('http://localhost:5000/get_image')
      .then(response => response.blob())
      .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        setImageSrc(imageUrl);
      })
      .catch(error => console.error('Error fetching image:', error));
  }

  //selects
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

  //traducir codigo a c3d
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

  //ejecutar codigo
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

  return (

    <div className="App">
      <div>
        <div className="navbar" >
          <h1 className="custom-color">XSQL-IDE</h1>
          <h1 className="custom-color">XSQL-IDE</h1>
          <h1 class="custom-color2">XSQL-IDE</h1>
          <h1 className="custom-color">XSQL-IDE</h1>

          <div className="file-input-wrapper" style={{ display: 'flex', justifyContent: 'space-between', border: '3px solid #000000' }} >
            <input className="file-input" type="file" id="fileInput" onChange={impport_data} />
            <label className="file-input-label" htmlFor="fileInput"> ABRIR </label>
            <button className="buttons" onClick={handleSave}> GUARDAR </button>
          </div>
        </div>
      </div>


      <div style={{ display: 'flex' }}>
        <div>

          {/* sidebar */}
          <div className="file-input-wrapper" style={{ display: 'flex', justifyContent: 'space-between'}} >
            <input className="file-input" type="file" id="fileInput2" onChange={import_table} />
            <label className="file-input-label" htmlFor="fileInput2"> IMPORTAR </label>
            <button className="buttons" onClick={export_table}> EXPORTAR </button>
            <button className="buttons" onClick={export_dump}> D </button>
            <button className="buttons" onClick={xml_datas}> R </button>

          </div>
          <div className="sidebar">



            <div style={{ display: 'flex', justifyContent: 'space-between' }}>

            </div>

            <hr />
            <div>
              <h4 style={{ display: 'flex', justifyContent: 'center' }}>DBMS</h4 >

              {
                estado && <h4 className='side_header' style={{ display: 'flex', justifyContent: 'center' }}>{current_item[0].current[0]}</h4 >
              }

            </div>
            <hr />

            <div style={{ display: 'flex' }}>
              {
                estado && <DatabaseInfo asdf={current_item} />
              }
              {estado === false}
            </div>

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

              <div style={{ display: 'flex', justifyContent: 'space-between', border: '3px solid #000000'  }}>
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
