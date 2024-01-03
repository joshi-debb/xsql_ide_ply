CREATE DATA BASE tbbanco;
--usar tbbanco;
use tbbanco;
CREATE TABLE tbestado (
idestado int PRIMARY KEY,
estado nvarchar(50) NOT NULL);

CREATE TABLE tbidentificaciontipo (
ididentificaciontipo int PRIMARY KEY,
identificaciontipo nvarchar(15) not null);

CREATE TABLE tbcliente (codigocliente nvarchar(15) PRIMARY KEY,
primer_nombre nvarchar(50) not null,
segundo_nombre nvarchar(50),
primer_apellido nvarchar(50) not null,
segundo_apellido nvarchar(50),
fecha_nacimiento date not null, 
genero nvarchar(1),
idestado int not null REFERENCE tbestado (idestado));

CREATE TABLE tbidentificacion (
ididentificacion int PRIMARY KEY,
codigocliente nvarchar(15) PRIMARY KEY REFERENCE tbcliente (codigocliente),
identificacion nvarchar(20) NOT NULL,
ididentificaciontipo int REFERENCE tbidentificaciontipo (ididentificaciontipo),
idestado int);

INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(1,'DPI');
INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(2,'NIT');
INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(3,'PASAPORTE');

INSERT INTO tbestado (idestado,estado) VALUES(1,'Activo');
INSERT INTO tbestado (idestado,estado) VALUES(2,'Inactivo');
INSERT INTO tbestado (idestado,estado) VALUES(3,'Eliminado');

INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0001','PETER','JUAN','PARKER','SEGUNDO','01-01-1900','M',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,idestado)
VALUES ('GT-0002','JULIO','PEREZ','LOPEZ','01-12-1950',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,idestado)
VALUES ('GT-0003','ALFREDO','ORTIZ','LOPEZ','05-06-1979',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0004','KARLA','LETICIA','SANTOS','JUAREZ','1975-01-01','F',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0006','KIMBERLY','ESQUIBEL','CASTILLO','14-09-1991','F',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0007','ROBERTO','ALEJANDRO','MONTEPEQUE','14-09-1991','M',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0008','JUAN','CARLOS','DAVILA','14-12-1998','F',3);
INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0009','ESPERANZA','MARIA','BOLAÑOS','10-10-2000','F',2);
INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0010','ALICIA','DEL CARMEN','HERRERA','15-09-1976','F',1);


INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (1,'GT-0001','45784560101',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (2,'GT-0001','94675057',2);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (3,'GT-0002','4854560101',1);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (4,'GT-0003','1513117',2);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (5,'GT-0003','12345678910',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (6,'GT-0003','78456564554',3);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (7,'GT-0004','78456501014554',3);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (8,'GT-0005','1610417050101',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (9,'GT-0006','9467505010150',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (10,'GT-0007','0167805210150',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (11,'GT-0008','0101505010150',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (12,'GT-0009','1610417050101',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (13,'GT-0010','1513115',2);



CREATE TABLE tbproducto (idproducto int primary key,
producto nvarchar(100) not null,
idestado int not null);

INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(1,'Credito Fiduiciario',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(2,'Credito Hipotecario',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(3,'Tarjeta de Credito Oro',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(4,'Tarjeta de Credito Platinu',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(5,'Credito Personal',2);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(6,'Credito Pesonal Avanza',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(7,'Cuenta de Ahorro',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(8,'Cuenta Monetaria',1);


-- ALTER TABLE tbproducto ADD COLUMN tasa decimal;
ALTER TABLE tbproducto ADD tasa decimal;


update tbproducto set tasa = 0.00 where idproducto = 8; 
update tbproducto set tasa = 0.05 where idproducto = 7; 
update tbproducto set tasa = 0.17 where idproducto = 6; 
update tbproducto set tasa = 0.20 where idproducto = 5; 
update tbproducto set tasa = 0.36 where idproducto = 4; 
update tbproducto set tasa = 0.45 where idproducto = 3; 

CREATE TABLE tbclienteba (idclienteint int PRIMARY KEY,nombrecliente nvarchar(150) not null,idestado int);
INSERT INTO tbclienteba (idclienteint,nombrecliente,idestado) values(1,'Banrural',1);
INSERT INTO tbclienteba (idclienteint,nombrecliente,idestado) values(2,'Banco Industrial',1);
INSERT INTO tbclienteba (idclienteint,nombrecliente,idestado) values(3,'Banco Inmobiliario',2);
INSERT INTO tbclienteba (idclienteint,nombrecliente,idestado) values(4,'Banco G&T',1);
INSERT INTO tbclienteba (idclienteint,nombrecliente,idestado) values(5,'Banco de Antigua',1);


CREATE TABLE tbcredito (credito int PRIMARY KEY,nocuenta nvarchar(35) not null,
idclienteint int not null REFERENCE tbclienteba (idclienteint),
fechaultimocorte date not null,idproducto int REFERENCE tbproducto (idproducto));

CREATE TABLE tbobligaciontipo (idobligaciontipo int PRIMARY KEY,obligaciontipo nvarchar(30));

INSERT INTO tbobligaciontipo (idobligaciontipo,obligaciontipo) VALUES (1,'DIRECTO');
INSERT INTO tbobligaciontipo (idobligaciontipo,obligaciontipo) VALUES (2,'INDIRECTO');

CREATE TABLE tbcreditoobligacion (codigocliente nvarchar(15) PRIMARY KEY REFERENCE tbcliente (codigocliente),
credito int PRIMARY KEY REFERENCE tbcredito (credito),
idobligaciontipo int REFERENCE tbobligaciontipo (idobligaciontipo));

INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (1,'45-5454',1,'30-11-2023',1);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (2,'AF4545D',3,'30-11-2023',1);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (3,'785455-5',2,'31-12-2023',2);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (4,'4545-4785-4578-4545',2,'31-12-2023',3);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (5,'3654-4785-4768-4555',2,'31-12-2023',4);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (6,'315447854768',2,'31-12-2023',8);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (7,'45875545',4,'31-10-2023',7);
INSERT INTO tbcredito (credito,nocuenta,idclienteint,fechaultimocorte,idproducto) VALUES (8,'788854556',5,'31-12-2023',5);

INSERT INTO tbcreditoobligacion (codigocliente,Credito,idobligaciontipo) VALUES ('GT-0001',1,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0002',2,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0002',3,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0003',3,2);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0004',4,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0005',5,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0006',5,2);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0007',6,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0008',7,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0009',9,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0010',8,1);
INSERT INTO tbcreditoobligacion  (codigocliente,Credito,idobligaciontipo) VALUES('GT-0011',7,1);


CREATE TABLE tbcreditoSaldo (credito int PRIMARY KEY, fechacorte date PRIMARY KEY, idmoneda int PRIMARY KEY,
idcreditoestado int PRIMARY KEY, SaldoActual decimal, SaldoMora decimal,ValorCuota decimal,DiasMora int,
alturamora int not null,limite decimal not null,idcalificacion int not null);


insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'31-01-2023',1,1,05,0,600,0,0,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'28-02-2023',1,1,4400,0,600,0,0,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'31-03-2023',1,1,3800,0,600,0,0,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'30-04-2023',1,1,3200,0,600,0,0,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'31-05-2023',1,1,2600,0,600,0,0,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'30-06-2023',1,1,2600,600,600,30,1,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'31-07-2023',1,1,3150,1200.25,600,60,2,5000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (1,'30-08-2023',1,1,3760,1700,600,90,3,5000,1);


insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'31-01-2023',1,1,15000,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'28-02-2023',1,1,14249.75,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'31-03-2023',1,1,12999.50,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'30-04-2023',1,1,11748.75,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'31-05-2023',1,1,10498,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'30-06-2023',1,1,9247.25,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'31-07-2023',1,1,7996.50,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (2,'30-08-2023',1,1,6745.75,0,1250.75,0,0,15000,1);



insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'31-01-2023',1,1,15000,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'28-02-2023',1,1,14249.75,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'31-03-2023',1,1,12999.50,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'30-04-2023',1,1,11748.75,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'31-05-2023',1,1,10498,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'30-06-2023',1,1,9247.25,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'31-07-2023',1,1,7996.50,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (3,'30-08-2023',1,1,6745.75,0,1250.75,0,0,15000,1);



insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'31-01-2023',1,1,15000,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'28-02-2023',1,1,14249.75,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'31-03-2023',1,1,12999.50,0,1250.25,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'30-04-2023',1,1,11748.75,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'31-05-2023',1,1,10498,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'30-06-2023',1,1,9247.25,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'31-07-2023',1,1,7996.50,0,1250.75,0,0,15000,1);
insert into tbcreditoSaldo (credito,fechacorte,idmoneda,idcreditoestado,SaldoActual,SaldoMora,ValorCuota,DiasMora,
alturamora,limite,idcalificacion) values (4,'30-08-2023',1,1,6745.75,0,1250.75,0,0,15000,1);


-- ### Lo acepta gramaticalmente, pero da error en la logica "
SELECT tbcliente.codigocliente,CONCATENAR(tbcliente.primer_nombre,tbcliente.primer_apellido),
tbidentificacion.identificacion,tbidentificaciontipo.identificaciontipo
FROM tbcliente,tbidentificacion ,tbidentificaciontipo 
where tbcliente.codigocliente = tbidentificacion.codigocliente 
&& tbidentificacion.ididentificaciontipo = tbidentificaciontipo.ididentificaciontipo;

-- ### Lo acepta gramaticalmente, pero da error en la logica "
SELECT tbcredito.credito,tbcredito.fechaultimocorte,tbcredito.nocuenta,fechaultimocorte,tbproducto.producto,
tbcreditoSaldo.idmoneda,tbcreditoSaldo.SaldoActual,tbcreditoSaldo.SaldoMora,
tbcreditoSaldo.ValorCuota,tbcreditoSaldo.DiasMora,
tbcreditoSaldo.alturamora,tbcreditoSaldo.limite,
tbcreditoSaldo.idcalificacion
FROM tbcredito,tbcreditoobligacion,tbcreditoSaldo,tbcliente,tbproducto 
where tbcredito.credito = tbcreditoobligacion.credito 
&& tbcreditoobligacion.Credito = tbcreditoSaldo.credito 
&& tbcliente.codigocliente = tbcreditoobligacion.codigocliente
&& tbproducto.idproducto = tbcredito.idproducto;

-- ### Lo acepta gramaticalmente, pero da error en la logica "
SELECT contar(*)
FROM tbcredito,tbcreditoobligacion,tbcreditoSaldo,tbcliente,tbproducto 
where tbcredito.credito = tbcreditoobligacion.credito 
&& tbcreditoobligacion.Credito = tbcreditoSaldo.credito 
&& tbcliente.codigocliente = tbcreditoobligacion.codigocliente
&& tbproducto.idproducto = tbcredito.idproducto;

-- ### Lo acepta gramaticalmente, pero da error en la logica "
SELECT *
FROM tbcredito.idclienteint, tbclienteba.idclienteint
where tbcredito.idclienteint = tbclienteba.idclienteint;
----------------------------------------------------------------

select CONTAR(*) FROM tbcredito;   
select CONTAR(*) FROM tbcreditoSaldo;   

SELECT SUMA(SaldoActual) from tbcreditoSaldo;
SELECT SUMA(SaldoMora) from tbcreditoSaldo where DiasMora != 0;
SELECT HOY();

select * from tbproducto;

-- ### Lo acepta gramaticalmente, pero da error en la logica "
SELECT HOY(),SUBSTRAER(primer_nombre,1,5),SUBSTRAER(identificacion,0,3)
from tbcliente,tbcreditoobligacion,tbidentificacion
where tbcliente.idcliente = tbcreditoobligacion.idcliente
&& tbcliente.idcliente = tbidentificacion.idcliente; -- Correccion and




