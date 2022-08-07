def cetakSiku(x):
    string=""
    bar = 1

    while bar <= x:
        kolom = bar

        while kolom > 0:
            string = string + "*"
            kolom = kolom - 1
        
        string = string + "\n"
        bar = bar +1
    print(string)

cetakSiku(5)