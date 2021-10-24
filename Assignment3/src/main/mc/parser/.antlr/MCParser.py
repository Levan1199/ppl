# Generated from c:\PrinciplesOfProgrammingLanguage\a3\upload\src\main\mc\parser\MC.g4 by ANTLR 4.8
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
        buf.write("\u013f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\6\2J\n")
        buf.write("\2\r\2\16\2K\3\2\3\2\3\3\3\3\5\3R\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5[\n\5\f\5\16\5^\13\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6d\n\6\3\7\3\7\3\7\3\7\5\7j\n\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\5\br\n\b\3\t\3\t\3\t\7\tw\n\t\f\t\16\tz\13\t\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u0080\n\n\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u008d\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\7\16\u0095\n\16\f\16\16\16\u0098\13\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\7\17\u00a0\n\17\f\17\16\17\u00a3")
        buf.write("\13\17\3\20\3\20\3\20\3\20\3\20\5\20\u00aa\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00b1\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\7\22\u00b9\n\22\f\22\16\22\u00bc\13\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\7\23\u00c4\n\23\f\23\16\23\u00c7")
        buf.write("\13\23\3\24\3\24\3\24\5\24\u00cc\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d9\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00e0\n\26\3\27\3\27\3")
        buf.write("\27\5\27\u00e5\n\27\3\30\3\30\3\31\3\31\3\31\5\31\u00ec")
        buf.write("\n\31\3\31\3\31\3\32\3\32\3\32\7\32\u00f3\n\32\f\32\16")
        buf.write("\32\u00f6\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u010a\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0113")
        buf.write("\n\34\3\35\3\35\6\35\u0117\n\35\r\35\16\35\u0118\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\5!\u012e\n!\3\"\3\"\3#\3#")
        buf.write("\7#\u0134\n#\f#\16#\u0137\13#\3#\3#\3$\3$\5$\u013d\n$")
        buf.write("\3$\2\6\32\34\"$%\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDF\2\t\3\2\4\7\3\2\33\34")
        buf.write("\3\2\35 \3\2\23\24\4\2\25\26\30\30\4\2\24\24\27\27\4\2")
        buf.write("\3\3+-\2\u013f\2I\3\2\2\2\4Q\3\2\2\2\6S\3\2\2\2\bW\3\2")
        buf.write("\2\2\n_\3\2\2\2\fe\3\2\2\2\16q\3\2\2\2\20s\3\2\2\2\22")
        buf.write("{\3\2\2\2\24\u0081\3\2\2\2\26\u0083\3\2\2\2\30\u008c\3")
        buf.write("\2\2\2\32\u008e\3\2\2\2\34\u0099\3\2\2\2\36\u00a9\3\2")
        buf.write("\2\2 \u00b0\3\2\2\2\"\u00b2\3\2\2\2$\u00bd\3\2\2\2&\u00cb")
        buf.write("\3\2\2\2(\u00d8\3\2\2\2*\u00df\3\2\2\2,\u00e4\3\2\2\2")
        buf.write(".\u00e6\3\2\2\2\60\u00e8\3\2\2\2\62\u00ef\3\2\2\2\64\u0109")
        buf.write("\3\2\2\2\66\u010b\3\2\2\28\u0114\3\2\2\2:\u011d\3\2\2")
        buf.write("\2<\u0127\3\2\2\2>\u0129\3\2\2\2@\u012b\3\2\2\2B\u012f")
        buf.write("\3\2\2\2D\u0131\3\2\2\2F\u013c\3\2\2\2HJ\5\4\3\2IH\3\2")
        buf.write("\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\2\2\3")
        buf.write("N\3\3\2\2\2OR\5\6\4\2PR\5\f\7\2QO\3\2\2\2QP\3\2\2\2R\5")
        buf.write("\3\2\2\2ST\5\24\13\2TU\5\b\5\2UV\7(\2\2V\7\3\2\2\2W\\")
        buf.write("\5\n\6\2XY\7)\2\2Y[\5\n\6\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2")
        buf.write("\2\2\\]\3\2\2\2]\t\3\2\2\2^\\\3\2\2\2_c\7*\2\2`a\7&\2")
        buf.write("\2ab\7+\2\2bd\7\'\2\2c`\3\2\2\2cd\3\2\2\2d\13\3\2\2\2")
        buf.write("ef\5\16\b\2fg\7*\2\2gi\7\"\2\2hj\5\20\t\2ih\3\2\2\2ij")
        buf.write("\3\2\2\2jk\3\2\2\2kl\7#\2\2lm\5D#\2m\r\3\2\2\2nr\5\24")
        buf.write("\13\2or\7\b\2\2pr\5\26\f\2qn\3\2\2\2qo\3\2\2\2qp\3\2\2")
        buf.write("\2r\17\3\2\2\2sx\5\22\n\2tu\7)\2\2uw\5\22\n\2vt\3\2\2")
        buf.write("\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\21\3\2\2\2zx\3\2\2\2")
        buf.write("{|\5\24\13\2|\177\7*\2\2}~\7&\2\2~\u0080\7\'\2\2\177}")
        buf.write("\3\2\2\2\177\u0080\3\2\2\2\u0080\23\3\2\2\2\u0081\u0082")
        buf.write("\t\2\2\2\u0082\25\3\2\2\2\u0083\u0084\5\24\13\2\u0084")
        buf.write("\u0085\7&\2\2\u0085\u0086\7\'\2\2\u0086\27\3\2\2\2\u0087")
        buf.write("\u0088\5\32\16\2\u0088\u0089\7!\2\2\u0089\u008a\5\30\r")
        buf.write("\2\u008a\u008d\3\2\2\2\u008b\u008d\5\32\16\2\u008c\u0087")
        buf.write("\3\2\2\2\u008c\u008b\3\2\2\2\u008d\31\3\2\2\2\u008e\u008f")
        buf.write("\b\16\1\2\u008f\u0090\5\34\17\2\u0090\u0096\3\2\2\2\u0091")
        buf.write("\u0092\f\4\2\2\u0092\u0093\7\31\2\2\u0093\u0095\5\34\17")
        buf.write("\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\33\3\2\2\2\u0098\u0096")
        buf.write("\3\2\2\2\u0099\u009a\b\17\1\2\u009a\u009b\5\36\20\2\u009b")
        buf.write("\u00a1\3\2\2\2\u009c\u009d\f\4\2\2\u009d\u009e\7\32\2")
        buf.write("\2\u009e\u00a0\5\36\20\2\u009f\u009c\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\35\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5 \21\2\u00a5")
        buf.write("\u00a6\t\3\2\2\u00a6\u00a7\5 \21\2\u00a7\u00aa\3\2\2\2")
        buf.write("\u00a8\u00aa\5 \21\2\u00a9\u00a4\3\2\2\2\u00a9\u00a8\3")
        buf.write("\2\2\2\u00aa\37\3\2\2\2\u00ab\u00ac\5\"\22\2\u00ac\u00ad")
        buf.write("\t\4\2\2\u00ad\u00ae\5\"\22\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write("\u00b1\5\"\22\2\u00b0\u00ab\3\2\2\2\u00b0\u00af\3\2\2")
        buf.write("\2\u00b1!\3\2\2\2\u00b2\u00b3\b\22\1\2\u00b3\u00b4\5$")
        buf.write("\23\2\u00b4\u00ba\3\2\2\2\u00b5\u00b6\f\4\2\2\u00b6\u00b7")
        buf.write("\t\5\2\2\u00b7\u00b9\5$\23\2\u00b8\u00b5\3\2\2\2\u00b9")
        buf.write("\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb#\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\b\23\1")
        buf.write("\2\u00be\u00bf\5&\24\2\u00bf\u00c5\3\2\2\2\u00c0\u00c1")
        buf.write("\f\4\2\2\u00c1\u00c2\t\6\2\2\u00c2\u00c4\5&\24\2\u00c3")
        buf.write("\u00c0\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6%\3\2\2\2\u00c7\u00c5\3\2\2")
        buf.write("\2\u00c8\u00c9\t\7\2\2\u00c9\u00cc\5&\24\2\u00ca\u00cc")
        buf.write("\5(\25\2\u00cb\u00c8\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\'\3\2\2\2\u00cd\u00ce\5*\26\2\u00ce\u00cf\7&\2\2\u00cf")
        buf.write("\u00d0\5\30\r\2\u00d0\u00d1\7\'\2\2\u00d1\u00d9\3\2\2")
        buf.write("\2\u00d2\u00d9\5*\26\2\u00d3\u00d4\7*\2\2\u00d4\u00d5")
        buf.write("\7&\2\2\u00d5\u00d6\5\30\r\2\u00d6\u00d7\7\'\2\2\u00d7")
        buf.write("\u00d9\3\2\2\2\u00d8\u00cd\3\2\2\2\u00d8\u00d2\3\2\2\2")
        buf.write("\u00d8\u00d3\3\2\2\2\u00d9)\3\2\2\2\u00da\u00e0\5,\27")
        buf.write("\2\u00db\u00dc\7\"\2\2\u00dc\u00dd\5\30\r\2\u00dd\u00de")
        buf.write("\7#\2\2\u00de\u00e0\3\2\2\2\u00df\u00da\3\2\2\2\u00df")
        buf.write("\u00db\3\2\2\2\u00e0+\3\2\2\2\u00e1\u00e5\5.\30\2\u00e2")
        buf.write("\u00e5\7*\2\2\u00e3\u00e5\5\60\31\2\u00e4\u00e1\3\2\2")
        buf.write("\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5-\3\2")
        buf.write("\2\2\u00e6\u00e7\t\b\2\2\u00e7/\3\2\2\2\u00e8\u00e9\7")
        buf.write("*\2\2\u00e9\u00eb\7\"\2\2\u00ea\u00ec\5\62\32\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ee\7#\2\2\u00ee\61\3\2\2\2\u00ef\u00f4\5\30")
        buf.write("\r\2\u00f0\u00f1\7)\2\2\u00f1\u00f3\5\30\r\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\63\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write("\u010a\5\66\34\2\u00f8\u00f9\58\35\2\u00f9\u00fa\7(\2")
        buf.write("\2\u00fa\u010a\3\2\2\2\u00fb\u010a\5:\36\2\u00fc\u00fd")
        buf.write("\5<\37\2\u00fd\u00fe\7(\2\2\u00fe\u010a\3\2\2\2\u00ff")
        buf.write("\u0100\5> \2\u0100\u0101\7(\2\2\u0101\u010a\3\2\2\2\u0102")
        buf.write("\u0103\5@!\2\u0103\u0104\7(\2\2\u0104\u010a\3\2\2\2\u0105")
        buf.write("\u0106\5B\"\2\u0106\u0107\7(\2\2\u0107\u010a\3\2\2\2\u0108")
        buf.write("\u010a\5D#\2\u0109\u00f7\3\2\2\2\u0109\u00f8\3\2\2\2\u0109")
        buf.write("\u00fb\3\2\2\2\u0109\u00fc\3\2\2\2\u0109\u00ff\3\2\2\2")
        buf.write("\u0109\u0102\3\2\2\2\u0109\u0105\3\2\2\2\u0109\u0108\3")
        buf.write("\2\2\2\u010a\65\3\2\2\2\u010b\u010c\7\r\2\2\u010c\u010d")
        buf.write("\7\"\2\2\u010d\u010e\5\30\r\2\u010e\u010f\7#\2\2\u010f")
        buf.write("\u0112\5\64\33\2\u0110\u0111\7\13\2\2\u0111\u0113\5\64")
        buf.write("\33\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\67")
        buf.write("\3\2\2\2\u0114\u0116\7\17\2\2\u0115\u0117\5\64\33\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7")
        buf.write("\20\2\2\u011b\u011c\5\30\r\2\u011c9\3\2\2\2\u011d\u011e")
        buf.write("\7\f\2\2\u011e\u011f\7\"\2\2\u011f\u0120\5\30\r\2\u0120")
        buf.write("\u0121\7(\2\2\u0121\u0122\5\30\r\2\u0122\u0123\7(\2\2")
        buf.write("\u0123\u0124\5\30\r\2\u0124\u0125\7#\2\2\u0125\u0126\5")
        buf.write("\64\33\2\u0126;\3\2\2\2\u0127\u0128\7\t\2\2\u0128=\3\2")
        buf.write("\2\2\u0129\u012a\7\n\2\2\u012a?\3\2\2\2\u012b\u012d\7")
        buf.write("\16\2\2\u012c\u012e\5\30\r\2\u012d\u012c\3\2\2\2\u012d")
        buf.write("\u012e\3\2\2\2\u012eA\3\2\2\2\u012f\u0130\5\30\r\2\u0130")
        buf.write("C\3\2\2\2\u0131\u0135\7$\2\2\u0132\u0134\5F$\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2")
        buf.write("\u0138\u0139\7%\2\2\u0139E\3\2\2\2\u013a\u013d\5\6\4\2")
        buf.write("\u013b\u013d\5\64\33\2\u013c\u013a\3\2\2\2\u013c\u013b")
        buf.write("\3\2\2\2\u013dG\3\2\2\2\35KQ\\ciqx\177\u008c\u0096\u00a1")
        buf.write("\u00a9\u00b0\u00ba\u00c5\u00cb\u00d8\u00df\u00e4\u00eb")
        buf.write("\u00f4\u0109\u0112\u0118\u012d\u0135\u013c")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'boolean'", "'int'", "'float'", 
                     "'string'", "'void'", "'break'", "'continue'", "'else'", 
                     "'for'", "'if'", "'return'", "'do'", "'while'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", 
                     "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", 
                     "'>='", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLLIT", "BOOLTYPE", "INTTYPE", "FLOATTYPE", 
                      "STRINGTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "ELSE", 
                      "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", 
                      "ADD", "SUB", "MUL", "DIV", "NOT", "MOD", "OR", "AND", 
                      "NEQ", "EQ", "LT", "GT", "LTE", "GTE", "ASN", "LB", 
                      "RB", "LP", "RP", "LS", "RS", "SM", "CM", "ID", "INTLIT", 
                      "FLOATLIT", "STRLIT", "WS", "BLOCKCMT", "LINECMT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_varDecl = 2
    RULE_listVar = 3
    RULE_var = 4
    RULE_funcDecl = 5
    RULE_functive = 6
    RULE_paralist = 7
    RULE_paradecl = 8
    RULE_primitive = 9
    RULE_arrayPointerType = 10
    RULE_express = 11
    RULE_express_asn = 12
    RULE_express_or = 13
    RULE_express_and = 14
    RULE_express_ENEQ = 15
    RULE_express_LTGT = 16
    RULE_express_ADDSUB = 17
    RULE_express_MulDivMod = 18
    RULE_express_Neg = 19
    RULE_express_LS = 20
    RULE_operands = 21
    RULE_lits = 22
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
    RULE_block_mem = 34

    ruleNames =  [ "program", "decls", "varDecl", "listVar", "var", "funcDecl", 
                   "functive", "paralist", "paradecl", "primitive", "arrayPointerType", 
                   "express", "express_asn", "express_or", "express_and", 
                   "express_ENEQ", "express_LTGT", "express_ADDSUB", "express_MulDivMod", 
                   "express_Neg", "express_LS", "operands", "lits", "func_call", 
                   "list_express", "statement", "if_stmt", "doWhile_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "expression_stmt", "block_stmt", "block_mem" ]

    EOF = Token.EOF
    BOOLLIT=1
    BOOLTYPE=2
    INTTYPE=3
    FLOATTYPE=4
    STRINGTYPE=5
    VOIDTYPE=6
    BREAK=7
    CONTINUE=8
    ELSE=9
    FOR=10
    IF=11
    RETURN=12
    DO=13
    WHILE=14
    TRUE=15
    FALSE=16
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
    STRLIT=43
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

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclsContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclsContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.decls()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 75
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MCParser.VarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MCParser.FuncDeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decls




    def decls(self):

        localctx = MCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.funcDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(MCParser.PrimitiveContext,0)


        def listVar(self):
            return self.getTypedRuleContext(MCParser.ListVarContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varDecl




    def varDecl(self):

        localctx = MCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.primitive()
            self.state = 82
            self.listVar()
            self.state = 83
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_listVar




    def listVar(self):

        localctx = MCParser.ListVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listVar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.var()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 86
                self.match(MCParser.CM)
                self.state = 87
                self.var()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(MCParser.ID)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 94
                self.match(MCParser.LS)
                self.state = 95
                self.match(MCParser.INTLIT)
                self.state = 96
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):

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
            return MCParser.RULE_funcDecl




    def funcDecl(self):

        localctx = MCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.functive()
            self.state = 100
            self.match(MCParser.ID)
            self.state = 101
            self.match(MCParser.LB)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 102
                self.paralist()


            self.state = 105
            self.match(MCParser.RB)
            self.state = 106
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
        self.enterRule(localctx, 12, self.RULE_functive)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
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
        self.enterRule(localctx, 14, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.paradecl()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 114
                self.match(MCParser.CM)
                self.state = 115
                self.paradecl()
                self.state = 120
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
        self.enterRule(localctx, 16, self.RULE_paradecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.primitive()
            self.state = 122
            self.match(MCParser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 123
                self.match(MCParser.LS)
                self.state = 124
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

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

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
            self.state = 127
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_arrayPointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.primitive()
            self.state = 130
            self.match(MCParser.LS)
            self.state = 131
            self.match(MCParser.RS)
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
        self.enterRule(localctx, 22, self.RULE_express)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.express_asn(0)
                self.state = 134
                self.match(MCParser.ASN)
                self.state = 135
                self.express()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_express_asn, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.express_or(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_asnContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_asn)
                    self.state = 143
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 144
                    self.match(MCParser.OR)
                    self.state = 145
                    self.express_or(0) 
                self.state = 150
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_express_or, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.express_and()
            self._ctx.stop = self._input.LT(-1)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_orContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_or)
                    self.state = 154
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 155
                    self.match(MCParser.AND)
                    self.state = 156
                    self.express_and() 
                self.state = 161
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
        self.enterRule(localctx, 28, self.RULE_express_and)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.express_ENEQ()
                self.state = 163
                _la = self._input.LA(1)
                if not(_la==MCParser.NEQ or _la==MCParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.express_ENEQ()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_express_ENEQ)
        self._la = 0 # Token type
        try:
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.express_LTGT(0)
                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT) | (1 << MCParser.GT) | (1 << MCParser.LTE) | (1 << MCParser.GTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.express_LTGT(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_express_LTGT, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.express_ADDSUB(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_LTGTContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_LTGT)
                    self.state = 179
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 180
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 181
                    self.express_ADDSUB(0) 
                self.state = 186
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

        def express_MulDivMod(self):
            return self.getTypedRuleContext(MCParser.Express_MulDivModContext,0)


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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_express_ADDSUB, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.express_MulDivMod()
            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Express_ADDSUBContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_express_ADDSUB)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 192
                    self.express_MulDivMod() 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Express_MulDivModContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def express_MulDivMod(self):
            return self.getTypedRuleContext(MCParser.Express_MulDivModContext,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def express_Neg(self):
            return self.getTypedRuleContext(MCParser.Express_NegContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_express_MulDivMod




    def express_MulDivMod(self):

        localctx = MCParser.Express_MulDivModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_express_MulDivMod)
        self._la = 0 # Token type
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB, MCParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB or _la==MCParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.express_MulDivMod()
                pass
            elif token in [MCParser.BOOLLIT, MCParser.LB, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_express_Neg




    def express_Neg(self):

        localctx = MCParser.Express_NegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_express_Neg)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.express_LS()
                self.state = 204
                self.match(MCParser.LS)
                self.state = 205
                self.express()
                self.state = 206
                self.match(MCParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.express_LS()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(MCParser.ID)
                self.state = 210
                self.match(MCParser.LS)
                self.state = 211
                self.express()
                self.state = 212
                self.match(MCParser.RS)
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
        self.enterRule(localctx, 40, self.RULE_express_LS)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLLIT, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.operands()
                pass
            elif token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(MCParser.LB)
                self.state = 218
                self.express()
                self.state = 219
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

        def func_call(self):
            return self.getTypedRuleContext(MCParser.Func_callContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operands




    def operands(self):

        localctx = MCParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operands)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.lits()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(MCParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
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

        def STRLIT(self):
            return self.getToken(MCParser.STRLIT, 0)

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
        self.enterRule(localctx, 44, self.RULE_lits)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0)):
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
            self.state = 230
            self.match(MCParser.ID)
            self.state = 231
            self.match(MCParser.LB)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0):
                self.state = 232
                self.list_express()


            self.state = 235
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
            self.state = 237
            self.express()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 238
                self.match(MCParser.CM)
                self.state = 239
                self.express()
                self.state = 244
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
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.if_stmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.doWhile_stmt()
                self.state = 247
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.for_stmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.break_stmt()
                self.state = 251
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.continue_stmt()
                self.state = 254
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 256
                self.return_stmt()
                self.state = 257
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.BOOLLIT, MCParser.SUB, MCParser.NOT, MCParser.LB, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 259
                self.expression_stmt()
                self.state = 260
                self.match(MCParser.SM)
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 262
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
            self.state = 265
            self.match(MCParser.IF)
            self.state = 266
            self.match(MCParser.LB)
            self.state = 267
            self.express()
            self.state = 268
            self.match(MCParser.RB)
            self.state = 269
            self.statement()
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 270
                self.match(MCParser.ELSE)
                self.state = 271
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
            self.state = 274
            self.match(MCParser.DO)
            self.state = 276 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 275
                self.statement()
                self.state = 278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0)):
                    break

            self.state = 280
            self.match(MCParser.WHILE)
            self.state = 281
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
            self.state = 283
            self.match(MCParser.FOR)
            self.state = 284
            self.match(MCParser.LB)
            self.state = 285
            self.express()
            self.state = 286
            self.match(MCParser.SM)
            self.state = 287
            self.express()
            self.state = 288
            self.match(MCParser.SM)
            self.state = 289
            self.express()
            self.state = 290
            self.match(MCParser.RB)
            self.state = 291
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
            self.state = 293
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
            self.state = 295
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
            self.state = 297
            self.match(MCParser.RETURN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0):
                self.state = 298
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
            self.state = 301
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

        def block_mem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Block_memContext)
            else:
                return self.getTypedRuleContext(MCParser.Block_memContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_stmt




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(MCParser.LP)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.SUB) | (1 << MCParser.NOT) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0):
                self.state = 304
                self.block_mem()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 310
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_memContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(MCParser.VarDeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_block_mem




    def block_mem(self):

        localctx = MCParser.Block_memContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_mem)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.varDecl()
                pass
            elif token in [MCParser.BOOLLIT, MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.SUB, MCParser.NOT, MCParser.LB, MCParser.LP, MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.statement()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.express_asn_sempred
        self._predicates[13] = self.express_or_sempred
        self._predicates[16] = self.express_LTGT_sempred
        self._predicates[17] = self.express_ADDSUB_sempred
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
         




