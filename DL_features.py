# -*- coding: utf-8 -*-
#Pseudocódigo Deep Learning

''' 1) Leer una imágen de mxm
        im.read()
    2) hacerle un reshape para crear un vector transpuesto de m^2 píxels
        np.reshape()
    3) Declarar el modelo de keras que queramos usar.
        Modelo=get_alexnet([500,500],nº de lables, true)
    4)Pasar las imágenes de la base de datos diferenciando si son de train o val
        if train
            A.fit
        if val
            A.predict
    
    5) La función de get_alexnet nos sacará un vector con las probabilidades de cada "label".5)
    6) Habrá que normalizarlas con la función softmax
    7) Solo quedará mirar el valor más alto del vector para saber que tipo de imágen es.
    
    
    