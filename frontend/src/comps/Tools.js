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
            <th>ambito</th>
            <th>id</th>
            <th>parametros</th>
            <th>simbolo</th>
            <th>tipo</th>
            <th>valor</th>
          </tr>
        </thead>
        <tbody>
          {env.map(item => {
            return (
              <tr key={item.id}>
                <td> {item.ambito} </td>
                <td> {item.id} </td>
                <td>{item.parametros}</td>
                <td>{item.tipo_simbolo}</td>
                <td>{item.tipo}</td>
                <td>{item.valor}</td>
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
          <pre key={1}>{item}</pre>
        );
      })}
    </div>

  );
}

export function ASTPrint({ ast }) {
  return (
    <div style={{ withSpace: 'nowrap', overflow: 'hidden', width: '1250px', height: 'calc(100vh - 474px)', overflowX: 'auto', overflowY: 'auto' }}>
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
          <Tab>AST-GDA</Tab>
          <Tab>SELECT</Tab>
        </TabList>
        <TabPanel style={{ height: 'calc(100vh - 474px)' }}>
          < TerminalPrint console={terminal} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 474px)' }}>
          < TableEnviroments env={env} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 474px)' }}>
          < TableErrors datos={items} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 474px)' }}>
          < ASTPrint ast={ast} />
        </TabPanel>
        <TabPanel style={{ height: 'calc(100vh - 474px)' }}>
          < Select_Table select={select} />
        </TabPanel>
      </Tabs>
    </div>
  );
}