import functools
from tkinter import Label, Button, Frame, messagebox
import easygui as eg

# Funciones


def cargar_AFD():
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    imprimir2 = 'Archivo no seleccionado, vuelva a intentarlo'
    extension = ["*.py", "*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='C:/Users/neri_/OneDrive/Escritorio/*afd',
                             filetypes=extension)
    mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
        75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    messagebox.showinfo(message=mensaje, title="Mensaje")
    f = open(archivo, 'r', encoding="utf8")
    f.close()


def cargar_AFN():
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    imprimir2 = 'Archivo no seleccionado, vuelva a intentarlo'
    extension = ["*.py", "*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='C:/Users/neri_/OneDrive/Escritorio/*afn',
                             filetypes=extension)
    mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
        75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    messagebox.showinfo(message=mensaje, title="Mensaje")
    f = open(archivo, 'r', encoding="utf8")
    f.close()
# Ventanas


def ventana_afn(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    label = Label(main_frame, text="AFN")
    label.place(x=615, y=30)
    boton1 = Button(main_frame, text='Listar Cursos',
                    width=15, height=3, bd="4", command=None)
    boton1.place(x=600, y=70)
    boton2 = Button(main_frame, text='Mostrar Curso',
                    width=15, height=3, bd="4", command=None)
    boton2.place(x=600, y=140)
    boton3 = Button(main_frame, text='Agregar Curso',
                    width=15, height=3, bd="4", command=None)
    boton3.place(x=600, y=210)
    boton4 = Button(main_frame, text='Editar Curso',
                    width=15, height=3, bd="4", command=None)
    boton4.place(x=600, y=280)
    boton5 = Button(main_frame, text='Eliminar curso',
                    width=15, height=3, bd="4", command=None)
    boton5.place(x=600, y=350)
    boton5 = Button(main_frame, text='Regresar', width=15,
                    height=3, command=callback, bd="4")
    boton5.place(x=600, y=420)
    return main_frame


def ventana_afd(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    label = Label(main_frame, text="AFD")
    label.place(x=615, y=30)
    boton1 = Button(main_frame, text='Listar Cursos',
                    width=15, height=3, bd="4", command=None)
    boton1.place(x=600, y=70)
    boton2 = Button(main_frame, text='Mostrar Curso',
                    width=15, height=3, bd="4", command=None)
    boton2.place(x=600, y=140)
    boton3 = Button(main_frame, text='Agregar Curso',
                    width=15, height=3, bd="4", command=None)
    boton3.place(x=600, y=210)
    boton4 = Button(main_frame, text='Editar Curso',
                    width=15, height=3, bd="4", command=None)
    boton4.place(x=600, y=280)
    boton5 = Button(main_frame, text='Eliminar curso',
                    width=15, height=3, bd="4", command=None)
    boton5.place(x=600, y=350)
    boton5 = Button(main_frame, text='Regresar', width=15,
                    height=3, command=callback, bd="4")
    boton5.place(x=600, y=420)
    return main_frame


def ventana_oe(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    label = Label(main_frame, text="OE")
    label.place(x=615, y=30)
    boton1 = Button(main_frame, text='Listar Cursos',
                    width=15, height=3, bd="4", command=None)
    boton1.place(x=600, y=70)
    boton2 = Button(main_frame, text='Mostrar Curso',
                    width=15, height=3, bd="4", command=None)
    boton2.place(x=600, y=140)
    boton3 = Button(main_frame, text='Agregar Curso',
                    width=15, height=3, bd="4", command=None)
    boton3.place(x=600, y=210)
    boton4 = Button(main_frame, text='Editar Curso',
                    width=15, height=3, bd="4", command=None)
    boton4.place(x=600, y=280)
    boton5 = Button(main_frame, text='Eliminar curso',
                    width=15, height=3, bd="4", command=None)
    boton5.place(x=600, y=350)
    boton5 = Button(main_frame, text='Regresar', width=15,
                    height=3, command=callback, bd="4")
    boton5.place(x=600, y=420)
    return main_frame


def ventana_cargar(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Cargar Archivo")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton1 = Button(frame_centrado, text='Cargar AFD',
                    width=15, height=3, bd="4", command=cargar_AFD)
    boton1.grid(row=1, column=0, padx=10, pady=10)
    boton2 = Button(frame_centrado, text='Cargar AFN',
                    width=15, height=3, bd="4", command=cargar_AFN)
    boton2.grid(row=2, column=0, padx=10, pady=10)
    boton3 = Button(frame_centrado, text='Regresar', width=15,
                    height=3, command=callback, bd="4")
    boton3.grid(row=3, column=0, padx=10, pady=10)
    return main_frame
