# Generated from c:\PrinciplesOfProgrammingLanguage\a1\initial\src\main\mc\parser\MC.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u017d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\7)\u00fe\n)\f)\16)\u0101\13)\3*\6*\u0104\n*\r*\16")
        buf.write("*\u0105\3+\3+\3+\3+\5+\u010c\n+\3+\6+\u010f\n+\r+\16+")
        buf.write("\u0110\5+\u0113\n+\3,\6,\u0116\n,\r,\16,\u0117\3,\3,\7")
        buf.write(",\u011c\n,\f,\16,\u011f\13,\5,\u0121\n,\3,\7,\u0124\n")
        buf.write(",\f,\16,\u0127\13,\3,\3,\7,\u012b\n,\f,\16,\u012e\13,")
        buf.write("\6,\u0130\n,\r,\16,\u0131\5,\u0134\n,\3-\3-\7-\u0138\n")
        buf.write("-\f-\16-\u013b\13-\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\5\60\u0148\n\60\3\61\3\61\3\62\6\62\u014d\n\62\r\62\16")
        buf.write("\62\u014e\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u0157\n\63")
        buf.write("\f\63\16\63\u015a\13\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\7\64\u0165\n\64\f\64\16\64\u0168\13\64")
        buf.write("\3\64\3\64\3\65\3\65\7\65\u016e\n\65\f\65\16\65\u0171")
        buf.write("\13\65\3\66\3\66\7\66\u0175\n\66\f\66\16\66\u0178\13\66")
        buf.write("\3\66\3\66\3\67\3\67\3\u0158\28\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y-[\2]\2_\2")
        buf.write("a\2c.e/g\60i\61k\62m\63\3\2\13\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\3\2\62;\4\2GGgg\3\2\60\60\t\2$$^^ddhhppttvv\6\2\f")
        buf.write("\f\17\17$$^^\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u018b")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2Y\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2")
        buf.write("\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3q\3\2\2\2\5s\3")
        buf.write("\2\2\2\7y\3\2\2\2\t\u0082\3\2\2\2\13\u0087\3\2\2\2\r\u008b")
        buf.write("\3\2\2\2\17\u008e\3\2\2\2\21\u0095\3\2\2\2\23\u0098\3")
        buf.write("\2\2\2\25\u009e\3\2\2\2\27\u00a3\3\2\2\2\31\u00a9\3\2")
        buf.write("\2\2\33\u00b1\3\2\2\2\35\u00b5\3\2\2\2\37\u00bb\3\2\2")
        buf.write("\2!\u00c2\3\2\2\2#\u00c7\3\2\2\2%\u00c9\3\2\2\2\'\u00cb")
        buf.write("\3\2\2\2)\u00cd\3\2\2\2+\u00cf\3\2\2\2-\u00d1\3\2\2\2")
        buf.write("/\u00d3\3\2\2\2\61\u00d6\3\2\2\2\63\u00d9\3\2\2\2\65\u00dc")
        buf.write("\3\2\2\2\67\u00df\3\2\2\29\u00e1\3\2\2\2;\u00e3\3\2\2")
        buf.write("\2=\u00e6\3\2\2\2?\u00e9\3\2\2\2A\u00eb\3\2\2\2C\u00ed")
        buf.write("\3\2\2\2E\u00ef\3\2\2\2G\u00f1\3\2\2\2I\u00f3\3\2\2\2")
        buf.write("K\u00f5\3\2\2\2M\u00f7\3\2\2\2O\u00f9\3\2\2\2Q\u00fb\3")
        buf.write("\2\2\2S\u0103\3\2\2\2U\u0112\3\2\2\2W\u0133\3\2\2\2Y\u0135")
        buf.write("\3\2\2\2[\u013f\3\2\2\2]\u0142\3\2\2\2_\u0147\3\2\2\2")
        buf.write("a\u0149\3\2\2\2c\u014c\3\2\2\2e\u0152\3\2\2\2g\u0160\3")
        buf.write("\2\2\2i\u016b\3\2\2\2k\u0172\3\2\2\2m\u017b\3\2\2\2or")
        buf.write("\5\25\13\2pr\5\27\f\2qo\3\2\2\2qp\3\2\2\2r\4\3\2\2\2s")
        buf.write("t\7d\2\2tu\7t\2\2uv\7g\2\2vw\7c\2\2wx\7m\2\2x\6\3\2\2")
        buf.write("\2yz\7e\2\2z{\7q\2\2{|\7p\2\2|}\7v\2\2}~\7k\2\2~\177\7")
        buf.write("p\2\2\177\u0080\7w\2\2\u0080\u0081\7g\2\2\u0081\b\3\2")
        buf.write("\2\2\u0082\u0083\7g\2\2\u0083\u0084\7n\2\2\u0084\u0085")
        buf.write("\7u\2\2\u0085\u0086\7g\2\2\u0086\n\3\2\2\2\u0087\u0088")
        buf.write("\7h\2\2\u0088\u0089\7q\2\2\u0089\u008a\7t\2\2\u008a\f")
        buf.write("\3\2\2\2\u008b\u008c\7k\2\2\u008c\u008d\7h\2\2\u008d\16")
        buf.write("\3\2\2\2\u008e\u008f\7t\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7v\2\2\u0091\u0092\7w\2\2\u0092\u0093\7t\2\2\u0093\u0094")
        buf.write("\7p\2\2\u0094\20\3\2\2\2\u0095\u0096\7f\2\2\u0096\u0097")
        buf.write("\7q\2\2\u0097\22\3\2\2\2\u0098\u0099\7y\2\2\u0099\u009a")
        buf.write("\7j\2\2\u009a\u009b\7k\2\2\u009b\u009c\7n\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\24\3\2\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7g\2\2\u00a2\26")
        buf.write("\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7n\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7g\2\2\u00a8\30")
        buf.write("\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write("\7c\2\2\u00af\u00b0\7p\2\2\u00b0\32\3\2\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\34")
        buf.write("\3\2\2\2\u00b5\u00b6\7h\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7v\2\2\u00ba\36")
        buf.write("\3\2\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1 \3\2\2\2\u00c2\u00c3\7x\2\2\u00c3\u00c4")
        buf.write("\7q\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7f\2\2\u00c6\"")
        buf.write("\3\2\2\2\u00c7\u00c8\7-\2\2\u00c8$\3\2\2\2\u00c9\u00ca")
        buf.write("\7/\2\2\u00ca&\3\2\2\2\u00cb\u00cc\7,\2\2\u00cc(\3\2\2")
        buf.write("\2\u00cd\u00ce\7\61\2\2\u00ce*\3\2\2\2\u00cf\u00d0\7#")
        buf.write("\2\2\u00d0,\3\2\2\2\u00d1\u00d2\7\'\2\2\u00d2.\3\2\2\2")
        buf.write("\u00d3\u00d4\7~\2\2\u00d4\u00d5\7~\2\2\u00d5\60\3\2\2")
        buf.write("\2\u00d6\u00d7\7(\2\2\u00d7\u00d8\7(\2\2\u00d8\62\3\2")
        buf.write("\2\2\u00d9\u00da\7#\2\2\u00da\u00db\7?\2\2\u00db\64\3")
        buf.write("\2\2\2\u00dc\u00dd\7?\2\2\u00dd\u00de\7?\2\2\u00de\66")
        buf.write("\3\2\2\2\u00df\u00e0\7>\2\2\u00e08\3\2\2\2\u00e1\u00e2")
        buf.write("\7@\2\2\u00e2:\3\2\2\2\u00e3\u00e4\7>\2\2\u00e4\u00e5")
        buf.write("\7?\2\2\u00e5<\3\2\2\2\u00e6\u00e7\7@\2\2\u00e7\u00e8")
        buf.write("\7?\2\2\u00e8>\3\2\2\2\u00e9\u00ea\7?\2\2\u00ea@\3\2\2")
        buf.write("\2\u00eb\u00ec\7*\2\2\u00ecB\3\2\2\2\u00ed\u00ee\7+\2")
        buf.write("\2\u00eeD\3\2\2\2\u00ef\u00f0\7}\2\2\u00f0F\3\2\2\2\u00f1")
        buf.write("\u00f2\7\177\2\2\u00f2H\3\2\2\2\u00f3\u00f4\7]\2\2\u00f4")
        buf.write("J\3\2\2\2\u00f5\u00f6\7_\2\2\u00f6L\3\2\2\2\u00f7\u00f8")
        buf.write("\7=\2\2\u00f8N\3\2\2\2\u00f9\u00fa\7.\2\2\u00faP\3\2\2")
        buf.write("\2\u00fb\u00ff\t\2\2\2\u00fc\u00fe\t\3\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100R\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0104\t\4\2\2\u0103\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106T\3\2\2")
        buf.write("\2\u0107\u0113\5W,\2\u0108\u0109\5W,\2\u0109\u010b\t\5")
        buf.write("\2\2\u010a\u010c\7/\2\2\u010b\u010a\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010e\3\2\2\2\u010d\u010f\t\4\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0113\3\2\2\2\u0112\u0107\3")
        buf.write("\2\2\2\u0112\u0108\3\2\2\2\u0113V\3\2\2\2\u0114\u0116")
        buf.write("\t\4\2\2\u0115\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0120\3\2\2\2")
        buf.write("\u0119\u011d\t\6\2\2\u011a\u011c\t\4\2\2\u011b\u011a\3")
        buf.write("\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3\2\2\2\u0120")
        buf.write("\u0119\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0134\3\2\2\2")
        buf.write("\u0122\u0124\t\4\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3")
        buf.write("\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u012f")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012c\t\6\2\2\u0129")
        buf.write("\u012b\t\4\2\2\u012a\u0129\3\2\2\2\u012b\u012e\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u0130\3")
        buf.write("\2\2\2\u012e\u012c\3\2\2\2\u012f\u0128\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0134\3\2\2\2\u0133\u0115\3\2\2\2\u0133\u0125\3\2\2\2")
        buf.write("\u0134X\3\2\2\2\u0135\u0139\5a\61\2\u0136\u0138\5_\60")
        buf.write("\2\u0137\u0136\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013c\u013d\5a\61\2\u013d\u013e\b-\2\2")
        buf.write("\u013eZ\3\2\2\2\u013f\u0140\7^\2\2\u0140\u0141\t\7\2\2")
        buf.write("\u0141\\\3\2\2\2\u0142\u0143\7^\2\2\u0143\u0144\n\7\2")
        buf.write("\2\u0144^\3\2\2\2\u0145\u0148\n\b\2\2\u0146\u0148\5[.")
        buf.write("\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148`\3\2")
        buf.write("\2\2\u0149\u014a\7$\2\2\u014ab\3\2\2\2\u014b\u014d\t\t")
        buf.write("\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\b\62\3\2\u0151d\3\2\2\2\u0152\u0153\7\61\2\2\u0153")
        buf.write("\u0154\7,\2\2\u0154\u0158\3\2\2\2\u0155\u0157\13\2\2\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0159\3")
        buf.write("\2\2\2\u0158\u0156\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158")
        buf.write("\3\2\2\2\u015b\u015c\7,\2\2\u015c\u015d\7\61\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u015f\b\63\3\2\u015ff\3\2\2\2\u0160")
        buf.write("\u0161\7\61\2\2\u0161\u0162\7\61\2\2\u0162\u0166\3\2\2")
        buf.write("\2\u0163\u0165\n\n\2\2\u0164\u0163\3\2\2\2\u0165\u0168")
        buf.write("\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a\b\64\3")
        buf.write("\2\u016ah\3\2\2\2\u016b\u016f\5a\61\2\u016c\u016e\5_\60")
        buf.write("\2\u016d\u016c\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u016f\u0170\3\2\2\2\u0170j\3\2\2\2\u0171\u016f")
        buf.write("\3\2\2\2\u0172\u0176\5a\61\2\u0173\u0175\5_\60\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177\u0179\3\2\2\2\u0178\u0176\3")
        buf.write("\2\2\2\u0179\u017a\5]/\2\u017al\3\2\2\2\u017b\u017c\13")
        buf.write("\2\2\2\u017cn\3\2\2\2\27\2q\u00ff\u0105\u010b\u0110\u0112")
        buf.write("\u0117\u011d\u0120\u0125\u012c\u0131\u0133\u0139\u0147")
        buf.write("\u014e\u0158\u0166\u016f\u0176\4\3-\2\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    BREAK = 2
    CONTINUE = 3
    ELSE = 4
    FOR = 5
    IF = 6
    RETURN = 7
    DO = 8
    WHILE = 9
    TRUE = 10
    FALSE = 11
    BOOLEANTYPE = 12
    INTTYPE = 13
    FLOATTYPE = 14
    STRINGTYPE = 15
    VOIDTYPE = 16
    ADD = 17
    SUB = 18
    MUL = 19
    DIV = 20
    NOT = 21
    MOD = 22
    OR = 23
    AND = 24
    NEQ = 25
    EQ = 26
    LT = 27
    GT = 28
    LTE = 29
    GTE = 30
    ASN = 31
    LB = 32
    RB = 33
    LP = 34
    RP = 35
    LS = 36
    RS = 37
    SM = 38
    CM = 39
    ID = 40
    INTLIT = 41
    FLOATLIT = 42
    STRINGLIT = 43
    WS = 44
    BLOCKCMT = 45
    LINECMT = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'else'", "'for'", "'if'", "'return'", 
            "'do'", "'while'", "'true'", "'false'", "'boolean'", "'int'", 
            "'float'", "'string'", "'void'", "'+'", "'-'", "'*'", "'/'", 
            "'!'", "'%'", "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", 
            "'<='", "'>='", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", 
            "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", 
            "DO", "WHILE", "TRUE", "FALSE", "BOOLEANTYPE", "INTTYPE", "FLOATTYPE", 
            "STRINGTYPE", "VOIDTYPE", "ADD", "SUB", "MUL", "DIV", "NOT", 
            "MOD", "OR", "AND", "NEQ", "EQ", "LT", "GT", "LTE", "GTE", "ASN", 
            "LB", "RB", "LP", "RP", "LS", "RS", "SM", "CM", "ID", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "BLOCKCMT", "LINECMT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLLIT", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", 
                  "DO", "WHILE", "TRUE", "FALSE", "BOOLEANTYPE", "INTTYPE", 
                  "FLOATTYPE", "STRINGTYPE", "VOIDTYPE", "ADD", "SUB", "MUL", 
                  "DIV", "NOT", "MOD", "OR", "AND", "NEQ", "EQ", "LT", "GT", 
                  "LTE", "GTE", "ASN", "LB", "RB", "LP", "RP", "LS", "RS", 
                  "SM", "CM", "ID", "INTLIT", "FLOATLIT", "DECP", "STRINGLIT", 
                  "ESC", "ILLEGAL_ESC", "STR_CHAR", "DOUBLEQUOTES", "WS", 
                  "BLOCKCMT", "LINECMT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[43] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text=self.text[1:-1]

     


