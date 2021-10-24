#1752255
"""
 * @author nhphung
"""
from functools import reduce
from os import TMP_MAX, symlink
from typing import Dict
from unittest.case import skip
from main.mc.utils.AST import ArrayCell, ArrayPointerType, ArrayType, BoolType, BooleanLiteral, FloatType, FuncDecl, Id, IntType, StringType, VarDecl, VoidType
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt", MType([], IntType)),
    Symbol("putIntLn", MType([IntType], VoidType)),
    Symbol("putInt", MType([IntType], VoidType)),
    Symbol("getFloat", MType([], FloatType)),
    Symbol("putFloat", MType([FloatType], VoidType)),
    Symbol("putFloatLn", MType([FloatType], VoidType)),
    Symbol("putBool", MType([BoolType], VoidType)),
    Symbol("putBoolLn", MType([BoolType], VoidType)),
    Symbol("putString", MType([StringType], VoidType)),
    Symbol("putStringLn", MType([StringType], VoidType)),
    Symbol("putLn", MType([], VoidType))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def flatCgetSymbol(self, c):
        lst = []
        for ele in c:
            if type(ele) is list:
                for i in ele:
                    lst.append(i)
            else:
                lst.append(ele)
        return lst

    def visitProgram(self, ast,c):        
        lst = [x for x in c]
        for mem in ast.decl:    
            lst.insert(0,self.visit(mem,lst))
        lst = [lst]     
      
        checkList = []
        for ele in lst:
            if type(ele) is list:
                for i in ele:
                    if type(i) is Symbol and type(i.mtype) is MType:
                        checkList.append(i.name)
            elif type(ele) is Symbol and type(ele.mtype) is MType:
                checkList.append(ele.name)

        if 'main' not in checkList:
            raise NoEntryPoint()

        for x in ast.decl:            
            if type(x) is FuncDecl:             
                self.visit(x, lst)

        checkReach = self.flatCgetSymbol(lst)
        for ele in checkReach:
            if type(ele) is Symbol and type(ele.mtype) is MType:
                if ele.name in ["getInt","putIntLn","putInt", 
                "getFloat","putFloat","putFloatLn","putBool", "putBoolLn",
                "putString","putStringLn","putLn","main"]:
                    continue
                elif ele.name not in checkReach :
                    raise UnreachableFunction(ele.name)
        return lst

    def visitVarDecl(self, ast, c):  
        temp = []
        if c and type(c[0]) is list:
            temp = c[0]
        else:
            temp = c
        for sym in temp:
            if type(sym) is Symbol and ast.variable == sym.name:
                raise Redeclared(Variable(), ast.variable)
        varType = self.visit(ast.varType,c)
        return Symbol(ast.variable, varType)

    
    def visitFuncDecl(self, ast, c):  
        paraLst = []
        for para in ast.param:
            try:
                #should insert 0 ?
                paraLst = paraLst + [self.visit(para, paraLst)]
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)

        funcType = self.visit(ast.returnType, c)        
        parType = [mem.mtype for mem in paraLst]
        funcDecl =  Symbol(ast.name.name, MType(parType, funcType))           

        if c and type(c[0]) is not list:
            for symbol in c:
                if type(symbol) is Symbol and symbol.name == ast.name.name:
                    raise Redeclared(Function(), ast.name.name)
            return funcDecl
        else:       
            c.insert(0,paraLst)            
            c[0].insert(0,ast.name.name)
            for mem in ast.body.member:           
                c[0].insert(0,self.visit(mem,c))
            flag = True
            for ele in c[0]:
                if type(ele) is str and ele == 'isReturn' :
                    flag = False
            if flag and ast.name.name != 'main' and type(funcType) is not VoidType:
                raise FunctionNotReturn(ast.name.name)            
            c.pop(0)
            

    def visitBlock(self, ast, c):                  
        localScope = c
        localScope.insert(0,[])
        for x in c[1]:
            if type(x) is str and x == 'isLoop':
                localScope[0].insert(0,'isLoop')
        for mem in ast.member:
            #should insert 0 ?
            localScope[0].insert(0,self.visit(mem, localScope))   
        localScope.pop(0)
                
    def visitReturn(self, ast, c):
        funcSym = None
        funcName = ''
        funcSym = None
        for localPara in c[-2]:
            if type(localPara) is str:
                funcName = localPara
        for outsideSym in c[-1]:
            if type(outsideSym) is Symbol and outsideSym.name == funcName:
                funcSym = outsideSym
        returnType = funcSym.mtype.rettype
        if ast.expr:            
            exp = self.visit(ast.expr,c)       
            if type(returnType) is VoidType:
                raise TypeMismatchInStatement(ast)
            if type(returnType) is FloatType and (type(exp) is FloatType or type(exp) is IntType):
                c[0].insert(0,'isReturn')
                return
            if type(returnType) is ArrayPointerType:
                if type(exp) is not ArrayPointerType and type(exp) is not ArrayType:       
                    raise TypeMismatchInStatement(ast)
                else:
                    if type(returnType.eleType) is not type(exp.eleType):
                        raise TypeMismatchInStatement(ast)
            elif type(returnType) is not type(exp):
                raise TypeMismatchInStatement(ast)
        elif type(returnType) is not VoidType:
            raise TypeMismatchInStatement(ast)     
        c[0].insert(0,'isReturn')

    def visitCallExpr(self, ast, c): 
        flatC = []
        actualParameters = []
        formalParameters = []
        funcCall = None
        for x in c:
            if type(x) is list:
                for y in x:
                    if type(y) is Symbol:
                        flatC.append(y)
            elif type(x) is Symbol:
                flatC.append(x)
        nameInC = [ele.name for ele in flatC] 

        if ast.method.name not in nameInC:
            raise Undeclared(Function(),ast.method.name)
        else:
            for x in flatC:
                if ast.method.name == x.name:
                    funcCall = x
                    formalParameters = x.mtype.partype
        for expr in ast.param:
            actualParameters.append(self.visit(expr, c))

        if len(formalParameters) != len(actualParameters):
            raise TypeMismatchInExpression(ast)

        check_list = list(zip(formalParameters,actualParameters))
        
        for para in check_list:
            if type(para[0]) is ArrayPointerType and type(para[1]) in [ArrayPointerType, ArrayType]:
                if type(para[0].eleType) is not type(para[1].eleType):
                    raise TypeMismatchInExpression(ast)
                else:
                    continue
            elif type(para[0]) is not type(para[1]):
                if type(para[0]) is FloatType and type(para[1]) is IntType:
                    continue
                else:
                    raise TypeMismatchInExpression(ast)
        #append name of function to marked it reached        
        c[-1].append(funcCall.name)
        return funcCall.mtype.rettype
        

    def visitId(self, ast ,c):
        flatC = []
        for x in c:
            if type(x) is list:
                for i in x:
                    if type(i) is Symbol:
                        flatC.append(i)
            elif type(x) is Symbol:
                flatC.append(x)

        nameInC = [ele.name for ele in flatC]

        if ast.name not in nameInC:
            raise Undeclared(Identifier(), ast.name)
        res = self.lookup(ast.name, flatC, lambda x:x.name)
        return res.mtype

    def visitIf(self, ast,c):
        v = self.visit(ast.expr,c)
        if type(v) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if ast.thenStmt:        
            self.visit(ast.thenStmt,c)
        if ast.elseStmt:
            self.visit(ast.elseStmt,c)
        return

    def visitFor(self, ast,c):
        expr1 = self.visit(ast.expr1,c)
        expr2 = self.visit(ast.expr2,c)
        expr3 = self.visit(ast.expr3,c)
        if type(expr1)  is not IntType or type(expr3) is not IntType or type(expr2) is not BoolType:
            raise TypeMismatchInStatement(ast)

        c.insert(0,['isLoop'])
        self.visit(ast.loop, c) 
        c.pop(0)

    def visitDowhile(self, ast,c):
        lstStmt = c
        lstStmt.insert(0,['isLoop'])
        for stmt in ast.sl:
            lstStmt[0].insert(0,self.visit(stmt,lstStmt))
        
        expr = self.visit(ast.exp,lstStmt)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        lstStmt.pop(0)

        
    def visitBreak(self, ast, c):
        for y in c[0]:
            if type(y) is str and y == 'isLoop':
                return
        raise BreakNotInLoop()
    
    def visitContinue(self, ast,c):
        for y in c[0]:
            if type(y) is str and y == 'isLoop':
                return
        raise ContinueNotInLoop()


    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        exp = self.visit(ast.idx, c)

        if type(exp) is not IntType or (type(arr) not in [ArrayType, ArrayPointerType]):
            raise TypeMismatchInExpression(ast)
        return arr.eleType

    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if ast.op == '=':
            if type(ast.left) is not Id and type(ast.left) is not ArrayCell:
                raise NotLeftValue(ast.left)
            if type(left) in [VoidType, ArrayType, ArrayPointerType]:
                raise TypeMismatchInExpression(ast)
            elif type(left) is FloatType:
                if type(right) not in [IntType, FloatType]:
                    raise TypeMismatchInExpression(ast)
            elif type(left) is not type(right):
                raise TypeMismatchInExpression(ast)
            else:
                return left
        elif ast.op in ['!', '&&', '||']:
            if type(left) is not BoolType or type(right) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return left
        elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
            if ast.op in ['==', '!=']:
                if type(left) is not type(right):
                    raise TypeMismatchInExpression(ast)
                else:
                    return BoolType()
            elif type(left) not in[IntType, FloatType] or type(right) not in[IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()
        elif ast.op in ['+', '-', '*', '/', '%']:
            if ast.op == '%':
                if type(left) is not IntType or type(right) is not IntType:
                    raise TypeMismatchInExpression(ast)
                else:
                    return IntType()
            elif type(left) in [IntType, FloatType] and type(right) in [IntType, FloatType]:
                if type(left) is IntType and type(right) is IntType:
                    return IntType()
                else:
                    return FloatType()
            else:
                raise TypeMismatchInExpression(ast)           
    
    def visitUnaryOp(self, ast,c):
        body = self.visit(ast.body,c)
        if (ast.op == '!' and type(body) is not BoolType) or (ast.op == '-' and type(body) not in [IntType, FloatType]):
            raise TypeMismatchInExpression(ast)
        return body

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitBooleanLiteral(self,ast, c): 
        return BoolType()

    def visitStringLiteral(self,ast, c): 
        return StringType()

    def visitFloatLiteral(self,ast, c): 
        return FloatType()

    def visitIntType(self, ast, c):
        return IntType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitFloatType(self, ast, c):
        return FloatType()    

    def visitBoolType(self, ast, c):
        return BoolType()
    
    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen, self.visit(ast.eleType,c))

    def visitArrayPointerType(self, ast, c):
        return ArrayPointerType(self.visit(ast.eleType,c))
