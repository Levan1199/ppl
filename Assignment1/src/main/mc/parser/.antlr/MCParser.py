# Generated from c:\PrinciplesOfProgrammingLanguage\a1\initial\src\main\mc\parser\MC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u013a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\6\2H\n\2\r\2")
        buf.write("\16\2I\3\2\3\2\3\3\3\3\5\3P\n\3\3\4\3\4\3\4\3\4\7\4V\n")
        buf.write("\4\f\4\16\4Y\13\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5a\n\5\3\6")
        buf.write("\3\6\3\6\3\6\5\6g\n\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7o\n\7")
        buf.write("\3\b\3\b\3\b\7\bt\n\b\f\b\16\bw\13\b\3\t\3\t\3\t\3\t\5")
        buf.write("\t}\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u008a\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0092\n\r\f")
        buf.write("\r\16\r\u0095\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u009d\n\16\f\16\16\16\u00a0\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00a7\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00ae")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00b6\n\21\f")
        buf.write("\21\16\21\u00b9\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00c1\n\22\f\22\16\22\u00c4\13\22\3\23\3\23\3\23\5")
        buf.write("\23\u00c9\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00d1")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00d8\n\25\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u00de\n\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\5\31\u00ea\n\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\7\32\u00f1\n\32\f\32\16\32\u00f4\13\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0108\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0111\n\34\3\35")
        buf.write("\3\35\6\35\u0115\n\35\r\35\16\35\u0116\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\5!\u012c\n!\3\"\3\"\3#\3#\3#\7#\u0133")
        buf.write("\n#\f#\16#\u0136\13#\3#\3#\3#\2\6\30\32 \"$\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BD\2\t\3\2\16\21\3\2\33\34\3\2\35 \3\2\23\24\4\2\25")
        buf.write("\26\30\30\4\2\24\24\27\27\4\2\3\3+-\2\u013b\2G\3\2\2\2")
        buf.write("\4O\3\2\2\2\6Q\3\2\2\2\b\\\3\2\2\2\nb\3\2\2\2\fn\3\2\2")
        buf.write("\2\16p\3\2\2\2\20x\3\2\2\2\22~\3\2\2\2\24\u0082\3\2\2")
        buf.write("\2\26\u0089\3\2\2\2\30\u008b\3\2\2\2\32\u0096\3\2\2\2")
        buf.write("\34\u00a6\3\2\2\2\36\u00ad\3\2\2\2 \u00af\3\2\2\2\"\u00ba")
        buf.write("\3\2\2\2$\u00c8\3\2\2\2&\u00d0\3\2\2\2(\u00d7\3\2\2\2")
        buf.write("*\u00dd\3\2\2\2,\u00df\3\2\2\2.\u00e1\3\2\2\2\60\u00e6")
        buf.write("\3\2\2\2\62\u00ed\3\2\2\2\64\u0107\3\2\2\2\66\u0109\3")
        buf.write("\2\2\28\u0112\3\2\2\2:\u011b\3\2\2\2<\u0125\3\2\2\2>\u0127")
        buf.write("\3\2\2\2@\u0129\3\2\2\2B\u012d\3\2\2\2D\u012f\3\2\2\2")
        buf.write("FH\5\4\3\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3")
        buf.write("\2\2\2KL\7\2\2\3L\3\3\2\2\2MP\5\6\4\2NP\5\n\6\2OM\3\2")
        buf.write("\2\2ON\3\2\2\2P\5\3\2\2\2QR\5\24\13\2RW\5\b\5\2ST\7)\2")
        buf.write("\2TV\5\b\5\2US\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X")
        buf.write("Z\3\2\2\2YW\3\2\2\2Z[\7(\2\2[\7\3\2\2\2\\`\7*\2\2]^\7")
        buf.write("&\2\2^_\7+\2\2_a\7\'\2\2`]\3\2\2\2`a\3\2\2\2a\t\3\2\2")
        buf.write("\2bc\5\f\7\2cd\7*\2\2df\7\"\2\2eg\5\16\b\2fe\3\2\2\2f")
        buf.write("g\3\2\2\2gh\3\2\2\2hi\7#\2\2ij\5D#\2j\13\3\2\2\2ko\5\24")
        buf.write("\13\2lo\7\22\2\2mo\5\22\n\2nk\3\2\2\2nl\3\2\2\2nm\3\2")
        buf.write("\2\2o\r\3\2\2\2pu\5\20\t\2qr\7)\2\2rt\5\20\t\2sq\3\2\2")
        buf.write("\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2v\17\3\2\2\2wu\3\2\2\2")
        buf.write("xy\5\24\13\2y|\7*\2\2z{\7&\2\2{}\7\'\2\2|z\3\2\2\2|}\3")
        buf.write("\2\2\2}\21\3\2\2\2~\177\5\24\13\2\177\u0080\7&\2\2\u0080")
        buf.write("\u0081\7\'\2\2\u0081\23\3\2\2\2\u0082\u0083\t\2\2\2\u0083")
        buf.write("\25\3\2\2\2\u0084\u0085\5\30\r\2\u0085\u0086\7!\2\2\u0086")
        buf.write("\u0087\5\26\f\2\u0087\u008a\3\2\2\2\u0088\u008a\5\30\r")
        buf.write("\2\u0089\u0084\3\2\2\2\u0089\u0088\3\2\2\2\u008a\27\3")
        buf.write("\2\2\2\u008b\u008c\b\r\1\2\u008c\u008d\5\32\16\2\u008d")
        buf.write("\u0093\3\2\2\2\u008e\u008f\f\4\2\2\u008f\u0090\7\31\2")
        buf.write("\2\u0090\u0092\5\32\16\2\u0091\u008e\3\2\2\2\u0092\u0095")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\31\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\b\16\1\2\u0097")
        buf.write("\u0098\5\34\17\2\u0098\u009e\3\2\2\2\u0099\u009a\f\4\2")
        buf.write("\2\u009a\u009b\7\32\2\2\u009b\u009d\5\34\17\2\u009c\u0099")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\33\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\5\36\20\2\u00a2\u00a3\t\3\2\2\u00a3\u00a4\5\36")
        buf.write("\20\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5\36\20\2\u00a6")
        buf.write("\u00a1\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\35\3\2\2\2\u00a8")
        buf.write("\u00a9\5 \21\2\u00a9\u00aa\t\4\2\2\u00aa\u00ab\5 \21\2")
        buf.write("\u00ab\u00ae\3\2\2\2\u00ac\u00ae\5 \21\2\u00ad\u00a8\3")
        buf.write("\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\37\3\2\2\2\u00af\u00b0")
        buf.write("\b\21\1\2\u00b0\u00b1\5\"\22\2\u00b1\u00b7\3\2\2\2\u00b2")
        buf.write("\u00b3\f\4\2\2\u00b3\u00b4\t\5\2\2\u00b4\u00b6\5\"\22")
        buf.write("\2\u00b5\u00b2\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8!\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00ba\u00bb\b\22\1\2\u00bb\u00bc\5$\23\2\u00bc")
        buf.write("\u00c2\3\2\2\2\u00bd\u00be\f\4\2\2\u00be\u00bf\t\6\2\2")
        buf.write("\u00bf\u00c1\5$\23\2\u00c0\u00bd\3\2\2\2\u00c1\u00c4\3")
        buf.write("\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3#")
        buf.write("\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\t\7\2\2\u00c6")
        buf.write("\u00c9\5$\23\2\u00c7\u00c9\5&\24\2\u00c8\u00c5\3\2\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c9%\3\2\2\2\u00ca\u00cb\5(\25")
        buf.write("\2\u00cb\u00cc\7&\2\2\u00cc\u00cd\5\26\f\2\u00cd\u00ce")
        buf.write("\7\'\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d1\5(\25\2\u00d0")
        buf.write("\u00ca\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\'\3\2\2\2\u00d2")
        buf.write("\u00d8\5*\26\2\u00d3\u00d4\7\"\2\2\u00d4\u00d5\5\26\f")
        buf.write("\2\u00d5\u00d6\7#\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d2")
        buf.write("\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d8)\3\2\2\2\u00d9\u00de")
        buf.write("\5,\27\2\u00da\u00de\7*\2\2\u00db\u00de\5.\30\2\u00dc")
        buf.write("\u00de\5\60\31\2\u00dd\u00d9\3\2\2\2\u00dd\u00da\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de+\3\2")
        buf.write("\2\2\u00df\u00e0\t\b\2\2\u00e0-\3\2\2\2\u00e1\u00e2\7")
        buf.write("*\2\2\u00e2\u00e3\7&\2\2\u00e3\u00e4\5\26\f\2\u00e4\u00e5")
        buf.write("\7\'\2\2\u00e5/\3\2\2\2\u00e6\u00e7\7*\2\2\u00e7\u00e9")
        buf.write("\7\"\2\2\u00e8\u00ea\5\62\32\2\u00e9\u00e8\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\7#\2\2")
        buf.write("\u00ec\61\3\2\2\2\u00ed\u00f2\5\26\f\2\u00ee\u00ef\7)")
        buf.write("\2\2\u00ef\u00f1\5\26\f\2\u00f0\u00ee\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\63\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u0108\5\66\34\2")
        buf.write("\u00f6\u00f7\58\35\2\u00f7\u00f8\7(\2\2\u00f8\u0108\3")
        buf.write("\2\2\2\u00f9\u0108\5:\36\2\u00fa\u00fb\5<\37\2\u00fb\u00fc")
        buf.write("\7(\2\2\u00fc\u0108\3\2\2\2\u00fd\u00fe\5> \2\u00fe\u00ff")
        buf.write("\7(\2\2\u00ff\u0108\3\2\2\2\u0100\u0101\5@!\2\u0101\u0102")
        buf.write("\7(\2\2\u0102\u0108\3\2\2\2\u0103\u0104\5B\"\2\u0104\u0105")
        buf.write("\7(\2\2\u0105\u0108\3\2\2\2\u0106\u0108\5D#\2\u0107\u00f5")
        buf.write("\3\2\2\2\u0107\u00f6\3\2\2\2\u0107\u00f9\3\2\2\2\u0107")
        buf.write("\u00fa\3\2\2\2\u0107\u00fd\3\2\2\2\u0107\u0100\3\2\2\2")
        buf.write("\u0107\u0103\3\2\2\2\u0107\u0106\3\2\2\2\u0108\65\3\2")
        buf.write("\2\2\u0109\u010a\7\b\2\2\u010a\u010b\7\"\2\2\u010b\u010c")
        buf.write("\5\26\f\2\u010c\u010d\7#\2\2\u010d\u0110\5\64\33\2\u010e")
        buf.write("\u010f\7\6\2\2\u010f\u0111\5\64\33\2\u0110\u010e\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\67\3\2\2\2\u0112\u0114\7")
        buf.write("\n\2\2\u0113\u0115\5\64\33\2\u0114\u0113\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118\u0119\7\13\2\2\u0119\u011a")
        buf.write("\5\26\f\2\u011a9\3\2\2\2\u011b\u011c\7\7\2\2\u011c\u011d")
        buf.write("\7\"\2\2\u011d\u011e\5\26\f\2\u011e\u011f\7(\2\2\u011f")
        buf.write("\u0120\5\26\f\2\u0120\u0121\7(\2\2\u0121\u0122\5\26\f")
        buf.write("\2\u0122\u0123\7#\2\2\u0123\u0124\5\64\33\2\u0124;\3\2")
        buf.write("\2\2\u0125\u0126\7\4\2\2\u0126=\3\2\2\2\u0127\u0128\7")
        buf.write("\5\2\2\u0128?\3\2\2\2\u0129\u012b\7\t\2\2\u012a\u012c")
        buf.write("\5\26\f\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("A\3\2\2\2\u012d\u012e\5\26\f\2\u012eC\3\2\2\2\u012f\u0134")
        buf.write("\7$\2\2\u0130\u0133\5\6\4\2\u0131\u0133\5\64\33\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0137\u0138\7%\2\2\u0138E\3")
        buf.write("\2\2\2\35IOW`fnu|\u0089\u0093\u009e\u00a6\u00ad\u00b7")
        buf.write("\u00c2\u00c8\u00d0\u00d7\u00dd\u00e9\u00f2\u0107\u0110")
        buf.write("\u0116\u012b\u0132\u0134")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'else'", "'for'", "'if'", "'return'", "'do'", "'while'", 
                     "'true'", "'false'", "'boolean'", "'int'", "'float'", 
                     "'string'", "'void'", "'+'", "'-'", "'*'", "'/'", "'!'", 
                     "'%'", "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLLIT", "BREAK", "CONTINUE", "ELSE", 
                      "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", 
                      "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", "STRINGTYPE", 
                      "VOIDTYPE", "ADD", "SUB", "MUL", "DIV", "NOT", "MOD", 
                      "OR", "AND", "NEQ", "EQ", "LT", "GT", "LTE", "GTE", 
                      "ASN", "LB", "RB", "LP", "RP", "LS", "RS", "SM", "CM", 
                      "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "BLOCKCMT", 
                      "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_var = 3
    RULE_funcdecl = 4
    RULE_functive = 5
    RULE_paralist = 6
    RULE_paradecl = 7
    RULE_arrayPointerType = 8
    RULE_primitive = 9
    RULE_express = 10
    RULE_express_asn = 11
    RULE_express_or = 12
    RULE_express_and = 13
    RULE_express_ENEQ = 14
    RULE_express_LTGT = 15
    RULE_express_ADDSUB = 16
    RULE_express_MulDivMol = 17
    RULE_express_Neg = 18
    RULE_express_LS = 19
    RULE_operands = 20
    RULE_lits = 21
    RULE_arr_el = 22
    RULE_func_call = 23
    RULE_list_express = 24
    RULE_statement = 25
    RULE_if_stmt = 26
    RULE_doWhile_stmt = 27
    RULE_for_stmt = 28
    RULE_break_stmt = 29
    RULE_continue_stmt = 30
    RULE_return_stmt = 31
    RULE_expression_stmt = 32
    RULE_block_stmt = 33

    ruleNames =  [ "program", "decl", "vardecl", "var", "funcdecl", "functive", 
                   "paralist", "paradecl", "arrayPointerType", "primitive", 
                   "express", "express_asn", "express_or", "express_and", 
                   "express_ENEQ", "express_LTGT", "express_ADDSUB", "express_MulDivMol", 
                   "express_Neg", "express_LS", "operands", "lits", "arr_el", 
                   "func_call", "list_express", "statement", "if_stmt", 
                   "doWhile_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "expression_stmt", "block_stmt" ]

    EOF = Token.EOF
    BOOLLIT=1
    BREAK=2
    CONTINUE=3
    ELSE=4
    FOR=5
    IF=6
    RETURN=7
    DO=8
    WHILE=9
    TRUE=10
    FALSE=11
    BOOLEANTYPE=12
    INTTYPE=13
    FLOATTYPE=14
    STRINGTYPE=15
    VOIDTYPE=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    NOT=21
    MOD=22
    OR=23
    AND=24
    NEQ=25
    EQ=26
    LT=27
    GT=28
    LTE=29
    GTE=30
    ASN=31
    LB=32
    RB=33
    LP=34
    RP=35
    LS=36
    RS=37
    SM=38
    CM=39
    ID=40
    INTLIT=41
    FLOATLIT=42
    STRINGLIT=43
    WS=44
    BLOCKCMT=45
    LINECMT=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_CHAR=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.decl()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 73
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MCParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(MCParser.PrimitiveContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_vardecl




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.primitive()
            self.state = 80
            self.var()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 81
                self.match(MCParser.CM)
                self.state = 82
                self.var()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MCParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 91
                self.match(MCParser.LS)
                self.state = 92
                self.match(MCParser.INTLIT)
                self.state = 93
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functive(self):
            return self.getTypedRuleContext(MCParser.FunctiveContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(MCParser.ParalistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdecl




    def funcdecl(self):

        localctx = MCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.functive()
            self.state = 97
            self.match(MCParser.ID)
            self.state = 98
            self.match(MCParser.LB)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 99
                self.paralist()


            self.state = 102
            self.match(MCParser.RB)
            self.state = 103
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(MCParser.PrimitiveContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def arrayPointerType(self):
            return self.getTypedRuleContext(MCParser.ArrayPointerTypeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_functive




    def functive(self):

        localctx = MCParser.FunctiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functive)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.arrayPointerType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParadeclContext)
            else:
                return self.getTypedRuleContext(MCParser.ParadeclContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_paralist




    def paralist(self):

        localctx = MCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.paradecl()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 111
                self.match(MCParser.CM)
                self.state = 112
                self.paradecl()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(MCParser.PrimitiveContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_paradecl




    def paradecl(self):

        localctx = MCParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paradecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.primitive()
            self.state = 119
            self.match(MCParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 120
                self.match(MCParser.LS)
                self.state = 121
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayPointerTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(MCParser.PrimitiveContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arrayPointerType




    def arrayPointerType(self):

        localctx = MCParser.ArrayPointerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayPointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.primitive()
            self.state = 125
            self.match(MCParser.LS)
            self.state = 126
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANTYPE(self):
            return self.getToken(MCParser.BOOLEANTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive




    def primitive(self):

        localctx = MCParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_primitive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_asn(self):
            return self.getTypedRuleContext(MCParser.Express_asnContext,0)


        def ASN(self):
            return self.getToken(MCParser.ASN, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_express




    def express(self):

        localctx = MCParser.ExpressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_express)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.express_asn(0)
                self.state = 131
                self.match(MCParser.ASN)
                self.state = 132
                self.express()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.express_asn(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_asnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_or(self):
            return self.getTypedRuleContext(MCParser.Express_orContext,0)


        def express_asn(self):
            return self.getTypedRuleContext(MCParser.Express_asnContext,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_asn



    def express_asn(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Express_asnContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_express_asn, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.express_or(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_asnContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_asn)
                    self.state = 140
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 141
                    self.match(MCParser.OR)
                    self.state = 142
                    self.express_or(0) 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express_orContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_and(self):
            return self.getTypedRuleContext(MCParser.Express_andContext,0)


        def express_or(self):
            return self.getTypedRuleContext(MCParser.Express_orContext,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_or



    def express_or(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Express_orContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_express_or, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.express_and()
            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_orContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_or)
                    self.state = 151
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 152
                    self.match(MCParser.AND)
                    self.state = 153
                    self.express_and() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express_andContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_ENEQ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Express_ENEQContext)
            else:
                return self.getTypedRuleContext(MCParser.Express_ENEQContext,i)


        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MCParser.NEQ, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_and




    def express_and(self):

        localctx = MCParser.Express_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_express_and)
        self._la = 0 # Token type
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.express_ENEQ()
                self.state = 160
                _la = self._input.LA(1)
                if not(_la==MCParser.NEQ or _la==MCParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.express_ENEQ()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.express_ENEQ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_ENEQContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_LTGT(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Express_LTGTContext)
            else:
                return self.getTypedRuleContext(MCParser.Express_LTGTContext,i)


        def LT(self):
            return self.getToken(MCParser.LT, 0)

        def LTE(self):
            return self.getToken(MCParser.LTE, 0)

        def GT(self):
            return self.getToken(MCParser.GT, 0)

        def GTE(self):
            return self.getToken(MCParser.GTE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_ENEQ




    def express_ENEQ(self):

        localctx = MCParser.Express_ENEQContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_express_ENEQ)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.express_LTGT(0)
                self.state = 167
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT) | (1 << MCParser.GT) | (1 << MCParser.LTE) | (1 << MCParser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.express_LTGT(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.express_LTGT(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_LTGTContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_ADDSUB(self):
            return self.getTypedRuleContext(MCParser.Express_ADDSUBContext,0)


        def express_LTGT(self):
            return self.getTypedRuleContext(MCParser.Express_LTGTContext,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_LTGT



    def express_LTGT(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Express_LTGTContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_express_LTGT, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.express_ADDSUB(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_LTGTContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_LTGT)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.express_ADDSUB(0) 
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express_ADDSUBContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_MulDivMol(self):
            return self.getTypedRuleContext(MCParser.Express_MulDivMolContext,0)


        def express_ADDSUB(self):
            return self.getTypedRuleContext(MCParser.Express_ADDSUBContext,0)


        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_ADDSUB



    def express_ADDSUB(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Express_ADDSUBContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_express_ADDSUB, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.express_MulDivMol()
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_ADDSUBContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_ADDSUB)
                    self.state = 187
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 188
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 189
                    self.express_MulDivMol() 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express_MulDivMolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_MulDivMol(self):
            return self.getTypedRuleContext(MCParser.Express_MulDivMolContext,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def express_Neg(self):
            return self.getTypedRuleContext(MCParser.Express_NegContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_express_MulDivMol




    def express_MulDivMol(self):

        localctx = MCParser.Express_MulDivMolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_express_MulDivMol)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB, MCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB or _la==MCParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.express_MulDivMol()
                pass
            elif token in [MCParser.BOOLLIT, MCParser.LB, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.express_Neg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_NegContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_LS(self):
            return self.getTypedRuleContext(MCParser.Express_LSContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_Neg




    def express_Neg(self):

        localctx = MCParser.Express_NegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_express_Neg)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.express_LS()
                self.state = 201
                self.match(MCParser.LS)
                self.state = 202
                self.express()
                self.state = 203
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.express_LS()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Express_LSContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(MCParser.OperandsContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_LS




    def express_LS(self):

        localctx = MCParser.Express_LSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_express_LS)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLLIT, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.operands()
                pass
            elif token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(MCParser.LB)
                self.state = 210
                self.express()
                self.state = 211
                self.match(MCParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lits(self):
            return self.getTypedRuleContext(MCParser.LitsContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def arr_el(self):
            return self.getTypedRuleContext(MCParser.Arr_elContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MCParser.Func_callContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operands




    def operands(self):

        localctx = MCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operands)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.lits()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(MCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.arr_el()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 218
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_lits




    def lits(self):

        localctx = MCParser.LitsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arr_el




    def arr_el(self):

        localctx = MCParser.Arr_elContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arr_el)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MCParser.ID)
            self.state = 224
            self.match(MCParser.LS)
            self.state = 225
            self.express()
            self.state = 226
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def list_express(self):
            return self.getTypedRuleContext(MCParser.List_expressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_call




    def func_call(self):

        localctx = MCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MCParser.ID)
            self.state = 229
            self.match(MCParser.LB)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 230
                self.list_express()


            self.state = 233
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_express




    def list_express(self):

        localctx = MCParser.List_expressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_express)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.express()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 236
                self.match(MCParser.CM)
                self.state = 237
                self.express()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def doWhile_stmt(self):
            return self.getTypedRuleContext(MCParser.DoWhile_stmtContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def expression_stmt(self):
            return self.getTypedRuleContext(MCParser.Expression_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.if_stmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.doWhile_stmt()
                self.state = 245
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
                self.for_stmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 248
                self.break_stmt()
                self.state = 249
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 251
                self.continue_stmt()
                self.state = 252
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.return_stmt()
                self.state = 255
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.BOOLLIT, MCParser.SUB, MCParser.NOT, MCParser.LB, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 257
                self.expression_stmt()
                self.state = 258
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 260
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_stmt




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MCParser.IF)
            self.state = 264
            self.match(MCParser.LB)
            self.state = 265
            self.express()
            self.state = 266
            self.match(MCParser.RB)
            self.state = 267
            self.statement()
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(MCParser.ELSE)
                self.state = 269
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_doWhile_stmt




    def doWhile_stmt(self):

        localctx = MCParser.DoWhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_doWhile_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MCParser.DO)
            self.state = 274 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 273
                self.statement()
                self.state = 276 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 278
            self.match(MCParser.WHILE)
            self.state = 279
            self.express()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def express(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SM)
            else:
                return self.getToken(MCParser.SM, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(MCParser.FOR)
            self.state = 282
            self.match(MCParser.LB)
            self.state = 283
            self.express()
            self.state = 284
            self.match(MCParser.SM)
            self.state = 285
            self.express()
            self.state = 286
            self.match(MCParser.SM)
            self.state = 287
            self.express()
            self.state = 288
            self.match(MCParser.RB)
            self.state = 289
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MCParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MCParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(MCParser.RETURN)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 296
                self.express()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express(self):
            return self.getTypedRuleContext(MCParser.ExpressContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expression_stmt




    def expression_stmt(self):

        localctx = MCParser.Expression_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.express()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardeclContext)
            else:
                return self.getTypedRuleContext(MCParser.VardeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_stmt




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MCParser.LP)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 304
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.BOOLEANTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                    self.state = 302
                    self.vardecl()
                    pass
                elif token in [MCParser.BOOLLIT, MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.SUB, MCParser.NOT, MCParser.LB, MCParser.LP, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT]:
                    self.state = 303
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 309
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.express_asn_sempred
        self._predicates[12] = self.express_or_sempred
        self._predicates[15] = self.express_LTGT_sempred
        self._predicates[16] = self.express_ADDSUB_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def express_asn_sempred(self, localctx:Express_asnContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def express_or_sempred(self, localctx:Express_orContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def express_LTGT_sempred(self, localctx:Express_LTGTContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def express_ADDSUB_sempred(self, localctx:Express_ADDSUBContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




