

"""Proyecto 0 LYM"""





lista_defprocs = []
numero_llaves_abiertas = 0
numero_llaves_cerradas = 0

lineas_archivo = 0
lineas_validas = 0




def isCommand (texto_n):
    
    Command = False
        
    if "jump" in texto_n:
        if texto_n[5].isdigit() and texto_n[7].isdigit():
            Command = True
            
    if "walk" in texto_n:
        if texto_n[5].isdigit():
            
            if (texto_n[5].isdigit())and (texto_n[6] == ")" ):
                Command = True
            
            if ("front" == texto_n[7:12]) or ("right" == texto_n[7:12]) or ("left" == texto_n[7:11]) or ("back" == texto_n[7:11]):
                Command = True
            
            if ("north" == texto_n[7:12]) or ("east" == texto_n[7:11]) or ("south" == texto_n[7:12]) or ("west" == texto_n[7:11]):
                Command = True
                
    if "leap" in texto_n:
        if texto_n[5].isdigit():
            
            if (texto_n[5].isdigit())and (texto_n[6] == ")" ):
                Command = True
            
            if ("front" == texto_n[7:12]) or ("right" == texto_n[7:12]) or ("left" == texto_n[7:11]) or ("back" == texto_n[7:11]):
                Command = True
            
            if ("north" == texto_n[7:12]) or ("east" == texto_n[7:11]) or ("south" == texto_n[7:12]) or ("west" == texto_n[7:11]):
                Command = True
                
    if "turn" in texto_n:
        if texto_n[5:9] == "left" or texto_n[5:10] == "right" or texto_n[5:11] == "around":
            Command = True
            
    if "turnto" in texto_n:
        if texto_n[7:12] == "north" or texto_n[7:11] == "east" or texto_n[7:12] == "south" or texto_n[7:11] == "west":
            Command = True
            
    if "drop" in texto_n:
        if texto_n[5].isdigit():
            Command = True
            
    if "get" in texto_n:
        if texto_n[4].isdigit():
            Command = True
        
    if "grab" in texto_n:
        if texto_n[5].isdigit():
            Command = True
            
    if "letGo" in texto_n:
        if texto_n[6].isdigit():
            Command = True
            
    if "nop()" in texto_n:
        Command = True
    
    return Command        
                
def isCondition(text):
    Condition = False
    
    
    if "facing(north)" in text or  "facing(east)" in text or  "facing(west)" in text or  "facing(south)" in text:
        Condition = True
        

    
    if "can" in text:
        donde_can = text.find("can")
        pos_comando = donde_can + 4
        palabra_comando = text[pos_comando:(pos_comando+12)]
        if isCommand(palabra_comando) == True:
            Condition = True 
            
    return Condition
    
    
def isValidControl (text):
    
    Valid_control = False
    
    if "if" in text:
        
        condicion = text[2:25]
    
        if isCondition(condicion) == True:
            
            if (  "{"  in text) and (  "}" in text):
                
                split1 = text.split("{")
                split2 = split1[1].split("}")
                comando = split2[0]
                
                
                if (isCommand(comando) == True) and ("else" in text):
                    
                    comando2 = text[(text.find("else")+4):(len(text))]
                    
                    if isCommand(comando2) == True:
                        Valid_control = True
                        
    
    if "while" in text:

        condicion2 = text[5:35]
        
        if isCondition(condicion2) == True:
          
            Valid_control = True
                    
                    
    if "repeat" in text and "times" in text and text[6].isdigit():
        
        if (  "{"  in text) and (  "}" in text):
            
            split7 = text.split("{")
            split8 = split7[1].split("}")
            comando4 = split8[0]
                
            if isCommand(comando4) == True:
                Valid_control = True
        
            
    return Valid_control



def isValidDefinition (text):
    
    Valid_definition = False
    
    if ("defVar" in text) and (text[len(text)-1].isdigit() == True):
        Valid_definition = True
    
    if ("defProc" in text) and ("(" in text) and (")" in text):
        Valid_definition = True
        x = text.split("c")
        z = x[1].split("(")
        nombre_defproc = z[0]
        lista_defprocs.append(nombre_defproc)
    
    return Valid_definition
        



with open("data/valido_1.txt", "r") as archivo:
    
    for linea in archivo:
        
        lineas_archivo += 1
        defproc_valido = False
        linea_n = linea.replace(" ", "")
        
        if linea_n == "{" or "{" in linea_n:
            numero_llaves_abiertas += 1
        
        if linea_n == "}" or "}" in linea_n:
            numero_llaves_cerradas += 1
        
        
        for defproc in lista_defprocs:
           if (defproc in linea_n) and ("defProc" not in linea_n):
               defproc_valido = True
                
        
        if ( (isCommand(linea_n) == True and linea_n[len(linea_n)-1] == ";" )  or (isValidControl(linea_n) == True)  or 
            (isValidDefinition(linea_n) == True) or (defproc_valido == True)  ):
            
            lineas_validas += 1
            
        if len(linea_n) == 1:
            lineas_validas += 1
            
            
 

lvalidas = lineas_validas        
larchivo = lineas_archivo
nabiertas = numero_llaves_abiertas
ncerradas = numero_llaves_cerradas
print(lvalidas)
print(larchivo)
print(nabiertas)
print(ncerradas)
try:
    if (nabiertas == ncerradas):
        lfinales = lvalidas + nabiertas + ncerradas   
    if (larchivo == lfinales+1): 
         print("Programa válido")
    else:
        print("Programa inválido")
except:
     if (nabiertas != ncerradas):
         print("Programa inválido")
                   

print(lfinales)

