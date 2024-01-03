CREATE FUNCTION fn_retornaalturamora (@diasmora int)
RETURN nvarchar(100)
AS
BEGIN
	DECLARE @alturamora nvarchar(100);

		IF (@diasmora > 0 && @diasmora < 30) 
		BEGIN
			SET @alturamora = 'Al dia';
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 'Altura Mora 2';	
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 'Altura Mora 3';				
		END;

		IF (@diasmora >= 60 && @diasmora < 90) 
		BEGIN 
			SET @alturamora = 'Altura Mora 4';		
		END;
	
		IF (@diasmora >= 90 && @diasmora < 120) 
		BEGIN 
			SET @alturamora = 'Altura Mora 5';				
		END;

		
	RETURN @alturamora;

END;

CREATE PROCEDURE sp_actualizaalturamora (@credito int,@diasmora int)
AS
BEGIN
	DECLARE @alturamora int;		
		IF (@diasmora > 0 && @diasmora < 30) 
		BEGIN
			SET @alturamora = 0;
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 1;	
		END;
	
		IF (@diasmora >= 30 && @diasmora < 60) 
		BEGIN 
			SET @alturamora = 2;				
		END;

		IF (@diasmora >= 60 && @diasmora < 90) 
		BEGIN 
			SET @alturamora = 3;		
		END;
	
		IF (@diasmora >= 90 && @diasmora < 120) 
		BEGIN 
			SET @alturamora = 4;				
		END;

		update tbcreditosaldo set alturamora = @alturamora 
		where credito = @credito && diasmora = @diasmora;
END;


CREATE FUNCTION sp_calculacuota (@saldo decimal, @plazo int ,@diasmora int)
RETURN decimal
AS
BEGIN
		DECLARE @cuota decimal;
		DECLARE @ajuste decimal; 
		
		if (@saldo > 5000 && @diasmora > 30)
		begin 
			set @cuota = (@saldo/@plazo)*0.45;
		END;
	
		if (@saldo > 15000 && @diasmora > 30) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.65;	
		END;

		if (@saldo > 25000 && @diasmora > 60) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.70;			
		END;
	
		if (@saldo < 15000 && @diasmora < 30) 
		BEGIN
			set @cuota = (@saldo/@plazo)*0.15;			
		END;
	
		CASE WHEN @cuota > 1000 && @cuota <  1500
				THEN SET @ajuste = 75;
			WHEN @cuota >= 1500 && @cuota <  2000
				THEN SET @ajuste = 125;	
			WHEN @cuota > 0 &&  @cuota < 1000
				THEN SET @ajuste = 25;
			WHEN @cuota >=  2000
				THEN SET @ajuste = 150;					
			ELSE 
				THEN SET @ajuste = 0;
		END;
		
		SET @cuota = @cuota-@ajuste;	
			
		RETURN @cuota;	
		
		
END;


select fn_retornaalturamora(45);