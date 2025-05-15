from windowcapture import WindowCapture
import time
from brawapi import braw
from kontroller import kontrol
from filtrasyon import filtre

sure = time.time()
wincap = WindowCapture('Brawlhalla',1530,0,640,360)#1530
k = kontrol()

dongu = 0

karakter= braw.aranan_goruntu("kahramangorselleri\\quen-nai.png")
oda = braw.aranan_goruntu("odalar\\free-for-all.png")
hud = braw.aranan_goruntu("hud1.png")
mac_sonu = braw.aranan_goruntu("win.png")

time.sleep(1)

#Mactan cikip cikmadigimizi kontrol eden fonksiyon
def mac_tespiti():
    sc = wincap.get_screenshot(0)
    #Ekran goruntusune filtre uyguluyoruz
    sc_f = filtre.filtre_uygulama(0, sc, 90,105,0,40,232,249)#winLow(90,0,232) winHig(105,40,249)
    #Filtreli ekran goruntusunde arama yapiyoruz
    son4 = braw.tespit(sc_f, mac_sonu, 0.64 , 1 )
    if (son4[0] == 1):
        print('Mactan cikiliyor...')    
        time.sleep(1) 
        return son4[0]   
    else:
        print('Mac Devam Ediyor...')

#Mactayken konumumuzu belirlemek icin    
def hud_tespit(sc_position=0, threshold=0.6):
    #SAGA HARAKET ETTIRMEK ICIN
    if sc_position == 1:
        sc = wincap.get_screenshot(sc_position)
        sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
        t = braw.tespit(sc_f, hud, threshold, 1)
        if t[0] == 0: 
            print('Hud Tespit Edilemedi')
        
        #Mactan cikip cikmadigimizi kontrol ediyoruz
        if mac_tespiti() == 1:
            dongu = 1
            return dongu
        
        while t[0] == 1: 
            
            k.right_L_M_attack
            if mac_tespiti() == 1:
                dongu = 1
                return dongu
  
            sc = wincap.get_screenshot(sc_position)
            sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
            t = braw.tespit(sc_f, hud, threshold, 1)
            if t[0] == 0: 
                print('Hud Tespit Edilemedi')
            
            k.right_H_M_attack()
            if mac_tespiti() == 1:
                dongu = 1
                return dongu

            sc = wincap.get_screenshot(sc_position)
            sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
            t = braw.tespit(sc_f, hud, threshold, 1)
            if t[0] == 0: 
                print('Hud Tespit Edilemedi')
    
    #SOLA HARAKET ETTIRMEK ICIN
    elif sc_position == 2:
        sc = wincap.get_screenshot(sc_position)
        sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
        t = braw.tespit(sc_f, hud, threshold, 1)
        if t[0] == 0: 
            print('Hud Tespit Edilemedi')
        
        #Mactan cikip cikmadigimizi kontrol ediyoruz
        if mac_tespiti() == 1:
            dongu = 1
            return dongu
                
        while t[0] == 1: 
            
            k.left_L_M_attack()
            if mac_tespiti() == 1:
                dongu = 1
                return dongu
  
            sc = wincap.get_screenshot(sc_position)
            sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
            t = braw.tespit(sc_f, hud, threshold, 1)
            if t[0] == 0: 
                print('Hud Tespit Edilemedi')
            
            k.left_H_M_attack()
            if mac_tespiti() == 1:
                dongu = 1
                return dongu

            sc = wincap.get_screenshot(sc_position)
            sc_f = filtre.filtre_uygulama(0, sc, 96,97,252,255,254,255)
            t = braw.tespit(sc_f, hud, threshold, 1)
            if t[0] == 0: 
                print('Hud Tespit Edilemedi')
        
##################################################################       
# OYUNDA YAPACAKLARIMIZ SIRASI ILE 
while True:
    #Odada oldugumuzu tespit ediyoruz
    while (dongu == 0):
        #screenshot aliyoruz
        sc = wincap.get_screenshot(0)
        #screenshotu ve ornek resmi karsilastiriyoruz
        son = braw.tespit(sc, oda, 0.7 , 1 )
        if (son[0] == 1):
            dongu = 1
        else:
            print('Oda tespit edilemedi')
    
    dongu = 0
    
    #Karakteri aradigimiz bolum
    while (dongu == 0):
        #screenshot aliyoruz
        sc = wincap.get_screenshot(0)
        #screenshotu ve ornek resmi karsilastiriyoruz
        son2 = braw.tespit(sc, karakter, 0.52 , 1 )
        if (son2[0] == 1):
            dongu = 1
        else:
            print('Karakter Tespit edilemedi')
        
    dongu = 0
    
    #Oda ici hazirliklar ve odadan cikis
    while(dongu == 0):    
        #karakterin ekrandaki kordinatlarini buluyoruz
        #DIKKAT!!! Fonksiyon __init___ icersinde yer almiyor bu yuzden oyunu haraket ettirmeyin
        x,y = wincap.get_screen_position(son2[1], son2[2])
        # Fare ile karaktere sol tiklayip seciyoruz
        k.l_click_POS(x, y, son2[3], son2[4])
        #braw.sol_click(x, y, son2[3], son2[4])
        time.sleep(1)
        
        # Oyunu baslatiyoruz        
        k.light_attack()
        time.sleep(1)
        k.light_attack()
        time.sleep(1)
        k.light_attack()
        time.sleep(1)
            
        #Odadan cikip cikmadigimizi kontrol ediyoruz
        sc = wincap.get_screenshot(0)
        son = braw.tespit(sc, oda, 0.7 , 1 )
        if (son[0] == 0):
            print('Maca giriliyor...')
            dongu = 1
            time.sleep(30)

    dongu = 0
          
    #Mac Icersinde yaptiklarimiz
    while (dongu == 0):
        #Karakterimizin yerini tespit edip duruma gore hareket ettiriyoruz
        if hud_tespit(sc_position=1, threshold=0.40) == 1:
            dongu = 1
        #Karakterimizin yerini tespit edip duruma gore hareket ettiriyoruz
        if hud_tespit(sc_position=2, threshold=0.40) == 1:
            dongu = 1

    dongu = 0
    
    #Odaya donmek icin ugrasiyoruz
    while (dongu == 0):
        #screenshot aliyoruz
        sc = wincap.get_screenshot(0)
        #screenshotu ve ornek resmi karsilastiriyoruz
        son = braw.tespit(sc, oda, 0.7 , 1 )
        if (son[0] == 1):
            dongu = 1
        else:
            k.light_attack()
            time.sleep(1)
            k.light_attack()
            time.sleep(1)
            k.light_attack()
            time.sleep(1)
    
    dongu = 0
    

             