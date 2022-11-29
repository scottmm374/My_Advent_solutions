from main import Not_Quite_Lisp_P1, Not_Quite_Lisp_P2

def test_should_be_zero():
    assert Not_Quite_Lisp_P1('(())') == 0;
    assert Not_Quite_Lisp_P1('()()') == 0;


def test_should_be_three():
    assert Not_Quite_Lisp_P1('(((') == 3;
    assert Not_Quite_Lisp_P1('(()(()(') == 3;
    assert Not_Quite_Lisp_P1('))(((((') == 3;

def test_should_be_negative():
    assert Not_Quite_Lisp_P1('())') == -1;
    assert Not_Quite_Lisp_P1('))(') == -1;
    assert Not_Quite_Lisp_P1(')))') == -3;
    assert Not_Quite_Lisp_P1(')())())') == -3;

def test_should_enter_basement():
    assert Not_Quite_Lisp_P2(')') == 1;
    assert Not_Quite_Lisp_P2('()())') == 5;
