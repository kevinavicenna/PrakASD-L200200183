print(
"""meggunakan dua pola
pertama menggunakan konsep Big-O yang dipakai
rumus O(log n) dengan 1 = 1, 2 = 2, 4 = 3, 10 = 4, 100 = 7, 1000=10.
log berasal dari pangkat log 2. 
Untuk pola sendiri:
        jika ingin menebak angka 70
        a = tebakan pertama // 2
        tebakan selanjutnya = nilai tebakan "lebih dari" + a
        *jika hasil tebakan selanjutnya "kurang dari", maka nilai yang digunakan
        tetap nilai lebih dari sebelumnya*
        a = a // 2
    Simulasi
        tebakan ke 1: 50 (mengambil nilai tengah) jawaban= "lebih dari itu"
        tebakan ke 2: 75 (dari 50 + 25) jawaban = "kurang dari nilai itu"
        tebakan ke 3: 62 (dari 50 + 12) jawaban = "lebih dari nilai itu"
        tebakan ke 4: 68 (dari 62 + 6) jawaban = "lebih dari nilai itu"
        tebakan ke 5: 71 (dari 68 + 3) jawaban = "kurang dari nilai itu"
        tebakan ke 6: 69 (dari 68 + 1) jawaban = "lebih dari nilai itu"
        tebakan ke 7: antara 71 dan 69 hanya ada 1 angka = 70!!!
        
menggunakan barisan geometri Sn = 2^n
        barisan yang terjadi adalah : 2, 4, 8, 16, 32, 64
        Misal angka yang akan diebak adalah 68
        Tebakan ke-1 : 64 dijawab "lebih dari niali itu"
        Tebakan ke-2 : 96(dari 64 + 32) dijawab "Kurang dari nilai itu"
        Tebakan ke-3 : 80(dari 64 + 16) dijawab "Kurang dari nilai itu"
        Tebakan ke-4 : 72(dari 64 + 8) dijawab "Kurang dari nilai itu"
        Tebakan ke-5 : 68(dari 64 + 4) dijawab "Lebih dari nilai itu"
        Tebakan ke-6 : 70(dari 68 + 2) dijawab "TEPAT"
        """)
