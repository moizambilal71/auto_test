# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import satask as module_0
import sympy.assumptions.cnf as module_1
import sympy.core.expr as module_2
import sympy.logic.boolalg as module_3
import sympy.assumptions.assume as module_4


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1405
    module_0.satask(int_0, context=int_0, iterations=int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1107.75
    module_0.find_symbols(float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '\\ *?3(R"#x1x#F u'
    module_0.get_relevant_clsfacts(str_0)


def test_case_3():
    c_n_f_0 = module_1.CNF()
    var_0 = module_0.get_all_relevant_facts(c_n_f_0, c_n_f_0, c_n_f_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.assumptions.cnf.EncodedCNF"
    )
    assert var_0.data == []
    assert var_0.encoding == {}


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 653
    module_0.get_relevant_clsfacts(int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x9f\r\x84\xd9\xefJx/5"
    module_0.get_all_relevant_facts(bytes_0, bytes_0, bytes_0)


def test_case_6():
    c_n_f_0 = module_1.CNF()
    var_0 = module_0.extract_predargs(c_n_f_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    int_0 = -1405
    module_0.satask(int_0)


def test_case_8():
    c_n_f_0 = module_1.CNF()
    var_0 = module_0.extract_predargs(c_n_f_0, c_n_f_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    none_type_0 = None
    c_n_f_0 = module_1.CNF()
    bool_0 = True
    var_0 = module_0.get_all_relevant_facts(
        c_n_f_0, none_type_0, c_n_f_0, iterations=bool_0
    )
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.assumptions.cnf.EncodedCNF"
    )
    assert var_0.data == []
    assert var_0.encoding == {}
    var_1 = module_0.get_all_relevant_facts(c_n_f_0, none_type_0, c_n_f_0)
    none_type_0.__float__()


def test_case_10():
    none_type_0 = None
    c_n_f_0 = module_1.CNF()
    var_0 = module_0.get_all_relevant_facts(c_n_f_0, c_n_f_0, none_type_0, none_type_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.assumptions.cnf.EncodedCNF"
    )
    assert var_0.data == []
    assert var_0.encoding == {}


@pytest.mark.xfail(strict=True)
def test_case_11():
    expr_0 = module_2.Expr()
    var_0 = expr_0.extract_branch_factor()
    module_0.get_relevant_clsfacts(var_0)


def test_case_12():
    c_n_f_0 = module_1.CNF()
    var_0 = module_0.get_all_relevant_facts(c_n_f_0, c_n_f_0, c_n_f_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.assumptions.cnf.EncodedCNF"
    )
    assert var_0.data == []
    assert var_0.encoding == {}
    with pytest.raises(ValueError):
        module_0.check_satisfiability(c_n_f_0, c_n_f_0, var_0)


def test_case_13():
    boolean_0 = module_3.Boolean()
    var_0 = module_0.satask(boolean_0, boolean_0)
    assert var_0 is True


def test_case_14():
    boolean_0 = module_3.Boolean()
    var_0 = module_0.satask(boolean_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    boolean_0 = module_3.Boolean()
    var_0 = boolean_0.__xor__(boolean_0)
    var_1 = module_0.satask(var_0, boolean_0, use_known_facts=boolean_0)
    assert var_1 is False
    module_4.AppliedPredicate()
