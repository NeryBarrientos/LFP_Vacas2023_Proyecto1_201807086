from ventanas import ventana_afn, ventana_afd, ventana_oe, ventana_cargar
from ttkthemes import ThemedTk
from tkinter import Frame, Label, Button
import functools
# Llamados Ventanas


def mostrar_principal():
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    # conteo.pack_forget()
    miFrameV.pack(side="top", fill="both", expand=True)


def mostrar_ventana_afn():
    miFrameV.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    # eliminar.pack_forget()
    # conteo.pack_forget()
    # mostrarCurso.pack_forget()
    var_ventana_afn.pack(side="top", fill="both", expand=True)


def mostrar_ventana_afd():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    # eliminar.pack_forget()
    # conteo.pack_forget()
    # mostrarCurso.pack_forget()
    var_ventana_afd.pack(side="top", fill="both", expand=True)


def mostrar_ventana_oe():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    # eliminar.pack_forget()
    # conteo.pack_forget()
    # mostrarCurso.pack_forget()
    var_ventana_oe.pack(side="top", fill="both", expand=True)


def mostrar_ventana_cargar():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    # eliminar.pack_forget()
    # conteo.pack_forget()
    # mostrarCurso.pack_forget()
    var_ventana_cargar_archivos.pack(side="top", fill="both", expand=True)

# Funcion Salir


def salir():
    exit()


#ventana = tkinter.Tk()
# Abro venta
ventana = ThemedTk(theme="ubuntu")
ancho_ventana = 1280
alto_ventana = 720
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title('Proyecto 1')
# Frame con nombre proyecto
miFrame = Frame()
miFrame.pack(side="top", fill="x")
miFrame.config(width="500", height="50", relief="solid", bd="3")
label = Label(
    miFrame, text='Lenguajes Formales y de Programacióñ | Sección: P | 201807086 | Nery Barrientos')
label.pack(side="top")
# frame Variable
miFrameV = Frame()
miFrameV.pack(fill="x")
miFrameV.place(x=0, y=25)
miFrameV.config(width=ancho_ventana, height=alto_ventana,
                relief="solid", bd="3")
# Funciones para ventanas en botones
var_ventana_afn = ventana_afn(ventana, mostrar_principal)
var_ventana_afd = ventana_afd(ventana, mostrar_principal)
var_ventana_oe = ventana_oe(ventana, mostrar_principal)
var_ventana_cargar_archivos = ventana_cargar(ventana, mostrar_principal)
# agregando Items a frame Variable
frame_centrado = Frame(miFrameV, height=310, width=450)
frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
boton1 = Button(frame_centrado, text='AFN',
                width=10, height=3, bd="4", command=mostrar_ventana_afn)
boton1.grid(row=0, column=0, padx=10, pady=10)
boton2 = Button(frame_centrado, text='AFD',
                width=10, height=3, bd="4", command=mostrar_ventana_afd)
boton2.grid(row=0, column=1, padx=10, pady=10)
boton3 = Button(frame_centrado, text='OE',
                width=10, height=3, bd="4", command=mostrar_ventana_oe)
boton3.grid(row=1, column=0, padx=10, pady=10)
boton4 = Button(frame_centrado, text='Cargar Archivo', width=10,
                height=3, command=mostrar_ventana_cargar, bd="4")
boton4.grid(row=1, column=1, padx=10, pady=10)
boton5 = Button(frame_centrado, text='Salir', width=10,
                height=3, command=salir, bd="4")
boton5.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom", fill="x")
miFrame1.config(width="500", height="30", relief="solid", bd="3")
ventana.mainloop()
