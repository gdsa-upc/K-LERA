# -*- coding: utf-8 -*-
import os #accedes al directorio de trabajo
from get_params import get_params #importa get_params de param

def build_database(params): # define la función y entramos param
    
    
    image_names = os.listdir(os.path.join(params['root'],params['database'],params['split'],'images')) # retorna una lista
# de imágenes, el os.path.join hace un conjunto de strings, params es un dictionary donde almacenamos variables(keys)
# donde tenemos root  (el directorio), database (nuestra base de datos), 'val'(archivo de la base de datos 
# con las imagenes), 

    file = open(os.path.join(params['root'],params['root_save'],params['image_lists'],params['split'] + '.txt'),'w')

#abrir un fichero que tenga el directorio, el directorio donde se guardará la lista de imágenes, rankings, kaggles, etc
# las imágenes +.txt al final, la w es para escribir en el archivo

    for imagname in image_names: #itera en la lista de image_names
        file.write(imagname + "\n") #guardamos la lista de imágenes
    file.close() #cerramos fichero

if __name__=="__main__":
    params = get_params()
    # Build image list for validation set
    build_database(params)
    
    # Switch to training set
    params['split'] = 'train'  
    
    # Build image list for training set
build_database(params)