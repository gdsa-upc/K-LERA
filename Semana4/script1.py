# -*- coding: utf-8 -*-
import numpy as np
import time
import sys
sys.path.insert(0,'/Users/andrea/Desktop/gdsa')
from get_params import get_params 
from rank import rank
#añadir desde src funciona get_params de params.py
rank=rank()
get_params = get_params() 
#guardamos en params todos los parametros
print "Number of clusters:", get_params['descriptor_size']
print "Descriptor type:",get_params['descriptor_type']
print "Keypoint detector:", get_params['keypoint_type']
print "Resize dimension:", get_params['max_size']
print "Distance metric:", get_params['distance_type']


#descriptors=get_local_features() function semana pasada

import get_features as GF 
#añadir desde src

get_params['split'] = 'train' 
#solo imagenes de entrenamiento

t = time.time()
#t en segundos
X= GF.stack_features(get_params)
print 'Tiempo que ha tardado:', time.time() - t
print np.shape(X) 
#sacamos el num de descriptores y el num de imagenes ue hemos mirado (tupla de valores)

#codebook=train_codebook(,descriptors)

#usar MiniBatchKMeans, sale en la función
t = time.time()
GF.train_codebook(get_params,X) #funcion de get_features.py
#usamos los X descriptores de las imágenes de entrenamiento

print 'Tiempo que ha tardado:', time.time() - t


#gwt_assignments y build_bow

#sacamos las X a las imágenes de entrenamiento y validación
t = time.time()
GF.get_features(get_params)

print 'Tiempo que ha tardado:', time.time() - t

params['split'] = 'val' #imagenes de validacion

t = time.time()
# Run again
GF.get_features(get_params)

print 'Tiempo que ha tardado:', time.time() - t

t = time.time()
rank(get_params)

print 'Done. Time elapsed:', time.time() - t