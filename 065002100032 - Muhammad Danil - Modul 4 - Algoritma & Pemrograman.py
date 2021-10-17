# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : Minggu,20211710
@author: Muhammad Danil Hidayat
@NIM : 065002100032
@Materi : Struktur kendali II
"""

hitung = 0
jawab = "ya"


while(jawab == "ya"):
    inputbulan = int(input("masukkan bulan nya: "))
    inputtahun = int(input("masukkan tahun nya: "))
    
  
    
    if(inputbulan >= 13 or inputbulan <= 0):
	    print("bulan tidak terdaftar di dalam kalender")

    elif(inputbulan == 1 or inputbulan == 3 or inputbulan == 5 or inputbulan == 7 or inputbulan == 8 or inputbulan == 10 or inputbulan == 12):
	    print("Ini termasuk 31 hari")
    
    elif(inputbulan == 2):
      
        if(inputtahun % 4 == 0 and inputbulan == 2):
          print("Ini 29 hari")
          
        else:
            print("ini termasuk 28 hari")
            
    else:
        print("ini termasuk 30 hari")