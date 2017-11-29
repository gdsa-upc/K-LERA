# -*- coding: utf-8 -*-


import numpy as np
import time
import sys
sys.path.insert(0,'/Users/andrea/Desktop/gdsa')
from get_params import get_params 
#añadir desde src funciona get_params de params.py

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
