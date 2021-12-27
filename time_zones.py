from datetime import datetime
import pytz

#look in the database for the timezone that you would like
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime('%d/%m/%Y, %H:%M:%S'))

cdmx_timezone = pytz.timezone("America/Mexico_City")
cdmx_date = datetime.now(cdmx_timezone)
print("Mexico City: ", cdmx_date.strftime('%d/%m/%Y, %H:%M:%S'))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime('%d/%m/%Y, %H:%M:%S'))