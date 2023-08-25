

"""Proyecto 0 LYM"""

#archivo = open("archivo.txt")

definiciones = {"defVar": "definicion_variable", "defProc": "definicion_procedure" }



def isCommand (texto):
    Command = False
    texto_n = texto.replace(" ", "")
    
    if "jump" in texto_n:
        if texto_n[5].isdigit() and texto_n[7].isdigit():
            Command = True
            
    if "walk" in texto_n:
        if texto_n[5].isdigit():
            
            if ("front" == texto_n[7:12]) or ("right" == texto_n[7:12]) or ("left" == texto_n[7:11]) or ("back" == texto_n[7]):
                Command = True
            
            if ("north" == texto_n[7:12]) or ("east" == texto_n[7:11]) or ("south" == texto_n[7:12]) or ("west" == texto_n[7:11]):
                Command = True
                
    if "leap" in texto_n:
        if texto_n[5].isdigit():
            
            if ("front" == texto_n[7:12]) or ("right" == texto_n[7:12]) or ("left" == texto_n[7:11]) or ("back" == texto_n[7]):
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
        condicion = text[2:17]
    
        if isCondition(condicion) == True:
            
            if (  "{"  in text) and (  "}" in text):
                
                split1 = text.split("{")
                split2 = split1[1].split("}")
                comando = split2[0]
                
                if (isCommand(comando) == True) and ("else" in text) and text[text.find("else")+4] == "{" and  text[len(text)-1] == "}":
                    
                    split3 = text.split("{")
                    split4 = split3[2].split("}")
                    comando2 = split2[0]
                    
                    if isCommand(comando2) == True:
                        Valid_control = True
                        
    
    if "while" in text:

        condicion2 = text[2:17]
        
        if isCondition(condicion2) == True:
            
            if (  "{"  in text) and (  "}" in text):
                
                split5 = text.split("{")
                split6 = split5[1].split("}")
                comando3 = split6[0]
                
                if isCommand(comando3) == True:
                    Valid_control = True
                    
                    
    if "repeat" in text and "times" in text and text[6].isdigit():
        
        if (  "{"  in text) and (  "}" in text):
            
            split7 = text.split("{")
            split8 = split7[1].split("}")
            comando4 = split8[0]
                
            if isCommand(comando4) == True:
                Valid_control = True
        
            
                    
                    
                    
                    
                
                
            
            
            
    
    
       
        
            
    
print(isCommand(("  turn( left   )  ")))