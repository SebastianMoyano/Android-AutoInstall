#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import tkinter as tk
from tkinter import ttk
import os
import subprocess
import sys
import threading





    

def proceso():
    
    
    print("Desactivando Suspension")
    os.system(dir2+" shell svc power stayon true")
    print("Listo")
    print("Comenzando Instalacion: ")
    filtered = [x for x in apks if ".apk" in x]
    count = 0
    countP = 0
    text.set("Instalacion en progreso")
    for x in filtered:

            print(str(len(filtered)-count)+" Programas por instalar")
            print("Instalando "+x)
            try:
                r =subprocess.check_output([dir2,"install",os.path.join(dirapk,x)], shell=False)
                color.config(bg="green", fg="white")
                
                textProceso.set(x+" instalado")
            except:
                color.config(bg="red",fg="white")
                textProceso.set("Error "+x)
                
                count += 1
            countP += 1
            print(int((100.0*countP)/len(filtered)))
            progress['value'] = int((100.0*countP)/len(filtered))
            screen.update_idletasks()
    color.config(bg="white")      
    textProceso.set("")
    if count == 0:
        text.set("Proceso terminado")
        color2.config(bg="green")
    else:
        text.set("Proceso terminado con errores: "+str(count))
        color2.config(bg="red")

    print("Listo!")
    sys.stdout = sys.__stdout__
    kill()
def Check():
    s = subprocess.check_output([dir2,"devices"], shell=False)
    lista = s.decode("utf-8").split()
    if "device" in lista:
        text.set("Dispositivo Encontrado")
    else:
        text.set("Dispositivo No Encontrado")
def kill():
    command = '''kill -9 `pgrep -f fork-server`'''
    os.system(command)
    print("cerrado")

def threadProxy():
    thread = threading.Thread(target=proceso)
    thread.daemon = True
    thread.start()
    
def register(direct):
    global dir1, dir2, dirapk,apks
    dirapk = os.path.join(direct,"apk")
    dir1 = os.listdir(dirapk)
    dir2 = os.path.join(direct,"platform-tools","adb")
    
    dir1 = os.listdir(dirapk)
    apks = []
    for x in dir1:
        s = x.split()
        if len(s)>1:
            new = "_".join(s)
            os.rename(os.path.join(dirapk,x),os.path.join(dirapk,new)) 
            apks.append(new)
        else:
            apks.append(x)
    global screen,text,textProceso,color,color2,progress
    screen = tk.Tk()
    s = ttk.Style(screen)
    text = tk.StringVar()
    textProceso = tk.StringVar()
    s.theme_use('clam')
    s.configure('TButton', background = "white",borderwidth=0)
    s.configure('TLabel', background = "white",borderwidth=0)

    screen.title("APK")
    screen.geometry("400x450")    
    compra = tk.PhotoImage(file = r"images/boton.png") 
    startimg = tk.PhotoImage(file = r"images/START.png") 
    salirImg = tk.PhotoImage(file = r"images/salir.png") 
    start = ttk.Button(screen, image = startimg, command = Check )
    start.image = startimg
    start.pack()
    Bcompra = ttk.Button(screen, image = compra, command = threadProxy )
    Bcompra.image = compra
    Bcompra.pack()
    emergencia = ttk.Button(screen, image = salirImg, command = kill )
    emergencia.image = salirImg
    emergencia.pack()

    color2 = tk.Label(screen, textvariable=text)
    color2.pack(pady=3)
    color = tk.Label(screen, textvariable=textProceso)
    color.pack(pady=3)
    progress = ttk.Progressbar(screen, orient = tk.HORIZONTAL, 
              length = 100, mode = 'determinate')
    progress.pack(pady=3)
    
    screen.mainloop()




