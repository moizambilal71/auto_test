# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sathandlers as module_0
import sympy.matrices.expressions.matexpr as module_1
import sympy.core.expr as module_2


def test_case_0():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = class_fact_registry_0.__call__(class_fact_registry_0)
    var_1 = module_0.anyarg(class_fact_registry_0, var_0, matrix_expr_0)
    var_2 = module_0.allargs(matrix_expr_0, var_1, var_1)
    class_fact_registry_1 = module_0.ClassFactRegistry()
    var_3 = module_0.exactlyonearg(var_1, var_0, var_1)


def test_case_1():
    class_fact_registry_0 = module_0.ClassFactRegistry()


def test_case_2():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    var_0 = class_fact_registry_0.__call__(class_fact_registry_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    class_fact_registry_0.__getitem__(class_fact_registry_0)


def test_case_4():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = module_0.allargs(matrix_expr_0, matrix_expr_0, matrix_expr_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    module_0.anyarg(none_type_0, none_type_0, none_type_0)


def test_case_6():
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = module_0.anyarg(matrix_expr_0, matrix_expr_0, matrix_expr_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    class_fact_registry_1 = module_0.ClassFactRegistry()
    expr_0 = module_2.Expr()
    var_0 = class_fact_registry_1.__call__(class_fact_registry_1)
    var_1 = class_fact_registry_1.__call__(var_0)
    class_fact_registry_1.__getitem__(class_fact_registry_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = module_0.anyarg(matrix_expr_0, matrix_expr_0, matrix_expr_0)
    var_1 = matrix_expr_0.__neg__()
    var_2 = var_1.as_coeff_Mul()
    module_0.exactlyonearg(var_2, var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = matrix_expr_0.adjoint()
    module_0.exactlyonearg(var_0, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = class_fact_registry_0.__call__(class_fact_registry_0)
    var_1 = matrix_expr_0.__neg__()
    module_0.allargs(matrix_expr_0, var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_11():
    class_fact_registry_0 = module_0.ClassFactRegistry()
    matrix_expr_0 = module_1.MatrixExpr()
    var_0 = matrix_expr_0.conjugate()
    var_1 = class_fact_registry_0.__call__(var_0)
    module_0.anyarg(var_0, matrix_expr_0, var_0)
