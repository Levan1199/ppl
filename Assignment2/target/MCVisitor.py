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


    # Visit a parse tree produced by MCParser#decls.
    def visitDecls(self, ctx:MCParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDecl.
    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#listVar.
    def visitListVar(self, ctx:MCParser.ListVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDecl.
    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#functive.
    def visitFunctive(self, ctx:MCParser.FunctiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paralist.
    def visitParalist(self, ctx:MCParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paradecl.
    def visitParadecl(self, ctx:MCParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primitive.
    def visitPrimitive(self, ctx:MCParser.PrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arrayPointerType.
    def visitArrayPointerType(self, ctx:MCParser.ArrayPointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express.
    def visitExpress(self, ctx:MCParser.ExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_asn.
    def visitExpress_asn(self, ctx:MCParser.Express_asnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_or.
    def visitExpress_or(self, ctx:MCParser.Express_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_and.
    def visitExpress_and(self, ctx:MCParser.Express_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_ENEQ.
    def visitExpress_ENEQ(self, ctx:MCParser.Express_ENEQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_LTGT.
    def visitExpress_LTGT(self, ctx:MCParser.Express_LTGTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_ADDSUB.
    def visitExpress_ADDSUB(self, ctx:MCParser.Express_ADDSUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_MulDivMod.
    def visitExpress_MulDivMod(self, ctx:MCParser.Express_MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_Neg.
    def visitExpress_Neg(self, ctx:MCParser.Express_NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_LS.
    def visitExpress_LS(self, ctx:MCParser.Express_LSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#lits.
    def visitLits(self, ctx:MCParser.LitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_express.
    def visitList_express(self, ctx:MCParser.List_expressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#doWhile_stmt.
    def visitDoWhile_stmt(self, ctx:MCParser.DoWhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression_stmt.
    def visitExpression_stmt(self, ctx:MCParser.Expression_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_mem.
    def visitBlock_mem(self, ctx:MCParser.Block_memContext):
        return self.visitChildren(ctx)



del MCParser