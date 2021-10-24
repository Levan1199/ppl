import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """int main() {foo();}"""
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """
        int main;
        void main () {
        putIntLn(getInt(4));
        }"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_variable(self):
        input = """void main () {
        int a;
        float a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_undeclared_variable(self):
        input = """void main(){
        int a;
        b=a+2;
        }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_param(self):
        input = """void main (float a, int b, int a) {
        int d;
        float e;
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_function(self):
        input = """void foo1() {
        int a;
        float d;
        }
        float foo1(){
        return 9;}
        int main(){}"""
        expect = "Redeclared Function: foo1"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_undeclared_variable_in_function_call(self):
        input = """int foo(int a){return 1;}
        void main(){
        foo(c);
        }"""
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_undeclared_function_in_functioncall(self):
        input = """int foo(int a){
        return 1;
        }
        void main(){
        foo(b(1));
        }"""
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_typemissmatch_arraytype_inttype(self):
        input = """void main(){
        int a[5];
        {
            a = 1; 
        }
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_variable_in_two_function(self):
        input = """int foo(int i) {
        return 0;
        }
        int main(int a) {
        int main;
        main = foo(2) + i;
        return 0;
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_mismatch_callexpr(self):
        input = """int foo(int i) {
        return 0;
        }
        int main(int a) {
        int main;
        main = foo() + a;
        return 0;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_mismatch_arraycell(self):
        input = """int foo[10];
        int boo[10];
        int main() {
        foo[3] = boo + 1;
        return 0;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(boo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_mismatch_statement_if(self):
        input = """int main () {
        int a;
        if (a+1) {
        return a = 2;}
        }"""
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),IntLiteral(1))," \
                 "Block([Return(BinaryOp(=,Id(a),IntLiteral(2)))]))"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_mismatch_expr_wrong_length(self):
        input = """void foo(int a,int b){}
        void main(){
        foo(1);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_mismatch_funcall_not_same_type(self):
        input = """void foo(int a,int b){}
        void main(){
        foo(1,"a");
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),StringLiteral(a)])"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_mismatch_statement_if_assign_expr(self):
        input = """int main () {
        if (a - 1) {
        return a;}
        }
        int a;"""
        expect = "Type Mismatch In Statement: If(BinaryOp(-,Id(a),IntLiteral(1)),Block([Return(Id(a))]))"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_mismatch_if_stmt_not_booltype(self):
        input = """int main () {
        int a;
        if (a = 1) {
        return a;}
        }"""
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(a),IntLiteral(1)),Block([Return(Id(a))]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_arraycell(self):
        input = """float c (int b) {
        return b +2.5;
        }
        void main() {
        a[10];}"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_redeclared_variable_para(self):
        input = """int[] main(float foo[]){
        int foo; }"""
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_other_undeclared_variable(self):
        input = """void main(){
        x;
        int x; }"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_undeclared_variable1894(self):
        input = """void main(){
        int c;
        {
        c;
        d;
        int d;
        }
        }"""
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_typemismatch_expr_arraycell(self):
        input = """void main() {
        2[2];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(IntLiteral(2),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_typemismatch_bool_arraycell(self):
        input = """void main() {
        boolean a;
        a[2];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_typemismatch_not_int_array_cell(self):
        input = """void main() {
        float a[2];
        a[2.2]; }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.2))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_binary_op_string(self):
        input = """void main(){ int a;
        a = 2.3 * "2"; }"""
        expect = "Type Mismatch In Expression: BinaryOp(*,FloatLiteral(2.3),StringLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_typemismatch_not_booltype_andop(self):
        input = """void main() {
        2&&3;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLiteral(2),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_typemismatch_not_booltype_orop(self):
        input = """void main() {
        2.2||"3";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,FloatLiteral(2.2),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_typemismatch_not_booltype_equalop(self):
        input = """void main() {
        2.2=="3";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,FloatLiteral(2.2),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_typemismatch_not_booltype_right_expr(self):
        input = """void main() {
        boolean a;
        true == "3"; }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLiteral(true),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_typemismatch_notequal_op(self):
        input = """void main() {
        2!="3";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(!=,IntLiteral(2),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_typemismatch_notequal_op_not_booltype_right_expr(self):
        input = """void main() {
        true!=3;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(!=,BooleanLiteral(true),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_mismatch_greater_float_booltype(self):
        input = """void main(){
        3.2 > true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,FloatLiteral(3.2),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_mismatch_binary_expr_modop_not_inttype(self):
        input = """void main() {
        3.2%2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLiteral(3.2),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_mismatch_equal_booltype_int(self):
        input = """void main() {
        true == 2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLiteral(true),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_mismatch_divop_int_booltype(self):
        input = """void main() {
        int a;
        float b;
        boolean c;
        a+b-a*b;
        a/c; }"""
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_mismatch_int_booltype(self):
        input = """void main() { int a;
        boolean b, c;
        b || c && a; }"""
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_mismatch_equal_not_same_type(self):
        input = """void main(){
        int a,b;
        float c;
        a!=b;
        a==c; }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_mismatch_seq_booltype_float(self):
        input = """void main(){
        int a;
        float b;
        boolean c;
        a<b;
        b>=a;
        a>b;
        b<=c;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(<=,Id(b),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_mismatch_binary_addop_int_booltype(self):
        input = """void main(){
        int a;
        a+true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_mismatch_variable_string_in_lessop(self):
        input = """void main(){
        float a;
        a/3>2;
        a<"3";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(<,Id(a),StringLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_mismatch_addop_int_booltype(self):
        input = """void main(){
        boolean a,b;
        a||b&&a==true;
        a+2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_mmismatch_modop_not_intype(self):
        input = """void main(){
        int a;
        a%2+3.2;
        a%3.2; }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),FloatLiteral(3.2))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_undeclared_variable169(self):
        input = """void main(){ int a; !a; }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_mismatch_pointer_type_assign_int(self):
        input = """int foo(int arr[]) {
        arr = 2; }
        void main(){  }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_mismatch_wrongtype_callexpr(self):
        input = """void noo(int a){}
        void main(){
        int a;
        noo(getInt(a));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_simple_not_left_value(self):
        input = """void main(){
        int a;
        a = 3;
        3 = a;
        }"""
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_mismatch_stmt_for_not_int(self):
        input = """void main(){
        float a;
        for(a; 3<4; 3){}
        }"""
        expect = "Type Mismatch In Statement: For(Id(a);BinaryOp(<,IntLiteral(3),IntLiteral(4));IntLiteral(3);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_mismatch_stmt_for_not_bool(self):
        input = """void main(){
        int a;
        for(a; a; a){}
        }"""
        expect = "Type Mismatch In Statement: For(Id(a);Id(a);Id(a);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_mismatch_stmt_for_not_int_expr3(self):
        input = """void main(){
        float a;
        for(3; 3<4; a){}
        }"""
        expect = "Type Mismatch In Statement: For(IntLiteral(3);BinaryOp(<,IntLiteral(3),IntLiteral(4));Id(a);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_mismatch_equal_inttype_floattype(self):
        input = """void main(){
        int a;
        float b;
        b=a;
        a=b;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_undeclared_variable48941(self):
        input = """void main(){
        boolean a;
        do {} while(a);
        do {} while("test");
        }"""
        expect = "Type Mismatch In Statement: Dowhile([Block([])],StringLiteral(test))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_mismatch_stmt_not_booltype(self):
        input = """void main(){
        int a;
        if(a==3){
        if(a){}
        }
        }"""
        expect = "Type Mismatch In Statement: If(Id(a),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_mismatch_assign_not_same_type(self):
        input = """void main(){
        int a;
        boolean b;
        string c;
        a=2;
        b=true;
        c="c";
        a=b;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_mismatch_for_stmt_expr3_not_booltype(self):
        input = """void main(){
        int x;
        for(x+2; x=10; x*21){
        }
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(+,Id(x),IntLiteral(2));BinaryOp(=,Id(x),IntLiteral(10));BinaryOp(*,Id(x),IntLiteral(21));Block([]))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_mismatch_stmt_expr_not_booltype(self):
        input = """void main(){
        string x;
        do {} while(x="test");
        }"""
        expect = "Type Mismatch In Statement: Dowhile([Block([])],BinaryOp(=,Id(x),StringLiteral(test)))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_mismatch_for_stmt_in_if_stmt(self):
        input = """void main(){
        int a,x;
        if(a==3){
        for(x;x;x){}
        }
        }"""
        expect = "Type Mismatch In Statement: For(Id(x);Id(x);Id(x);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_no_entry_point(self):
        input = """int foo() {
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_other_no_entry_point(self):
        input = """int main;"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_not_left_value_stringtype(self):
        input = """void main(){
        int a[3];
        a[2] = 3;
        "2.5" = 3;
        }"""
        expect = "Not Left Value: StringLiteral(2.5)"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_redeclared_func_name_variable(self):
        input = """int a; float b;
        int foo(){ int a; }
        void main(){ int main; }
        void b(){}"""
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_complicated_typemismatch_expr(self):
        input = """boolean a(){
        return d;
        }
        int b;
        int c;
        boolean d;
        void main(){
        do
        a();
        {
        -!!!!!!!!!!a();
        }
        while(b > c);
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(-,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,CallExpr(Id(a),[]))))))))))))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_typemismatch_id_same_name_with_function(self):
        input = """int foo() {
        return 3;
        }
        void main() {
        foo[3]; 
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_break_not_inloop_simple(self):
        input = """int main () {
        break;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_continue_notinloop_break_inloop(self):
        input = """void main() { 
        do 
        break; 
        while(true); 
        int a; int b; 
        {{{ 
        for(a;true;b) break; 
        {{{ 
        continue;
        }}}  
        }}} 
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_complex_continue_not_inloop(self):
        input = """void main(){
        if(true) if(3==3) do for(3; 3<4; 4) if(false) if(true) break; while(false);
        continue;
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_simple_continue_not_inloop(self):
        input = """void main(){
        continue;
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_break_not_inloop_but_in_if_smt(self):
        input = """void main(){
        int a;
        do a = a+1;
        while(false);
        if(true) break;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_mismatch_stmt_return_not_inttype(self):
        input = """int main () {
        int a;
        float b;
        return;
        }"""
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_mismatch_stmt_voidtype(self):
        input = """void foo () {
        }
        void main(){
        return foo();}"""
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_return_wrong_arraytype(self):
        input = """int[] foo(int a, float b[]) {
        float c[3];
        if (a>0) 
        foo(a-1,b);
        return c; }
        void main(){}"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_other_return_wrong_arraytype(self):
        input = """int[] foo(int a, float b[]) {
        float c[3];
        if (a>0) 
        foo(a-1,b);
        return c; }
        void main(){}"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,471))

    # def test_simple_unreachable_func(self):
    #     input = """int foo () {
    #     int a;
    #     float d;
    #     }
    #     void main(){int foo;}"""
    #     expect = "Unreachable Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,472))

    # def test_complex_unreachable_func(self):
    #     input = """int foo1 () {
    #     int a;
    #     float d;
    #     }
    #     void main(){int foo;
    #     foo2();}
    #     int foo2 () {
    #     int a;
    #     float d;
    #     }"""
    #     expect = "Unreachable Function: foo1"
    #     self.assertTrue(TestChecker.test(input,expect,473))

    def test_mismatch_expr_wrong_type_assign(self):
        input = """int func(){
        return 2;
        }
        void main(){
        func(); //1
        int func; //2
        func = "string";
        return;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(func),StringLiteral(string))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_mismatch_built_in_expr(self):
        input = """void main(){
        putIntLn(3, getInt(), 3);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(putIntLn),[IntLiteral(3),CallExpr(Id(getInt),[]),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_undeclared_more_complex(self):
        input = """int a;
        int foo(){ flo(); return a; }
        float flo(){ foo(); return flo(); }
        void main(){ str(); 
        }"""
        expect = "Undeclared Function: str"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_redeclared_funcname(self):
        input = """int a; float b;
        int foo(){ int a; }
        void main(){ int main; }
        void a(){}"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_simple_func_not_return(self):
        input = """string foo(){ 
        { for(2; 2==2; 2){ 
        { return "s"; } } } 
        }
        void main(){foo();}"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_complex_continue_not_in_loop(self):
        input = """void main(){ 
        if(true) do if(false) break; while(false); 
        continue; 
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_not_left_value_func(self):
        input = """void main(){
        int a;
        a = 3;
        foo() = a;
        }
        int foo(){
        return 5;}"""
        expect = "Not Left Value: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_other_break_not_inloop(self):
        input = """void main(){ 
        do if(true) 
        continue; 
        while(false); 
        break; 
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_func_not_return_in_ifstmt(self):
        input = """string str(){ 
        if(2==2){ 
        return "s"; 
        } 
        }
        void main(){ str(); }"""
        expect = "Function str Not Return "
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_mismatch_expr_addop(self):
        input = """void main(){
        int a;
        boolean b;
        a+b; }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_complex_not_return_ifstmt(self):
        input = """string foo(){ 
        int a, b;
        if(2==2){ 
        {
        return "s";
        }
        } else {
        if(a>b)
        return "str";
        else
        if(a<=b)
        return "s";
        else
        "s"; // Error
        } 
        }
        void main(){}"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_normal_not_return_func(self):
        input = """int foo(){ 
        for(2; 2==2; 2){ 
        if(2==2){ 
        return 2;    
        } 
        } 
        }
        void main(){ str(); }"""
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_complex_typemismatch_expr(self):
        input = """int[] t(int a){ int arr[2]; return arr; }
        void main(){
        int b[10], a[10];
        int c, d, x;
        t(11)[true || false] == a[1] - b[1] * x; 
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(t),[IntLiteral(11)]),BinaryOp(||,BooleanLiteral(true),BooleanLiteral(false)))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_mismatch_unary_op(self):
        input = """void main(){ 
        float a,b; 
        -(a>b);}"""
        expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(>,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_mismatch_expr_inttype_arraytype(self):
        input = """void main(){ 
        float a,b; 
        -(a-b);
        int c[3];
        a - c;}"""
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_mismatch_expr_binaryop_arraycell_intype(self):
        input = """void main(){ 
        float a,b; 
        -(a-b);
        int c[3];
        boolean d;
        a - c[1];
        c[2] - d;}"""
        expect = "Type Mismatch In Expression: BinaryOp(-,ArrayCell(Id(c),IntLiteral(2)),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_mismatch_expr_binaryop_stringtype_intype(self):
        input = """void main(){ 
        float a,b; 
        -(a-b);
        int c[3];
        string d;
        a - c[1];
        c[2] - d;}"""
        expect = "Type Mismatch In Expression: BinaryOp(-,ArrayCell(Id(c),IntLiteral(2)),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_mismatch_expr_assign_arraycell_inttype(self):
        input = """void main () {
        string a[3];
        string b;
        a[3] = b;
        a[2] = 2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(2)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_mismatch_unary_op_stringtype(self):
        input = """void main(){ 
        string a; 
        !a; }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_mismatch_assign_op_booltype(self):
        input = """void main() {
        int a;
        float b;
        boolean c[3];
        a+b-a*b;
        c[3] = true;
        c[2] = 2;}"""
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(c),IntLiteral(2)),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_mismatch_stmt_wrongtype_return_booltype(self):
        input = """int[] main () {
        int a;
        float d;
        boolean c[2];
        return c;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_mismatch_stmt_wrongtype_return_floatype(self):
        input = """int[] main () {
        int a;
        float d;
        float c[2];
        return c;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_mismatch_stmt_wrongtype_return_inttype(self):
        input = """float[] main () {
        int a;
        float d;
        int c[2];
        return c;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(c))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_mismatch_stmt_wrongtype_return_not_arraytype(self):
        input = """float[] main () {
        int a;
        float d;
        float c[2];
        return d;
        }"""
        expect = "Type Mismatch In Statement: Return(Id(d))"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_mismatch_arraytype_booltype(self):
        input = """float[] foo () {
        int a;
        float d;
        float c[2];
        return c;
        }
        void main(){
        foo()[2] = true;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(CallExpr(Id(foo),[]),IntLiteral(2)),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_unreachable_func_global(self):
        input = """float[] foo () {
        int a;
        float d;
        float c[2];
        return c;
        }
        void main(){
        foo()[2] = 2;
        foo()[1] = 1.5;
        }
        int foo2(){return 1;}"""
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,499))






