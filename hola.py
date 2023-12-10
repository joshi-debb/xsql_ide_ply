from datetime import datetime

# Obtener la fecha y hora actual
now = datetime.now()

# Formatear la fecha y hora sin segundos
formato = "%Y-%m-%d %H:%M"
fecha_hora_formateada = now.strftime(formato)

# Imprimir el resultado
print("Fecha y hora actual sin segundos:", fecha_hora_formateada)