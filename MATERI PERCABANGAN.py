print ("""
Nama : Satria Bagus Eka Candra
NIM  : 2009106016

""")

kue_keju = 6000
kue_coklat = 3500

start = True
while start:
    print("""
    Selamat Datang di Toko Kue Sule
    ====================================

    Menu :

    [1] Kue Keju   = Rp.6000 per satuan
    [2] Kue Coklat = Rp.3500 per satuan

    STOCK :

    Kue Keju   = 25 Buah
    Kue Coklat = 35 Buah
    ====================================
    """)
    pilih = int(input("Masukkan Pilihan Anda : "))

    if pilih == 1:
        print("""
        
    PROMO PEMBELIAN KUE KEJU

    1. Beli 4  Kue Keju hingga 15 mendapat diskon 10%
    2. Beli 16 Kue Keju hingga 25 mendapat diskon 15%
        
    """)

        while True:

            memesan = int(input("Masukkan Berapa Kue Keju Yang ingin anda beli : "))

            if memesan < 4:
                jumlah = memesan * kue_keju
                print("====================================")
                print("Total biaya pembelian anda Rp.",jumlah)
                print("====================================")
                print()
                tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                if tanya == "t":
                    start = False
                    print("====================================")
                    print ("Terima Kasih Tekah mengunjungin toko kami")
                    print("====================================")
                break
                    
            
            elif memesan >= 4 and memesan <= 15:
                jumlah = memesan * kue_keju
                jumlah2 = memesan * kue_keju * 10 / 100
                jumlah3 = jumlah - jumlah2
                print("Total biaya pembelian anda Rp.",jumlah)
                print()
                print("Karena total pesanan anda ",str(memesan) + " selamat anda mendapatkan diskon 10% sebesar",str(jumlah2))
                print("====================================")
                print("Total biaya pembelian anda Rp.",jumlah3)
                print("====================================")
                print()
                tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                if tanya == "t":
                    start = False
                    print("====================================")
                    print ("Terima Kasih Tekah mengunjungin toko kami")
                    print("====================================")
                break
            
            elif memesan >= 16 and memesan <= 25:
                jumlah = memesan * kue_keju
                jumlah2 = memesan * kue_keju * 15 / 100
                jumlah3 = jumlah - jumlah2
                print("Total biaya pembelian anda Rp.",jumlah)
                print()
                print("Karena total pesanan anda ",str(memesan) + " selamat anda mendapatkan diskon 15% sebesar",str(jumlah2))
                print("====================================")
                print("Total biaya pembelian anda Rp.",jumlah3)
                print("====================================")
                print()
                tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                if tanya == "t":
                    start = False
                    print("====================================")
                    print ("Terima Kasih Tekah mengunjungin toko kami")
                    print("====================================")
                break
            
            else:
                print("====================================")
                print("stock kami hanya 25 yah :) silahkan inputkan ulang")

    if pilih == 2:
        print("""
        
    PROMO PEMBELIAN KUE COKLAT

    1. Beli 5  Kue Coklat hingga 20 mendapat diskon 7%
    2. Beli 21 Kue Coklat hingga 35 mendapat diskon 12%
        
    """)

        while True:

                memesan = int(input("Masukkan Berapa Kue Coklat Yang ingin anda beli : "))

                if memesan < 5:
                    jumlah = memesan * kue_coklat
                    print("====================================")
                    print("Total biaya pembelian anda Rp.",jumlah)
                    print("====================================")
                    print()
                    tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                    if tanya == "t":
                        start = False
                        print("====================================")
                        print ("Terima Kasih Tekah mengunjungin toko kami")
                        print("====================================")
                    break
                        
                
                elif memesan >= 5 and memesan <= 20:
                    jumlah = memesan * kue_coklat
                    jumlah2 = memesan * kue_coklat * 7 / 100
                    jumlah3 = jumlah - jumlah2
                    print("Total biaya pembelian anda Rp.",jumlah)
                    print()
                    print("Karena total pesanan anda ",str(memesan) + " selamat anda mendapatkan diskon 7% sebesar",str(jumlah2))
                    print("====================================")
                    print("Total biaya pembelian anda Rp.",jumlah3)
                    print("====================================")
                    print()
                    tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                    if tanya == "t":
                        start = False
                        print("====================================")
                        print ("Terima Kasih Tekah mengunjungin toko kami")
                        print("====================================")
                    break
                
                elif memesan >= 21 and memesan <= 35:
                    jumlah = memesan * kue_coklat
                    jumlah2 = memesan * kue_coklat * 12 / 100
                    jumlah3 = jumlah - jumlah2
                    print("Total biaya pembelian anda Rp.",jumlah)
                    print()
                    print("Karena total pesanan anda ",str(memesan) + " selamat anda mendapatkan diskon 12% sebesar",str(jumlah2))
                    print("====================================")
                    print("Total biaya pembelian anda Rp.",jumlah3)
                    print("====================================")
                    print()
                    tanya = str(input("Apakah anda ingin memesan lagi? (y/t)"))
                    if tanya == "t":
                        start = False
                        print("====================================")
                        print ("Terima Kasih Tekah mengunjungin toko kami")
                        print("====================================")
                    break
                else:
                    print("====================================")
                    print("stock kami hanya 35 yah :) silahkan inputkan ulang")

    else:
        print("yang anda inputkan salah, pilih 1 atau 2 saja")





    
