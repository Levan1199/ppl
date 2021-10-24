// Le Van Hung 1752255
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program: decl+ EOF;
decl: vardecl | funcdecl;

//Declaration
////Variable declaration
vardecl : primitive var (CM var)* SM;

var: ID (LS INTLIT RS)?;
////Function declaration
funcdecl: functive ID LB paralist? RB block_stmt;

//
functive: primitive | VOIDTYPE | arrayPointerType;
paralist: paradecl (CM paradecl)*;
////Common use
paradecl: primitive ID (LS RS)?;
arrayPointerType: primitive LS RS;
//
primitive: BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE;

//Expression
express: express_asn ASN express 
        | express_asn;

express_asn: express_asn OR express_or 
        | express_or;

express_or: express_or AND express_and
        | express_and;

express_and: express_ENEQ (EQ | NEQ) express_ENEQ 
        | express_ENEQ;

express_ENEQ: express_LTGT (LT | LTE | GT | GTE) express_LTGT 
        | express_LTGT;

express_LTGT: express_LTGT (ADD | SUB) express_ADDSUB 
        | express_ADDSUB;

express_ADDSUB: express_ADDSUB (MUL | DIV | MOD) express_MulDivMol
        | express_MulDivMol;

express_MulDivMol: (SUB | NOT) express_MulDivMol 
        | express_Neg;

express_Neg: express_LS LS express RS  
        | express_LS;

express_LS: operands 
        | LB express RB;

operands: lits | ID | arr_el | func_call ;
////
lits: STRINGLIT | INTLIT | BOOLLIT | FLOATLIT;
arr_el: ID LS express RS;
func_call: ID LB list_express? RB;
list_express: express (CM express)*;
//

//Statement
statement: if_stmt
        | doWhile_stmt SM
        | for_stmt
        | break_stmt SM
        | continue_stmt SM
        | return_stmt SM
        | expression_stmt SM
        | block_stmt;

if_stmt: IF LB express RB statement (ELSE statement)?;
doWhile_stmt: DO statement+ WHILE express;
for_stmt: FOR LB express SM express SM express RB statement;
break_stmt: BREAK;
continue_stmt: CONTINUE;
return_stmt: RETURN express?;
expression_stmt: express;
block_stmt: LP (vardecl | statement)* RP;
////common

BOOLLIT: TRUE | FALSE ;
// Keywords
//
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true';
FALSE: 'false';
//Types
BOOLEANTYPE: 'boolean';
INTTYPE: 'int' ;
FLOATTYPE: 'float';
STRINGTYPE: 'string';
VOIDTYPE: 'void' ;
//

//Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
NOT: '!';
MOD: '%';
OR: '||';
AND: '&&';
NEQ: '!=';
EQ: '==';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
ASN: '=';
//

//Separators
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LS: '[';
RS: ']';
SM: ';' ;
CM: ',';
//
//


// Identify
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
//Literals
INTLIT: [0-9]+;
FLOATLIT: DECP | DECP [eE] '-'? [0-9]+  ;
fragment DECP: [0-9]+ ([.][0-9]*)? | [0-9]* ([.][0-9]*)+ ;

STRINGLIT: DOUBLEQUOTES STR_CHAR* DOUBLEQUOTES {
    self.text=self.text[1:-1]
};


//Escape Sequence
fragment ESC: '\\' [bfrnt"\\];
fragment ILLEGAL_ESC: '\\' ~[bfrnt"\\];
fragment STR_CHAR: ~["\r\n\\] | ESC ;
fragment DOUBLEQUOTES: '"';
//
//


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
//Comments
BLOCKCMT: '/*' .*? '*/' -> skip;
LINECMT: '//' ~[\r\n]* ->skip;

UNCLOSE_STRING: DOUBLEQUOTES  STR_CHAR* ;
ILLEGAL_ESCAPE: DOUBLEQUOTES (STR_CHAR)*  ILLEGAL_ESC;
ERROR_CHAR: .;
