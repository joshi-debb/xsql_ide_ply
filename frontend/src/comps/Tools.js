import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import '../css/App.css'

export function MyButtons({ texto, manejarClic }) {

  return (
    <button
      className="MyBoton"
      onClick={manejarClic}>
      {texto}
    </button>
  );
}




export function TableErrors({ datos }) {
  return (
    <table className='custom-table'>
      <tbody>
        {datos.map(item => {

          if (item.tipo === 'SINTACTICO') {
            return (
              <tr key={item.id}>
                <td> {item.tipo} </td>
                <td> Fila:{item.fila}</td>
                <td>Columna:{item.columna}</td>
                <td>Token invalido:{item.instruccion}</td>
                <td  > Se esperaba:{item.descripcion} </td>
              </tr>
            );
          } else {
            return (
              <tr key={item.id}>
                <td> {item.tipo} </td>
                <td>Fila: {item.fila}</td>
                <td>Columna: {item.columna}</td>
                <td>{item.instruccion}</td>
                <td>{item.descripcion} </td>
              </tr>
            );
          }
        })}
      </tbody>
    </table>
  );


}

export function TableEnviroments({ env }) {
  return (
    <table className='EntornoTable'>
      <thead>
        <tr>
          <th>ID</th>
          <th>TIPO DE SIMBOLO</th>
          <th>PRIMITIVO</th>
          <th>ENTORNO</th>
          <th>FILA</th>
          <th>COLUMNA</th>
        </tr>
      </thead>
      <tbody>
        {env.map(item => {
          return (
            <tr key={item.id}>
              <td> {item.id} </td>
              <td> {item.typesymbol} </td>
              <td>{item.type}</td>
              <td>{item.env}</td>
              <td>{item.line}</td>
              <td>{item.col}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );


}


export function TerminalPrint({ console }) {
  return (
    <div>
      {console.map(item => {
        return (
          <pre>{item}</pre>
        );
      })}
    </div>

  );


}


export function Pestaña({ items, env, terminal }) {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabSelect = (index) => {
    setActiveTab(index);
  };

  return (
    <div>
      <Tabs selectedIndex={activeTab} onSelect={handleTabSelect}>
        <TabList>
          <Tab>CONSOLA</Tab>
          {/* <Tab>TABLA DE SIMBOLOS</Tab>
          <Tab>ERRORES</Tab> */}
        </TabList>
        <TabPanel>
          < TerminalPrint console={terminal} />
        </TabPanel>
        {/* <TabPanel>
          < TableEnviroments env={env} />
        </TabPanel>
        <TabPanel>
          < TableErrors datos={items} />
        </TabPanel> */}
      </Tabs>
    </div>
  );
}