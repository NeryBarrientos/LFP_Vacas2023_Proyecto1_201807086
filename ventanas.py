import functools
from tkinter import Label, Button, Frame, messagebox, Entry, StringVar, Text, ttk
import easygui as eg
from ttkthemes import ThemedTk
import graphviz
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import ImageTk, Image
import os

informacion_afn = []
informacion_afd =[]

# Llamados Ventanas

def mostrar_principal():
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    miFrameV.pack(side="top", fill="both", expand=True)


def mostrar_ventana_afn():
    miFrameV.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_afn.pack(side="top", fill="both", expand=True)

def mostrar_ventana_evaluar_afn():
    miFrameV.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_evaluar_afn.pack(side="top", fill="both", expand=True)

def mostrar_ventana_afn_crear():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_afn_crear.pack(side="top", fill="both", expand=True)

def mostrar_ventana_ayuda_afn():
    miFrameV.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_ayuda_afn.pack(side="top", fill="both", expand=True)

def mostrar_ventana_afd():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_afd.pack(side="top", fill="both", expand=True)

def mostrar_ventana_evaluar_afd():
    miFrameV.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_evaluar_afd.pack(side="top", fill="both", expand=True)

def mostrar_ventana_afd_crear():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_afd_crear.pack(side="top", fill="both", expand=True)

def mostrar_ventana_validar_afd():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_validar_afd.pack(side="top", fill="both", expand=True)

def mostrar_ventana_validar_afn():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_validar_afn.pack(side="top", fill="both", expand=True)

def mostrar_ventana_ruta_afn():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_ruta_afn.pack(side="top", fill="both", expand=True)

def mostrar_ventana_ruta_afd():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack(side="top", fill="both", expand=True)

def mostrar_ventana_ayuda_afd():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_afd_crear.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_ayuda_afd.pack(side="top", fill="both", expand=True)


def mostrar_ventana_oe():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_cargar_archivos.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_oe.pack(side="top", fill="both", expand=True)


def mostrar_ventana_cargar():
    miFrameV.pack_forget()
    var_ventana_afn.pack_forget()
    var_ventana_afd.pack_forget()
    var_ventana_oe.pack_forget()
    var_ventana_afn_crear.pack_forget()
    var_ventana_evaluar_afn.pack_forget()
    var_ventana_ayuda_afn.pack_forget()
    var_ventana_ayuda_afd.pack_forget()
    var_ventana_evaluar_afd.pack_forget()
    var_ventana_validar_afd.pack_forget()
    var_ventana_validar_afn.pack_forget()
    var_ventana_ruta_afn.pack_forget()
    var_ventana_ruta_afd.pack_forget()
    var_ventana_cargar_archivos.pack(side="top", fill="both", expand=True)

# Funcion Salir


def salir():
    exit()

# Funciones

def aceptar_afn():
    diccionario = {}
    transiciones_afn = campo_transiciones_afn.get('1.0','end')
    temporal_sin_vacios = []
    temporal = transiciones_afn.split('\n')
    for datos in temporal:
        if datos != '' and datos != ' ':
            temporal_sin_vacios.append(datos)
    transiciones_afn = temporal_sin_vacios
    trans_corregidas = []
    for datos in transiciones_afn:
        lista_trans = []
        dato = datos.split(',')
        temporal = dato[1].split(';')
        lista_trans.append(dato[0])
        lista_trans.append(temporal[0])
        lista_trans.append(temporal[1])
        trans_corregidas.append(lista_trans)
    diccionario["nombre"] = nombre_afn.get()
    diccionario["estados"] = estados_afn.get().split(',')
    diccionario["alfabeto"] = alfabeto_afn.get().split(',')
    diccionario["estado inicial"] = estado_inicial_afn.get()
    diccionario["estados de aceptacion"] = estados_aceptacion_afn.get().split(',')
    diccionario["transciciones"] = trans_corregidas
    informacion_afn.append(diccionario)
    imprimir = '*********************************************'
    imprimir1 = 'AFN Agregado exitosamente'
    mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    messagebox.showinfo(message=mensaje, title="Mensaje")


def aceptar_afd():
    diccionario = {}
    transiciones_afd = campo_transiciones_afd.get('1.0','end')
    temporal_sin_vacios = []
    temporal = transiciones_afd.split('\n')
    for datos in temporal:
        if datos != '' and datos != ' ':
            temporal_sin_vacios.append(datos)
    transiciones_afd = temporal_sin_vacios
    trans_corregidas = []
    for datos in transiciones_afd:
        lista_trans = []
        dato = datos.split(',')
        temporal = dato[1].split(';')
        lista_trans.append(dato[0])
        lista_trans.append(temporal[0])
        lista_trans.append(temporal[1])
        trans_corregidas.append(lista_trans)
    diccionario["nombre"] = nombre_afd.get()
    diccionario["estados"] = estados_afd.get().split(',')
    diccionario["alfabeto"] = alfabeto_afd.get().split(',')
    diccionario["estado inicial"] = estado_inicial_afd.get()
    diccionario["estados de aceptacion"] = estados_aceptacion_afd.get().split(',')
    diccionario["transciciones"] = trans_corregidas
    informacion_afd.append(diccionario)
    imprimir = '*********************************************'
    imprimir1 = 'AFD Agregado exitosamente'
    mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    messagebox.showinfo(message=mensaje, title="Mensaje")

#Carga Masiva
def cargar_AFD():
    global informacion_afd
    lista = []
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
    leer = f.read()
    lista_temporal = leer.split('%')
    for element in lista_temporal:
        temporal_sin_vacios = ''
        if element != '' and element != ' ':
            temporal_sin_vacios = element   
        temporal = temporal_sin_vacios.split('\n')
        temporal_sin_vacios = []
        for datos in temporal:
            if datos != '' and datos != ' ':
                temporal_sin_vacios.append(datos)
        if element != '' and element != ' ':
            lista.append(temporal_sin_vacios)
    for element in lista:
        diccionario = {}
        diccionario["nombre"] = element[0]
        diccionario["estados"] = element[1].split(',')
        diccionario["alfabeto"] = element[2].split(',')
        diccionario["estado inicial"] = element[3]
        diccionario["estados de aceptacion"] = element[4].split(',')
        transiciones = element[5::]
        trans_corregidas = []
        for datos in transiciones:
            lista_trans = []
            dato = datos.split(',')
            temporal = dato[1].split(';')
            lista_trans.append(dato[0])
            lista_trans.append(temporal[0])
            lista_trans.append(temporal[1])
            trans_corregidas.append(lista_trans)
        diccionario["transciciones"] = trans_corregidas 
        informacion_afd.append(diccionario)
    f.close()


def cargar_AFN():
    global informacion_afn
    lista = []
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
    leer = f.read()
    lista_temporal = leer.split('%')
    for element in lista_temporal:
        temporal_sin_vacios = ''
        if element != '' and element != ' ':
            temporal_sin_vacios = element   
        temporal = temporal_sin_vacios.split('\n')
        temporal_sin_vacios = []
        for datos in temporal:
            if datos != '' and datos != ' ':
                temporal_sin_vacios.append(datos)
        if element != '' and element != ' ':
            lista.append(temporal_sin_vacios)
    for element in lista:
        diccionario = {}
        diccionario["nombre"] = element[0]
        diccionario["estados"] = element[1].split(',')
        diccionario["alfabeto"] = element[2].split(',')
        diccionario["estado inicial"] = element[3]
        diccionario["estados de aceptacion"] = element[4].split(',')
        transiciones = element[5::]
        trans_corregidas = []
        for datos in transiciones:
            lista_trans = []
            dato = datos.split(',')
            temporal = dato[1].split(';')
            lista_trans.append(dato[0])
            lista_trans.append(temporal[0])
            lista_trans.append(temporal[1])
            trans_corregidas.append(lista_trans)
        diccionario["transciciones"] = trans_corregidas 
        informacion_afn.append(diccionario)
    f.close()

#Generacion grafica
def generarDOT_afd():
    # Nombre de la carpeta
    carpeta_automatas = "automatas"

    # Crear la carpeta si no existe
    if not os.path.exists(carpeta_automatas):
        os.makedirs(carpeta_automatas)
    for element in informacion_afd:
        index = str(informacion_afd.index(element))
        ruta_archivo = os.path.join(carpeta_automatas, f'AFDPrueba{index}')
        dot = Digraph('AFD', filename=ruta_archivo, format='png')
        dot.attr(rankdir='LR', size='8,5')
        dot.attr('node', shape='doublecircle')
        for estadosA in element["estados de aceptacion"]:
            dot.node(estadosA)
        dot.attr('node', shape='circle')
        for estados in element["estados"]:
            dot.node(estados)
        for trans in element["transciciones"]:
            dot.edge(trans[0], trans[2], label=trans[1])
        dot.render(f'automatas/AFDPrueba{index}', view=False)

def generarDOT_afn():
    carpeta_automatas = "automatas"

    # Crear la carpeta si no existe
    if not os.path.exists(carpeta_automatas):
        os.makedirs(carpeta_automatas)
    for element in informacion_afn:
        index = str(informacion_afn.index(element))
        ruta_archivo = os.path.join(carpeta_automatas, f'AFNPrueba{index}')
        dot = Digraph('AFN', filename=ruta_archivo, format='png')
        dot.attr(rankdir='LR', size='8,5')
        dot.attr('node', shape='doublecircle')
        for estadosA in element["estados de aceptacion"]:
            dot.node(estadosA)
        dot.attr('node', shape='circle')
        for estados in element["estados"]:
            dot.node(estados)
        for trans in element["transciciones"]:
            dot.edge(trans[0], trans[2], label=trans[1])
        dot.render(f'automatas/AFNPrueba{index}', view=False)

#Reportes

def reporte_afd():
    generarDOT_afd()
    w, h = A4
    pdf = canvas.Canvas("Reporte_afd.pdf", pagesize=A4)
    pdf.setTitle("Reporte de AFD")
    for element in informacion_afd:
        index = str(informacion_afd.index(element))
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)
        text.textLine('Nombre: '+  element['nombre'])
        text.textLine("Estados: " + ','.join(element['estados']))
        text.textLine("Alfabeto: " + ','.join(element['alfabeto']))
        text.textLine("Estado Inicial: "+ element['estado inicial'])
        text.textLine("Estados de Aceptacion: "+ ','.join(element['estados de aceptacion']))
        text.textLine("Transiciones:")
        for datos in element['transciciones']:
            text.textLine(f'{datos[0]} , {datos[1]} ; {datos[2]}')
        text.textLine()
        pdf.drawText(text)
        text = "AFD generado con Graphviz"
        text_width = pdf.stringWidth(text, "Times-Roman", 12)
        pdf.drawCentredString(w / 2, h - 200, text)

        image_path = f'automatas/AFDPrueba{index}.png'
        image_width = 200
        image_height = 200
        image_x = (w - image_width) / 2
        image_y = h - 250 - image_height  # Adjust the vertical position as needed
        pdf.drawInlineImage(image_path, image_x, image_y, width=image_width, height=image_height, preserveAspectRatio=True)
        pdf.showPage()  # Agregar una nueva página antes de la imagen
    pdf.save()
    webbrowser.open_new_tab('Reporte_afd.pdf')

def reporte_afn():
    generarDOT_afn()
    w, h = A4
    pdf = canvas.Canvas("Reporte_afn.pdf", pagesize=A4)
    pdf.setTitle("Reporte de AFN")
    for element in informacion_afn:
        index = str(informacion_afn.index(element))
        text = pdf.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)
        text.textLine('Nombre: '+  element['nombre'])
        text.textLine("Estados: " + ','.join(element['estados']))
        text.textLine("Alfabeto: " + ','.join(element['alfabeto']))
        text.textLine("Estados Inicial: "+ element['estado inicial'])
        text.textLine("Estados de Aceptacion: "+ ','.join(element['estados de aceptacion']))
        text.textLine("Transiciones:")
        for datos in element['transciciones']:
            text.textLine(f'{datos[0]} , {datos[1]} ; {datos[2]}')
        text.textLine()
        pdf.drawText(text)
        text = "AFN generado con Graphviz"
        text_width = pdf.stringWidth(text, "Times-Roman", 12)
        pdf.drawCentredString(w / 2, h - 200, text)

        image_path = f'automatas/AFNPrueba{index}.png'
        image_width = 200
        image_height = 200
        image_x = (w - image_width) / 2
        image_y = h - 250 - image_height  # Adjust the vertical position as needed
        pdf.drawInlineImage(image_path, image_x, image_y, width=image_width, height=image_height, preserveAspectRatio=True)
        pdf.showPage()  # Agregar una nueva página antes de la imagen
    pdf.save()
    webbrowser.open_new_tab('Reporte_afn.pdf')
# Ventanas
def ventana_afn(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_crear = Button(frame_centrado, text='Crear AFN',
                         width=15, height=3, bd="4", command=mostrar_ventana_afn_crear)
    boton_crear.grid(row=1, column=0, padx=10, pady=10)
    boton_evaluar = Button(frame_centrado, text='Evaluar Cadena',
                           width=15, height=3, bd="4", command=mostrar_ventana_evaluar_afn)
    boton_evaluar.grid(row=2, column=0, padx=10, pady=10)
    boton_reporte = Button(frame_centrado, text='Generar Reporte',
                           width=15, height=3, bd="4", command=reporte_afn)
    boton_reporte.grid(row=3, column=0, padx=10, pady=10)
    boton_ayuda = Button(frame_centrado, text='Ayuda',
                         width=15, height=3, bd="4", command=mostrar_ventana_ayuda_afn)
    boton_ayuda.grid(row=4, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=5, column=0, padx=10, pady=10)
    return main_frame

def ventana_evaluar_afn(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo Evaluar AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_validar = Button(frame_centrado, text='Solo Validar',
                         width=15, height=3, bd="4", command=mostrar_ventana_validar_afn)
    boton_validar.grid(row=1, column=0, padx=10, pady=10)
    boton_ruta = Button(frame_centrado, text='Ruta',
                           width=15, height=3, bd="4", command=mostrar_ventana_ruta_afn)
    boton_ruta.grid(row=2, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=5, column=0, padx=10, pady=10)
    return main_frame

def ventana_afn_crear(master, callback=None, args=(), kwargs={}):
    global nombre_afn,estados_afn,alfabeto_afn,estado_inicial_afn,estados_aceptacion_afn,campo_transiciones_afn
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # saveEntry
    nombre_afn = StringVar()
    estados_afn = StringVar()
    alfabeto_afn = StringVar()
    estado_inicial_afn = StringVar()
    estados_aceptacion_afn = StringVar()

    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # Labels
    label = Label(frame_centrado, text="Modulo Crear AFN")
    label.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

    label1 = Label(frame_centrado, text="Nombre:")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    label2 = Label(frame_centrado, text="Estados:")
    label2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    label3 = Label(frame_centrado, text="Alfabeto:")
    label3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    label4 = Label(frame_centrado, text="Estado Inicial:")
    label4.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    label5 = Label(frame_centrado, text="Estados de Aceptación:")
    label5.grid(row=5, column=0, padx=10, pady=10, sticky="W")

    label6 = Label(frame_centrado, text="Transiciones:")
    label6.grid(row=6, column=0, padx=10, pady=10, sticky="W")
    # Entry box
    campo_nombre = Entry(frame_centrado, font=('Arial', 12), textvariable=nombre_afn)
    campo_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    campo_estados = Entry(frame_centrado, font=('Arial', 12), textvariable=estados_afn)
    campo_estados.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    campo_alfabeto = Entry(frame_centrado, font=('Arial', 12), textvariable=alfabeto_afn)
    campo_alfabeto.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    campo_estado_inicial = Entry(frame_centrado, font=('Arial', 12), textvariable=estado_inicial_afn)
    campo_estado_inicial.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    campo_estados_aceptacion = Entry(frame_centrado, font=('Arial', 12), textvariable=estados_aceptacion_afn)
    campo_estados_aceptacion.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    campo_transiciones_afn = Text(frame_centrado, font=('Arial', 12), height=10 , width=25) 
    campo_transiciones_afn.grid(row=6, column=1, padx=10, pady=10, sticky="E")

    # Boton Regresar
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,height=3, command=callback, bd="4")
    boton_regresar.grid(row=7, column=0, padx=10, pady=10)
    boton_aceptar = Button(frame_centrado, text='Aceptar', width=15,height=3, command=aceptar_afn, bd="4")
    boton_aceptar.grid(row=7, column=1, padx=10, pady=10)
    return main_frame

def ventana_afn_ayuda(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo Ayuda AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    imagen_ayuda = Image.open("imagenes/afn.png")
    imagen_ejemplo = Image.open("imagenes/ejemploafn.png")
    max_width = 600
    max_height = 250
    ajustada_ayuda = imagen_ayuda.resize((max_width,max_height-50), Image.ANTIALIAS)
    ajustada_ejemplo = imagen_ejemplo.resize((max_width,max_height-50), Image.ANTIALIAS)
    imagen_ayuda_tk = ImageTk.PhotoImage(ajustada_ayuda)
    imagen_ejemplo_tk = ImageTk.PhotoImage(ajustada_ejemplo)
    
    label_image = Label(frame_centrado, image=imagen_ayuda_tk)
    label_ejemplo = Label(frame_centrado, image=imagen_ejemplo_tk)
    label_image.grid(row=1, column=0)
    label_ejemplo.grid(row=2, column=0)
    
    # Mantén una referencia global a la imagen
    label_image.image = imagen_ayuda_tk
    label_ejemplo.image = imagen_ejemplo_tk
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_afd(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo AFD")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_crear = Button(frame_centrado, text='Crear AFD', width=15,height=3, bd="4", command=mostrar_ventana_afd_crear)
    boton_crear.grid(row=1, column=0, padx=10, pady=10)
    boton_evaluar = Button(frame_centrado, text='Evaluar Cadena',width=15, height=3, bd="4", command=mostrar_ventana_evaluar_afd)
    boton_evaluar.grid(row=2, column=0, padx=10, pady=10)
    boton_reporte = Button(frame_centrado, text='Generar Reporte',width=15, height=3, bd="4", command=reporte_afd)
    boton_reporte.grid(row=3, column=0, padx=10, pady=10)
    boton_ayuda = Button(frame_centrado, text='Ayuda',width=15, height=3, bd="4", command=mostrar_ventana_ayuda_afd)
    boton_ayuda.grid(row=4, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar',width=15, height=3, command=callback, bd="4")
    boton_regresar.grid(row=5, column=0, padx=10, pady=10)
    return main_frame

def ventana_evaluar_afd(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo Evaluar AFD")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_validar = Button(frame_centrado, text='Solo Validar',
                         width=15, height=3, bd="4", command=mostrar_ventana_validar_afd)
    boton_validar.grid(row=1, column=0, padx=10, pady=10)
    boton_ruta = Button(frame_centrado, text='Ruta',
                           width=15, height=3, bd="4", command=mostrar_ventana_ruta_afd)
    boton_ruta.grid(row=2, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=5, column=0, padx=10, pady=10)
    return main_frame


#Evaluador de cadenas
def verificar_cadena_en_afd(cadena, afd):
    imprimir = '************************************************'
    estado_actual = afd['estado inicial']
    for caracter in cadena:
        if caracter not in afd['alfabeto']:
            imprimir1 = f'\n\n\n\n\nEl caracter: {caracter}\n no está en el alfabeto del AFD:  {afd["nombre"]}'
            mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
            messagebox.showinfo(message=mensaje, title="Mensaje")
            return False

        transicion_encontrada = False
        for transicion in afd['transciciones']:
            if transicion[0] == estado_actual and transicion[1] == caracter:
                estado_actual = transicion[2]
                transicion_encontrada = True
                break

        if not transicion_encontrada:
            imprimir1 = f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AFD: '{afd['nombre']}'"
            mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
            messagebox.showinfo(message=mensaje, title="Mensaje")
            return False

    if estado_actual in afd['estados de aceptacion']:
        imprimir1 = f'La cadena {cadena} es válida en el AFD: {afd["nombre"]}'
        mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
        return messagebox.showinfo(message=mensaje, title="Mensaje")
    else:
        imprimir1 = f'La cadena {cadena} no es válida en el AFD: {afd["nombre"]}'
        mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75,' ') + imprimir.center(75, ' ') + '\n'
        return messagebox.showinfo(message=mensaje, title="Mensaje")


def verificar_cadena_en_afn(cadena,afn):
    imprimir = '************************************************'
    estado_actual = [afn['estado inicial']]

    for caracter in cadena:
        if caracter not in afn['alfabeto']:
            imprimir1 = f'El caracter: {caracter} no está en el alfabeto del AFN:  {afn["nombre"]}'
            mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
            messagebox.showinfo(message=mensaje, title="Mensaje")
            return False

        nuevas_transiciones = []

        for estado in estado_actual:
            for transicion in afn['transciciones']:
                estado_origen, simbolo, estado_destino = transicion

                if estado_origen == estado and (simbolo == caracter or simbolo == 'ε'):
                    if estado_destino not in nuevas_transiciones:
                        nuevas_transiciones.append(estado_destino)

        if not nuevas_transiciones:
            imprimir1 = f"No hay una transición definida para el estado(s) '{estado_actual}' y el caracter '{caracter}' en el AFN '{afn['nombre']}'"
            mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
            messagebox.showinfo(message=mensaje, title="Mensaje")
            return False

        estado_actual = nuevas_transiciones

        nuevas_transiciones_epsilon = []
        nuevas_transiciones_0 = []

        for estado in estado_actual:
            for transicion in afn['transciciones']:
                estado_origen, simbolo, estado_destino = transicion

                if estado_origen == estado and simbolo == 'ε':
                    if estado_destino not in nuevas_transiciones_epsilon:
                        nuevas_transiciones_epsilon.append(estado_destino)
                elif estado_origen == estado and simbolo == '0':
                    if estado_destino not in nuevas_transiciones_0:
                        nuevas_transiciones_0.append(estado_destino)

        estado_actual += nuevas_transiciones_epsilon

    # Realizar nuevas transiciones para los ceros ('0')
    for _ in range(len(estado_actual)):
        for estado in estado_actual:
            for transicion in afn['transciciones']:
                estado_origen, simbolo, estado_destino = transicion

                if estado_origen == estado and simbolo == '0':
                    if estado_destino not in estado_actual:
                        estado_actual.append(estado_destino)

    # Verificar si se acepta la cadena en algún estado de aceptación
    if any(estado in afn['estados de aceptacion'] for estado in estado_actual):
        imprimir1 = f"La cadena '{cadena}' es válida en el AFN '{afn['nombre']}'"
        mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
        messagebox.showinfo(message=mensaje, title="Mensaje")
        return True
    else:
        imprimir1 = f"La cadena '{cadena}' no es válida en el AFN '{afn['nombre']}'"
        mensaje = '\n\n\n\n\n' + imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ') + '\n'
        messagebox.showinfo(message=mensaje, title="Mensaje")
        return False

def crear_grafico_afn(afn):
    dot = graphviz.Digraph()
    dot.attr(rankdir='LR', size='8,5')

    dot.node('inicio', shape='point')

    for estado in afn['estados']:
        if estado in afn['estados de aceptacion']:
            dot.node(estado, shape='doublecircle')
        else:
            dot.node(estado)

    dot.edge('inicio', afn['estado inicial'])

    for transicion in afn['transciciones']:
        estado_origen, simbolo, estado_destino = transicion
        dot.edge(estado_origen, estado_destino, label=simbolo)

    dot.render('afn', format='png', view=False)

def graficar_afd(afd):
    dot = Digraph('AFD', format='png')
    dot.attr(rankdir='LR')
    dot.node('inicio', shape='point')

    dot.attr('node', shape='circle')
    
    for estado_aceptacion in afd['estados de aceptacion']:
        dot.node(estado_aceptacion, shape='doublecircle')
    if afd['estado inicial'] not in afd['estados de aceptacion']:
        dot.node(afd['estado inicial'], shape='circle', style='filled')
    
    for estado in afd['estados']:
        if estado != afd['estado inicial']:
            dot.node(estado)
    
    # Agregar flecha desde "inicio" al estado inicial
    dot.edge('inicio', afd['estado inicial'], style='dashed')
    
    for transicion in afd['transciciones']:
        origen = transicion[0]
        simbolo = transicion[1]
        destino = transicion[2]
        dot.edge(origen, destino, label=simbolo)
    
    dot.render('afd', format='png', view=False)

def crear_tabla_recorrido_afn(cadena, afn):
    estado_actual = [afn['estado inicial']]
    recorrido = []

    for caracter in cadena:
        nuevas_transiciones = []

        for estado in estado_actual:
            for transicion in afn['transciciones']:
                estado_origen, simbolo, estado_destino = transicion

                if estado_origen == estado and (simbolo == caracter or simbolo == 'ε'):
                    nuevas_transiciones.append(estado_destino)

        recorrido.append({
            'Caracter': caracter,
            'Estado Actual': estado_actual,
            'Nuevas Transiciones': nuevas_transiciones
        })

        estado_actual = nuevas_transiciones

    # Crear tabla HTML del recorrido
    table_html = '<html><head><style>table, th, td { border: 1px solid black; border-collapse: collapse; padding: 5px; }</style></head><body>'
    table_html += '<table>'
    table_html += '<tr><th>Caracter</th><th>Estado Actual</th><th>Nuevas Transiciones</th></tr>'

    for paso in recorrido:
        caracter = paso['Caracter']
        estado_actual = ','.join(paso['Estado Actual'])
        nuevas_transiciones = ','.join(paso['Nuevas Transiciones'])

        table_html += f'<tr><td>{caracter}</td><td>{estado_actual}</td><td>{nuevas_transiciones}</td></tr>'

    table_html += '</table>'
    table_html += '</body></html>'

    # Agregar gráfico del autómata
    crear_grafico_afn(afn)
    with open('recorrido_afn.html', 'w') as file:
        file.write(table_html)
        file.write(f'<br><p>Nombre Del Automata: {afn["nombre"]}</p>')
        file.write('<br><img src="afn.png" alt="Gráfico del Autómata">')

def obtener_camino_en_tabla_afd(cadena, afd, nombre_archivo):
    tabla_html = '<table style="border-collapse: collapse; width: 100%;">\n'
    tabla_html += '<tr><th style="border: 1px solid black; padding: 8px; text-align: center;">Estado Actual</th><th style="border: 1px solid black; padding: 8px; text-align: center;">Caracter</th><th style="border: 1px solid black; padding: 8px; text-align: center;">Estado Siguiente</th></tr>\n'
    
    estado_actual = afd['estado inicial']
    for caracter in cadena:
        if caracter not in afd['alfabeto']:
            return None

        transicion_encontrada = False
        for transicion in afd['transciciones']:
            if transicion[0] == estado_actual and transicion[1] == caracter:
                estado_siguiente = transicion[2]
                tabla_html += f'<tr><td style="border: 1px solid black; padding: 8px; text-align: center;">{estado_actual}</td><td style="border: 1px solid black; padding: 8px; text-align: center;">{caracter}</td><td style="border: 1px solid black; padding: 8px; text-align: center;">{estado_siguiente}</td></tr>\n'
                estado_actual = estado_siguiente
                transicion_encontrada = True
                break

        if not transicion_encontrada:
            return None

    if estado_actual in afd['estados de aceptacion']:
        tabla_html += '</table>'
        tabla_html += '</body></html>'
        graficar_afd(afd)
        try:
            with open(nombre_archivo, 'w') as file:
                file.write(tabla_html)
                file.write(f'<center><br><p>Nombre Del Automata: {afd["nombre"]}</p></center>')
                file.write('<center><br><img src="afd.png" alt="Gráfico del Autómata"></center>')
        except IOError:
            return None
        return nombre_archivo
    else:
        return None
#Funcion valifar afds
def validar_cadena_afd():
    afd_seleccionado = combo.get()
    for element in informacion_afd:
        indice = str(informacion_afd.index(element))
        if element['nombre'] == afd_seleccionado:
            afd_seleccionado = int(indice)
    verificar_cadena_en_afd(cadena.get(),informacion_afd[afd_seleccionado])

def validar_cadena_afn():
    afn_seleccionado = combo_afn.get()
    for element in informacion_afn:
        indice = str(informacion_afn.index(element))
        if element['nombre'] == afn_seleccionado:
            afn_seleccionado = int(indice)
    verificar_cadena_en_afn(cadena_afn.get(),informacion_afn[afn_seleccionado])

def validar_ruta_afd():
    afd_seleccionado = combo_ruta.get()
    for element in informacion_afd:
        indice = str(informacion_afd.index(element))
        if element['nombre'] == afd_seleccionado:
            afd_seleccionado = int(indice)
    bandera = verificar_cadena_en_afd(cadena_ruta.get(),informacion_afd[afd_seleccionado])#Aca
    if bandera:
        obtener_camino_en_tabla_afd(cadena_ruta.get(),informacion_afd[afd_seleccionado],'recorrido_afd.html')
        webbrowser.open_new_tab('recorrido_afd.html')

def validar_ruta_afn():
    afn_seleccionado = combo_ruta_afn.get()
    for element in informacion_afn:
        indice = str(informacion_afn.index(element))
        if element['nombre'] == afn_seleccionado:
            afn_seleccionado = int(indice)
    crear_tabla_recorrido_afn(cadena_ruta_afn.get(), informacion_afn[afn_seleccionado])
    bandera = verificar_cadena_en_afn(cadena_ruta_afn.get(), informacion_afn[afn_seleccionado])
    if bandera:
        crear_tabla_recorrido_afn(cadena_ruta_afn.get(), informacion_afn[afn_seleccionado])
        webbrowser.open_new_tab('recorrido_afn.html')
    # verificar_ruta_en_afn(ruta_afn.get(),informacion_afn[afn_seleccionado])

#Funcion mostrar AFD combobox
def mostrar_afd():
    global combo,cadena
    afd_nombres = []
    for element in informacion_afd:
        afd_nombres.append(element['nombre'])
    combo = ttk.Combobox(frame_validar,font=('Arial',10),state="readonly",values=afd_nombres)
    combo.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_validar, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='w')
    cadena = StringVar()
    entry_cadena = Entry(frame_validar,font=('Arial',12),justify="center",textvariable=cadena)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_validar = Button(frame_validar,text='Validar',width=15,height=3,command=validar_cadena_afd,bd="4")
    boton_validar.grid(row=2,column=2,padx=10,pady=10,sticky='w')
#Funcion mostrar AFN combobox
def mostrar_afn():
    global combo_afn,cadena_afn
    afn_nombres = []
    for element in informacion_afn:
        afn_nombres.append(element['nombre'])
    combo_afn = ttk.Combobox(frame_validar_afn,font=('Arial',10),state="readonly",values=afn_nombres)
    combo_afn.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_afn.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_validar_afn, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='w')
    cadena_afn = StringVar()
    entry_cadena = Entry(frame_validar_afn,font=('Arial',12),justify="center",textvariable=cadena_afn)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_validar = Button(frame_validar_afn,text='Validar',width=15,height=3,command=validar_cadena_afn,bd="4")
    boton_validar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

def mostrar_ruta_afd():
    global combo_ruta,cadena_ruta
    afd_nombres = []
    for element in informacion_afd:
        afd_nombres.append(element['nombre'])
    combo_ruta = ttk.Combobox(frame_ruta,font=('Arial',10),state="readonly",values=afd_nombres)
    combo_ruta.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_ruta, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='w')
    cadena_ruta = StringVar()
    entry_cadena = Entry(frame_ruta,font=('Arial',12),justify="center",textvariable=cadena_ruta)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_validar = Button(frame_ruta,text='Validar',width=15,height=3,command=validar_ruta_afd,bd="4")
    boton_validar.grid(row=2,column=2,padx=10,pady=10,sticky='w')
#Funcion mostrar AFN combobox
def mostrar_ruta_afn():
    global combo_ruta_afn,cadena_ruta_afn
    afn_nombres = []
    for element in informacion_afn:
        afn_nombres.append(element['nombre'])
    combo_ruta_afn = ttk.Combobox(frame_ruta_afn,font=('Arial',10),state="readonly",values=afn_nombres)
    combo_ruta_afn.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_ruta_afn.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_ruta_afn, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='w')
    cadena_ruta_afn = StringVar()
    entry_cadena = Entry(frame_ruta_afn,font=('Arial',12),justify="center",textvariable=cadena_ruta_afn)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_validar = Button(frame_ruta_afn,text='Validar',width=15,height=3,command=validar_ruta_afn,bd="4")
    boton_validar.grid(row=2,column=2,padx=10,pady=10,sticky='w')
#Ventanas
def ventana_validar_afd(master, callback=None, args=(), kwargs={}):
    global frame_validar, boton_regresar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_validar = Frame(main_frame, height=310, width=450)
    frame_validar.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_validar, text="Modulo Validar AFD")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_validar, text="Elija un AFD")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_validar,text='Mostrar AFDs',width=15,height=3,command=mostrar_afd,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar = Button(frame_validar, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_validar_afn(master, callback=None, args=(), kwargs={}):
    global frame_validar_afn,boton_regresar_afn
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_validar_afn = Frame(main_frame, height=310, width=450)
    frame_validar_afn.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_validar_afn, text="Modulo Validar AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_validar_afn, text="Elija un AFN")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_validar_afn,text='Mostrar AFNs',width=15,height=3,command=mostrar_afn,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_afn = Button(frame_validar_afn, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_afn.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_ruta_afd(master, callback=None, args=(), kwargs={}):
    global frame_ruta, boton_regresar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_ruta = Frame(main_frame, height=310, width=450)
    frame_ruta.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_ruta, text="Modulo ruta AFD")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_ruta, text="Elija un AFD")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_ruta,text='Mostrar AFDs',width=15,height=3,command=mostrar_ruta_afd,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar = Button(frame_ruta, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_ruta_afn(master, callback=None, args=(), kwargs={}):
    global frame_ruta_afn,boton_regresar_ruta_afn
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_ruta_afn = Frame(main_frame, height=310, width=450)
    frame_ruta_afn.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_ruta_afn, text="Modulo Ruta AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_ruta_afn, text="Elija un AFN")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_ruta_afn,text='Mostrar AFNs',width=15,height=3,command=mostrar_ruta_afn,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_ruta_afn = Button(frame_ruta_afn, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_ruta_afn.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_afd_crear(master, callback=None, args=(), kwargs={}):
    global nombre_afd,estados_afd,alfabeto_afd,estado_inicial_afd,estados_aceptacion_afd,campo_transiciones_afd
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # saveEntry
    nombre_afd = StringVar()
    estados_afd = StringVar()
    alfabeto_afd = StringVar()
    estado_inicial_afd = StringVar()
    estados_aceptacion_afd = StringVar()
    transiciones_afd = StringVar()

    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # Labels
    label = Label(frame_centrado, text="Modulo Crear AFD")
    label.grid(row=0, column=0, padx=10, pady=10,columnspan=2)

    label1 = Label(frame_centrado, text="Nombre:")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    label2 = Label(frame_centrado, text="Estados:")
    label2.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    label3 = Label(frame_centrado, text="Alfabeto:")
    label3.grid(row=3, column=0, padx=10, pady=10, sticky="W")

    label4 = Label(frame_centrado, text="Estado Inicial:")
    label4.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    label5 = Label(frame_centrado, text="Estados de Aceptación:")
    label5.grid(row=5, column=0, padx=10, pady=10, sticky="W")

    label6 = Label(frame_centrado, text="Transiciones:")
    label6.grid(row=6, column=0, padx=10, pady=10, sticky="W")
    # Entry box
    campo_nombre = Entry(frame_centrado, font=('Arial', 12), textvariable=nombre_afd)
    campo_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    campo_estados = Entry(frame_centrado, font=('Arial', 12), textvariable=estados_afd)
    campo_estados.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    campo_alfabeto = Entry(frame_centrado, font=('Arial', 12), textvariable=alfabeto_afd)
    campo_alfabeto.grid(row=3, column=1, padx=10, pady=10, sticky="E")

    campo_estado_inicial = Entry(frame_centrado, font=('Arial', 12), textvariable=estado_inicial_afd)
    campo_estado_inicial.grid(row=4, column=1, padx=10, pady=10, sticky="E")

    campo_estados_aceptacion = Entry(frame_centrado, font=('Arial', 12), textvariable=estados_aceptacion_afd)
    campo_estados_aceptacion.grid(row=5, column=1, padx=10, pady=10, sticky="E")

    campo_transiciones_afd = Text(frame_centrado, font=('Arial', 12), height=10 , width=25) 
    campo_transiciones_afd.grid(row=6, column=1, padx=10, pady=10, sticky="E")

    # Boton Regresar
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,height=3, command=callback, bd="4")
    boton_regresar.grid(row=7, column=0, padx=10, pady=10)

    boton_aceptar = Button(frame_centrado, text='Aceptar', width=15,height=3, command=aceptar_afd, bd="4")
    boton_aceptar.grid(row=7, column=1, padx=10, pady=10)
    return main_frame

def ventana_afd_ayuda(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo Ayuda AFN")
    label.grid(row=0, column=0, padx=10, pady=10)
    imagen_ayuda = Image.open("imagenes/afd.png")
    imagen_ejemplo = Image.open("imagenes/ejemploafd.png")
    max_width = 600
    max_height = 250
    ajustada_ayuda = imagen_ayuda.resize((max_width,max_height-50), Image.ANTIALIAS)
    ajustada_ejemplo = imagen_ejemplo.resize((max_width,max_height-50), Image.ANTIALIAS)
    imagen_ayuda_tk = ImageTk.PhotoImage(ajustada_ayuda)
    imagen_ejemplo_tk = ImageTk.PhotoImage(ajustada_ejemplo)
    
    label_image = Label(frame_centrado, image=imagen_ayuda_tk)
    label_ejemplo = Label(frame_centrado, image=imagen_ejemplo_tk)
    label_image.grid(row=1, column=0)
    label_ejemplo.grid(row=2, column=0)
    
    # Mantén una referencia global a la imagen
    label_image.image = imagen_ayuda_tk
    label_ejemplo.image = imagen_ejemplo_tk
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_oe(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Modulo OE")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_crear = Button(frame_centrado, text='Seleccionar AFD',
                         width=15, height=3, bd="4", command=None)
    boton_crear.grid(row=1, column=0, padx=10, pady=10)
    boton_reporte = Button(frame_centrado, text='Generar Reporte OE',
                           width=15, height=3, bd="4", command=None)
    boton_reporte.grid(row=2, column=0, padx=10, pady=10)
    boton_ayuda = Button(frame_centrado, text='Ayuda',
                         width=15, height=3, bd="4", command=None)
    boton_ayuda.grid(row=3, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=4, column=0, padx=10, pady=10)
    return main_frame

def ventana_crear(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Cargar Archivo")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_cargar_afd = Button(frame_centrado, text='Cargar AFD',
                              width=15, height=3, bd="4", command=cargar_AFD)
    boton_cargar_afd.grid(row=1, column=0, padx=10, pady=10)
    boton_cargar_afn = Button(frame_centrado, text='Cargar AFN',
                              width=15, height=3, bd="4", command=cargar_AFN)
    boton_cargar_afn.grid(row=2, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
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
    boton_cargar_afd = Button(frame_centrado, text='Cargar AFD',
                              width=15, height=3, bd="4", command=cargar_AFD)
    boton_cargar_afd.grid(row=1, column=0, padx=10, pady=10)
    boton_cargar_afn = Button(frame_centrado, text='Cargar AFN',
                              width=15, height=3, bd="4", command=cargar_AFN)
    boton_cargar_afn.grid(row=2, column=0, padx=10, pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

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
label = Label(miFrame, text='Lenguajes Formales y de Programacióñ | Sección: P | 201807086 | Nery Barrientos')
label.pack(side="top")
# frame Variable
miFrameV = Frame()
miFrameV.pack(fill="x")
miFrameV.place(x=0, y=25)
miFrameV.config(width=ancho_ventana, height=alto_ventana,relief="solid", bd="3")
# Funciones para ventanas en botones
var_ventana_afn = ventana_afn(ventana, mostrar_principal)
var_ventana_evaluar_afn = ventana_evaluar_afn(ventana,mostrar_ventana_afn)
var_ventana_validar_afn = ventana_validar_afn(ventana,mostrar_ventana_evaluar_afn)
var_ventana_ruta_afn = ventana_ruta_afn(ventana,mostrar_ventana_evaluar_afn)
var_ventana_ruta_afd = ventana_ruta_afd(ventana,mostrar_ventana_evaluar_afd)
var_ventana_afn_crear = ventana_afn_crear(ventana, mostrar_ventana_afn)
var_ventana_ayuda_afn = ventana_afn_ayuda(ventana,mostrar_ventana_afn)
var_ventana_afd = ventana_afd(ventana, mostrar_principal)
var_ventana_evaluar_afd = ventana_evaluar_afd(ventana,mostrar_ventana_afd)
var_ventana_validar_afd = ventana_validar_afd(ventana,mostrar_ventana_evaluar_afd)
var_ventana_afd_crear = ventana_afd_crear(ventana, mostrar_ventana_afd)
var_ventana_ayuda_afd = ventana_afd_ayuda(ventana,mostrar_ventana_afd)
var_ventana_oe = ventana_oe(ventana, mostrar_principal)
var_ventana_cargar_archivos = ventana_cargar(ventana, mostrar_principal)
# agregando Items a frame Variable
frame_centrado = Frame(miFrameV, height=310, width=450)
frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
boton_afn = Button(frame_centrado, text='AFN',width=10, height=3, bd="4", command=mostrar_ventana_afn)
boton_afn.grid(row=0, column=0, padx=10, pady=10)
boton_afd = Button(frame_centrado, text='AFD',width=10, height=3, bd="4", command=mostrar_ventana_afd)
boton_afd.grid(row=0, column=1, padx=10, pady=10)
boton_oe = Button(frame_centrado, text='OE',width=10, height=3, bd="4", command=mostrar_ventana_oe)
boton_oe.grid(row=1, column=0, padx=10, pady=10)
boton_cargar = Button(frame_centrado, text='Cargar Archivo', width=10,height=3, command=mostrar_ventana_cargar, bd="4")
boton_cargar.grid(row=1, column=1, padx=10, pady=10)
boton_salir = Button(frame_centrado, text='Salir', width=10,height=3, command=salir, bd="4")
boton_salir.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
# frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom", fill="x")
miFrame1.config(width="500", height="30", relief="solid", bd="3")