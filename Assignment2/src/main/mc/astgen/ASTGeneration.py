#1752255
from main.mc.utils.AST import ArrayCell, ArrayPointerType, ArrayType, BinaryOp, Block, BoolType, BooleanLiteral, Break, CallExpr, Continue, Dowhile, FloatLiteral, FloatType, For, FuncDecl, Id, If, IntLiteral, IntType, Program, Return, StringLiteral, StringType, UnaryOp, VarDecl, VoidType
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
  
class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        lst = []
        for x in ctx.decls():           
            if isinstance(self.visit(x),list):
                lst.extend(self.visit(x))
            else:
                lst.append(self.visit(x))
        return Program(lst)
    
    def visitDecls(self, ctx:MCParser.DeclsContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        else:
            return self.visit(ctx.funcDecl())

    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        lst = []
        primitiveType = self.visit(ctx.primitive())
        for variable in self.visit(ctx.listVar()):
            if isinstance(variable, list):
                temp = VarDecl(variable[0], ArrayType(variable[1], primitiveType))
                lst.append(temp)
            else:
                temp = VarDecl(variable, primitiveType)
                lst.append(temp)
        return lst

    def visitListVar(self, ctx: MCParser.ListVarContext):
        return [self.visit(x) for x in ctx.var()]   
 
   
    def visitVar(self, ctx:MCParser.VarContext):
        if ctx.getChildCount() == 1:
           return ctx.ID().getText()
        else:
            return [ctx.ID().getText(), int(ctx.INTLIT().getText())]

    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.paralist()) if ctx.paralist() else []
        returnType = self.visit(ctx.functive())
        body = self.visit(ctx.block_stmt())
        return FuncDecl(name, param, returnType, body)

    def visitFunctive(self, ctx:MCParser.FunctiveContext):
        if ctx.VOIDTYPE():
            return VoidType()
        elif ctx.primitive():
            return self.visit(ctx.primitive())
        else:
            return self.visit(ctx.arrayPointerType())
    
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return [self.visit(x) for x in ctx.paradecl()]

    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        primitiveType = self.visit(ctx.primitive())
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.ID().getText(), primitiveType)
        else:
            return VarDecl(ctx.ID().getText(), ArrayPointerType(primitiveType))

    def visitPrimitive(self, ctx:MCParser.PrimitiveContext):
        if ctx.BOOLTYPE():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        else:
            return StringType()

    def visitArrayPointerType(self, ctx:MCParser.ArrayPointerTypeContext):
        return ArrayPointerType(self.visit(ctx.primitive()))

    def visitExpress(self, ctx:MCParser.ExpressContext):
        if ctx.express():
            op = ctx.ASN().getText()
            left = self.visit(ctx.express_asn())
            right = self.visit(ctx.express())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.express_asn())
    

    def visitExpress_asn(self, ctx:MCParser.Express_asnContext):
        if ctx.express_asn():
            op = ctx.OR().getText()
            left = self.visit(ctx.express_asn())
            right = self.visit(ctx.express_or())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.express_or())

            
    def visitExpress_or(self, ctx:MCParser.Express_orContext):
        if ctx.express_or():
            op = ctx.AND().getText()
            left = self.visit(ctx.express_or())
            right = self.visit(ctx.express_and())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.express_and())

    def visitExpress_and(self, ctx:MCParser.Express_andContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_ENEQ(0))       
        
        left = self.visit(ctx.express_ENEQ(0))
        right = self.visit(ctx.express_ENEQ(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op,left,right)
  
    def visitExpress_ENEQ(self, ctx:MCParser.Express_ENEQContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_LTGT(0))
        else:
            # if ctx.LT():
            #     op = ctx.LT().getText()
            # elif ctx.LTE():
            #     op = ctx.LTE().getText()
            # elif ctx.GT():
            #     op = ctx.GT().getText()
            # else:                
            #     op = ctx.GTE().getText()
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.express_LTGT(0))
            right = self.visit(ctx.express_LTGT(1))
            return BinaryOp(op,left,right)
    
    def visitExpress_LTGT(self, ctx:MCParser.Express_LTGTContext):
        if ctx.express_LTGT():
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            left = self.visit(ctx.express_LTGT())
            right = self.visit(ctx.express_ADDSUB())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.express_ADDSUB())
    
    def visitExpress_ADDSUB(self, ctx:MCParser.Express_ADDSUBContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_MulDivMod())
        else:
            if ctx.MUL():
                op = ctx.MUL().getText()
            elif ctx.DIV():
                op = ctx.DIV().getText()           
            else:                
                op = ctx.MOD().getText()
            left = self.visit(ctx.express_ADDSUB())
            right = self.visit(ctx.express_MulDivMod())
            return BinaryOp(op,left,right)
    
    def visitExpress_MulDivMod(self, ctx:MCParser.Express_MulDivModContext):
        if ctx.express_MulDivMod():
            op = ctx.SUB().getText() if ctx.SUB() else ctx.NOT().getText()
            body = self.visit(ctx.express_MulDivMod())
            return UnaryOp(op,body)
        else:
            return self.visit(ctx.express_Neg())
      
    def visitExpress_Neg(self, ctx:MCParser.Express_NegContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_LS())
        else:
            if ctx.ID():
                return self.visit(ctx.express())
            else:                
                idx = self.visit(ctx.express())
                arr = self.visit(ctx.express_LS())
                return ArrayCell(arr, idx)

    def visitExpress_LS(self, ctx:MCParser.Express_LSContext):
        if ctx.operands():
           return self.visit(ctx.operands())
        else:
            return self.visit(ctx.express()) 
    
    def visitOperands(self, ctx:MCParser.OperandsContext):
        if ctx.lits():
           return self.visit(ctx.lits())
        elif ctx.ID():
            return Id(ctx.ID().getText())       
        else:
            return self.visit(ctx.func_call())
           
    def visitLits(self, ctx:MCParser.LitsContext):
        if ctx.STRLIT():
           return StringLiteral(str(ctx.STRLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(True if ctx.BOOLLIT().getText()=='true' else False)
        else:
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.list_express()) if ctx.list_express() else []
        return CallExpr(method, param)
    
    def visitList_express(self, ctx:MCParser.List_expressContext):
        return [self.visit(x) for x in ctx.express()]
    
    def visitStatement(self, ctx:MCParser.StatementContext):
        if ctx.getChildCount() == 2:
            stmt = ctx.getChild(0)
            return self.visit(stmt)
        else:
            if ctx.if_stmt():
                return self.visit(ctx.if_stmt())
            elif ctx.for_stmt():
                return self.visit(ctx.for_stmt())
            else:
                return self.visit(ctx.block_stmt())

    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        exp = self.visit(ctx.express())
        if ctx.getChildCount() == 5:
            then = self.visit(ctx.statement(0))
            else_s = None
        else:
            then = self.visit(ctx.statement(0))
            else_s = self.visit(ctx.statement(1))              
        return If(exp,then,else_s)
    
    def visitDoWhile_stmt(self, ctx:MCParser.DoWhile_stmtContext):
        stmts = [self.visit(x) for x in ctx.statement()]
        expr = self.visit(ctx.express())
        return Dowhile(stmts, expr)
      
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        expr1 = self.visit(ctx.express(0))
        expr2 = self.visit(ctx.express(1))
        expr3 = self.visit(ctx.express(2))
        loop = self.visit(ctx.statement())
        return For(expr1, expr2, expr3, loop)
    
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):      
        return Break()
    
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):      
        return Continue() 

    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):      
        return Return(self.visit(ctx.express())) if ctx.express() else Return()

    def visitExpression_stmt(self, ctx:MCParser.Expression_stmtContext): 
        return self.visit(ctx.express())

    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        lstMem = []
        for x in ctx.block_mem():
            block = self.visit(x)
            if isinstance(block, list):
                lstMem.extend(block if block else [])
            else:
                lstMem.append(block)
        return Block(lstMem)
    
    def visitBlock_mem(self, ctx:MCParser.Block_memContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        else:
            return self.visit(ctx.statement())