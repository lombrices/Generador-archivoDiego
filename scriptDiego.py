import csv

def extrae_respuesta(respuesta):
    inicio = respuesta.find("['")
    fin = respuesta.find("']", inicio)
    primera_respuesta = respuesta[inicio + 2:fin]  
    # Agrega comillas dobles alrededor de la respuesta
    primera_respuesta = f'"{primera_respuesta}"'
    return primera_respuesta

with open("salida.csv", "r") as archivo_entrada, open("archivoDiego.csv", "w", newline='') as archivo_salida:
    lector = csv.reader(archivo_entrada)
    escritor = csv.writer(archivo_salida)
    
    # Leer y descartar la primera línea 
    next(lector)
    
    # Escribir los encabezados de las columnas
    escritor.writerow(["Codigo del ejercicio","Paso","Respuesta Correcta","Respuesta incorrecta 1","Pista respuesta incorrecta 1","Respuesta incorrecta 2","Pista respuesta incorrecta 2","Respuesta incorrecta 3","Pista respuesta incorrecta 3"])  # Ajusta las columnas según necesites

    # Recorremos las líneas del archivo
    for linea in lector:
        respuestaCorrectaStr = linea[8]
        if True:
            try:
                #Transformamos el campo respuestaCorrecta a un raw string para poder trabajar con las barras invertidas dobles
                respuestaCorrectaStr = respuestaCorrectaStr.replace("'", "r'",1)
                #Transformamos el string en una lista
                respuestaCorrecta = eval(respuestaCorrectaStr)
                
            #Esto es para el caso de que el campo respuesta Correcta este vacio
            except Exception as e:
                respuestaCorrecta=[""]
                
            if len(respuestaCorrecta) == 1:
                #En esta lista añadiremos lo que ira en una fila del archivo de salida
                lista=[]
                #Extraemos el codigo del ejercicio, el numero del paso y respuesta correcta
                codigoEjercicio=linea[0]
                lista.append(codigoEjercicio)
                paso=linea[3]
                lista.append(paso)
                
                respuestaCorrectaStr=f'"{respuestaCorrecta[0]}"'
                
                #Obtenemos las 3 respuestas incorrectas y cada una de sus pistas
                lista.append(respuestaCorrectaStr)
                resIncorrecta1=linea[10]
                pista1=linea[11]
                resIncorrecta2=linea[12]
                pista2=linea[13]
                resIncorrecta3=linea[14]
                pista3=linea[15]
                

                #En el caso de que haya una respuesta vacia, la dejamos tal cual y extraemos las otras respuestas
                if resIncorrecta3=='\"\"':
                    print("vacia")
                    resIncorrecta1=extrae_respuesta(resIncorrecta1)
                    resIncorrecta2=extrae_respuesta(resIncorrecta2)
                    resIncorrecta3='\"\"'

                else:
                    resIncorrecta1=extrae_respuesta(resIncorrecta1)
                    resIncorrecta2=extrae_respuesta(resIncorrecta2)
                    resIncorrecta3=extrae_respuesta(resIncorrecta3)

                lista.append(resIncorrecta1)
                lista.append(pista1)
                lista.append(resIncorrecta2)
                lista.append(pista2)
                lista.append(resIncorrecta3)
                lista.append(pista3)

                # Escribir en el archivo de salida
                escritor.writerow(lista)
            
        