#import numpy as np
#from PIL import ImageGrab
#import time
#import mouse
import cv2
import os
 
# YARARLANDIGIM KAYNAKLAR 
# http://wwphp.com/python-opencv-object-detection/

class braw():
    
    def kahraman_ismi(self):
        with open("kahramanlar.txt" , "r") as f:
            
            lst_kahramanlar = f.readlines()
            x = lst_kahramanlar[self]
            
        return x
    
    def kahraman_rakami(self):
        
        lst_rakamlar = [*range(0,53,1)]
        x = lst_rakamlar[self]
        
        return x
            
    def dosyadan_karakter_bulma(self):
            baslangic = os.getcwd()
            os.chdir("kahramangorselleri")
            lst_gorseller = os.listdir()
            lst_yol = [' ']
            for dosyalar in lst_gorseller:
                lst_yol.append(dosyalar)
            aranan_yol = os.path.abspath(lst_yol[self])
            if os.path.exists(aranan_yol) == False:
                print(' Sectiginiz kahraminin yolu bulunamiyor lutfen kontrol ediniz')
                os.chdir(baslangic)
            else:
                os.chdir(baslangic)
                return aranan_yol
            
    def aranan_goruntu(self):
        #Arayacagimizi goruntuyu sisteme aktarip gri formata donusturuyoruz
        OrnekResim 							=	cv2.imread(self) #Tespit Edeceğimiz Resim
        OrnekResimDonustur 					=	cv2.cvtColor(OrnekResim, cv2.COLOR_RGB2GRAY) #Tespit Edeceğimiz Resimi Gri Formata Donustur
        return OrnekResimDonustur
    
    def tespit(EkranGoruntusu, OrnekResimDonustur,threshold=0.7, ciz=1):
        #Ekran goruntusunun icerisinde aradigimiz goruntuyu tespit etmeye calisiyoruz 
        EkranGoruntusuDonustur 				=	cv2.cvtColor(EkranGoruntusu,cv2.COLOR_RGB2GRAY) #Ekran Goruntusunu Gri Formata Donusturuyoruz
        Sonuc 								=	cv2.matchTemplate(EkranGoruntusuDonustur, OrnekResimDonustur, cv2.TM_CCOEFF_NORMED) #Ekran Grountusunun Icerisinde Resmi Ariyoruz
        min_val, max_val, min_loc, max_loc	=	cv2.minMaxLoc(Sonuc) #Bulunan Objenin Koordinatlarini Bul
        
        if (max_val > threshold):
            
            d = 1
            w, h = OrnekResimDonustur.shape[::-1]
            x, y = max_loc
            
            if(ciz == 0):
                Ust_Sol 							=	max_loc #Bulunan Objenin Ust ve Sol Uzakligi
                Alt_Sag								=	(Ust_Sol[0] + w, Ust_Sol[1] + h) #Bulunan Objenin Alt ve Sag Uzakligi
                cv2.rectangle(EkranGoruntusu, Ust_Sol, Alt_Sag, (0,255,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle    
                cv2.imshow('EKRAN', EkranGoruntusu) #Ekran Goruntusunu Goster cv2.cvtColor(EkranGoruntusu,cv2.COLOR_BGR2RGB
                cv2.waitKey(30)
                return d, x, y, w, h
            else:
                return d, x, y, w, h
        else:
            d = 0
            m = 0
            #cv2.destroyAllWindows()
            print('hadiama', max_val)
            print("Tespit Edilemedi")
            return d, m

#Kullanilmayan fonksiyonlar
'''   
                
    def ekran_kontrol_yedek(path):
        while(True):
            OrnekResim 							=	cv2.imread(path) #Tespit Edeceğimiz Resim
            OrnekResimDonustur 					=	cv2.cvtColor(OrnekResim,cv2.COLOR_BGR2GRAY) #Tespit Edeceğimiz Resimi Gri Formata Donustur
            EkranGoruntusu 						=	np.array(ImageGrab.grab()) #Anlik Ekran Goruntusunu Al bbox=(0,0,1366,380)
            EkranGoruntusuDonustur 				=	cv2.cvtColor(EkranGoruntusu,cv2.COLOR_BGR2GRAY) #Ekran Goruntusunu Gri Formata Donusturuyoruz
            Sonuc 								=	cv2.matchTemplate(EkranGoruntusuDonustur,OrnekResimDonustur,cv2.TM_CCOEFF_NORMED) #Ekran Grountusunun Icerisinde Resmi Ariyoruz
            sin_val, max_val, min_loc, max_loc	=	cv2.minMaxLoc(Sonuc) #Bulunan Objenin Koordinatlarini Bul
            Ust_Sol 							=	max_loc #Bulunan Objenin Ust ve Sol Uzakligi
            Alt_Sag								=	(Ust_Sol[0]+50, Ust_Sol[1]+50) #Bulunan Objenin Alt ve Sag Uzakligi
            cv2.rectangle(EkranGoruntusu, Ust_Sol, Alt_Sag, (0,255,0),5) #Ekranda Bulunan Nesnenin Koordinatlarini Isaretle
            cv2.imshow('EKRAN',cv2.cvtColor(EkranGoruntusu,cv2.COLOR_BGR2RGB)) #Ekran Goruntusunu Goster 
    
    def sol_click(x, y, w, h):
        pozisyon = mouse.get_position()
        w1 = int(w/2)
        h1 = int(h/2)
        x1 = x + w1
        y1 = y + h1
        mouse.move(x1,y1)
        mouse.click()
        mouse.move(pozisyon[0], pozisyon[1])
'''
        
       
    