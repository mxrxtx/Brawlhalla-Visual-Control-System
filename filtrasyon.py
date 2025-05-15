from windowcapture import WindowCapture
import cv2 as cv

#YARARLANDIGIM KAYNAKLAR
#https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html
#https://realpython.com/python-opencv-color-spaces/  

class filtre ():
    
    max_value = 255
    max_value_H = 360//2
    low_H = 0
    low_S = 0
    low_V = 0
    high_H = max_value_H
    high_S = max_value
    high_V = max_value
    window_detection_name = 'Object Detection'
    low_H_name = 'Low H'
    low_S_name = 'Low S'
    low_V_name = 'Low V'
    high_H_name = 'High H'
    high_S_name = 'High S'
    high_V_name = 'High V'
    def on_low_H_thresh_trackbar(self, val):
        self.low_H = val
        self.low_H = min(self.high_H-1, self.low_H)
        cv.setTrackbarPos(self.low_H_name, self.window_detection_name, self.low_H)
    def on_high_H_thresh_trackbar(self, val):
        self.high_H = val
        self.high_H = max(self.high_H, self.low_H+1)
        cv.setTrackbarPos(self.high_H_name, self.window_detection_name, self.high_H)
    def on_low_S_thresh_trackbar(self,val):
        self.low_S = val
        self.low_S = min(self.high_S-1, self.low_S)
        cv.setTrackbarPos(self.low_S_name, self.window_detection_name, self.low_S)
    def on_high_S_thresh_trackbar(self, val):
        self.high_S = val
        self.high_S = max(self.high_S, self.low_S+1)
        cv.setTrackbarPos(self.high_S_name, self.window_detection_name, self.high_S)
    def on_low_V_thresh_trackbar(self, val):
        self.low_V = val
        self.low_V = min(self.high_V-1, self.low_V)
        cv.setTrackbarPos(self.low_V_name, self.window_detection_name, self.low_V)
    def on_high_V_thresh_trackbar(self, val):
        self.high_V = val
        self.high_V = max(self.high_V, self.low_V+1)
        cv.setTrackbarPos(self.high_V_name, self.window_detection_name, self.high_V)
    
    def filtre_ayarlari(self, window_name=None, x=0, y=0, w=640, h=360):
        cv.namedWindow(self.window_detection_name , cv.WINDOW_GUI_EXPANDED)
        
        imgsize = cv.imread(window_name)
        h, w, channels = imgsize.shape

        cv.resizeWindow(self.window_detection_name, w, (h+390)) #barlarin uzunlugu 390 pixel
        cv.createTrackbar(self.low_H_name, self.window_detection_name , self.low_H, self.max_value_H, self.on_low_H_thresh_trackbar)
        cv.createTrackbar(self.high_H_name, self.window_detection_name , self.high_H, self.max_value_H, self.on_high_H_thresh_trackbar)
        cv.createTrackbar(self.low_S_name, self.window_detection_name , self.low_S, self.max_value, self.on_low_S_thresh_trackbar)
        cv.createTrackbar(self.high_S_name, self.window_detection_name , self.high_S, self.max_value, self.on_high_S_thresh_trackbar)
        cv.createTrackbar(self.low_V_name, self.window_detection_name , self.low_V, self.max_value, self.on_low_V_thresh_trackbar)
        cv.createTrackbar(self.high_V_name, self.window_detection_name , self.high_V, self.max_value, self.on_high_V_thresh_trackbar)
        
        wincap = WindowCapture(window_name,x,y,w,h)
        while True:
            screen = wincap.get_screenshot()
            frame_HSV = cv.cvtColor(screen, cv.COLOR_RGB2HSV)
            frame_threshold = cv.inRange(frame_HSV, (self.low_H, self.low_S, self.low_V), (self.high_H, self.high_S, self.high_V))
            result = cv.bitwise_and(screen, screen, mask=frame_threshold)
            
            cv.imshow(self.window_detection_name, result)
            
            key = cv.waitKey(30)
            if key == ord('q') or key == 27:
                cv.destroyAllWindows()
                break
            if key == ord('s'):
                cv.imwrite('filtreli-goruntu.png', result)
    
    def filtre_ayarlari_picture(self, picture ):
        cv.namedWindow(self.window_detection_name , cv.WINDOW_GUI_EXPANDED)
        img = cv.imread(picture)
        h, w, channels = img.shape
        cv.resizeWindow(self.window_detection_name, w, (h+390)) #barlarin uzunlugu 390 pixel 
        cv.createTrackbar(self.low_H_name, self.window_detection_name , self.low_H, self.max_value_H, self.on_low_H_thresh_trackbar)
        cv.createTrackbar(self.high_H_name, self.window_detection_name , self.high_H, self.max_value_H, self.on_high_H_thresh_trackbar)
        cv.createTrackbar(self.low_S_name, self.window_detection_name , self.low_S, self.max_value, self.on_low_S_thresh_trackbar)
        cv.createTrackbar(self.high_S_name, self.window_detection_name , self.high_S, self.max_value, self.on_high_S_thresh_trackbar)
        cv.createTrackbar(self.low_V_name, self.window_detection_name , self.low_V, self.max_value, self.on_low_V_thresh_trackbar)
        cv.createTrackbar(self.high_V_name, self.window_detection_name , self.high_V, self.max_value, self.on_high_V_thresh_trackbar)

        while True:
            frame_HSV = cv.cvtColor(img, cv.COLOR_RGB2HSV)
            frame_threshold = cv.inRange(frame_HSV, (self.low_H, self.low_S, self.low_V), (self.high_H, self.high_S, self.high_V))
            result = cv.bitwise_and(img, img, mask=frame_threshold)
            
            cv.imshow(self.window_detection_name, result)
            
            key = cv.waitKey(30)
            if key == ord('q') or key == 27:
                cv.destroyAllWindows()
                break
            if key == ord('s'):
                cv.imwrite('filtreli-goruntu.png', img)
                
    # cv2.resizeWindow('image', 350, 700)
    def filtre_uygulama (imgshow=0, screen=None, hmin=0, hmax=0, smin=0, smax=0, vmin=0, vmax=0):    
        #Gorsele uygulayacagimiz filtrenin degerlerini giriyoruz 
        hsvmin = (hmin, smin, vmin) # hud(96, 252, 254) #win( 90,  0, 232) 
        hsvmax = (hmax, smax, vmax) # hud(97, 255, 255) #win(105, 40, 249)
        
        frame_HSV = cv.cvtColor(screen, cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV, hsvmin, hsvmax)
        result = cv.bitwise_and(screen, screen, mask=frame_threshold)
        #blur = cv2.GaussianBlur(mask, (7, 7), 0)
        
        
        if imgshow == 1:
            cv.imshow('Filtreli Goruntu', result)
            key = cv.waitKey(30)
            if key == ord('s'):
                cv.imwrite('filtreli-goruntu.png', result)
        
        return result    
        #key = cv.waitKey(30)
        #if key == ord('q') or key == 27:
        #    cv.destroyAllWindows()
        #    break
        
        #baska bir tane ile birlestirmek istersek
        #final_mask = mask + mask_white
        #final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
        
        

    