def jumlahHurufVokal(a):
    vokal = "AIUEOaiueo"
    jumVokal=0
    hasil = 0

    for cha in a:
        if cha in vokal:
            jumVokal+=len(cha)
        else:
            jumVokal+=0
    hasil = len(a),jumVokal
    return hasil

       
print(jumlahHurufVokal("aku"))