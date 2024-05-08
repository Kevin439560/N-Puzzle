def caseBL():
    print("BL")
    
def caseBPI():
    print("BPI")
    
def caseBAW():
    print("BAW")
    
def caseBAM():
    print("BAM")
    
case = {
    1: caseBL,
    2: caseBPI,
    3: caseBAW,
    4: caseBAM
}

def switch(case):
    case.get(case, lambda: print("Caso inválido"))()