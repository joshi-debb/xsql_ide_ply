from datetime import datetime

def comparar_fechas_con_timestamp(fecha1, fecha2):
    """
    Función que compara dos fechas utilizando timestamps.

    Parameters:
    - fecha1: Primera fecha a comparar (objeto datetime).
    - fecha2: Segunda fecha a comparar (objeto datetime).

    Returns:
    - 1 si fecha1 es posterior a fecha2.
    - -1 si fecha1 es anterior a fecha2.
    - 0 si ambas fechas son iguales.
    """
    timestamp_fecha1 = fecha1.timestamp()
    timestamp_fecha2 = fecha2.timestamp()
    
    print('timestamp_fecha1', timestamp_fecha1)
    print('timestamp_fecha2', timestamp_fecha2)

    if timestamp_fecha1 > timestamp_fecha2:
        return 1
    elif timestamp_fecha1 < timestamp_fecha2:
        return -1
    else:
        return 0

# Ejemplo de uso:
fecha_1 = datetime(2023, 1, 15)
fecha_2 = datetime(2023, 1, 10)

resultado = comparar_fechas_con_timestamp(fecha_1, fecha_2)

if resultado == 1:
    print(fecha_1, "es posterior a", fecha_2)
elif resultado == -1:
    print(fecha_1, "es anterior a", fecha_2)
else:
    print(fecha_1, "es igual a", fecha_2)