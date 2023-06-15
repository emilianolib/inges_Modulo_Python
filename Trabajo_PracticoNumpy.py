#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[3]:


import numpy as np


# In[4]:


#ejercicio cero
#crear matriz y vectores
import numpy as np
matriz=np.array([[-2,-4,2],[-2,1,2],[4,2,5]])
matriz


# In[5]:


v1=np.array([[1],[1],[1]])
v1


# In[6]:


v2=np.array([[1],[2],[3]])
v2


# In[7]:


#ejercicio 1 
#norma cero
def norma_cero(vector):
    '''
    (numpy.ndarray)-> int
    Retorna el valor de la norma cero del vector, siendo este la cantidad de valores distintos a cero.
    >norma_cero(v2)
    3
    '''
    contador=np.count_nonzero(vector)
    return(contador)


# In[8]:


#verifico con v2
norma_cero(v2)


# In[17]:


from numpy.linalg import norm
def norma2_l1(vector):
    '''
    (numpy.ndarray)-> float
    Retorna el valor de la norma 1 del vector, siendo este la suma de las componentes del vector
    >norma2_l1(v2)
    6.0
    '''
    norma2_l1=norm(vector,1)
    return norma2_l1
    


# In[18]:


norma2_l1(v2)


# In[22]:


#norma l2
def norma_l2(vector):
    '''
    (numpy.ndarray)->float
    Retorna el valor de la norma 2 de un vector, siendo este la raíz de la suma de las componentes al cuadrado
    >norma_l2(v2)
    3.7416573867739413
    '''
    norma_l2=np.linalg.norm(vector)
    return norma_l2
  


# In[23]:


#verifico con v2
norma_l2(v2)


# In[26]:


#norma infinito
def norma_inf(vector):
    '''
    (numpy.ndarray)-> float
    Retorna el valor de la norma infinito de un vector, siendo este el valor máximo absoluto entre las componentes del mismo
    norma_inf(v2)
    3.0
    '''
    norma_inf=np.linalg.norm(vector,ord=np.inf)
    return norma_inf
    


# In[27]:


#verifico con v2
norma_inf(v2)


# In[28]:


#ejercicio 2
#primero, norma 2 de cada vector
#segundo,ordenar norma de mayor a menor
#matriz original ordenada
def ejercicio2(matriz):
    '''  
    (numpy.ndarray)-> numpy.ndarray
    Retorna la matriz ordenada segun la norma de sus vectores, de mayor a menor, y calcula la norma de los vectores fila.
    >ejercicio2(matriz)
    array([[ 4,  2,  5],
       [-2, -4,  2],
       [-2,  1,  2]])
    '''
    vector_normas=np.linalg.norm(matriz,axis=1)#calcula la norma 2 de cada fila
    normas_ord=np.argsort(vector_normas)[::-1]#ordena norma de mayor a menor
    matriz_ordenada=matriz[normas_ord]#reordeno filas de la matriz
    return(matriz_ordenada)


# In[29]:


ejercicio2(matriz)


# In[33]:


#ejercicio 3
#funcion que reste la media y divida por el desvio estandar de la matriz A, por columna.
#primero debo obtener la media
#segundo sacar el desvio estandar
#tercero matrizA-media/desvio
def ejercicio3(matriz):
    '''
    (numpy.ndarray)-> numpy.ndarray
    funcion que resta la media y divide por el desvio estandar de la matriz, por columna.
    >ejercicio3(matrizdeprueba)
        array[[-1.22474487 -1.22474487 -1.22474487]
     [ 0.          0.          0.        ]
     [ 1.22474487  1.22474487  1.22474487]]
    '''
    prom_matriz=np.mean(matriz,axis=0)#obtengo la media
    desvío=np.std(matriz, axis=0)#obtengo el desvío estándar
    resta = np.subtract(matriz, prom_matriz)
    matriz_final=np.divide(resta,desvío)
    #matriz_final=(matriz*prom_matriz)/desvío
    return matriz_final


# In[34]:


ejercicio3(matriz)


# In[41]:


matrizdeprueba=np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[42]:


ejercicio3(matrizdeprueba)


# In[ ]:




