nama = 'Mhamhank Garox'
program = 'Gerak loorooss'

print (f'Program {program} oleh {nama}')

def hitung_kecepatan (jarak, waktu):
    return jarak / waktu

jarak = 1000
waktu = 5*60
kecepatan = hitung_kecepatan(jarak, waktu)

print (f'jarak = {jarak/1000} km ditempuh dalam waktu = {waktu/60} menit')
print (f'sehingga kecepatan = {kecepatan} m/s')