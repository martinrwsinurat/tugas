# Data awal
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# 1. Tampilkan seluruh data
print("Seluruh data panen:")
for lokasi, data in data_panen.items():
    print(f"{lokasi}: {data}")
print("\n")

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")
print("\n")

# 3. Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")
print("\n")

# 4. Masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
hasil_padi = {}
hasil_kedelai = {}

for lokasi, data in data_panen.items():
    hasil_padi[lokasi] = data['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']

print("Hasil panen padi setiap lokasi:", hasil_padi)
print("Hasil panen kedelai setiap lokasi:", hasil_kedelai)
print("\n")

# 5. Percabangan untuk memeriksa perhatian khusus
print("Status perhatian khusus:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
