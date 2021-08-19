from tkinter.filedialog import askopenfilename



chosen_option=""
route =""
original_text=""
course_name=""
parameters=""
shortener_text=""
lines=0
data=[]
numbers_data=[]
asc_data=[]
desc_data=[]
min_data2=[]
max_data=[]
apr_count=0
rep_count=0
avg=0


#Función que muestra en pantalla el menú principal, dicho menú nos dá 4 opciones a escoger.
def menu():
    print("===================Grades Control===================")
    print("|||1.Cargar Archivo                              |||")
    print("|||2.Mostrar reporte en consola                  |||")
    print("|||3.Exportar Reporte                            |||")
    print("|||4.Salir                                       |||")
    print("====================================================")
    print("")
    global chosen_option
    print("Seleccionar Una opción del menú presionando el número deseado: ")
    chosen_option=input()
    menu_actions(chosen_option)
    
    
# Función que recibe la ruta de un archivo.
def receive_document():
    global route
    route = askopenfilename()


# Función que lee el archivo mediante la ruta almacenada, muestra el texto en consola, para que la aplicación pueda funcionar N veces,
#Se inicializan nuevamente las variables globales.
def read_document():
    global route,original_text,chosen_option,data,asc_data,desc_data,rep_count,apr_count,avg
    asc_data=[]
    desc_data=[]
    data=[]
    apr_count=0
    rep_count=0
    avg=0
    archive = open(route,"r")
    original_text=archive.read()
    archive.close()
    route=""
    chosen_option=""
    print("")
    print("")
    print("El texto del documento recolectado es: ")
    print("===============================================")
    print(original_text)
    print("===============================================")
    print("")
    print("")
    course_name_search(original_text)
    parameters_search(original_text)
    text_shortener(original_text)


'''def read_document2():
    global route,original_text,chosen_option
    archive = open(route,"r")
    original_list=archive.readlines()
    archive.close()
    route=""
    chosen_option=0
    print("")
    print(original_list)
    course_name_search_2(original_list)
    parameters_search_2(original_list)
    text_shortener_2(original_list,lines_counter)'''

#Función donde buscamos el nombre de curso, que recibe como parametro el texto inicial
def course_name_search(text):
    global course_name
    for i in text:
        if i=="=":
            break
        else:
            course_name+=i
    print("")
    print("=====================================")
    print("El curso a evaluar es: ")
    print(course_name)
    print("=====================================")

'''def course_name_search_2(text):
    global course_name
    for i in text[0]:
        if i=="=":
            break
        else:
            course_name+=i
    print("")
    print("El curso a evaluar es: ")
    print(course_name)'''

#Función que busca los parametros del texto original, y los guarda en la variable global "parameters"
def parameters_search(text):
    text_length=len(text)
    a=text.find("}")
    global parameters
    parameters=text[a+1:text_length]
    parameters=parameters.strip()
    print("")
    print("=====================================")
    print("Los parámetros del análisis son: ")
    print(parameters)
    print("=====================================")

'''def parameters_search_2(text):
    global parameters,lines_counter
    count = 0
    for element in text:
        count += 1
    lines_counter=count-1
    for i in text[count-1]:
        if i!="}":
            parameters+=i
    print("Los parámetros del análisis son: ")
    print(parameters)'''

#Función que recibe como parámetro el texto original, y lo acorta, eliminando el nombre del curso y los símbolos extras:
def text_shortener(text):
    start=text.find("{")
    end=text.find("}")
    global shortener_text,lines
    shortener_text=text[start+2:end]
    not_required='"<>,\t""'
    for i in not_required:
        shortener_text = shortener_text.replace(i, '')
    print("")
    print("El texto sin simbolos es : ")
    print("===============================================")
    print(shortener_text)
    print("===============================================")
    lines=0
    students_counter(shortener_text)
    lists_creator(shortener_text)

'''def text_shortener_2(text,lines):
    text[0].remove
    text[lines].remove
    i=0
    not_required='"<>,;'
    for c in text[i-1]:
        for j in not_required:
            text = text[i-1].replace(j, '')
        i+=1

    print("")
    print("El texto sin simbolos es : ")
    print(text)
    lines=0
'''

#Función que nos permite contar las lineas del texto recortado, esto por consiguiente indica el número de estudiantes del curso
def students_counter(text):
    global lines
    for i in text:
        if i==("\n"):
            lines=lines+1
    print("")
    print("=====================================")
    print("El numero total de estudiantes es:")
    print(lines)
    print("=====================================")
    


'''def lists_creator(text):
    global data
    data=(text.split("\n"))
    data.remove("")
    print("")
    print("la data")
    print(data)'''


#Función que recibe como parámetro nuestro texto recortado y luego lo introduce en una lista.
def lists_creator(text):
    global data,asc_data,desc_data
    j=0
    interim=""
    for i in text:
        if i=="\n":
            data.append(interim.split(";"))
            data[j][0].strip()
            data[j][1].strip()
            data[j][1]=int(data[j][1])
            
            interim=""
            j+=1
        else: 
            interim+=i
    asc_data+=data
    desc_data+=data
    menu()

    #lists_separator(data)



'''def lists_separator(text):
    global names_data,numbers_data,data
    numbers_data=[int(temp)for temp in text.split() if temp.isdigit()]
    names_data=[temp for temp in text.split() if not temp.isdigit()]
    print("")
    print(numbers_data)
    print(names_data)'''



    
#Función que muestra las notas de manera descendente
'''def downward():
    global data
    data.sort(reverse = True, key=lambda x: x[1])
    print("====Reporte Notas de forma descendente====")
    print(*data,sep="\n")'''

#Función que muestra las notas de manera ascendente
'''def upward():
    global data
    data.sort(reverse = False, key=lambda x: x[1])
    print("====Reporte Notas de forma ascendente====")
    print(*data,sep="\n")'''

#Función que muestra las notas de manera ascendente
def upward():
    global asc_data
    i=0
    j=0
    print("")
    print ("====Reporte Notas Ascendentemente====")
    print("===========Estudiante / Nota==========")
    for k in range(len(asc_data)):
        print(asc_data[i][j]+" :"+" "+str(asc_data[i][j+1]))
        i+=1
    print("======================================")

#Función que muestra las notas desordenada
def messy_data():
    global data
    i=0
    j=0
    print("")
    print ("=====Reporte Notas Desordenadas======")
    print("===========Estudiante / Nota==========")
    for k in range(len(data)):
        print(data[i][j]+" :"+" "+str(data[i][j+1]))
        i+=1

#Función que muestra las notas de manera descendente
def downward():
    i=0
    j=0
    global desc_data
    print ("")
    print ("====Reporte Notas Descendentemente====")
    print("===========Estudiante / Nota==========")
    for k in range(len(desc_data)):
        print(desc_data[i][j]+" :"+" "+str(desc_data[i][j+1]))
        i+=1
    print("=======================================")



#Función que muestra el promedio de las notas obtenidas por los estudiantes del curso
def average():
    global data,avg
    i=1
    column = [fila[i] for fila in data]
    total_sum=0
    total_count=len(column)
    for j in column:
        total_sum = total_sum+ int(j)
    avg=float(total_sum/total_count)
    print("")
    print("======Reporte Promedio De Notas======")
    print("Suma total de notas: "+str(total_sum))
    print("Número de Notas: "+str(total_count))
    print("El promedio obtenido por los estudiantes del curso "+course_name+" es:")
    print(avg)
    print("======================================")
    

#Función que muestra la nota mínima obtenida, muestra el nombre del alumno y la nota obtenida
def min():
    global asc_data
    print ("")
    print("")
    print("=========Reporte Nota Mínima=========")
    print("La nota mínima fue obtenida por:")
    print("Estudiante  /  Nota obtenida")
    print(*asc_data[0])
    print("======================================")


#Función que muestra la nota máxima obtenida, muestra el nombre del alumno y la nota obtenida
def max():
    global desc_data
    print("")
    print("=========Reporte Nota Máximaa=========")
    print("Estudiante  /  Nota obtenida")
    print(*desc_data[0])
    print("======================================")
    

#Función que muestra el número de estudiantes que reprobaron el curso
def reprobate():
    global rep_count
    print("")
    print("=========Reporte Alumnos Reprobados=========")
    print("Los alumnos reprobados en el curso: ")
    print(rep_count)
    print("============================================")

    
#Función que muestra el número de estudiantes que aprobaron el curso
def passed():
    global apr_count
    print("")
    print("=========Reporte Alumnos Aprobados=========")
    print("Los alumnos aprobados en el curso: ")
    print(apr_count)
    print("===========================================")

#Función que recolecta el número de estudiantes que aprobaron el curso
def passed_counter():
    global data,apr_count

    promotion=61
    i=1
    column = [fila[i] for fila in data]
    for j in column:
        if int(j)>=promotion:
            apr_count+=1

#Función que recolecta el número de estudiantes que reprobaron el curso
def reprobate_counter():
    global data,rep_count
    promotion=61
    i=1
    column = [fila[i] for fila in data]
    for j in column:
        if not int(j)>=promotion:
            rep_count+=1

def asc_data_generator():
    global asc_data,desc_data
    length = len(asc_data)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if (asc_data[j][1] >= asc_data[j + 1][1]):
                interim = asc_data[j]
                asc_data[j]= asc_data[j + 1]
                asc_data[j + 1]= interim

def desc_data_generator():
    global desc_data
    length = len(desc_data)
    for i in range(0, length):
        for j in range(0, length-i-1):
            if (desc_data[j][1] < desc_data[j + 1][1]):
                interim = desc_data[j]
                desc_data[j]= desc_data[j + 1]
                desc_data[j + 1]= interim






#Función que verifica que parametros fueron recibidos para analizarlos y ejecutarlos
def parameters_verificator():
    global parameters,data
    asc_data_generator()
    desc_data_generator()
    reprobate_counter()
    passed_counter()
    print("")
    print("los parametros para los reportes son: "+parameters)
    messy_data()
    if parameters.count("ASC")>= 1:
        upward()
    else:
        print("")
        print("El reporte ASC no fue solicitado")

    if parameters.count("DESC")>= 1:
        downward()
        
    else:
        print("El reporte DESC no fue solicitado")

    if parameters.count("AVG")>= 1:
        average()
    else:
        print("El reporte AVG no fue solicitado")

    if parameters.count("MIN")>= 1:
        min()
    else:
        print("El reporte MIN no fue solicitado")

    if parameters.count("MAX")>= 1:
        max()
    else:
        print("El reporte MAX no fue solicitado")

    if parameters.count("APR")>= 1:
        passed()
    else:
        print("El reporte APR no fue solicitado")

    if parameters.count("REP")>= 1:
        reprobate()
    else:
        print("El reporte REP no fue solicitado")
    menu()



def html_verificator():
    global parameters
    print("")
    print("los parametros para los reportes HTML son: "+parameters)
    messy_html()
    if parameters.count("ASC")>= 1:
        upward_html()
    else:
        print("")
        print("El reporte ASC no fue solicitado")
    if parameters.count("DESC")>= 1:
        downward_html()
    else:
        print("El reporte DESC no fue solicitado")
    if parameters.count("AVG")>= 1:
        avg_html()
    else:
        print("El reporte AVG no fue solicitado")
    if parameters.count("MIN")>= 1:
        min_html()
    else:
        print("El reporte MIN no fue solicitado")
    if parameters.count("MAX")>= 1:
        max_html()
    else:
        print("El reporte MAX no fue solicitado")
    if parameters.count("APR")>= 1:
        apr_html()
    else:
        print("El reporte APR no fue solicitado")
    if parameters.count("REP")>= 1:
        rep_html()
    else:
        print("El reporte REP no fue solicitado")
    menu()
    


def upward_html():
    
    j=0
    global asc_data,course_name,apr_count,rep_count,lines
    i=0
    f = open('ASC.html','w')
    asc_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE DE NOTAS ASCENDENTEMENTE</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiante</th>
    <th>Nota Obtenida</th>
    </tr>"""
    for x in range(len(asc_data)-apr_count):
        asc_html+="""
        <tr>
        <td bgcolor= "#F9441D">"""+asc_data[i][j]+"""</td>
        <td bgcolor= "#F9441D">"""+str(asc_data[i][j+1])+"""</td>
        </tr>"""
        i+=1
    for x in range(len(asc_data)-rep_count):
        asc_html+="""
        <tr>
        <td bgcolor= "#1A86E2">"""+asc_data[i][j]+"""</td>
        <td bgcolor= "#1A86E2">"""+str(asc_data[i][j+1])+"""</td>
        </tr>"""
        i+=1
    
    asc_html+="""
    </table>
    </body>
    </html>"""
    f.write(asc_html)
    f.close()


def messy_html():
    
    j=0
    global data,course_name,apr_count,rep_count,lines
    i=0
    f = open('DESORDENADO.html','w')
    mess_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE DE NOTAS DESORDENADAS</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiante</th>
    <th>Nota Obtenida</th>
    </tr>"""
    for x in range(len(data)):
        if data[i][1]>=61:
            mess_html+="""
            <tr>
            <td bgcolor= "#1A86E2">"""+data[i][j]+"""</td>
            <td bgcolor= "#1A86E2">"""+str(data[i][j+1])+"""</td>
            </tr>"""
            i+=1
        else:
            mess_html+="""
            <tr>
            <td bgcolor= "#F9441D">"""+data[i][j]+"""</td>
            <td bgcolor= "#F9441D">"""+str(data[i][j+1])+"""</td>
            </tr>"""
            i+=1
    
    
    mess_html+="""
    </table>
    </body>
    </html>"""
    f.write(mess_html)
    f.close()  

def downward_html():
    i=0
    j=0
    global desc_data,course_name,apr_count,rep_count
    f = open('DESC.html','w')
    desc_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE DE NOTAS DESCENDENTEMENTE</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiante</th>
    <th>Nota Obtenida</th>
    </tr>"""
    for x in range(len(desc_data)-rep_count):
        desc_html+="""
        <tr>
        <td bgcolor= "#1A86E2">"""+desc_data[i][j]+"""</td>
        <td bgcolor= "#1A86E2">"""+str(desc_data[i][j+1])+"""</td>
        </tr>"""
        i+=1
    for x in range(len(desc_data)-apr_count):
        desc_html+="""
        <tr>
        <td bgcolor= "#F9441D">"""+desc_data[i][j]+"""</td>
        <td bgcolor= "#F9441D">"""+str(desc_data[i][j+1])+"""</td>
        </tr>"""
        i+=1
    desc_html+="""
    </table>
    </body>
    </html>"""
    f.write(desc_html)
    f.close() 
    

def min_html():
    global course_name,asc_data
    f = open('MIN.html','w')
    min_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE NOTA MINIMA</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiante</th>
    <th>Nota Obtenida</th>
    </tr>
    <tr>
    <td bgcolor= "#F9441D">"""+str(asc_data[0][0])+"""</td>
    <td bgcolor= "#F9441D">"""+str(asc_data[0][1])+"""</td>
    </tr>
    </table>
    </body>
    </html>"""
    f.write(min_html)
    f.close()  

def max_html():
    global desc_data,course_name
    f = open('MAX.html','w')
    max_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE NOTA MAXIMA</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiante</th>
    <th>Nota Obtenida</th>
    </tr>
    <tr>
    <td bgcolor= "1A86E2">"""+desc_data[0][0]+"""</td>
    <td bgcolor= "1A86E2">"""+str(desc_data[0][1])+"""</td>
    </tr>
    </table>
    </body>
    </html>"""
    f.write(max_html)
    f.close()  


def rep_html():
    global rep_count,course_name,lines
    f = open('REP.html','w')
    rep_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE ESTUDIANTES REPROBADOS</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiantes Totales</th>
    <th>Estudiantes Reprobados</th>
    </tr>
    <tr>
    <td bgcolor= "#F9441D">"""+str(lines)+"""</td>
    <td bgcolor= "#F9441D">"""+str(rep_count)+"""</td>
    </tr>
    </table>
    </body>
    </html>"""
    f.write(rep_html)
    f.close()  

def apr_html():
    global apr_count,course_name,lines
    f = open('APR.html','w')
    apr_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE ESTUDIANTES APROBADOS</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th>Estudiantes Totales</th>
    <th>Estudiantes APROBADOS</th>
    </tr>
    <tr>
    <td bgcolor= "1A86E2">"""+str(lines)+"""</td>
    <td bgcolor= "1A86E2">"""+str(apr_count)+"""</td>
    </tr>
    </table>
    </body>
    </html>"""
    f.write(apr_html)
    f.close()  


def avg_html():
    global course_name,avg
    f = open('AVG.html','w')
    avg_html ="""<html>
    <head></head>
    <body>
    <center>
    <h1>REPORTE PROMEDIO DEL CURSO</h1>
    </center>
    <style type="text/css" media="all">
    h1, h2 {display: inline;}
    </style>
    <h1> Curso: <h2 style="color:orange">"""+course_name+"""</h2> </h1>
    <hr />
    <center>
    <table width="500" border="2" cellpadding="5" >
    <tr>
    <th bgcolor= "1A86E2">Promedio</th>
    <th bgcolor= "1A86E2">"""+str(avg)+"""</th>
    </tr>
    </table>
    </body>
    </html>"""
    f.write(avg_html)
    f.close()  




#Función donde el usuario escoge que acción desea realizar.
def menu_actions(option):
    if option =="1":
        receive_document()
        read_document()
    elif option=="2":
        parameters_verificator()
    elif option=="3":
        html_verificator()
    elif option=="4":
        print("")
        print("Fue un gusto realizar los cálculos por usted, ven a utilizarme pronto :)")
        exit()
    else: 
        print("")
        print("=================================")
        print("Opción invalida, intente de nuevo")
        print("=================================")
        print("")
        menu()


menu()

