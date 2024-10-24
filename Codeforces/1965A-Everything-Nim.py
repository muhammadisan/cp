t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Mengambil tumpukan unik, kemudian mengurutkannya
    a = sorted(set(a))
    
    # Menghitung selisih antara elemen yang berurutan
    b = [a[0]] + [a[i+1] - a[i] for i in range(len(a) - 1)]
    
    # Membuat daftar c, yang akan menyimpan 1 atau 0 tergantung pola 1-an berturut-turut
    c = []
    i = 0
    while i < len(b):
        count1 = 0
        while i < len(b) and b[i] == 1:
            count1 += 1
            i += 1
        
        if count1 > 0:
            # Menyimpan 1 jika jumlah berturut-turut ganjil
            if count1 % 2 == 1:
                c.append(1)
            continue
        
        # Jika elemen tidak 1, tambahkan 0 ke c
        c.append(0)
        i += 1
    
    # Logika penentuan pemenang berdasarkan c
    if len(c) == 0:
        print("Bob")
    elif len(c) == 1:
        print("Alice")
    elif c[0] == 1:
        print("Bob")
    else:
        print("Alice")
