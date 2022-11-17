# Paschos Eleftherios AM 4151 cs04151
import sys,os,copy

cimple_words= ["program","declare","if","else","while","switchcase","forcase","incase","case","default",
                   "not","and","or","function","procedure","call","return","in","inout","input","print"]

# alphabet
id_Tk = 'identifier'
num_Tk = 'number'
add_Tk = 'plus'
minus_Tk = 'minus'
program_Tk = 'program'
declare_Tk = 'declare'
if_Tk = 'if'
else_Tk = 'else'
while_Tk = 'while'
switchcase_Tk = 'switchcase'
forcase_Tk = 'forcase'
incase_Tk = 'incase'
case_Tk = 'case'
default_Tk = 'default'
not_Tk = 'not'
and_Tk = 'and'
or_Tk = 'or'
function_Tk = 'function'
procedure_Tk = 'procedure'
call_Tk = 'call'
return_Tk = 'return'
in_Tk = 'in'
inout_Tk = 'inout'
input_Tk = 'input'
print_Tk = 'print'
plus_Tk = 'plus'
minus_Tk = 'minus'
mul_Tk = 'multiply'
div_Tk = 'divide'
equals_Tk = 'equals'
great_Eq_Tk = 'greaterEquals'
great_Tk = 'greater'
less_Tk = 'less'
less_Eq_Tk = 'lessEquals'
diff_Tk = 'differ'
assignment_Tk = 'assignment'
coma_Tk = 'coma'
period_Tk = 'period'
colon_Tk = 'colon'
semi_Col_Tk = 'semiColon'
left_Paren_Tk = 'leftParenthesis'
right_Paren_Tk = 'rightParenthesis'
left_Brack_Tk = 'leftBracket'
right_Brack_Tk = 'rightBracket'
left_Curly_Brack_Tk = 'leftCurlyBracket'
right_Curly_Brack_Tk = 'rightCurlyBracket'
comment_Tk = 'comment'
eof_Tk = 'eof'
unavail_Tk = 'unavailable'
minus = "-"
star = "*"
plus = "+"
semiEquals = ":="
# Global Vars
global tokenString
tokenString = ''
global tokenType
tokenType = ''
global lineNo
lineNo = 1
global counter
counter =0
global myReads
myReads = ''
global myChar
myChar = ''
global quadList
quadList = []
global quadCounter
quadCounter = 1
global temp
temp = 0
global tempVars
tempVars =[]
global FuncOrProc
FuncOrProc = True
global scopeList
scopeList = []
global hasReturn
hasReturn= 0
global hasFunction
hasFunction= 0
global finalCounter
global finalQuadList
finalQuadList =[]
global relOps
relOps = {"=" :"beq","<>":"bne",">" :"bgt","<":"blt",">=":"bge","<=":"ble"}
global operators
operators = {"+":"add","-":"sub","*" :"mul","/":"div"}
global checkForPar
checkForPar=True
global argList
argList=[]
global parList
parList=[]

def validationAndBoundaryCheck(flag) :
    global myReads,myChar, tokenString, tokenType, counter, lineNo, size
    if (flag == 'fileSize') :
        if (counter > size):
            tokenString = 'FiledEnded'
            tokenType = eof_Tk
            return True
    if (flag == 'id') :
        if (counter > size):
            if tokenString in cimple_words:
                tokenType = tokenString
            else:
                tokenType = id_Tk
            counter += 1
            return True
    if (flag == 'num') :
        if (counter > size):
            tokenType = num_Tk
            counter += 1
            return True





def lex():
    global myReads,myChar,tokenString,tokenType,counter,lineNo,size
    tokenString = ''
    tokenType = ''


    if(validationAndBoundaryCheck('fileSize')) :
        return True
    myChar = myReads[counter]
    if (myChar == '\n') :
        lineNo +=1
    while(myChar.isspace()) :
        counter +=1
        if (validationAndBoundaryCheck('fileSize')) :
            return True
        myChar = myReads[counter]
        if (myReads[counter] == '\n'):
            lineNo += 1
    if (myChar.isalpha()) :
        tokenString += myChar
        counter += 1
        if (validationAndBoundaryCheck('id')) :
            return True
        while (myReads[counter].isalpha() or myReads[counter].isdigit()) :
            myChar = myReads[counter]
            tokenString += myChar
            counter += 1
            if (validationAndBoundaryCheck('id')):
                return True
        counter -=1
        if tokenString in cimple_words :
            tokenType = tokenString
        else :
            tokenType = id_Tk
        if (len(tokenString)>30) :
            tokenType = unavail_Tk
            print("Syntax Error in line: " + str(lineNo) + " Unavailable id\n")
            sys.exit()
        counter += 1
        return True
    elif (myChar.isdigit()) :
        tokenString += myChar
        counter += 1
        if (validationAndBoundaryCheck('num')):
            return True
        while (myReads[counter].isdigit()) :
            myChar = myReads[counter]
            tokenString += myChar
            counter += 1
            if (validationAndBoundaryCheck('num')):
                return True
        counter -= 1
        if (int(tokenString) > 4294967295.0):
            print("Syntax Error in line: " + str(lineNo) + " Forbidden Number\n")
            sys.exit()
        tokenType = num_Tk
        counter += 1
        return True
    elif (myChar == '+') :
        tokenString = myChar
        tokenType = plus_Tk
        counter +=1
        return True
    elif (myChar == '-') :
        tokenString = myChar
        tokenType = minus_Tk
        counter +=1
        return True
    elif (myChar == '*') :
        tokenString = myChar
        tokenType = mul_Tk
        counter +=1
        return True
    elif (myChar == '/') :
        tokenString = myChar
        tokenType = div_Tk
        counter +=1
        return True
    elif ( myChar == ',') :
        tokenString = myChar
        tokenType = coma_Tk
        counter += 1
        return True
    elif ( myChar == ';') :
        tokenString = myChar
        tokenType = semi_Col_Tk
        counter += 1
        return True
    elif (myChar == '(') :
        tokenString = myChar
        tokenType = left_Paren_Tk
        counter += 1
        return True
    elif (myChar == ')') :
        tokenString = myChar
        tokenType = right_Paren_Tk
        counter += 1
        return True
    elif (myChar == '[') :
        tokenString = myChar
        tokenType = left_Brack_Tk
        counter += 1
        return True
    elif (myChar == ']') :
        tokenString = myChar
        tokenType = right_Brack_Tk
        counter += 1
        return True
    elif (myChar == '{') :
        tokenString = myChar
        tokenType = left_Curly_Brack_Tk
        counter += 1
        return True
    elif (myChar == '}') :
        tokenString = myChar
        tokenType = right_Curly_Brack_Tk
        counter += 1
        return True
    elif (myChar == ':') :
        tokenString = myChar
        if (validationAndBoundaryCheck('fileSize')):
            return True
        nextChar = myReads[counter+1]
        if (nextChar == '=') :
            tokenString += nextChar
            tokenType = assignment_Tk
            counter+=2
            return True
        else :
            counter+=1
            tokenType = unavail_Tk
            return True
    elif (myChar == '=') :
        tokenString = myChar
        tokenType = equals_Tk
        counter +=1
        return True
    elif(myChar == '>') :
        tokenString = myChar
        if (validationAndBoundaryCheck('fileSize')):
            return True
        nextChar = myReads[counter + 1]
        if (nextChar == '=') :
            tokenString += nextChar
            tokenType = great_Eq_Tk
            counter += 2
            return True
        else:
            counter += 1
            tokenType = great_Tk
            return True
    elif(myChar == '<') :
        tokenString = myChar
        if (validationAndBoundaryCheck('fileSize')):
            return True
        nextChar = myReads[counter + 1]
        if (nextChar == '='):
            tokenString += nextChar
            tokenType = less_Eq_Tk
            counter += 2
            return True
        elif(nextChar == '>') :
            tokenString += nextChar
            tokenType = diff_Tk
            counter += 2
            return True
        else:
            counter += 1
            tokenType = less_Tk
            return True
    elif(myChar == '#'):
        counter +=1
        while (True) :
            if (validationAndBoundaryCheck('fileSize')):
                print("Syntax Error in line: " + str(lineNo) + " comments never closed.Program crashed in :" + myChar + "\n")
                sys.exit()
            if (myReads[counter] == '\n') :
                print("Syntax Error in line: " + str(lineNo) + " comments never closed.Program crashed in :" + myChar + "\n")
                sys.exit()
            if (myReads[counter] == '#'):
                counter += 1
                break
            counter += 1
        lex()
    elif(myChar == '.') :
        tokenString = myChar
        tokenType = period_Tk
        counter +=1
    else:
        print("Syntax Error in line: " + str(lineNo) +"Program crashed in : " + myChar + "\n")
        sys.exit()
class Argument():
    def __init__(self):
        self.name = ''
        self.type = 'Int'
        self.parameterType = ''

class Entity():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.variable = {"type": "Int", "offset": 0}
        self.subprogram = {"type": "", "startQuad": 0, "frameLength": 0, "argumentList": [],"nestingLevel":0,"argType": []}
        self.parameter = {"mode": "", "offset": 0}
        self.tempVar = {"type": "Int", "offset": 0}

class Scope():
    def __init__(self):
        self.name = ''
        self.entityList = []
        self.nestingLevel = 0

def addScope(name):
    nextScope = Scope()
    nextScope.name = name
    scopeList.append(nextScope)
    if (len(scopeList)>1):
        scopeList[-1].nestingLevel = scopeList[-2].nestingLevel +1

def deleteScope():
    del scopeList[-1]

def calculateOffset():
    counter = 0
    if (scopeList[-1].entityList != []):
        for entity in (scopeList[-1].entityList):
            if (entity.type == 'TEMP' or entity.type == 'VAR' or entity.type == 'PARAM'):
                counter += 1
    offset = 12 + (counter * 4)
    return offset

def checkIfExistsAlready(name):
    global scopeList
    for i in scopeList[-1].entityList:
        if (i.name==name):
            print("Syntax Error in line: " + str(lineNo) + " you cant use same name twice " + name + "\n")
            sys.exit()
    return True

def checkSubProgramPars(name,funcPars):
    scope, entity = searchIfExists(name)
    args=entity.subprogram["argumentList"]
    if len (funcPars) != len(args):
        return False
    tempList=[]
    for i in funcPars:
        if i == "CV":
            tempList.append("in")
        elif i == "REF":
            tempList.append("inout")
    tempList2=entity.subprogram["argType"]
    for i,j in zip(tempList,tempList2):
        if i != j :
            return False
    return True

def searchIfExists(name):
    global scopeList
    scope=scopeList[-1]
    j = 1
    while scopeList != []:
        for i in scope.entityList:
            if (i.name==name):
                return scope,i
        j += 1
        if (j > len(scopeList)):
           break
        scope = scopeList[-j]
    if name.isdigit():
        return "digit",name
    print("Syntax Error in line: " + str(lineNo) +" not found in symbol table : " + str(name)+" Program crashed in : " + myChar + "\n")
    sys.exit()

def searchArgName(argList,arg):
    counter=0
    for i in range(0,len(argList)):
        if arg.name == argList[i]:
            counter+=1
            if counter==2:
                return True
    return False

def symbolTable():
    print("=" * 80)
    scope = scopeList[-1]
    i=1
    while scopeList != []:
        print("Current Scope: "+scope.name+ " with nestingLevel:" + str(scope.nestingLevel))
        symbolFile.write("Current Scope: "+scope.name+ " with nestingLevel:" + str(scope.nestingLevel)+ "\n")
        print("Current Entities: ")
        symbolFile.write("Current Entities: "+ "\n")
        for entity in scope.entityList:
            if (entity.type == 'VAR'):
                print("Entity: " + entity.name + " type: " + entity.type +" offset: " + str(entity.variable["offset"]))
                symbolFile.write("Entity: " + entity.name + " type: " + entity.type +" offset: " + str(entity.variable["offset"])+ "\n")
            elif (entity.type == 'TEMP'):
                print("Entity: " + entity.name + " type: " + entity.type +" offset:" + str(entity.tempVar["offset"]))
                symbolFile.write("Entity: " + entity.name + " type: " + entity.type +" offset:" + str(entity.tempVar["offset"])+ "\n")
            elif (entity.type == 'SUBPR'):
                if (entity.subprogram["type"] == 'Function'):
                    print("Entity: " + entity.name + " type: " + entity.type + "Subprogram :"+entity.subprogram["type"] + " startQuad :" + str(entity.subprogram["startQuad"]) + " frameLength :" + str(entity.subprogram["frameLength"]))
                    symbolFile.write("Entity: " + entity.name + " type: " + entity.type + "Subprogram :"+entity.subprogram["type"] + " startQuad :" + str(entity.subprogram["startQuad"]) + " frameLength :" + str(entity.subprogram["frameLength"])+ "\n")
                    print("Function Arguments:")
                    symbolFile.write("Function Arguments:"+ "\n")
                    for arg in entity.subprogram["argumentList"]:
                        print("Argument : "+ arg.name + " type :" + arg.type + " parameterType :" + arg.parameterType)
                        symbolFile.write("Argument : "+ arg.name + " type :" + arg.type + " parameterType :" + arg.parameterType+ "\n")
                elif (entity.subprogram["type"] == 'Procedure'):
                    print("Entity: " + entity.name + " type: " + entity.type + " Subprogram: " +entity.subprogram["type"] + " startQuad: " + str(entity.subprogram["startQuad"]) + " frameLength :" + str(entity.subprogram["frameLength"]))
                    symbolFile.write("Entity: " + entity.name + " type: " + entity.type + " Subprogram: " +entity.subprogram["type"] + " startQuad: " + str(entity.subprogram["startQuad"]) + " frameLength :" + str(entity.subprogram["frameLength"])+ "\n")
                    print("Procedure Arguments:")
                    symbolFile.write("Procedure Arguments:"+ "\n")
                    for arg in entity.subprogram["argumentList"]:
                        print("Argument : "+ arg.name + " type :" + arg.type + " parameterType: " + arg.parameterType)
                        symbolFile.write("Argument : "+ arg.name + " type :" + arg.type + " parameterType: " + arg.parameterType+ "\n")
            elif (entity.type == 'PARAM'):
                print("Entity: " + entity.name + " type: " + entity.type + " mode: " + entity.parameter[
                    "mode"] + " offset: " + str(entity.parameter["offset"]))
                symbolFile.write("Entity: " + entity.name + " type: " + entity.type + " mode: " + entity.parameter[
                    "mode"] + " offset: " + str(entity.parameter["offset"])+ "\n")
        i+=1
        if(i>len(scopeList)):
            break
        scope = scopeList[-i]
    print("="*80)

def gnvlcode(name):
    global scopeList,asmFile
    scope,entity=searchIfExists(name)
    asmFile.write("lw $t0,-4($sp)\n")
    for i in range(0,(scopeList[-1].nestingLevel-scope.nestingLevel)-1):
        asmFile.write("lw $t0,-4($t0)\n")
    if (entity.type=="PARAM"):
        offset = entity.parameter["offset"]
    elif(entity.type=="VAR"):
        offset = entity.variable["offset"]
    asmFile.write("addi $t0,$t0,-"+str(offset)+"\n")

def loadvr(v,r):
    global scopeList,asmFile
    scope,entity=searchIfExists(v)
    if (scope=="digit"):
        asmFile.write("li $t"+str(r)+","+str(v)+"\n")
    elif(entity.type=="VAR"):
        if (scope.nestingLevel==0):
            asmFile.write("lw $t"+str(r)+",-"+str(entity.variable["offset"])+"($s0)"+"\n")
        elif(scope.nestingLevel==scopeList[-1].nestingLevel):
            asmFile.write("lw $t"+str(r)+",-"+str(entity.variable["offset"])+"($sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("lw $t"+str(r)+",($t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.nestingLevel == 0):
            asmFile.write("lw $t" + str(r) + ",-" + str(entity.tempVar["offset"]) + "($s0)" + "\n")
        elif(scope.nestingLevel==scopeList[-1].nestingLevel):
            asmFile.write("lw $t" + str(r) + ",-" + str(entity.tempVar["offset"]) + "($sp)" + "\n")
    elif(entity.type=="PARAM" and entity.parameter["mode"]=="CV"):
        if (scope.nestingLevel == scopeList[-1].nestingLevel):
            asmFile.write("lw $t" + str(r) + ",-" + str(entity.parameter["offset"]) + "($sp)" + "\n")
        elif (scope.nestingLevel < scopeList[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("lw $t" + str(r) + ",($t0)" + "\n")
    elif (entity.type == "PARAM" and entity.parameter["mode"] == "REF"):
        if (scope.nestingLevel == scopeList[-1].nestingLevel):
            asmFile.write("lw $t0,-"+ str(entity.parameter["offset"]) + "($sp)" + "\n")
            asmFile.write("lw $t"+str(r)+",($t0)"+"\n")
        elif (scope.nestingLevel < scopeList[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("lw $t0,($t0)\n")
            asmFile.write("lw $t"+str(r)+",($t0)"+"\n")

def storerv(r,v):
    global scopeList, asmFile
    scope, entity = searchIfExists(v)
    if(entity.type=="VAR"):
        if (scope.nestingLevel==0):
            asmFile.write("sw $t"+str(r)+",-"+str(entity.variable["offset"])+"($s0)"+"\n")
        elif(scope.nestingLevel==scopeList[-1].nestingLevel):
            asmFile.write("sw $t"+str(r)+",-"+str(entity.variable["offset"])+"($sp)"+"\n")
        else :
            gnvlcode(v)
            asmFile.write("sw $t"+str(r)+",($t0)"+"\n")
    elif(entity.type=="TEMP"):
        if (scope.nestingLevel == 0):
            asmFile.write("sw $t" + str(r) + ",-" + str(entity.tempVar["offset"]) + "($s0)" + "\n")
        elif(scope.nestingLevel==scopeList[-1].nestingLevel):
            asmFile.write("sw $t" + str(r) + ",-" + str(entity.tempVar["offset"]) + "($sp)" + "\n")
    elif(entity.type=="PARAM" and entity.parameter["mode"]=="CV"):
        if (scope.nestingLevel == scopeList[-1].nestingLevel):
            asmFile.write("sw $t" + str(r) + ",-" + str(entity.parameter["offset"]) + "($sp)" + "\n")
        elif (scope.nestingLevel < scopeList[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("sw $t" + str(r) + ",($t0)" + "\n")
    elif (entity.type == "PARAM" and entity.parameter["mode"] == "REF"):
        if (scope.nestingLevel == scopeList[-1].nestingLevel):
            asmFile.write("lw $t0,-"+ str(entity.parameter["offset"]) + "($sp)" + "\n")
            asmFile.write("sw $t"+str(r)+",($t0)"+"\n")
        elif (scope.nestingLevel < scopeList[-1].nestingLevel):
            gnvlcode(v)
            asmFile.write("lw $t0,($t0)\n")
            asmFile.write("sw $t"+str(r)+",($t0)"+"\n")

def genFinalCode():
    global quadList,scopeList,finalCounter,asmFile,checkForPar
    for i in range(len(quadList)):
        count = quadList[i][0]
        op = quadList[i][1]
        x = quadList[i][2]
        y = quadList[i][3]
        z = quadList[i][4]
        asmFile.write("L%d: \n" % (count))
        if(op=="jump"):
            asmFile.write("b L"+str(z)+"\n")
        elif (op in relOps):
            loadvr(x,1)
            loadvr(y,2)
            asmFile.write(relOps.get(op) + ",$t1,$t2, L"+str(z)+"\n")
        elif (op== ":="):
            loadvr(x,1)
            storerv(1,z)
        elif (op in operators):
            loadvr(x, 1)
            loadvr(y, 2)
            asmFile.write(operators.get(op) + ",$t1,$t1,$t2"+"\n")
            storerv(1, z)
        elif(op == "out"):
            asmFile.write("li $v0,1" + "\n")
            loadvr(x, 1)
            asmFile.write("move $a0,$t1" + "\n")
            asmFile.write("syscall" + "\n")
        elif (op == "inp"):
            asmFile.write("li $v0,5" + "\n")
            asmFile.write("syscall" + "\n")
            asmFile.write("move $t1,$v0" + "\n")
            storerv(1, x)
        elif (op == "retv"):
            loadvr(x, 1)
            asmFile.write("lw $t0,-8($sp)"+ "\n")
            asmFile.write("sw $t1,($t0)"+ "\n")
        elif (op == "par"):
            if (checkForPar == True):
                checkForPar=False
                for j in range(i,len(quadList)):
                    if (quadList[j][1] == "call"):
                        FuncOrProcName = str(quadList[j][2])
                        break
                scope,entity=searchIfExists(FuncOrProcName)
                asmFile.write("addi $fp, $sp,"+str(entity.subprogram["frameLength"])+ "\n")
                finalCounter=0
            if (y=="CV"):
                loadvr(x, 0)
                asmFile.write("sw $t0,-" + str(12 + 4 * finalCounter) + "($fp)\n")
                finalCounter+=1
            elif (y == "REF"):
                scope,entity=searchIfExists(x)
                if (scope.nestingLevel==scopeList[-1].nestingLevel):
                    if (entity.type=="VAR"):
                        asmFile.write("addi $t0,$sp,-"+str(entity.variable["offset"])+"\n")
                        asmFile.write("sw $t0,-"+str(12+4*finalCounter)+"($fp)\n")
                    elif (entity.type=="PARAM" and entity.parameter["mode"]=="CV"):
                        asmFile.write("addi $t0,$sp,-" + str(entity.parameter["offset"]) + "\n")
                        asmFile.write("sw $t0,-" + str(12 + 4 * finalCounter) + "($fp)\n")
                    elif (entity.type == "PARAM" and entity.parameter["mode"] == "REF"):
                        asmFile.write("lw $t0,-"+str(entity.parameter["offset"])+"($sp) \n")
                        asmFile.write("sw $t0,-" + str(12 + 4 * finalCounter) + "($fp) \n")
                elif(scope.nestingLevel<scopeList[-1].nestingLevel):
                        gnvlcode(x)
                        if(entity.type == "PARAM" and entity.parameter["mode"] == "REF"):
                            asmFile.write("lw $t0,($t0)\n")
                            asmFile.write("sw $t0,-"+str(12 + 4 * finalCounter)+"($fp)\n")
                        else:
                            asmFile.write("sw $t0,-" + str(12 + 4 * finalCounter) + "($fp)\n")
                finalCounter+=1
            elif (y == "RET"):
                scope,entity=searchIfExists(x)
                asmFile.write("addi $t0,$sp,-"+str(entity.tempVar["offset"])+"\n")
                asmFile.write("sw $t0,-8($fp)\n")
        elif (op == "call"):
            checkForPar=True
            scope, entity = searchIfExists(x)
            if (entity.subprogram["nestingLevel"]==scopeList[-1].nestingLevel):
                asmFile.write("lw $t0,-4($sp)\n")
                asmFile.write("sw $t0,-4($fp)\n")
            elif(scopeList[-1].nestingLevel<entity.subprogram["nestingLevel"]):
                asmFile.write("sw $sp,-4($fp)\n")
            asmFile.write("addi $sp,$sp,"+str(entity.subprogram["frameLength"])+"\n")
            asmFile.write("jal L"+str(entity.subprogram["startQuad"])+"\n")
            asmFile.write("addi $sp,$sp,-"+str(entity.subprogram["frameLength"])+"\n")
        elif(op=="begin_block" and scopeList[-1].nestingLevel!=0):
            asmFile.write("sw $ra,($sp)\n")
        elif (op == "end_block" and scopeList[-1].nestingLevel != 0):
            asmFile.write("lw $ra,($sp)\n")
            asmFile.write("jr $ra\n")
        elif (op == "begin_block" and scopeList[-1].nestingLevel == 0):
            asmFile.seek(0, os.SEEK_SET)
            asmFile.write("j L"+str(count)+"\n")
            asmFile.seek(0, os.SEEK_END)
            asmFile.write("addi $sp,$sp,"+str(calculateOffset())+"\n")
            asmFile.write("move $s0,$sp\n")
        elif (op == "halt"):
            asmFile.write("li $v0, 10\n")
            asmFile.write("syscall\n")
    quadList=[]

def program():
    lex()
    if (program_Tk == tokenType) :
        lex()
        if (id_Tk == tokenType) :
            myToken=tokenString
            lex()
            block(myToken)
            if(period_Tk == tokenType) :
                lex()
                if(eof_Tk == tokenType) :
                    lex()
                else :
                    print("Syntax Error in line: " + str(lineNo) + " Cimple does not support code after '.' Program crashed in : " + myChar + "\n")
            else:
                print("Syntax Error in line: " + str(lineNo) + " Period '.' expected Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " name of program expected Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        print("Syntax Error in line: " + str(lineNo) + " Keyword 'program' expected Program crashed in : " + myChar + "\n")
        sys.exit()


def block(name):
    global scopeList
    addScope(name)
    if scopeList[-1].nestingLevel > 0:
        for arg in scopeList[-2].entityList[-1].subprogram["argumentList"]:
            ent = Entity()
            ent.name = arg.name
            ent.type = 'PARAM'
            ent.parameter["mode"] = arg.parameterType
            ent.parameter["offset"] = calculateOffset()
            scopeList[-1].entityList.append(ent)
    declarations()
    subprograms()
    if scopeList[-1].nestingLevel > 0:
        scopeList[-2].entityList[-1].subprogram["startQuad"] = nextQuad()
    genQuad("begin_block",name,"_","_")
    statements()
    if(period_Tk==tokenType):
        genQuad("halt","_","_","_")
    else :
        scopeList[-2].entityList[-1].subprogram["frameLength"] = calculateOffset()
    genQuad("end_block", name, "_", "_")
    symbolTable()
    genFinalCode()
    deleteScope()
    print("Scope deleted.")



def declarations():
    while(declare_Tk==tokenType) :
        lex()
        varlist()
        if(semi_Col_Tk==tokenType) :
            lex()
        else :
            print("Syntax Error in line: " + str(lineNo) + " Never found semicolon ';' Program crashed in : " + myChar + "\n")
            sys.exit()

def varlist():
    global scopeList
    if(id_Tk==tokenType) :
        checkIfExistsAlready(tokenString)
        tempVars.append(tokenString)
        entity = Entity()
        entity.type = 'VAR'
        entity.name = tokenString
        entity.variable["offset"] = calculateOffset()
        scopeList[-1].entityList.append(entity)
        lex()
        while(coma_Tk==tokenType) :
            lex()
            if(id_Tk==tokenType) :
                checkIfExistsAlready(tokenString)
                tempVars.append(tokenString)
                entity = Entity()
                entity.type = 'VAR'
                entity.name = tokenString
                entity.variable["offset"] = calculateOffset()
                scopeList[-1].entityList.append(entity)
                lex()
            else :
                print("Syntax Error in line: " + str(lineNo) + " Never found ID after the ',' Program crashed in : " + myChar + "\n")
                sys.exit()
    else:
        pass

def subprograms():
    global FuncOrProc
    while(procedure_Tk==tokenType or function_Tk==tokenType):
        FuncOrProc = False
        subprogram()

def subprogram() :
    global hasReturn,hasFunction,scopeList,argList
    if (function_Tk==tokenType) :
        hasFunction+=1
        lex()
        if(id_Tk==tokenType) :
            checkIfExistsAlready(tokenString)
            myToken=tokenString
            entity = Entity()
            entity.type = 'SUBPR'
            entity.name = myToken
            entity.subprogram["type"] = 'Function'
            entity.subprogram["nestingLevel"]=scopeList[-1].nestingLevel +1
            scopeList[-1].entityList.append(entity)
            lex()
            if(left_Paren_Tk==tokenType) :
                lex()
                formalparlist()
                argList = []
                if(right_Paren_Tk==tokenType) :
                    lex()
                    block(myToken)
                    if (hasReturn!=1):
                        print("Syntax Error in line: " + str(lineNo) + " did not found return statement inside Function Program crashed in : " + myChar + "\n")
                        sys.exit()
                    else:
                        hasReturn=0
                else:
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " name 'Id' missing after function Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        lex()
        if (id_Tk == tokenType):
            myToken = tokenString
            checkIfExistsAlready(tokenString)
            entity = Entity()
            entity.type = 'SUBPR'
            entity.name = myToken
            entity.subprogram["type"] = 'Procedure'
            entity.subprogram["nestingLevel"] = scopeList[-1].nestingLevel + 1
            scopeList[-1].entityList.append(entity)
            lex()
            if (left_Paren_Tk == tokenType):
                lex()
                formalparlist()
                argList = []
                if (right_Paren_Tk == tokenType):
                    lex()
                    block(myToken)
                else:
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " name 'Id' missing after function Program crashed in : " + myChar + "\n")
            sys.exit()

def formalparlist():
    if (in_Tk == tokenType or inout_Tk == tokenType):
        formalparitem()
        while(coma_Tk==tokenType) :
            lex()
            if (in_Tk == tokenType or inout_Tk == tokenType):
                formalparitem()
    pass

argList=[]


def formalparitem():
    global argList
    if (in_Tk==tokenType or inout_Tk==tokenType) :
        inOrInout=tokenType
        lex()
        if(id_Tk==tokenType):
            arg = Argument()
            arg.name = tokenString
            argList.append(tokenString)
            if searchArgName(argList,arg):
                print("Syntax Error in line: " + str(lineNo) + " You cant use same parameter name  : " + tokenString + "\n")
                sys.exit()
            if (inOrInout==in_Tk):
                arg.parameterType = 'CV'
                scopeList[-1].entityList[-1].subprogram["argType"].append("in")
            else:
                arg.parameterType = 'REF'
                scopeList[-1].entityList[-1].subprogram["argType"].append("inout")
            scopeList[-1].entityList[-1].subprogram["argumentList"].append(arg)
            lex()
        else:
            print("Syntax Error in line: " + str(lineNo) + " name expected Program crashed in : " + myChar + "\n")
            sys.exit()

def statements():
    if(left_Curly_Brack_Tk==tokenType) :
        lex()
        statement()
        while(semi_Col_Tk == tokenType) :
            lex()
            statement()
        if(right_Curly_Brack_Tk==tokenType) :
            lex()
        else:
            print("Syntax Error in line: " + str(lineNo) + " '}' expected Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        statement()
        if(semi_Col_Tk == tokenType):
            lex()
        else:
            print("Syntax Error in line: " + str(lineNo) + " expected semicolon ';' after statement Program crashed in : " + myChar + "\n")
            sys.exit()

def statement():
    if(id_Tk==tokenType) :
        assignStat()
    elif(if_Tk==tokenType) :
        ifStat()
    elif(while_Tk==tokenType) :
        whileStat()
    elif(switchcase_Tk==tokenType) :
        switchcaseStat()
    elif(forcase_Tk==tokenType) :
        forcaseStat()
    elif(incase_Tk==tokenType) :
        incaseStat()
    elif(call_Tk==tokenType) :
        callStat()
    elif(return_Tk==tokenType) :
        returnStat()
    elif(input_Tk==tokenType) :
        inputStat()
    elif(print_Tk==tokenType) :
        printStat()
    else :
        pass

def assignStat() :
    if(id_Tk==tokenType) :
        myToken=tokenString
        scope,entity=searchIfExists(myToken)
        lex()
        if(assignment_Tk==tokenType) :
            lex()
            EPlace=expression()
            genQuad(semiEquals, EPlace, "_", myToken)
        else :
            print("Syntax Error in line: " + str(lineNo) + " expected assignment operator ':=' after name Program crashed in : " + myChar + "\n")
    else :
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()

def ifStat():
    if(if_Tk==tokenType) :
        lex()
        if(left_Paren_Tk==tokenType) :
            lex()
            CPlace=condition()
            backpatch(CPlace[0], nextQuad())
            if(right_Paren_Tk==tokenType) :
                lex()
                statements()
                ifList=makeList(nextQuad())
                genQuad("jump","_","_","_")
                backpatch(CPlace[1], nextQuad())
                elsepart()
                backpatch(ifList, nextQuad())
            else :
                print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else :
            print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
            sys.exit()
    else :
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()

def elsepart():
    if(else_Tk==tokenType) :
        lex()
        statements()
    else :
        pass

def whileStat():
    if(while_Tk==tokenType) :
        lex()
        if(left_Paren_Tk==tokenType) :
            lex()
            BQuad=nextQuad()
            CPlace=condition()
            backpatch(CPlace[0],nextQuad())
            if(right_Paren_Tk==tokenType) :
                lex()
                statements()
                genQuad("jump","_","_",BQuad)
                backpatch(CPlace[1], nextQuad())
            else:
                print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def switchcaseStat() :
    if(switchcase_Tk==tokenType) :
        lex()
        endList=emptyList()
        while(case_Tk==tokenType) :
            lex()
            if(left_Paren_Tk==tokenType) :
                lex()
                CPlace=condition()
                backpatch(CPlace[0], nextQuad())
                if(right_Paren_Tk==tokenType) :
                    lex()
                    statements()
                    w=makeList(nextQuad())
                    genQuad("jump","_","_","_")
                    endList=merge(endList,w)
                    backpatch(CPlace[1], nextQuad())
                else :
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else :
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        if(default_Tk==tokenType) :
            lex()
            statements()
            backpatch(endList,nextQuad())
        else :
            print("Syntax Error in line: " + str(lineNo) + " problem with 'Default' Program crashed in : " + myChar + "\n")
            sys.exit()
    else :
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def forcaseStat() :
    if (forcase_Tk == tokenType):
        lex()
        startQuad = nextQuad()
        while (case_Tk == tokenType):
            lex()
            if (left_Paren_Tk == tokenType):
                lex()
                CPlace=condition()
                backpatch(CPlace[0], nextQuad())
                if (right_Paren_Tk == tokenType):
                    lex()
                    statements()
                    genQuad("jump", "_", "_",startQuad)
                    backpatch(CPlace[1], nextQuad())
                else:
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis   misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        if (default_Tk == tokenType):
            lex()
            statements()
        else:
            print("Syntax Error in line: " + str(lineNo) + " problem with 'Default' Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()

def incaseStat() :
    if(incase_Tk==tokenType) :
        lex()
        w = newTemp()
        startQuad = nextQuad()
        genQuad(":=", "1", "_", w)
        while (case_Tk == tokenType):
            lex()
            if (left_Paren_Tk == tokenType):
                lex()
                CPlace=condition()
                backpatch(CPlace[0], nextQuad())
                if (right_Paren_Tk == tokenType):
                    lex()
                    statements()
                    genQuad(":=", "0", "_", w)
                    backpatch(CPlace[1], nextQuad())
                else:
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        genQuad("=", w,"0", startQuad)
    else:
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def returnStat() :
    global hasReturn,hasFunction
    if (return_Tk==tokenType) :
        hasReturn=1
        if hasFunction<0:
            print("Syntax Error in line: " + str(lineNo) + " found return outside of function Program crashed in : " + myChar + "\n")
            sys.exit()
        else:
            hasFunction-=1
        lex()
        if (left_Paren_Tk == tokenType):
            lex()
            EPlace=expression()
            if (right_Paren_Tk == tokenType):
                lex()
                genQuad("retv", EPlace, "_", "_")
            else:
                print("Syntax Error in line: " + str(lineNo) + " right parenthesis misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def callStat() :
    global parList
    if(call_Tk==tokenType) :
        lex()
        if(id_Tk==tokenType) :
            myToken=tokenString
            scope,entity=searchIfExists(myToken)
            if (entity.subprogram["type"] != "Procedure"):
                print("Syntax Error in line: " + str(lineNo) + " That's defined as Function or Variable you can only call Procedures : " + myToken + "\n")
                sys.exit()
            lex()
            if(left_Paren_Tk==tokenType) :
                lex()
                actualparlist()
                if checkSubProgramPars(myToken, parList):
                    genQuad("call",myToken,"_","_")
                    parList=[]
                else:
                    print("Syntax Error in line: " + str(lineNo) + " parameters dosent much in Procedure: " + myToken + "\n")
                    sys.exit()
                if(right_Paren_Tk==tokenType) :
                    lex()
                else:
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else :
            print("Syntax Error in line: " + str(lineNo) + " id missing after 'call' Program crashed in : " + myChar + "\n")
            sys.exit()
    else :
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def printStat() :
    if (print_Tk==tokenType) :
        lex()
        if (left_Paren_Tk == tokenType):
            lex()
            EPlace=expression()
            if (right_Paren_Tk == tokenType):
                lex()
                genQuad("out", EPlace, "_", "_")
            else:
                print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()


def inputStat() :
    if (input_Tk==tokenType) :
        lex()
        if (left_Paren_Tk == tokenType):
            lex()
            if(id_Tk==tokenType) :
                idPlace = tokenString
                lex()
                if (right_Paren_Tk == tokenType):
                    lex()
                    genQuad("inp",idPlace,"_","_")
                else :
                    print("Syntax Error in line: " + str(lineNo) + " right parenthesis  misisng Program crashed in : " + myChar + "\n")
                    sys.exit()
            else:
                print("Syntax Error in line: " + str(lineNo) + " id missing after 'input' Program crashed in : " + myChar + "\n")
                sys.exit()
        else :
            print("Syntax Error in line: " + str(lineNo) + " left parenthesis  misisng Program crashed in : " + myChar + "\n")
            sys.exit()
    else :
        print("Syntax Error in line: " + str(lineNo) + " \n")
        sys.exit()

def actualparlist() :
    if (in_Tk == tokenType or inout_Tk == tokenType):
        actualparitem()
        while(coma_Tk==tokenType) :
            lex()
            if (in_Tk == tokenType or inout_Tk == tokenType):
                actualparitem()
            else:
                print("Syntax Error in line: " + str(lineNo) + "expected in or inout Program crashed in : " + myChar + "\n")

def actualparitem() :
    global parList
    if(in_Tk==tokenType) :
        lex()
        EPlace=expression()
        genQuad("par", EPlace, "CV", "_")
        parList.append("CV")
    elif(inout_Tk==tokenType) :
        lex()
        if(id_Tk==tokenType) :
            myToken=tokenString
            scope,entity = searchIfExists(myToken)
            lex()
            genQuad("par", myToken, "REF", "_")
            parList.append("REF")
        else :
            print("Syntax Error in line: " + str(lineNo) + " id missing after 'inout' Program crashed in : " + myChar + "\n")
            sys.exit()
    else :
        print("Syntax Error in line: " + str(lineNo) + " Program crashed in : " + myChar + "\n")
        sys.exit()

def condition() :
    CPlace1=boolterm()
    C1True=CPlace1[0]
    C1False=CPlace1[1]
    while(or_Tk==tokenType) :
        lex()
        backpatch(C1False, nextQuad())
        CPlace2=boolterm()
        C2True=CPlace2[0]
        C2False=CPlace2[1]
        C1True=merge(C1True,C2True)
        C1False=C2False
    return [C1True,C1False]

def boolterm() :
    BPlace1=boolfactor()
    B1True = BPlace1[0]
    B1False = BPlace1[1]
    while(and_Tk==tokenType) :
        lex()
        backpatch(B1True,nextQuad())
        BPlace2=boolfactor()
        B2True = BPlace2[0]
        B2False = BPlace2[1]
        B1False=merge(B1False,B2False)
        B1True=B2True
    return [B1True,B1False]


def boolfactor() :
    if(not_Tk==tokenType) :
        lex()
        if(left_Brack_Tk==tokenType) :
            lex()
            CPlace=condition()
            if(right_Brack_Tk==tokenType) :
                lex()
                B1True=CPlace[1]
                B1False=CPlace[0]
            else:
                print("Syntax Error in line: " + str(lineNo) + " right bracket  missing Program crashed in : " + myChar + "\n")
                sys.exit()
        else:
            print("Syntax Error in line: " + str(lineNo) + " left bracket missing Program crashed in : " + myChar + "\n")
            sys.exit()
    elif(left_Brack_Tk==tokenType) :
            lex()
            CPlace=condition()
            if(right_Brack_Tk==tokenType) :
                lex()
                B1True = CPlace[0]
                B1False = CPlace[1]
            else:
                print("Syntax Error in line: " + str(lineNo) + " right bracket missing Program crashed in : " + myChar + "\n")
                sys.exit()
    else :
        EPlace1=expression()
        relOp=relationalOperator()
        EPlace2=expression()
        B1True=makeList(nextQuad())
        genQuad(relOp,EPlace1,EPlace2,"_")
        B1False = makeList(nextQuad())
        genQuad("jump","_","_","_")
    return [B1True,B1False]


def expression():
    osPlace=optionalSign()
    T1Place=term()
    #if (osPlace==minus):
    #    q=newTemp()
    #    genQuad(star, T1Place, "-1", q)
    #    T1Place=q
    while(plus_Tk==tokenType or minus_Tk==tokenType) :
        myToken=tokenString
        addOperator()
        T2Place=term()
        w=newTemp()
        genQuad(myToken, T1Place, T2Place, w)
        T1Place=w
    EPlace = T1Place
    return EPlace

def term():
    F1Place=factor()
    while(mul_Tk==tokenType or div_Tk==tokenType) :
        myToken=mulOperator()
        F2Place=factor()
        w=newTemp()
        genQuad(myToken,F1Place,F2Place,w)
        F1Place=w
    TPlace=F1Place
    return TPlace





def factor():
    global parList
    if(num_Tk==tokenType) :
        myToken=tokenString
        lex()
    elif(left_Paren_Tk==tokenType) :
        lex()
        EPlace=expression()
        if(right_Paren_Tk==tokenType) :
            myToken=EPlace
            lex()
        else :
            print("Syntax Error in line: " + str(lineNo) + " right parenthesis  missing Program crashed in : " + myChar + "\n")
            sys.exit()
    elif(id_Tk==tokenType) :
        myToken = tokenString
        scope,entity = searchIfExists(myToken)
        if entity.subprogram["type"] == "Procedure":
            print("\nSyntax Error in line: " + str(lineNo) +" You cant assign a procedure in a variable :" + tokenString +"\n")
            sys.exit()
        lex()
        myToken=idtail(myToken)
    else :
        print("Syntax Error in line: " + str(lineNo) + " Program crashed in : " + myChar + "\n")
        sys.exit()
    return myToken


def idtail(myId):
    global parList
    if(left_Paren_Tk==tokenType) :
        lex()
        actualparlist()
        w=newTemp()
        genQuad("par",w,"RET","_")
        if checkSubProgramPars(myId,parList):
            genQuad("call",myId,"_","_")
            parList=[]
        else:
            print("Syntax Error in line: " + str(lineNo) + "parameters dosent much in function: " + myId + "\n")
            sys.exit()
        if(right_Paren_Tk == tokenType) :
            lex()
            return w
        else:
            print("Syntax Error in line: " + str(lineNo) + " right parenthesis  missing Program crashed in : " + myChar + "\n")
            sys.exit()
    else:
        return myId

def optionalSign():
    if(add_Tk==tokenType or minus_Tk==tokenType) :
       return addOperator()
    else:
        return plus

def relationalOperator():
    if(equals_Tk==tokenType) :
        myToken=tokenString
        lex()
    elif(less_Eq_Tk==tokenType) :
        myToken = tokenString
        lex()
    elif (great_Eq_Tk == tokenType):
        myToken = tokenString
        lex()
    elif (great_Tk == tokenType):
        myToken = tokenString
        lex()
    elif (less_Tk == tokenType):
        myToken = tokenString
        lex()
    elif (diff_Tk == tokenType):
        myToken = tokenString
        lex()
    else:
        print("Syntax Error in line: " + str(lineNo) + " Program crashed in : " + myChar + "\n")
        sys.exit()
    return myToken

def addOperator():
    if(add_Tk==tokenType or minus_Tk == tokenType) :
        myToken = tokenString
        lex()
        return myToken
    else :
        print("Syntax Error in line: " + str(lineNo) + " Program crashed in : " + myChar + "\n")
        sys.exit()

def mulOperator():
    if(mul_Tk==tokenType or div_Tk==tokenType) :
        myToken=tokenString
        lex()
    return myToken


def nextQuad():
    global quadCounter
    return quadCounter

def genQuad(op, x, y, z):
    global quadList,quadCounter,finalQuadList,intFile

    tempList = []
    tempList+= [nextQuad()] +[op] + [x] + [y] + [z]
    quadCounter += 1
    quadList+=[tempList]
    finalQuadList+=[tempList]

def newTemp():
    global temp,tempVars,scopeList
    temp+=1
    tempVar="T_"+str(temp)
    tempVars.append(tempVar)
    entity = Entity()
    entity.type = 'TEMP'
    entity.name = tempVar
    entity.tempVar["offset"] = calculateOffset()
    scopeList[-1].entityList.append(entity)
    return tempVar

def emptyList():
    return []

def makeList(x):
    return [x]

def merge(list1,list2):
    return list1+list2

def backpatch(list,z):
    global quadList
    for i in list:
        for j in quadList:
            if(j[0]==i):
                j[4]=z
                break

fileName=os.path.basename(sys.argv[1])

if len(sys.argv) <= 1:
    sys.exit("Please give me a file.")
elif (fileName[-3:] != '.ci'):
    sys.exit("I need a '.ci' file,I am a Cimple compiler")
else:
    myFile = open(sys.argv[1])
myReads = myFile.read()
global size
size = int(len(myReads))-1
intFile=open(fileName[:-3]+'.int','w')
asmFile = open(fileName[:-3] + '.asm', 'w')
symbolFile = open(fileName[:-3] + '.txt', 'w')
asmFile.write('         \n\n\n\n\n')
program()


if(FuncOrProc):
    cFile = open(fileName[:-3] + '.c', 'w')
    cFile.write('#include <stdio.h>\n\nint main()\n{\n')
    cFile.write("\tint ")
    for i in tempVars[:-1]:
        cFile.write(str(i) + ",")
    cFile.write(str(tempVars[-1]) + ";\n")
    cFile.write("\t")
    for i in range(len(finalQuadList)):
        count = finalQuadList[i][0]
        op = finalQuadList[i][1]
        x = finalQuadList[i][2]
        y = finalQuadList[i][3]
        z = finalQuadList[i][4]
        label = i + 1
        if (op == "begin_block"):
            cFile.write("L_%d:  //(%s,%s,%s,%s)\n\t" % (count, op, x, y, z))
        elif (op == "+"):
            cFile.write("L_%d: %s=%s+%s; //(%s,%s,%s,%s)\n\t" % (count, z, x, y, op, x, y, z))
        elif (op == "-"):
            cFile.write("L_%d: %s=%s-%s; //(%s,%s,%s,%s)\n\t" % (count, z, x, y, op, x, y, z))
        elif (op == "*"):
            cFile.write("L_%d: %s=%s*%s; //(%s,%s,%s,%s)\n\t" % (count, z, x, y, op, x, y, z))
        elif (op == "/"):
            cFile.write("L_%d: %s=%s/%s; //(%s,%s,%s,%s)\n\t" % (count, z, x, y, op, x, y, z))
        elif (op == ":="):
            cFile.write("L_%d: %s=%s; //(%s,%s,%s,%s)\n\t" % (count, z, x, op, x, y, z))
        elif (op == "jump"):
            cFile.write("L_%d: goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, z, op, x, y, z))
        elif (op == "<"):
            cFile.write("L_%d: if (%s<%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == ">"):
            cFile.write("L_%d: if (%s>%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == "<="):
            cFile.write("L_%d: if (%s<=%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == ">="):
            cFile.write("L_%d: if (%s>=%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == "<>"):
            cFile.write("L_%d: if (%s!=%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == "="):
            cFile.write("L_%d: if (%s==%s) goto L_%d; //(%s,%s,%s,%s)\n\t" % (count, x, y, z, op, x, y, z))
        elif (op == "halt"):
            cFile.write("L_%d: //(%s,%s,%s,%s)\n} \n\t" % (count, op, x, y, z))
        elif (op == "out"):
            cFile.write("L_" + str(label) + ": " + "printf(\"" + x + "= %d\", " + x + ");\n\t")
        elif (op == "inp"):
            cFile.write("L_" + str(label) + ": " + "scanf(\"" + x + "= %d\",&"+ x + ");\n\t")

for i in finalQuadList:
    intFile.write(str(i[0])+": "+str(i[1])+" "+str(i[2])+" "+str(i[3])+" "+str(i[4])+"\n")
if(FuncOrProc):
    cFile.close()
intFile.close()
asmFile.close()
symbolFile.close()