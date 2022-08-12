# Generated from /home/Aluno/PycharmProjects/rb4/rbgram.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rbgramParser import rbgramParser
else:
    from rbgramParser import rbgramParser

# This class defines a complete listener for a parse tree produced by rbgramParser.
class rbgramListener(ParseTreeListener):

    # Enter a parse tree produced by rbgramParser#line.
    def enterLine(self, ctx:rbgramParser.LineContext):
        pass

    # Exit a parse tree produced by rbgramParser#line.
    def exitLine(self, ctx:rbgramParser.LineContext):
        pass


    # Enter a parse tree produced by rbgramParser#ETerm.
    def enterETerm(self, ctx:rbgramParser.ETermContext):
        pass

    # Exit a parse tree produced by rbgramParser#ETerm.
    def exitETerm(self, ctx:rbgramParser.ETermContext):
        pass


    # Enter a parse tree produced by rbgramParser#ExprTerm.
    def enterExprTerm(self, ctx:rbgramParser.ExprTermContext):
        pass

    # Exit a parse tree produced by rbgramParser#ExprTerm.
    def exitExprTerm(self, ctx:rbgramParser.ExprTermContext):
        pass


    # Enter a parse tree produced by rbgramParser#TermFactor.
    def enterTermFactor(self, ctx:rbgramParser.TermFactorContext):
        pass

    # Exit a parse tree produced by rbgramParser#TermFactor.
    def exitTermFactor(self, ctx:rbgramParser.TermFactorContext):
        pass


    # Enter a parse tree produced by rbgramParser#TFactor.
    def enterTFactor(self, ctx:rbgramParser.TFactorContext):
        pass

    # Exit a parse tree produced by rbgramParser#TFactor.
    def exitTFactor(self, ctx:rbgramParser.TFactorContext):
        pass


    # Enter a parse tree produced by rbgramParser#ExprPar.
    def enterExprPar(self, ctx:rbgramParser.ExprParContext):
        pass

    # Exit a parse tree produced by rbgramParser#ExprPar.
    def exitExprPar(self, ctx:rbgramParser.ExprParContext):
        pass


    # Enter a parse tree produced by rbgramParser#Num.
    def enterNum(self, ctx:rbgramParser.NumContext):
        pass

    # Exit a parse tree produced by rbgramParser#Num.
    def exitNum(self, ctx:rbgramParser.NumContext):
        pass



del rbgramParser