from main.mc.utils.AST import IntType
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
  
    def test_simple_vardecl_int(self):
    	input = """ int a;"""
    	expect = str(Program([VarDecl('a',IntType())]))
    	self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_simple_program_int_array_and_int(self):
        input = """int c[2],b,c; """
        expect = str(Program([VarDecl('c',ArrayType(2,IntType())),VarDecl('b',IntType()),VarDecl('c',IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_simple_vardecl_float(self):
    	input = """ float a;"""
    	expect = str(Program([VarDecl('a',FloatType())]))
    	self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_simple_vardecl_boolean(self):
    	input = """ boolean a;"""
    	expect = str(Program([VarDecl('a',BoolType())]))
    	self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_simple_vardecl_string(self):
    	input = """ string a;"""
    	expect = str(Program([VarDecl('a',StringType())]))
    	self.assertTrue(TestAST.checkASTGen(input,expect,305)) 
    def test_simple_vardecl_array(self):
    	input = """ int a[5];"""
    	expect = str(Program([VarDecl('a',ArrayType(5,IntType()))]))
    	self.assertTrue(TestAST.checkASTGen(input,expect,306)) 
    def test_many_variables_declaration_int(self):
        input = """int a,b,c;
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_many_variables_declaration_float(self):
        input = """float a,b,c;
        """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_many_variables_declaration_boolean(self):
        input = """boolean a,b,c;
        """
        expect = str(Program([VarDecl("a",BoolType()),VarDecl("b",BoolType()),VarDecl("c",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_many_variables_declaration_string(self):
        input = """string a,b,c;
        """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),VarDecl("c",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_many_variables_declaration_with_arrays(self):
        input = """float a[2],b[3],c[4];
        """
        expect = str(Program([VarDecl("a",ArrayType(2,FloatType())),VarDecl("b",ArrayType(3,FloatType())),VarDecl("c",ArrayType(4,FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_function_declaration_int_no_parameter_no_content_in_block_statement(self):
        input = """int funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_function_declaration_float_no_parameter_no_content_in_block_statement(self):
        input = """float funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_function_declaration_boolean_no_parameter_no_content_in_block_statement(self):
        input = """boolean funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_function_declaration_string_no_parameter_no_content_in_block_statement(self):
        input = """string funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315)) 
    def test_function_declaration_void_no_parameter_no_content_in_block_statement(self):
        input = """void funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_function_declaration_array_pointer_no_parameter_no_content_in_block_statement(self):
        input = """int[] funcdecl(){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_function_declaration_int_one_parameter_no_content_in_block_statement(self):
        input = """int funcdecl(int a){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_function_declaration_float_one_parameter_no_content_in_block_statement(self):
        input = """float funcdecl(int a){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_function_declaration_boolean_one_parameter_no_content_in_block_statement(self):
        input = """boolean funcdecl(float a){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",FloatType())],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_function_declaration_string_one_parameter_no_content_in_block_statement(self):
        input = """string funcdecl(boolean a){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",BoolType())],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_function_declaration_void_one_parameter_no_content_in_block_statement(self):
        input = """void funcdecl(string a){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",StringType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_function_declaration_array_pointer_one_parameter_no_content_in_block_statement(self):
        input = """float[] funcdecl(int c){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("c",IntType())],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_function_declaration_int_many_parameters_no_content_in_block_statement(self):
        input = """int funcdecl(int a,string b,boolean c,float d){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",BoolType()),VarDecl("d",FloatType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_function_declaration_float_many_parameters_no_content_in_block_statement(self):
        input = """float funcdecl(int a,string b,int c,float d,boolean e){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("e",BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_function_declaration_boolean_many_parameters_no_content_in_block_statement(self):
        input = """boolean funcdecl(int a,string b,string c,float d, int f[]){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("f",ArrayPointerType(IntType()))],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_function_declaration_string_many_parameters_no_content_in_block_statement(self):
        input = """string funcdecl(int a,string b, string c,float d ,string n, float a[], string g[]){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType()))],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_function_declaration_void_many_parameters_no_content_in_block_statement(self):
        input = """void funcdecl(int a,string b,string c,float d ,string n, float a[],string g[] ,boolean f){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_function_declaration_array_pointer_many_parameters_no_content_in_block_statement(self):
        input = """int[] funcdecl(int a,string b,string c,float d ,string n, float a[],string g[] ,boolean f){
            
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_function_and_variable_declaration(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_function_declaration_int_many_parameters_with_statements_in_block_statement(self):
        input = """
        int funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return 0;
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_function_declaration_float_many_parameters_with_statements_in_block_statement(self):
        input = """
        float funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return 0.0;
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_function_declaration_boolean_many_parameters_with_statements_in_block_statement(self):
        input = """
        boolean funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return true;
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],BoolType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(BooleanLiteral(True))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_function_declaration_string_many_parameters_with_statements_in_block_statement(self):
        input = """
        string funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return "abc";
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],StringType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(StringLiteral("abc"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_function_declaration_void_many_parameters_with_statements_in_block_statement(self):
        input = """
        void funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return ;
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_function_declaration_array_pointer_many_parameters_with_statements_in_block_statement(self):
        input = """
        float[] funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return d;
        }
        """
        expect = str(Program([FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],ArrayPointerType(FloatType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(Id("d"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_variable_and_function_declaration_int_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return 0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],IntType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(IntLiteral(0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_variable_and_function_declaration_float_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_variable_and_function_declaration_string_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        string funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return "ABCD";
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],StringType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(StringLiteral("ABCD"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_variable_and_function_declaration_boolean_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        boolean funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return false;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],BoolType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_variable_and_function_declaration_void_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        void funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],VoidType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType()))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_variable_and_function_declaration_array_pointer_many_parameters_with_statements_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float[] funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            return e;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],ArrayPointerType(FloatType()),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),Return(Id("e"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_variable_and_function_declaration_with_funcall_with_one_parameter(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_variable_and_function_declaration_with_funcall_with_many_parameters(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            function(a,b,c);
            text(a[2],1,3);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),CallExpr(Id("function"),[Id("a"),Id("b"),Id("c")]),CallExpr(Id("text"),[ArrayCell(Id("a"),IntLiteral(2)),IntLiteral(1),IntLiteral(3)]),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_variable_and_function_declaration_with_some_built_in_fucntion(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            boolean h;
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            getInt();
            putInt(3);
            getFloat();
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),VarDecl("h",BoolType()),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),CallExpr(Id("getInt"),[]),CallExpr(Id("putInt"),[IntLiteral(3)]),CallExpr(Id("getFloat"),[]),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_variable_and_function_declaration_with_assignment_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_variable_and_function_declaration_with_or_operater_equal_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            return 0.0;

        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_variable_and_function_declaration_with_and_operater_equal_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,boolean c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            return 0.0;

        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",BoolType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_variable_and_function_declaration_with_not_equal_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,string c,float d ,string n, float a[], int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_variable_and_function_declaration_assigment_with_many_variables(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b, int c,float d ,string n, float a[],float g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            a = b =c =d =e ;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("a"),BinaryOp("=",Id("b"),BinaryOp("=",Id("c"),BinaryOp("=",Id("d"),Id("e"))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_variable_and_function_declaration_assignment_with_funcall(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,float c,float d ,string n, float a[],int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            b = strin(a,b,c,d);
            a = foo(test(func(d)));
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("b"),CallExpr(Id("strin"),[Id("a"),Id("b"),Id("c"),Id("d")])),BinaryOp("=",Id("a"),CallExpr(Id("foo"),[CallExpr(Id("test"),[CallExpr(Id("func"),[Id("d")])])])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_variable_and_function_declaration_with_smaller_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,boolean c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            s = (c<d) || (b<e); 
            r = (a < e) &&( b != e);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",BoolType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_variable_and_function_declaration_with_greater_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,float c,float d ,string n, float a[], string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_variable_and_function_declaration_with_smaller_or_equal_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],float g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            s = (c<d) || (b <=e); 
            r = (a <= e)&& ( b != e);
            a = (b > c) != (a <= d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<=",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<=",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<=",Id("a"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_variable_and_function_declaration_with_greater_or_equal_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[], int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a == 12 || b == c ;
            d = c == 13 && e == c;
            c = a == b || e != d && e == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b >= c) != (a < d);
            f = c >= a;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),IntLiteral(12)),BinaryOp("==",Id("b"),Id("c")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",Id("c"),IntLiteral(13)),BinaryOp("==",Id("e"),Id("c")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">=",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),BinaryOp("=",Id("f"),BinaryOp(">=",Id("c"),Id("a"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_variable_and_function_declaration_with_plus_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a + 12 == c|| b + c == d;
            d = c + 13 == a && e + c == b;
            c = a == b || e != d && e == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("+",Id("a"),IntLiteral(12)),Id("c")),BinaryOp("==",BinaryOp("+",Id("b"),Id("c")),Id("d")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",BinaryOp("+",Id("c"),IntLiteral(13)),Id("a")),BinaryOp("==",BinaryOp("+",Id("e"),Id("c")),Id("b")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("e"),Id("d")),BinaryOp("==",Id("e"),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_variable_and_function_declaration_with_minus_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[], int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a + 12 == d || b - c != e ;
            d = c + 13 == a && e - c != f;
            c = a - b == 5|| (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("+",Id("a"),IntLiteral(12)),Id("d")),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),Id("e")))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp("==",BinaryOp("+",Id("c"),IntLiteral(13)),Id("a")),BinaryOp("!=",BinaryOp("-",Id("e"),Id("c")),Id("f")))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("-",Id("a"),Id("b")),IntLiteral(5)),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_variable_and_function_declaration_with_div_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,int c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c + 13 > 5 && e - c < 6;
            c = a - b == d || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            a = b/c/d/e;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("+",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("-",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("-",Id("a"),Id("b")),Id("d")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_variable_and_function_declaration_with_multi_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            a = b/c/d/e;
            c = a*b*c*d;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_variable_and_function_declaration_with_mod_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& ( b != e);
            a = (b > c) != (a < d);
            a = b/c/d/e;
            c = a*b*c*d;
            d = a%d%4 ;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),BinaryOp("!=",Id("b"),Id("e")))),BinaryOp("=",Id("a"),BinaryOp("!=",BinaryOp(">",Id("b"),Id("c")),BinaryOp("<",Id("a"),Id("d")))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("a"),Id("b")),Id("c")),Id("d"))),BinaryOp("=",Id("d"),BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_variable_and_function_declaration_with_not_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& -( b != e);
            a = -(b > c) != !(a < d);
            a = b/c/d/e;
            c = !a*b*c*d;
            d = a%d%4 ;
            q = ---!a;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d"))),BinaryOp("=",Id("d"),BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",Id("a")))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_variable_and_function_declaration_with_square_bracket_operator(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& -( b != e);
            a = -(b > c) != !(a < d);
            a = b/c/d/e;
            c = !a*b*c*d+d[b+f];
            d = a%d%4 - e[h%n] ;
            q = ---!a[m-n];
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n")))))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_variable_and_function_declaration_with_index_expression(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& -( b != e);
            a = -(b > c) != !(a < d);
            a = b/c/d/e;
            c = !a*b*c*d+d[b+f];
            d = a%d%4 - e[h%n] ;
            foo(2)[3+x] = a[b] +3;
            q = ---!a[m-n];
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),Id("b")),IntLiteral(3))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n")))))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_variable_and_function_declaration_with_index_expression_inside_index_expression(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,int c,float d ,string n, float a[],string g[] ,boolean f){
            int a,b,c;
            float d[10],e[11];
            a = 1;
            b = a = 2.2;
            boolean h;
            a = f(b);
            string q,w,r[20];
            foo(a);
            func(b);
            test(c);
            c = a / 12 == 3 || b - c != 4 ;
            d = c * 13 > 5 && e*c < 6;
            c = a - b || (e + d) != m && (e - f) == b;
            s = (c<d) || (b<e); 
            r = (a < e)&& -( b != e);
            a = -(b > c) != !(a < d);
            a = b/c/d/e;
            c = !a*b*c*d+d[b+f];
            d = a%d%4 - e[h%n] ;
            foo(2)[3+x] = a[b[2]] +3;
            test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
            q = ---!a[m-n];
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n")))))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_variable_and_function_declaration_with_if_statement_no_else_with_one_expression_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,int c,float d ,string n, float a[], string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_variable_and_function_declaration_with_if_statement_no_else_with_many_expression_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_variable_and_function_declaration_with_if_statement_no_else_with_many_expression_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[], float g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n];
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_variable_and_function_declaration_with_if_statement_with_else_one_expression_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if (a < b) a = b; else b = a;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_variable_and_function_declaration_with_if_statement_with_else_many_expressions_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,string c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if (a < b || a != c && d < b || c >= d) a = b; else b = a;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("||",BinaryOp("||",BinaryOp("<",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b")))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_variable_and_function_declaration_with_if_statement_with_else_many_expressions_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if (a < b || a != c && d < b || c >= d){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n];
            }
            else {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n];
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("||",BinaryOp("||",BinaryOp("<",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b")))),BinaryOp(">=",Id("c"),Id("d"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_variable_and_function_declaration_with_do_while_statement_one_expression_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],int g[] ,boolean f){
            do a = b+c; while ( a <10);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),Id("c")))],BinaryOp("<",Id("a"),IntLiteral(10))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_variable_and_function_declaration_with_do_while_statement_many_expressions_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],int g[] ,boolean f){
            do a = b+c; while ( a <10 || b > 5 && c == 8);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),Id("c")))],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(5)),BinaryOp("==",Id("c"),IntLiteral(8))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_variable_and_function_declaration_with_do_while_statement_many_expressions_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            do{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n]; 
            }
            while ( a <10 || b > 5 && c == 8);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(5)),BinaryOp("==",Id("c"),IntLiteral(8))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))
    def test_variable_and_function_declaration_with_for_statement_one_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1) a=b;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),BinaryOp("=",Id("a"),Id("b"))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))
    def test_variable_and_function_declaration_with_for_statement_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,string b,string c,float d ,string n, float a[],int g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1)
            {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n]; 
            }
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    def test_variable_and_function_declaration_with_break_statement_in_if_statement_no_else(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,string c,float d ,string n, float a[],int g[] ,boolean f){
            if(a < b) break;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp("<",Id("a"),Id("b")),Break()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))
    def test_variable_and_function_declaration_with_break_statement_in_if_statement_with_else(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,string b,float c,float d ,string n, float a[],float g[] ,boolean f){
            if(a < b || b == c) a =b; else break;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp("||",BinaryOp("<",Id("a"),Id("b")),BinaryOp("==",Id("b"),Id("c"))),BinaryOp("=",Id("a"),Id("b")),Break()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))
    def test_variable_and_function_declaration_with_break_statement_in_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,boolean c,float d ,string n, float a[],int g[] ,boolean f){
            do a = b+c; break; while ( a <10 || b > 5 && c == 8);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",BoolType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),Id("c"))),Break()],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(5)),BinaryOp("==",Id("c"),IntLiteral(8))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))
    def test_variable_and_function_declaration_with_break_statement_in_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,int c,float d ,string n, float a[],int g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1) break;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Break()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))
    def test_variable_and_function_declaration_with_continue_statement_in_if_statement_no_else(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if(a < b) continue;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp("<",Id("a"),Id("b")),Continue()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))
    def test_variable_and_function_declaration_with_continue_statement_in_if_statements_with_else(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,int b,float c,float d ,string n, float a[], int g[] ,boolean f){
            if(a < b || b == c) a =b; else break;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp("||",BinaryOp("<",Id("a"),Id("b")),BinaryOp("==",Id("b"),Id("c"))),BinaryOp("=",Id("a"),Id("b")),Break()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_variable_and_function_declaration_with_continue_statement_in_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,float b,int c,float d ,string n, float a[],string g[] ,boolean f){
            do a = b+c; continue; while ( a <10 || b > 5 && c == 8);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([Dowhile([BinaryOp("=",Id("a"),BinaryOp("+",Id("b"),Id("c"))),Continue()],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("&&",BinaryOp(">",Id("b"),IntLiteral(5)),BinaryOp("==",Id("c"),IntLiteral(8))))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))
    def test_variable_and_function_declaration_with_continue_statement_in_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        float funcdecl(int a,string b,int c,float d ,string n, float a[],float g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1) continue;
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(FloatType())),VarDecl("f",BoolType())],FloatType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))
    def test_variable_and_function_declaration_with_return_statement_funcall(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        int funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1) continue;
            return foo(a,b);
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],IntType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()),Return(CallExpr(Id("foo"),[Id("a"),Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))
    def test_variable_and_function_declaration_with_return_statement_expression(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        int funcdecl(int a,float b,float c,float d ,string n, float a[],int g[] ,boolean f){
            for(a = 1 ; a< 10 ; a= a+1) continue;
            return a>=b;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],IntType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Continue()),Return(BinaryOp(">=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))
    def test_variable_and_function_declaration_with_block_statement_in_block_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        int funcdecl(int a,string b,string c,float d ,string n, float a[],int g[] ,boolean f){
            {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n]; 
            }
            return a>=b;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],IntType(),Block([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Return(BinaryOp(">=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))
    def test_variable_and_function_declaration_with_many_block_statements(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        int a[3];
        int funcdecl(int a,string b,int c,float d ,string n, float a[],int g[] ,boolean f){
            {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n]; 
            }
            {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n]; 
            }
            return a>=b;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),VarDecl("a",ArrayType(3,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],IntType(),Block([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Return(BinaryOp(">=",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))
    def test_variable_and_function_declaration_with_if_else_statement_inside_if_else_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,string b,string c,float d ,string n, float a[], int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                c = a / 12 == 3 || b - c != 4 ;
                d = c * 13 > 5 && e*c < 6;
                c = a - b || (e + d) != m && (e - f) == b;
                s = (c<d) || (b<e); 
                r = (a < e)&& -( b != e);
                a = -(b > c) != !(a < d);
                a = b/c/d/e;
                c = !a*b*c*d+d[b+f];
                d = a%d%4 - e[h%n] ;
                foo(2)[3+x] = a[b[2]] +3;
                test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                q = ---!a[m-n];
            } else if ((a + b) >= ( c-d) || a < e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
            }
            else {
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",StringType()),VarDecl("c",StringType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),If(BinaryOp("||",BinaryOp(">=",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp("<",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")])]),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")])]))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))
    def test_variable_and_function_declaration_with_do_while_statement_inside_if_no_else_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                do{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
                while (a > b || c == d);
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Dowhile([Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))
    def test_variable_and_function_declaration_with_do_while_statement_inside_if_else_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                do{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
                while (a > b || c == d);
            }
            else{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                do{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
                while (a > b || c == d);
            }
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Dowhile([Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))))]),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Dowhile([Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d"))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))
    def test_variable_and_function_declaration_with_if_no_else_statement_inside_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            do{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                if ((a + b) < ( c -d) && a >= e){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            while (a > b || c == d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))
    def test_variable_and_function_declaration_with_if_else_statement_inside_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            do{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                if ((a + b) < ( c -d) && a >= e){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }else{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            while (a > b || c == d);
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))
    def test_variable_and_function_declaration_with_do_while_statement_inside_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            do{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                do{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
                while ((a + b) < ( c -d) && a >= e);
            }
            while (a > b || c == d);
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Dowhile([Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    def test_variable_and_function_declaration_with_for_statement_inside_do_while_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            do{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                for(a = 0 ; a < b ; a = a+1){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            while (a > b || c == d);
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])],BinaryOp("||",BinaryOp(">",Id("a"),Id("b")),BinaryOp("==",Id("c"),Id("d")))),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))
    def test_variable_and_function_declaration_with_for_statement_inside_if_no_else_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,float b,float c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                for(a = 0 ; a < b ; a = a+1){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",FloatType()),VarDecl("c",FloatType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))
    def test_variable_and_function_declaration_with_for_statement_inside_if_else_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            if ((a + b) < ( c -d) && a >= e){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                for(a = 0 ; a < b ; a = a+1){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }else{
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                for(a = 0 ; a < b ; a = a+1){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))]),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))
    def test_variable_and_function_declaration_with_if_no_else_statement_inside_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            for(a = 0 ; a < b ; a = a+1){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                if ((a + b) < ( c -d) && a >= e){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))
    def test_variable_and_function_declaration_with_if_else_statement_inside_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            for(a = 0 ; a < b ; a = a+1){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                if ((a + b) < ( c -d) && a >= e){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }else{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            return 0.0;
        }
        """
        expect = str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),If(BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))
    def test_variable_and_function_declaration_with_do_while_statement_inside_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],int g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            for(a = 0 ; a < b ; a = a+1){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                do{
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
                while ((a + b) < ( c -d) && a >= e);
            }
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(IntType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),Dowhile([Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))])],BinaryOp("&&",BinaryOp("<",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d"))),BinaryOp(">=",Id("a"),Id("e"))))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    def test_variable_and_function_declaration_with_for_statement_inside_for_statement(self):
        input = """
        int a,g[1] ;
        float b,h,t;
        boolean c;
        string d;
        int f[2];
        float funcdecl(int a,int b,int c,float d ,string n, float a[],string g[] ,boolean f){
            if (a > b) a = b;
            if (a == b) b = a ;
            if (a != c && d < b || c >= d) a[12] = 10;
            for(a = 0 ; a < b ; a = a+1){
                int a,b,c;
                float d[10],e[11];
                a = 1;
                b = a = 2.2;
                boolean h;
                a = f(b);
                string q,w,r[20];
                foo(a);
                func(b);
                test(c);
                for(b = 10 ; b < a*2 ; b = b+1){
                    c = a / 12 == 3 || b - c != 4 ;
                    d = c * 13 > 5 && e*c < 6;
                    c = a - b || (e + d) != m && (e - f) == b;
                    s = (c<d) || (b<e); 
                    r = (a < e)&& -( b != e);
                    a = -(b > c) != !(a < d);
                    a = b/c/d/e;
                    c = !a*b*c*d+d[b+f];
                    d = a%d%4 - e[h%n] ;
                    foo(2)[3+x] = a[b[2]] +3;
                    test(a,b,c)[3-a[2+b]] = c[e[5]] -5;
                    q = ---!a[m-n];
                }
            }
            return 0.0;
        }
        """
        expect =str(Program([VarDecl("a",IntType()),VarDecl("g",ArrayType(1,IntType())),VarDecl("b",FloatType()),VarDecl("h",FloatType()),VarDecl("t",FloatType()),VarDecl("c",BoolType()),VarDecl("d",StringType()),VarDecl("f",ArrayType(2,IntType())),FuncDecl(Id("funcdecl"),[VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",FloatType()),VarDecl("n",StringType()),VarDecl("a",ArrayPointerType(FloatType())),VarDecl("g",ArrayPointerType(StringType())),VarDecl("f",BoolType())],FloatType(),Block([If(BinaryOp(">",Id("a"),Id("b")),BinaryOp("=",Id("a"),Id("b"))),If(BinaryOp("==",Id("a"),Id("b")),BinaryOp("=",Id("b"),Id("a"))),If(BinaryOp("||",BinaryOp("&&",BinaryOp("!=",Id("a"),Id("c")),BinaryOp("<",Id("d"),Id("b"))),BinaryOp(">=",Id("c"),Id("d"))),BinaryOp("=",ArrayCell(Id("a"),IntLiteral(12)),IntLiteral(10))),For(BinaryOp("=",Id("a"),IntLiteral(0)),BinaryOp("<",Id("a"),Id("b")),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",IntType()),VarDecl("d",ArrayType(10,FloatType())),VarDecl("e",ArrayType(11,FloatType())),BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("=",Id("b"),BinaryOp("=",Id("a"),FloatLiteral(2.2))),VarDecl("h",BoolType()),BinaryOp("=",Id("a"),CallExpr(Id("f"),[Id("b")])),VarDecl("q",StringType()),VarDecl("w",StringType()),VarDecl("r",ArrayType(20,StringType())),CallExpr(Id("foo"),[Id("a")]),CallExpr(Id("func"),[Id("b")]),CallExpr(Id("test"),[Id("c")]),For(BinaryOp("=",Id("b"),IntLiteral(10)),BinaryOp("<",Id("b"),BinaryOp("*",Id("a"),IntLiteral(2))),BinaryOp("=",Id("b"),BinaryOp("+",Id("b"),IntLiteral(1))),Block([BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("==",BinaryOp("/",Id("a"),IntLiteral(12)),IntLiteral(3)),BinaryOp("!=",BinaryOp("-",Id("b"),Id("c")),IntLiteral(4)))),BinaryOp("=",Id("d"),BinaryOp("&&",BinaryOp(">",BinaryOp("*",Id("c"),IntLiteral(13)),IntLiteral(5)),BinaryOp("<",BinaryOp("*",Id("e"),Id("c")),IntLiteral(6)))),BinaryOp("=",Id("c"),BinaryOp("||",BinaryOp("-",Id("a"),Id("b")),BinaryOp("&&",BinaryOp("!=",BinaryOp("+",Id("e"),Id("d")),Id("m")),BinaryOp("==",BinaryOp("-",Id("e"),Id("f")),Id("b"))))),BinaryOp("=",Id("s"),BinaryOp("||",BinaryOp("<",Id("c"),Id("d")),BinaryOp("<",Id("b"),Id("e")))),BinaryOp("=",Id("r"),BinaryOp("&&",BinaryOp("<",Id("a"),Id("e")),UnaryOp("-",BinaryOp("!=",Id("b"),Id("e"))))),BinaryOp("=",Id("a"),BinaryOp("!=",UnaryOp("-",BinaryOp(">",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("<",Id("a"),Id("d"))))),BinaryOp("=",Id("a"),BinaryOp("/",BinaryOp("/",BinaryOp("/",Id("b"),Id("c")),Id("d")),Id("e"))),BinaryOp("=",Id("c"),BinaryOp("+",BinaryOp("*",BinaryOp("*",BinaryOp("*",UnaryOp("!",Id("a")),Id("b")),Id("c")),Id("d")),ArrayCell(Id("d"),BinaryOp("+",Id("b"),Id("f"))))),BinaryOp("=",Id("d"),BinaryOp("-",BinaryOp("%",BinaryOp("%",Id("a"),Id("d")),IntLiteral(4)),ArrayCell(Id("e"),BinaryOp("%",Id("h"),Id("n"))))),BinaryOp("=",ArrayCell(CallExpr(Id("foo"),[IntLiteral(2)]),BinaryOp("+",IntLiteral(3),Id("x"))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),IntLiteral(3))),BinaryOp("=",ArrayCell(CallExpr(Id("test"),[Id("a"),Id("b"),Id("c")]),BinaryOp("-",IntLiteral(3),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(2),Id("b"))))),BinaryOp("-",ArrayCell(Id("c"),ArrayCell(Id("e"),IntLiteral(5))),IntLiteral(5))),BinaryOp("=",Id("q"),UnaryOp("-",UnaryOp("-",UnaryOp("-",UnaryOp("!",ArrayCell(Id("a"),BinaryOp("-",Id("m"),Id("n"))))))))]))])),Return(FloatLiteral(0.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))


   