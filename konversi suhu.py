#program konversi suhu
print ('Konversi Suhu Dari Celcius Ke Fahrenheit Ke Reamur dan Kelvin')

suhu_celcius = float(input('Masukan Suhu Dalam Celcius '))
suhu_fahrenheit = (9/5)* suhu_celcius + 32
suhu_reamur = (4/5)* suhu_celcius
suhu_kelvin = suhu_celcius + 273.15
print ('Hasil Perhitungan Konversi Suhu: ')
print ('Suhu Celcius adalah    : %f' %(suhu_celcius))
print ('Suhu Fahrenheit adalah : %2f' %(suhu_fahrenheit))
print ('Suhu Reamur adalah     : %f' %(suhu_reamur))
print ('Suhu Kelvin adalah     : %f' % (suhu_kelvin))
