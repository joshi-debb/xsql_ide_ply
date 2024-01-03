-----lo del bit son puntos extras


CREATE FUNCTION fn_regresatasa (@idproducto int)
RETURN decimal
AS
BEGIN
	DECLARE @TASA as decimal; 
	set @TASA = (select tasa from tbproducto where idproducto = @idproducto and idestado = 1);

	RETURN @TASA;	

END;


CREATE FUNCTION fn_retornanombre (@identificacion nvarchar(20),@primernombre nvarchar(20),@segundonombre nvarchar(20))
RETURN nvarchar(100)
AS
BEGIN

	DECLARE @nombres nvarchar(100);
	DECLARE @apellidos nvarchar(100);	
	DECLARE @nombrecompleto nvarchar(100);	
	
	
	set @nombres = CONCATENA (@primer_nombre,@segundo_nombre) ;
		set @APELLIDOS = CONCATENA (@primer_nombre,@segundo_nombre) ;
	set @nombrecompleto = CONCATENA(@nombrecompleto,@apellidos);



	return @nombrecompleto;

END;

-- select fn_retornanombre(identificacion,primernombre,segundonombre);
select fn_retornanombre(identificacion,primernombre,segundonombre)
from tbidentificacion,tbcliente 
where idestado = 1 and tbcliente.codigocliente = tbidentificacion.codigocliente;

CREATE PROCEDURE sp_actualizatasa(@aumento int,@fecha date)
AS
BEGIN
		IF (@aumento > 0)
		BEGIN

			update tbproducto set tasa = tasa+(tasa*@aumento/100) 
			where idestado = 1;
		ELSE 
		BEGIN
			update tbproducto set tasa = tasa+(tasa*(@aumento)) 
			where idestado = 1;
		END;
		
			
		DECLARE @tasa nvarchar(5);
		SET @tasa = CAS(@aumento as nvarchar(5));
		-- ESTA TABLA NO EXISTE
		-- INSERT INTO tbbitacoracambio (tabla,fecha,cambio) 
		-- VALUES ('tbproducto',@fecha,CONCATENA('CAMBIO DE TASA, VALOR AUMENTA',@tasa));
	
END;


CREATE PROCEDURE sp_actualizanombre (@idcliente nvarchar(10),@nuevonombre nvarchar(100))
AS 
BEGIN
	UPDATE tbcliente set primernombre = @nuevonombre 
	where codigocliente = @idcliente; --- PyC
END;

SELECT * FROM tbproducto where tbproducto.idestado = 1;
exec sp_actualizatasa (10,'2023-12-18');


SELECT * FROM tbproducto where tbproducto.idestado = 1;

exec sp_actualizatasa ('GT-0004','ANNA');

SELECT * FROM tbcliente where tbcliente.codigocliente = 'GT-0004';




