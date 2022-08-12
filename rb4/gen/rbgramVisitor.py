# Generated from /home/Aluno/PycharmProjects/rb4/rbgram.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rbgramParser import rbgramParser
else:
    from rbgramParser import rbgramParser

# This class defines a complete generic visitor for a parse tree produced by rbgramParser.

class rbgramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by rbgramParser#line.
    def visitLine(self, ctx:rbgramParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#ETerm.
    def visitETerm(self, ctx:rbgramParser.ETermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#ExprTerm.
    def visitExprTerm(self, ctx:rbgramParser.ExprTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#TermFactor.
    def visitTermFactor(self, ctx:rbgramParser.TermFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#TFactor.
    def visitTFactor(self, ctx:rbgramParser.TFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#ExprPar.
    def visitExprPar(self, ctx:rbgramParser.ExprParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rbgramParser#Num.
    def visitNum(self, ctx:rbgramParser.NumContext):
        return self.visitChildren(ctx)



del rbgramParser