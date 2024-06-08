
############# APPNED ############
mi_lista = [1,2,3]
mi_lista.append(1)
print(mi_lista) # [1,2,3,4]
#################################

############# INSERT ############
mi_lista = [1,2,3]
mi_lista.insert(1,5)
print(mi_lista) # [1,5,2,3]
#################################

############# REMOVE ############
mi_lista = [1,2,3,2]
mi_lista.remove(2)
print(mi_lista) # [1,3,2]
#################################

############# POP #############
mi_lista = [1,2,3]
elemento = mi_lista.pop(1) # 2
print(mi_lista) # 2
print(mi_lista) # [1,3]
#################################

############# INDEX #############
mi_lista = [1,2,3,2]
indice = mi_lista.index(2) 
print(indice) # 1
#################################

############# SORT #############
mi_lista = [3,1,2]
mi_lista.sort() 
print(mi_lista) # [1,2,3]
#################################

############# REVERSE ###########
mi_lista = [1,2,3]
mi_lista.reverse() 
print(mi_lista) # [3,2,1]
#################################

############# CLEAR ############
mi_lista = [1,2,3]
mi_lista.clear() 
print(indice) # []
#################################