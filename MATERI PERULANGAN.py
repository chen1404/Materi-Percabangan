#2009106016 + 10 = 21
while True :
    nim = int(input("masukkan 3 digit terakhir nim anda : "))
    nim2 = nim + 10

    print ("NIM",str(nim) + " + 10 = ",str(nim2))

    x = 1
    y = 1

    while x <= nim2:
        print(y)
        y += 1
        if y == 10:
         y -= 9
        x += 1    
    break
              
