# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcall.
    def visitFuncall(self, ctx:MCParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardecl.
    def visitVardecl(self, ctx:MCParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listvar.
    def visitListvar(self, ctx:MCParser.ListvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primtype.
    def visitPrimtype(self, ctx:MCParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdecl.
    def visitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paralist.
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functype.
    def visitFunctype(self, ctx:MCParser.FunctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrpointertype.
    def visitArrpointertype(self, ctx:MCParser.ArrpointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paradecl.
    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#blockstmt.
    def visitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression1.
    def visitExpression1(self, ctx:MCParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression2.
    def visitExpression2(self, ctx:MCParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression3.
    def visitExpression3(self, ctx:MCParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression4.
    def visitExpression4(self, ctx:MCParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression5.
    def visitExpression5(self, ctx:MCParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression6.
    def visitExpression6(self, ctx:MCParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression7.
    def visitExpression7(self, ctx:MCParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression8.
    def visitExpression8(self, ctx:MCParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operator.
    def visitOperator(self, ctx:MCParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#subexpress.
    def visitSubexpress(self, ctx:MCParser.SubexpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#indexexpression.
    def visitIndexexpression(self, ctx:MCParser.IndexexpressionContext):
        return self.visitChildren(ctx)



del MCParser