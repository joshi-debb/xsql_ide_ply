import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import '../css/App.css'


export function DatabaseInfo({ asdf }) {
  return (
    <div className='base-info'>
      
      <div>
        
        {asdf.map((item, index) => (
          
          <div key={index} className="database-info">
            <ul>
            <hr />
              <li className="database-name">{item.db[0]}</li>
              <li className='titulos'>Tablas</li>
              <ul className="table-list">
                {item.tables.map((tab, tabIndex) => (
                  <li key={tabIndex}>{tab}</li>
                ))}
              </ul>
              <li className='titulos'>Vistas</li>
              <ul className="view-list">
                {item.views.map((view, viewIndex) => (
                  <li key={viewIndex}>{view}</li>
                ))}
              </ul>
              <li className='titulos'>Funciones</li>
              <ul className="function-list">
                {item.funcs.map((func, funcIndex) => (
                  <li key={funcIndex}>{func}</li>
                ))}
              </ul>
              <li className='titulos'>Procedimientos</li>
              <ul className="procedure-list">
                {item.procs.map((proc, procIndex) => (
                  <li key={procIndex}>{proc}</li>
                ))}
              </ul>
              <hr />
            </ul>
          </div>
        ))}
        
      </div>
      
    </div>
  );
}

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
    <div className='scroleados'>
      <table className='EntornoTable'>
        <thead>
          <tr>
            <th>Tipo</th>
            <th>Descripcion</th>
            <th>Linea</th>
            <th>Columna</th>
          </tr>
        </thead>
        <tbody>
          {datos.map(item => {
            return (
              <tr key={item.linea}>
                <td> {item.tipo} </td>
                <td> {item.descripcion} </td>
                <td>{item.linea}</td>
                <td>{item.columna}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export function TableEnviroments({ env }) {
  return (
    <div className='scroleados'>
      <table className='EntornoTable'>
        <thead>
          <tr>
            <th>Id</th>
            <th>Tipo</th>
            <th>Valor</th>
            <th>Entorno</th>
            <th>Parametros</th>
            <th>Simbolo</th>
          </tr>
        </thead>
        <tbody>
          {env.map(item => {
            return (
              <tr key={item.id}>
                <td> {item.id} </td>
                <td>{item.tipo}</td>
                <td>{item.valor}</td>
                <td> {item.ambito} </td>
                <td>{item.parametros}</td>
                <td>{item.simbolo}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>

  );
}


export function TerminalPrint({ console }) {
  return (
    <div className='scroleados'>
      {console.map(item => {
        return (
          <pre key={1}>{'> ' + item}</pre>
        );
      })}
    </div>

  );
}

export function ASTPrint({ ast }) {
  return (
    <div style={{ withSpace: 'nowrap', overflow: 'hidden', width: '1250px', height: 'calc(100vh - 550px)', overflowX: 'auto', overflowY: 'auto' }}>
      {ast && (
        <div className='scroll-container'>
          <img src={ast} />
        </div>
      )}
    </div>
  );
}

export function Select_Table({ select }) {
  return (
    <div className='scroleados'>
      <table className='EntornoTable'>
        <thead>
          <tr>
            {select.res.fields.map(item => {
              return (
                <th>{item}</th>
              );
            })}
          </tr>
        </thead>
        <tbody>
          {select.res.records.map(items => {
            return (
              <tr>
                {items.map((item) => {
                  return (
                    <td> {item} </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export function Pestaña({ items, env, terminal, ast, select }) {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabSelect = (index) => {
    setActiveTab(index);
  };

  return (
    <div>
      <Tabs selectedIndex={activeTab} onSelect={handleTabSelect}>
        <TabList>
          <Tab>CONSOLA</Tab>
          <Tab>TABLA DE SIMBOLOS</Tab>
          <Tab>ERRORES</Tab>
          <Tab>ASTGDA</Tab>
          <Tab>CONSULTAS</Tab>
        </TabList>
        <TabPanel style={{ height: 'calc(100vh - 525px)' }}>
          < TerminalPrint console={terminal} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 525px)' }}>
          < TableEnviroments env={env} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 525px)' }}>
          < TableErrors datos={items} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 525px)' }}>
          < ASTPrint ast={ast} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 525px)' }}>
          < Select_Table select={select} />
        </TabPanel>
      </Tabs>
    </div>
  );
}