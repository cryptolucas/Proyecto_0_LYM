

"""Proyecto 0 LYM"""

#archivo = open("archivo.txt")

definiciones = {"defVar": "definicion_variable", "defProc": "definicion_procedure" }

simbolos = { "{": "open_bracket",    "}": "close_bracket",    "(":"open_parentesis",    ")": "close_parentesis",
            "()": "combined_parentesis",    ":" : "colon",    ";" : "semicolon",     "," : "coma"}



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
    
    
if 
    
    
       
        
            
    
print(isCommand(("  turn( left   )  ")))