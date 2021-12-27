from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str_latam = my_datetime.strftime('%d/%m/%Y')
print(f'LATAM format: {my_str_latam}')

my_str_USA = my_datetime.strftime('%m/%d/%Y')
print(f'USA format: {my_str_USA}')

my_str_random = my_datetime.strftime('We are in %Y')
print(f'Random format: {my_str_random}')