# Generated from /home/Aluno/PycharmProjects/rb4/rbgram.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rbgramParser import rbgramParser
else:
    from rbgramParser import rbgramParser
# This class defines a complete listener for a parse tree produced by rbgramParser.
class rbgramListener(ParseTreeListener):

    # Exit a parse tree produced by rbgramParser#line.
    def exitLine(self, ctx: rbgramParser.LineContext):
        print("Resultado: ", ctx.expr().val)

    # Exit a parse tree produced by rbgramParser#ETerm.
    def exitETerm(self, ctx: rbgramParser.ETermContext):
        ctx.val = ctx.term().val

    # Exit a parse tree produced by rbgramParser#ExprTerm.
    def exitExprTerm(self, ctx:rbgramParser.ExprTermContext):
        if(ctx.op.text == '+'):
            ctx.val = ctx.expr().val + ctx.term().val
        else:
            ctx.val = ctx.expr().val - ctx.term().val

    # Exit a parse tree produced by rbgramParser#TermFactor.
    def exitTermFactor(self, ctx: rbgramParser.TermFactorContext):
        if(ctx.op.text == '*'):
            ctx.val = ctx.term().val * ctx.factor().val
        elif(ctx.op.text == '/'):
            ctx.val = ctx.term().val / ctx.factor().val
        else:
            ctx.val = ctx.term().val ** ctx.factor().val

    # Exit a parse tree produced by rbgramParser#TFactor.
    def exitTFactor(self, ctx:rbgramParser.TFactorContext):
        ctx.val = ctx.factor().val

    # Exit a parse tree produced by rbgramParser#ExprPar.
    def exitExprPar(self, ctx:rbgramParser.ExprParContext):
        ctx.val = ctx.expr().val

    # Exit a parse tree produced by rbgramParser#Num.
    def exitNum(self, ctx:rbgramParser.NumContext):
        ctx.val = int(ctx.NUM().getText())