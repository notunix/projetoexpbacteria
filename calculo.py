
class calculo:

    def __init__(self) -> None:
        pass

def calcula_bacterias(recurso):
    list =[1]
    numeroDeBacterias = 1
    quantum = 1
    num=recurso
    while(numeroDeBacterias>0):
        if(recurso>0):
            numeroDeBacterias = 2 ** quantum 
            #print('1-',numeroDeBacterias)
            list.append(numeroDeBacterias)
            quantum = quantum + 1
            recurso= recurso - 1
        elif(recurso==0):
            recurso=recurso-1
            for i in range(0,5):
                #print('2-',numeroDeBacterias)
                list.append(numeroDeBacterias)
        else:
            num=num-1
            numeroDeBacterias = int(numeroDeBacterias - 2**num)
            #print("3-",numeroDeBacterias)
            list.append(numeroDeBacterias)
    return list

def calcula_Max(recurso):
    numeroDeBacterias = 2**recurso
    return numeroDeBacterias

#print(calcula_bacterias(5))
#print('Maximo',calcula_Max(5))
