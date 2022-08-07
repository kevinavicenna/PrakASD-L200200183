def apakahKabisat(tahun):
    hasil = False
    if(tahun%4==0 and tahun%100!=0 and tahun%400!=0):
        hasil =True
    elif(tahun%100!=0 and tahun%400!=0):
        hasil = False
    elif(tahun%400!=0):
        hasil = True
    else:
        hasil = False
    return hasil

print(apakahKabisat(1896))