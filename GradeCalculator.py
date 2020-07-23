# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 17:50:09 2018

@author: alumno
"""
#Modulos, paquetes y librerias importados
from Tkinter import *
import Tkinter as tk
import ttk
import tkMessageBox
import random
import re
import numpy as np

#Inicializacion de variables globales
c=0
d=0
global t
PF=[]
CF=[]
t1=[range(10) for x in range (1)]

t2=[range(10) for x in range (1)]
t3=[range(10) for x in range (1)]
#Declaracion de funciones

 #1. Llenado de matriz

def llenarMatriz(b,t):
    
    for f in range (1):
        for g in range (10):
            t[f][g]=b[f][g]  
            
    return t

#2. Creacion de segunda ventana: Ingreso de codigo y notas

def abrirventana2():
    
    global win
    ventana.withdraw()
    win=tk.Toplevel()
    win.resizable(0, 0)
    
    w = 350
    h = 750
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))

    win.configure(background="dimgray")
    e3=tk.Label(win, text="Registro de notas", bg="brown", fg="white")
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5)
        
    e4=tk.Label(win, text="Ingrese codigo de 6 digitos: ", bg="orange", fg="black") 
    e4.pack(padx=5, pady=5, ipadx=5, ipady=5)
    codigo_int= StringVar()
    codigo_entry = tk.Entry(win,textvariable=codigo_int)
    codigo_entry.pack(fill=tk.X, padx=7, pady=7, ipadx=7, ipady=7)
    
    #NotaControl1
    e5=tk.Label(win, text="Ingrese nota control 1: ", bg="orange", fg="black") 
    e5.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    nota_int= StringVar()
    nota_entry = tk.Entry(win,textvariable=nota_int)
    nota_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
    
    #NotaControl2
    e6=tk.Label(win, text="Ingrese nota control 2: ", bg="orange", fg="black") 
    e6.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    nota2_int= StringVar()
    nota2_entry = tk.Entry(win,textvariable=nota2_int)
    nota2_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
    
    #NotaControl3
    e7=tk.Label(win, text="Ingrese nota control 3: ", bg="orange", fg="black") 
    e7.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    nota3_int= StringVar()
    nota3_entry = tk.Entry(win,textvariable=nota3_int)
    nota3_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
    #NotaControl4
    e8=tk.Label(win, text="Ingrese nota control 4: ", bg="orange", fg="black") 
    e8.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    nota4_int= StringVar()
    nota4_entry = tk.Entry(win,textvariable=nota4_int)
    nota4_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
    
    #NotaControlParcial
    e9=tk.Label(win, text="Ingrese nota exámen Parcial: ", bg="orange", fg="black") 
    e9.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    notap_int= StringVar()
    notap_entry = tk.Entry(win,textvariable=notap_int)
    notap_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
    
    #NotaControlFinal
    e10=tk.Label(win, text="Ingrese nota exámen Final: ", bg="orange", fg="black") 
    e10.pack(padx=9, pady=9, ipadx=9, ipady=9)
       
    notaf_int= StringVar()
    notaf_entry = tk.Entry(win,textvariable=notaf_int)
    notaf_entry.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)
            
    #Validacion notas. Ingreso dentro de la interfaz
    def validarnotas():
        nota=nota_int.get()
        correct1 = re.match("^[0-9-" "]+$", nota)
        
        
        nota2=nota2_int.get()
        correct2 = re.match("^[0-9-" "]+$", nota2)
        
        
        nota3=nota3_int.get()
        correct3 = re.match("^[0-9-" "]+$", nota3)
        
        
        
        nota4=nota4_int.get()
        correct4 = re.match("^[0-9-" "]+$", nota4)
        
        
        notap=notap_int.get()
        correct5 = re.match("^[0-9-" "]+$", notap)
            
        notaf=notaf_int.get()
        correct6 = re.match("^[0-9-" "]+$", notaf)
              
        
        if(correct1 and correct2 and correct3 and correct4 and correct5 and correct6):
            
            
            if(int(nota_int.get())>=0 and int(nota_int.get())<=20):
                if(int(nota2_int.get()) >=0 and int(nota2_int.get()) <=20):
                    if(int(nota3_int.get()) >=0 and int(nota3_int.get()) <=20):
                        if(int(nota4_int.get())>=0 and int(nota4_int.get()) <=20):
                            if(int(notap_int.get()) >=0 and int(notap_int.get()) <=20):
                                if(int(notaf_int.get()) >=0 and int(notaf_int.get()) <=20):
                                    return True
            else:
                return False 
                tkMessageBox.showinfo("Cuidado", "Ingrese de nuevo")
             
        else:
            return False
    #Validacion codigo              
    def validarcodigo():
        codigo=codigo_int.get()
        correct = re.match("^[0-9-" "]+$", codigo)
        
        if (correct):
            if(int(codigo_int.get())>=100000 and int(codigo_int.get())<=999999):
                return True
            
        else:
            return True
    #Validacion formulario2: Comprueba que se cumpla la validacion de codigo y nota
    def validarformulario2():
        global c       
        c=c+1
        if (validarcodigo()==True and validarnotas()==True):
            tkMessageBox.showinfo("Éxito", "Registro Aceptado")
            abrirventana3()
                
        else:
            tkMessageBox.showinfo("Cuidado", "Ingreso erroneo")
            
    
      
    boton3=tk.Button(win, text="Grabar Datos", fg="blue", command=validarformulario2)
    boton3.pack(side=tk.TOP)
    
    #Cálculo de promedio dentro de la interfaz:

    def calcularPromedio():
        
        global d
        n=1
        b=[range(10) for x in range (n)]
        for f in range (n):
                        
            for g in range (10):
                if (g==0):
                    b[f][g] =int(codigo_int.get())
                    
                 
                elif (g==1):
                    b[f][g]=int(nota_int.get())
                    
                    
                elif (g==2):
                    b[f][g] = int(nota2_int.get())
                    
                    
                elif (g==3):
                    b[f][g]=int(nota3_int.get())
                    
                    
                elif (g==4):
                    b[f][g]=int(nota4_int.get())
                    
                    
                    
                elif (g==5):
                    b[f][g]=int(notap_int.get())
                    
                    
                else:
                    b[f][g]=int(notaf_int.get()) 
            
            menor= min(b[f][1],b[f][2], b[f][3],b[f][4])
            
            promedioP = (b[f][5])*0.3
            
            
            promedioF= (b[f][6])*0.4
            b[f][7]=int(menor)
            
            promediopc = round((((b[f][1]+b[f][2]+ b[f][3]+ b[f][4])- menor)*1.0)/3)
            
            b[f][8]=int(promediopc)
            
            promediopca=promediopc*0.3
            promedioFinal= promediopca+promedioP+promedioF
            b[f][9]=int(promedioFinal)
            
                                  
            if(d==0):
                llenarMatriz(b,t1)
            elif(d==1):
                llenarMatriz(b,t2)
            else:
                llenarMatriz(b,t3)
            d=d+1
        return int(promedioFinal)
    
    #Funcion recurrente cerrar     
    def cerrar(a):
        a.destroy()
        
    #Funcion recurrente continuar: Actualizacion de la variable c que da paso a la apertura de ventanas
    def continuar():
        cantidad=int(cantidad_int.get())
        if(c<cantidad and c<3):
            cerrar(win2)
            abrirventana2()
        else:
            abrirventana4()          
        
    #Creacion de ventana 3       
    def abrirventana3():
        global win2
        
        cerrar(win)  
        
        win2=tk.Tk()
        win2.resizable(0, 0)
        w = 350
        h = 350
        
        ws = win2.winfo_screenwidth()
        hs = win2.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win2.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win2.configure(background='dimgray')
                    
                  
        e11=tk.Label(win2, text="Reporte de nota individual:  ", bg="skyblue", fg="black")
        e11.pack(padx=7, pady=7, ipadx=7, ipady=7, fill=tk.X)
            
        e12=tk.Label(win2, text=calcularPromedio(), bg="orange", fg="black")
        e12.pack(padx=7, pady=7, ipadx=7, ipady=7, fill=tk.X)
            
        boton5=tk.Button(win2, text='Continuar',  fg="blue",command=continuar)
        boton5.pack(padx=9, pady=9, ipadx=9, ipady=9)  
    
    #Funcion que guarda los datos del promedio final en el arreglo unidimensional PF para su posterior ordenamiento
    def guardarLista(PF,f):
        c=int(cantidad_int.get())

        j=9
        for i in range (c):            
                PF.append(f[i][j])
                
        return PF
        
    #Funcion que guarda los datos de los codigos en el arreglo unidimensional CF para su posterior ordenamiento
    
    def guardarCodigo(CF,f):
        c=int(cantidad_int.get())
        j=0
        for i in range (c):            
                CF.append(f[i][j])
                
        return CF
    #Funcion que ordena los arreglos PF Y CF de mayor a menor según corresponda   
    def ordenarLista(a,b):
        for i in range (1,len(a)):
            for j in range (len(a)-i):
                if(a[j]<a[j+1]):
                    temp=a[j]
                    temp2=b[j]
                    a[j]=a[j+1]
                    b[j]=b[j+1]
                    a[j+1]=temp
                    b[j+1]=temp2
            
                
    #Funcion que convierte las listas ordenadas a una matriz bidimensional  
    def mostrarListaOrdenada():
        
        cerrar(win3) 
        c=int(cantidad_int.get())
        a=guardarLista(PF,f)
        
        b=guardarCodigo(CF,f)
        ordenarLista(a,b)
        
        o=[range(2) for x in range (c)]
                
        for i in range (c):
            for m in range (2):
                if(m==0):
                    o[i][m]=b[i]
                else:
                    o[i][m]=a[i]
        print o
        
        win4=tk.Toplevel()
        win4.resizable(0, 0)
        w = 350
        h = 700
        
        ws = win4.winfo_screenwidth()
        hs = win4.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win4.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win4.configure(background='dark blue')
                    
                  
        e11=tk.Label(win4, text="Ponderado de notas: Lista Ordenada", bg="orange", fg="black")
        e11.pack(padx=7, pady=7, ipadx=7, ipady=7, fill=tk.X)
        
            
        data = o
                
        frame = Frame(win4)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2), height = 25, show = "headings")
        tree.pack(side = 'left')
        
        tree.heading(1, text="Código")  
        tree.heading(2, text="Nota ponderada")  
        
        
        tree.column(1, width = 100)
        tree.column(2, width = 100)
        
        
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'right', fill = 'y')
        
        tree.configure(yscrollcommand=scroll.set)
        
        for val in data:
            tree.insert('', 'end', values = (val[0], val[1]) )
        boton5=tk.Button(win4, text='Finalizar', command=win4.destroy)
        boton5.pack(side=tk.TOP)               
        
        
        win4.mainloop()
        
    #Creacion de ventana 4: Reporte de notas
    def abrirventana4():
        global f
        global win3
        cerrar(win2)
        
        c=int(cantidad_int.get())
        if(c==1):
            f=t1
        elif(c==2):
            r=np.concatenate((t1,t2), axis=0)
            f=r
        
        elif(c==3):
            r=np.concatenate((t1,t2,t3), axis=0)
            f=r
        else:
            e=c-3
            b=[range(10) for x in range (e)] 
            for s in range (e):
                for g in range (10):
                    if (g==0):
                        b[s][g] = int(random.randrange(000000, 999999))
                    elif (g==1):
                        b[s][g]=int(random.randrange(0, 20))
                        
                    
                    
                    elif (g==2):
                        b[s][g] = int(random.randrange(0, 20))
                    
                    
                    elif (g==3):
                        b[s][g]=int(random.randrange(0, 20))
                    
                    
                    elif (g==4):
                        b[s][g]=int(random.randrange(0, 20))
                    
                    
                    elif (g==5):
                        b[s][g]=int(random.randrange(0, 20))
                    
                    
                    elif (g==6):
                        b[s][g]=int(random.randrange(0, 20))
                        
                menor= min(b[s][1],b[s][2],b[s][3],b[s][4])
                
                
                promedioP = (b[s][5])*0.3
                promedioF= (b[s][6])*0.4
                b[s][7]=int(menor)
                
                
                promediopc = round((((b[s][1]+b[s][2]+ b[s][3]+ b[s][4])- menor)*1.0)/3)
                b[s][8]=int(promediopc)
                promediopca=promediopc*0.3
                promedioFinal= promediopca+promedioP+promedioF
                b[s][9]=int(promedioFinal)
                r=np.concatenate((t1,t2,t3,b), axis=0)
                f=r
                
        
        
                          
        win3=Tk()
        win3.resizable(0, 0)
        
        w = 1100
        h = 800
        ws = win3.winfo_screenwidth()
        hs = win3.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        win3.geometry('%dx%d+%d+%d' % (w, h, x, y))
        win3.configure(background='dark blue')         
                
        e11=tk.Label(win3, text="Reporte de notas del curso  ", bg="darkred", fg="white")
        e11.pack(padx=7, pady=7, ipadx=7, ipady=7, fill=tk.X)
                              
        data = f
                
        frame = Frame(win3)
        frame.pack()
        tree = ttk.Treeview(frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 30, show = "headings")
        tree.pack(side = 'left')
        
        tree.heading(1, text="Código")  
        tree.heading(2, text="Nota P1")  
        tree.heading(3, text="Nota P2")
        tree.heading(4, text="Nota P3")
        tree.heading(5, text="Nota P4")
        tree.heading(6, text="Nota Parcial")
        tree.heading(7, text="Nota Final")
        tree.heading(8, text="Nota minima P")
        tree.heading(9, text="Nota promedio P")
        tree.heading(10, text="Nota ponderado")
        
        
        tree.column(1, width = 100)
        tree.column(2, width = 100)
        tree.column(3, width = 100)
        tree.column(4, width = 100)
        tree.column(5, width = 100)
        tree.column(6, width = 100)
        tree.column(7, width = 100)
        tree.column(8, width = 100)
        tree.column(9, width = 100)
        tree.column(10, width = 100)
        
        
        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scroll.pack(side = 'left', fill = 'y')
        
        tree.configure(yscrollcommand=scroll.set)
        
        for val in data:
            tree.insert('', 'end', values = (val[0], val[1], val[2], val[3], val[4], val[5],val[6],val[7],val[8], val[9] ))
           
        boton5=tk.Button(win3, text='Mostrar reporte final', command=mostrarListaOrdenada)
        boton5.pack(side=tk.TOP)
        win3.mainloop()
        
#Validacion de la cantidad de alumnos ingresados en el rango de 1 a 30
def validarcantidad():

    cantidad=cantidad_int.get()

    correct = re.match("^[0-9-" "]+$", cantidad)
	
    if(correct):
        if(int(cantidad_int.get())>0 and int(cantidad_int.get())<=30):
            return True
            tkMessageBox.showinfo("Cuidado", "Ingrese nuevamente")
    else:
        return False
        
#Valida que la funcion validarcantidad () sea cierta y le de el paso de abrir la segunda ventana    
def validarformulario():

    if (validarcantidad()==True):
        tkMessageBox.showinfo("Correcto", "Acceso Aprobado")
        abrirventana2()
    else:
        tkMessageBox.showinfo("Cuidado", "Ingreso de dato incorrecto")

#1. Creacion de ventana principal: Ingreso de cantidad de alumnos
           
ventana=tk.Tk()
ventana.title("Registro")

fondo=PhotoImage(file="est.gif")
lblFondo=Label(ventana,image=fondo).place(x=0, y=0)

w = 350
h = 450
ws = ventana.winfo_screenwidth()
hs = ventana.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
ventana.geometry('%dx%d+%d+%d' % (w, h, x, y))

ventana.configure(background='skyblue')
e1=tk.Label(ventana, text="Bienvenido a SetGrade", bg="red", fg="white") 
e1.pack(padx=7, pady=7, ipadx=7, ipady=7)

e2=tk.Label(ventana, text="Ingrese la cantidad de alumnos ", bg="skyblue", fg="black") 
e2.pack(padx=10, pady=10, ipadx=10, ipady=10)

e2=tk.Label(ventana, text="Recuerde: Sólo ingresar valores entre 1 a 30", bg="skyblue", fg="black") 
e2.pack(padx=10, pady=10, ipadx=10, ipady=10)

global cantidad_int
cantidad_int =  StringVar()
cantidad_entry = tk.Entry(ventana,textvariable=cantidad_int)

cantidad_entry.pack( padx=5, pady=5, ipadx=5, ipady=5)

boton3=tk.Button(ventana, text="Ingresar", fg="blue", command=validarformulario)
boton3.pack(side=tk.TOP)
ventana.resizable(0, 0)
ventana.mainloop()


