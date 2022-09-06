import cv2 as cv
import numpy as np 
import pyautogui
pyautogui.FAILSAFE = False

cap = cv.VideoCapture(0)  
while(1):        
    
    _, frame = cap.read()  
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
    lower_green = np.array([19,109,57]) 
    upper_green = np.array([255,255,255]) 
    #parametro para cor verde detectada
  
    mask = cv.inRange(hsv, lower_green, upper_green) 
    res = cv.bitwise_and(frame,frame, mask= mask) 
    gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    _, borda = cv.threshold(gray, 3, 255, cv.THRESH_BINARY)
  
    
    contornos, _ = cv.findContours(
    borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        
        area = cv.contourArea(contorno)
        
        if area > 800:
            (x, y, w, h) = cv.boundingRect(contorno)
            #cv.drawContours(frame, contorno, -1, (255,0,0), 2)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv.putText(
                frame,
                str(f"x: {x} y: {y}"),
                (x, y-20),
                cv.FONT_HERSHEY_SIMPLEX,
                1, 1
            )
            pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)
            print("cor verde")
            #movimetação do mouse quando encontra a cor verde
        else:
            print("cor diferente")
            #pyautogui.drag(30, 0, 2, button='right')  
            pyautogui.click(1000,0,2,button='right')
            #movimentação do mouse botão direito quando encontra uma cor diferente
        break



    #cv.imshow("result mask", borda)
    
    
    
    
    k = cv.waitKey(5) & 0xFF
    if k == 27: 
      break

    cv.imshow('frame',frame) 
    cv.imshow('mask',mask) 
    cv.imshow('res',res) 


cv.destroyAllWindows() 
cap.release() 


