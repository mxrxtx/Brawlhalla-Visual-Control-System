from time import sleep , time
import win32api
import win32con
import win32gui

# YARARLANDIGIM KAYNAKLAR
# https://docs.microsoft.com/en-us/windows/win32/inputdev/mouse-input

class kontrol():
    
    def __init__(self):
        self.hwnd = win32gui.FindWindow(None, 'Brawlhalla')
    
    def light_attack(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('C'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('C'), 0)
        sleep(0.7)
        
    def heavy_attack(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('X'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('X'), 0)
        sleep(0.7)
        
    def up(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('W'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('W'), 0)
        sleep(0.005)
        
    def down(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('S'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('S'), 0)    
        sleep(0.005)
        
    def right(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('D'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('D'), 0)   
        sleep(0.005)
        
    def left(self):
        win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
        win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('A'), 0)    
        sleep(0.7)
        
    def l_click(self):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON)   
        
    def r_click(self):
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON)
    
    def l_click_POS(self, x, y, w, h):
        w1 = int(w/2)
        h1 = int(h/2)
        x1 = x + w1
        y1 = y + h1
        client_pos = win32gui.ScreenToClient(self.hwnd, (x1,y1))
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32gui.SendMessage(self.hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON,tmp) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON,tmp)    
    
    def r_click_POS(self, x, y, w, h):
        w1 = int(w/2)
        h1 = int(h/2)
        x1 = x + w1
        y1 = y + h1
        client_pos = win32gui.ScreenToClient(self.hwnd, (x1,y1))
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32gui.SendMessage(self.hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON,tmp) 
        win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON,tmp)        
        
    def left_Lattack(self):
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
            end = time()
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('C'), 0)
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('C'), 0) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('A'), 0) 
                sleep(0.7)
                break    
    
    def left_Hattack(self):
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
            end = time()
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('X'), 0)
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('X'), 0) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('A'), 0) 
                sleep(0.7)
                break         
    
    def right_Lattack(self):
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('D'), 0)
            end = time()
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('C'), 0)
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('C'), 0) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('D'), 0) 
                sleep(0.7)
                break      
    
    def right_Hattack(self):
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('D'), 0)
            end = time()
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('X'), 0)
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('X'), 0) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('D'), 0) 
                sleep(0.7)
                break   
            
    def left_L_M_attack(self):
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON)
            end = time()
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('A'), 0) 
                sleep(0.7)
                break       
    
    def left_H_M_attack(self):                
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('A'), 0)
            win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON)
            end = time()
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_LBUTTON) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('A'), 0) 
                sleep(0.7)
                break 
            
    def right_L_M_attack(self):                
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('D'), 0)
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON)
            end = time()
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('D'), 0) 
                sleep(0.7)
                break      
    
    def right_H_M_attack(self):                
        start = time()
        while True:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, ord('D'), 0)
            win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONDOWN, win32con.MK_LBUTTON)
            end = time()
            if (end - start) >= 0.1:
                win32api.SendMessage(self.hwnd, win32con.WM_RBUTTONUP, win32con.MK_LBUTTON) 
                win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, ord('D'), 0) 
                sleep(0.7)
                break            
    