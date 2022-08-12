grammar rbgram;

line: expr '\n'
    ;

expr returns [int val]
    : expr op=('+'|'-') term        #ExprTerm
    | term                          #ETerm
    ;

term returns [int val]
    : term op=('*'|'/'|'^') factor  #TermFactor
    | factor                        #TFactor
    ;

factor returns [int val]
    : '(' expr ')'                  #ExprPar
    | NUM                           #Num
    ;

NUM: [-]?[0-9]+
    ;
WS: [ \t\r\n] -> skip
    ;