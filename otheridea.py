import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image,ImageTk
import numpy as np
import threading

#Main window
window=tk.Tk()
window.title("OMCHS") #online meeting chat helping system
window.geometry("800x450") #same as zoom window
window.resizable(width=True, height=True)
#control window
control = tk.Toplevel()
control.title("control")
control.geometry('400x400')
control.grid()

maru = cv2.imread('maru.jpg',0)
batu = cv2.imread('batu.jpg',0)
toumei = cv2.imread('toumei.jpg',0)
actionImg = toumei

#Main window set up and function --------------------------------------------

#video canvas
Vcanvas=tk.Canvas(window, width=600, height=450, bg="green")
Vcanvas.place(x=0, y=0)

#get webCam capture
def capStart():
    print('camera-ON')
    try:
        global Capture, w, h
        Capture=cv2.VideoCapture(0)
        w, h= Capture.get(cv2.CAP_PROP_FRAME_WIDTH), Capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    except:
        import sys
        print("error-----")
        print(sys.exec_info()[0])
        print(sys.exec_info()[1])
        '''終了時の処理はここでは省略します。
        c.release()
        cv2.destroyAllWindows()'''

#updata
def update():
    global img
    ret, frame =Capture.read()
    windowsize = (1200, 900)
    frame = cv2.resize(frame, windowsize)
    if ret:
        img=ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        Vcanvas.create_image(0,0,image=img)
    else:
        print("u-Fail")
    window.after(1,update)

#control window set up and function--------------------------------------------

def btn_click():
    actionImg = maru
    Vcanvas.create_image(0,0,image=actionImg)
    messagebox.showinfo("メッセージ", "ボタンがクリックされました")

btn = tk.Button(control, text='ボタン', command = btn_click)
btn.place(x=130, y=80) #ボタンを配置する位置の設定


capStart()
update()
window.mainloop()

#参考にさせていただいたページ　https://shizenkarasuzon.hatenablog.com/entry/2018/12/31/064646　https://teratail.com/questions/187773
#今後、許可をとる予定です