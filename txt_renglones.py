import os
from URLSearchParams import URLSearchParams
#import pandas as pd
import requests
import urllib.parse

concatec = "https://"
i = 0
datos = []
subcadena = "/busqueda?q="

#Se abre el archivo de texto y se hace un arreglo de cada cadena para ser evaluada
with open("urlinfo.txt") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))

#Cada cadena va ser pasada al identificador del query string
for i in range(15006):
	verificador = subcadena in datos[i]
	if verificador == 1:
		url = concatec + datos[i]
		#Limpieza de texto 
		#url = url.replace('HTTP/1.1',"")
		url = url.replace('%22',"")
		#url = url.replace('%20'," ")
		#url = url.replace('200 4956',"")
		#url = url.replace('GET',"")
		#url = url.replace('"',"")
		#url = url.replace('-0600',"")
		url = url.replace('*',"")
		#url = url.replace('/busqueda?',"")
		#url = url.replace(']',"")
		#url = url.replace("/Feb","")
		#url = url.replace("/Mar","")
		
		#Obtienes todo
		#var = URLSearchParams(requests.utils.unquote(url)).getAll()

		#Obtienes solo q
		url = urllib.parse.unquote(url)
		var = URLSearchParams(url).get('q')
		print(var)

		file = open("url_07-03-2022.txt", "a")
		file.write(str(var) + '\n')
file.close()
