# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u018f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\5\2|\n\2\3\3\3\3\3\3\3\3\7\3\u0082")
        buf.write("\n\3\f\3\16\3\u0085\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4\u0090\n\4\f\4\16\4\u0093\13\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\6\24")
        buf.write("\u00ec\n\24\r\24\16\24\u00ed\3\25\3\25\5\25\u00f2\n\25")
        buf.write("\3\26\3\26\3\26\5\26\u00f7\n\26\3\26\5\26\u00fa\n\26\3")
        buf.write("\26\3\26\5\26\u00fe\n\26\3\27\3\27\5\27\u0102\n\27\3\27")
        buf.write("\3\27\5\27\u0106\n\27\3\27\3\27\3\30\3\30\3\30\7\30\u010d")
        buf.write("\n\30\f\30\16\30\u0110\13\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u011c\n\31\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\68\u0168\n8\r8\168\u0169\38\7")
        buf.write("8\u016d\n8\f8\168\u0170\138\39\69\u0173\n9\r9\169\u0174")
        buf.write("\39\39\3:\3:\7:\u017b\n:\f:\16:\u017e\13:\3:\3:\3:\3:")
        buf.write("\3;\3;\3;\7;\u0187\n;\f;\16;\u018a\13;\3;\3;\3<\3<\3\u0083")
        buf.write("\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\2-\2/\27")
        buf.write("\61\2\63\2\65\2\67\29\2;\2=\2?\2A\30C\31E\32G\33I\34K")
        buf.write("\35M\36O\37Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61")
        buf.write("u\62w\63\3\2\13\4\2\f\f\17\17\3\2\62;\4\2GGgg\6\2\f\f")
        buf.write("\17\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"")
        buf.write("\"\5\2\n\f\16\17^^\t\2$$^^ddhhppttvv\2\u019c\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2/\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\3{\3\2\2\2\5}\3\2\2\2\7\u008b\3\2")
        buf.write("\2\2\t\u0096\3\2\2\2\13\u009a\3\2\2\2\r\u009f\3\2\2\2")
        buf.write("\17\u00a7\3\2\2\2\21\u00ad\3\2\2\2\23\u00b6\3\2\2\2\25")
        buf.write("\u00bb\3\2\2\2\27\u00bf\3\2\2\2\31\u00c5\3\2\2\2\33\u00c8")
        buf.write("\3\2\2\2\35\u00cf\3\2\2\2\37\u00d2\3\2\2\2!\u00d8\3\2")
        buf.write("\2\2#\u00dd\3\2\2\2%\u00e3\3\2\2\2\'\u00eb\3\2\2\2)\u00f1")
        buf.write("\3\2\2\2+\u00fd\3\2\2\2-\u0101\3\2\2\2/\u0109\3\2\2\2")
        buf.write("\61\u011b\3\2\2\2\63\u011d\3\2\2\2\65\u0120\3\2\2\2\67")
        buf.write("\u0123\3\2\2\29\u0126\3\2\2\2;\u0129\3\2\2\2=\u012c\3")
        buf.write("\2\2\2?\u012f\3\2\2\2A\u0132\3\2\2\2C\u0134\3\2\2\2E\u0136")
        buf.write("\3\2\2\2G\u0138\3\2\2\2I\u013a\3\2\2\2K\u013c\3\2\2\2")
        buf.write("M\u013e\3\2\2\2O\u0140\3\2\2\2Q\u0142\3\2\2\2S\u0144\3")
        buf.write("\2\2\2U\u0146\3\2\2\2W\u0148\3\2\2\2Y\u014b\3\2\2\2[\u014e")
        buf.write("\3\2\2\2]\u0150\3\2\2\2_\u0153\3\2\2\2a\u0155\3\2\2\2")
        buf.write("c\u0157\3\2\2\2e\u0159\3\2\2\2g\u015b\3\2\2\2i\u015e\3")
        buf.write("\2\2\2k\u0161\3\2\2\2m\u0163\3\2\2\2o\u0167\3\2\2\2q\u0172")
        buf.write("\3\2\2\2s\u0178\3\2\2\2u\u0183\3\2\2\2w\u018d\3\2\2\2")
        buf.write("y|\5!\21\2z|\5#\22\2{y\3\2\2\2{z\3\2\2\2|\4\3\2\2\2}~")
        buf.write("\7\61\2\2~\177\7,\2\2\177\u0083\3\2\2\2\u0080\u0082\13")
        buf.write("\2\2\2\u0081\u0080\3\2\2\2\u0082\u0085\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0086\3\2\2\2\u0085")
        buf.write("\u0083\3\2\2\2\u0086\u0087\7,\2\2\u0087\u0088\7\61\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008a\b\3\2\2\u008a\6\3\2\2")
        buf.write("\2\u008b\u008c\7\61\2\2\u008c\u008d\7\61\2\2\u008d\u0091")
        buf.write("\3\2\2\2\u008e\u0090\n\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\b")
        buf.write("\4\2\2\u0095\b\3\2\2\2\u0096\u0097\7k\2\2\u0097\u0098")
        buf.write("\7p\2\2\u0098\u0099\7v\2\2\u0099\n\3\2\2\2\u009a\u009b")
        buf.write("\7x\2\2\u009b\u009c\7q\2\2\u009c\u009d\7k\2\2\u009d\u009e")
        buf.write("\7f\2\2\u009e\f\3\2\2\2\u009f\u00a0\7d\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7p\2\2\u00a6\16")
        buf.write("\3\2\2\2\u00a7\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\20")
        buf.write("\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\22")
        buf.write("\3\2\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9")
        buf.write("\7u\2\2\u00b9\u00ba\7g\2\2\u00ba\24\3\2\2\2\u00bb\u00bc")
        buf.write("\7h\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be\7t\2\2\u00be\26")
        buf.write("\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\30")
        buf.write("\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\32")
        buf.write("\3\2\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb")
        buf.write("\7v\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce")
        buf.write("\7p\2\2\u00ce\34\3\2\2\2\u00cf\u00d0\7f\2\2\u00d0\u00d1")
        buf.write("\7q\2\2\u00d1\36\3\2\2\2\u00d2\u00d3\7y\2\2\u00d3\u00d4")
        buf.write("\7j\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7 \3\2\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da")
        buf.write("\7t\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7g\2\2\u00dc\"")
        buf.write("\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7n\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2\7g\2\2\u00e2$\3")
        buf.write("\2\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7i\2\2\u00e9&\3\2\2\2\u00ea\u00ec\t\3\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee(\3\2\2\2\u00ef\u00f2\5+\26\2\u00f0")
        buf.write("\u00f2\5-\27\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2")
        buf.write("\u00f2*\3\2\2\2\u00f3\u00f4\5\'\24\2\u00f4\u00f6\7\60")
        buf.write("\2\2\u00f5\u00f7\5\'\24\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00fe\3\2\2\2\u00f8\u00fa\5\'\24\2\u00f9")
        buf.write("\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fc\7\60\2\2\u00fc\u00fe\5\'\24\2\u00fd\u00f3")
        buf.write("\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fe,\3\2\2\2\u00ff\u0102")
        buf.write("\5\'\24\2\u0100\u0102\5+\26\2\u0101\u00ff\3\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\t\4\2\2")
        buf.write("\u0104\u0106\7/\2\2\u0105\u0104\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\5\'\24\2\u0108")
        buf.write(".\3\2\2\2\u0109\u010e\7$\2\2\u010a\u010d\5\61\31\2\u010b")
        buf.write("\u010d\n\5\2\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2")
        buf.write("\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3")
        buf.write("\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112")
        buf.write("\7$\2\2\u0112\u0113\b\30\3\2\u0113\60\3\2\2\2\u0114\u011c")
        buf.write("\5\63\32\2\u0115\u011c\5\65\33\2\u0116\u011c\5\67\34\2")
        buf.write("\u0117\u011c\59\35\2\u0118\u011c\5;\36\2\u0119\u011c\5")
        buf.write("=\37\2\u011a\u011c\5? \2\u011b\u0114\3\2\2\2\u011b\u0115")
        buf.write("\3\2\2\2\u011b\u0116\3\2\2\2\u011b\u0117\3\2\2\2\u011b")
        buf.write("\u0118\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a\3\2\2\2")
        buf.write("\u011c\62\3\2\2\2\u011d\u011e\7^\2\2\u011e\u011f\7d\2")
        buf.write("\2\u011f\64\3\2\2\2\u0120\u0121\7^\2\2\u0121\u0122\7h")
        buf.write("\2\2\u0122\66\3\2\2\2\u0123\u0124\7^\2\2\u0124\u0125\7")
        buf.write("t\2\2\u01258\3\2\2\2\u0126\u0127\7^\2\2\u0127\u0128\7")
        buf.write("p\2\2\u0128:\3\2\2\2\u0129\u012a\7^\2\2\u012a\u012b\7")
        buf.write("v\2\2\u012b<\3\2\2\2\u012c\u012d\7^\2\2\u012d\u012e\7")
        buf.write("$\2\2\u012e>\3\2\2\2\u012f\u0130\7^\2\2\u0130\u0131\7")
        buf.write("^\2\2\u0131@\3\2\2\2\u0132\u0133\7*\2\2\u0133B\3\2\2\2")
        buf.write("\u0134\u0135\7+\2\2\u0135D\3\2\2\2\u0136\u0137\7}\2\2")
        buf.write("\u0137F\3\2\2\2\u0138\u0139\7\177\2\2\u0139H\3\2\2\2\u013a")
        buf.write("\u013b\7]\2\2\u013bJ\3\2\2\2\u013c\u013d\7_\2\2\u013d")
        buf.write("L\3\2\2\2\u013e\u013f\7.\2\2\u013fN\3\2\2\2\u0140\u0141")
        buf.write("\7=\2\2\u0141P\3\2\2\2\u0142\u0143\7-\2\2\u0143R\3\2\2")
        buf.write("\2\u0144\u0145\7,\2\2\u0145T\3\2\2\2\u0146\u0147\7#\2")
        buf.write("\2\u0147V\3\2\2\2\u0148\u0149\7~\2\2\u0149\u014a\7~\2")
        buf.write("\2\u014aX\3\2\2\2\u014b\u014c\7#\2\2\u014c\u014d\7?\2")
        buf.write("\2\u014dZ\3\2\2\2\u014e\u014f\7>\2\2\u014f\\\3\2\2\2\u0150")
        buf.write("\u0151\7>\2\2\u0151\u0152\7?\2\2\u0152^\3\2\2\2\u0153")
        buf.write("\u0154\7?\2\2\u0154`\3\2\2\2\u0155\u0156\7/\2\2\u0156")
        buf.write("b\3\2\2\2\u0157\u0158\7\61\2\2\u0158d\3\2\2\2\u0159\u015a")
        buf.write("\7\'\2\2\u015af\3\2\2\2\u015b\u015c\7(\2\2\u015c\u015d")
        buf.write("\7(\2\2\u015dh\3\2\2\2\u015e\u015f\7?\2\2\u015f\u0160")
        buf.write("\7?\2\2\u0160j\3\2\2\2\u0161\u0162\7@\2\2\u0162l\3\2\2")
        buf.write("\2\u0163\u0164\7@\2\2\u0164\u0165\7?\2\2\u0165n\3\2\2")
        buf.write("\2\u0166\u0168\t\6\2\2\u0167\u0166\3\2\2\2\u0168\u0169")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016e\3\2\2\2\u016b\u016d\t\7\2\2\u016c\u016b\3\2\2\2")
        buf.write("\u016d\u0170\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3")
        buf.write("\2\2\2\u016fp\3\2\2\2\u0170\u016e\3\2\2\2\u0171\u0173")
        buf.write("\t\b\2\2\u0172\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0177\b9\2\2\u0177r\3\2\2\2\u0178\u017c\7$\2\2")
        buf.write("\u0179\u017b\n\t\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\7^\2\2\u0180")
        buf.write("\u0181\n\n\2\2\u0181\u0182\b:\4\2\u0182t\3\2\2\2\u0183")
        buf.write("\u0188\7$\2\2\u0184\u0187\5\61\31\2\u0185\u0187\n\5\2")
        buf.write("\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\b;\5\2")
        buf.write("\u018cv\3\2\2\2\u018d\u018e\13\2\2\2\u018ex\3\2\2\2\26")
        buf.write("\2{\u0083\u0091\u00ed\u00f1\u00f6\u00f9\u00fd\u0101\u0105")
        buf.write("\u010c\u010e\u011b\u0169\u016e\u0174\u017c\u0186\u0188")
        buf.write("\6\b\2\2\3\30\2\3:\3\3;\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEANLIT = 1
    COMMENT = 2
    LINECOMMENT = 3
    INTTYPE = 4
    VOIDTYPE = 5
    BOOLTYPE = 6
    BREAK = 7
    CONTINUE = 8
    ELSE = 9
    FOR = 10
    FLOATTYPE = 11
    IF = 12
    RETURN = 13
    DO = 14
    WHILE = 15
    TRUE = 16
    FALSE = 17
    STRINGTYPE = 18
    INTLIT = 19
    FLOATLIT = 20
    STRINGLIT = 21
    LB = 22
    RB = 23
    LP = 24
    RP = 25
    LSB = 26
    RSB = 27
    COMMA = 28
    SEMI = 29
    ADD = 30
    MUL = 31
    NOT = 32
    OR = 33
    NE = 34
    LT = 35
    LTOE = 36
    ASSIGN = 37
    SUB = 38
    DIV = 39
    MOD = 40
    AND = 41
    EQ = 42
    GT = 43
    GTOE = 44
    ID = 45
    WS = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'boolean'", "'break'", "'continue'", "'else'", 
            "'for'", "'float'", "'if'", "'return'", "'do'", "'while'", "'true'", 
            "'false'", "'string'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "','", "';'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
            "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEANLIT", "COMMENT", "LINECOMMENT", "INTTYPE", "VOIDTYPE", 
            "BOOLTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", "FLOATTYPE", 
            "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "STRINGTYPE", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "LB", "RB", "LP", "RP", "LSB", 
            "RSB", "COMMA", "SEMI", "ADD", "MUL", "NOT", "OR", "NE", "LT", 
            "LTOE", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", "GT", "GTOE", 
            "ID", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "BOOLEANLIT", "COMMENT", "LINECOMMENT", "INTTYPE", "VOIDTYPE", 
                  "BOOLTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", "FLOATTYPE", 
                  "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "STRINGTYPE", 
                  "INTLIT", "FLOATLIT", "FloatWithoutExponent", "FloatWithExponent", 
                  "STRINGLIT", "EscapseSequence", "BackSpace", "FromFeed", 
                  "CarriageReturn", "Newline", "HorizontalTab", "DoubleQuote", 
                  "Backslash", "LB", "RB", "LP", "RP", "LSB", "RSB", "COMMA", 
                  "SEMI", "ADD", "MUL", "NOT", "OR", "NE", "LT", "LTOE", 
                  "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", "GT", "GTOE", 
                  "ID", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[22] = self.STRINGLIT_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text[1:]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:]
     


