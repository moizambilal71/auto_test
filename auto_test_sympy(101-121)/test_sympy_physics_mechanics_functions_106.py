# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sympy.physics.mechanics.functions as module_0
import sympy.physics.vector.vector as module_1


def test_case_0():
    bytes_0 = b"U\x9b\xf2=\xe3\x83\xd1\xc3g\xd6"
    with pytest.raises(TypeError):
        module_0.linear_momentum(bytes_0)


def test_case_1():
    none_type_0 = None
    with pytest.raises(TypeError):
        module_0.angular_momentum(none_type_0, none_type_0)


def test_case_2():
    set_0 = set()
    with pytest.raises(TypeError):
        module_0.kinetic_energy(set_0)


def test_case_3():
    var_0 = module_0.potential_energy()


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    list_0 = [none_type_0]
    module_0.center_of_mass(none_type_0, *list_0)


def test_case_5():
    none_type_0 = None
    with pytest.raises(TypeError):
        module_0.center_of_mass(none_type_0)


def test_case_6():
    var_0 = module_0.potential_energy()
    with pytest.raises(TypeError):
        module_0.Lagrangian(var_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    none_type_0 = None
    module_0.find_dynamicsymbols(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    module_0.msubs(none_type_0, smart=none_type_0)


def test_case_9():
    var_0 = module_0.mechanics_printing()


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = False
    none_type_0 = None
    module_0.inertia(bool_0, none_type_0, bool_0, none_type_0, iyz=bool_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    int_0 = 1112
    none_type_0 = None
    module_0.inertia_of_point_mass(int_0, int_0, none_type_0)


def test_case_12():
    none_type_0 = None
    var_0 = module_0.gravity(none_type_0)
    with pytest.raises(TypeError):
        module_0.angular_momentum(none_type_0, none_type_0)


def test_case_13():
    var_0 = module_0.potential_energy()
    var_1 = module_0.find_dynamicsymbols(var_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    int_0 = 1
    module_0.msubs(int_0, smart=int_0)


def test_case_15():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    with pytest.raises(TypeError):
        module_0.potential_energy(*list_0)


def test_case_16():
    var_0 = module_0.potential_energy()
    var_1 = module_0.msubs(var_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.core.numbers.Zero"
    )


@pytest.mark.xfail(strict=True)
def test_case_17():
    var_0 = module_0.potential_energy()
    set_0 = {var_0, var_0, var_0}
    var_1 = var_0.replace(var_0, set_0, var_0)
    var_2 = module_0.msubs(var_1, smart=var_1)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "sympy.sets.sets.FiniteSet"
    )
    assert len(var_2) == 1
    module_0.find_dynamicsymbols(set_0, set_0)


def test_case_18():
    int_0 = -2004
    with pytest.raises(TypeError):
        module_0.find_dynamicsymbols(int_0, int_0, int_0)


def test_case_19():
    var_0 = module_0.potential_energy()
    set_0 = {var_0, var_0, var_0}
    var_1 = module_0.msubs(var_0, smart=set_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.core.numbers.Zero"
    )


def test_case_20():
    var_0 = module_0.potential_energy()
    var_1 = module_1.Vector(var_0)
    var_2 = module_0.msubs(var_1)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_2.args == []
    var_3 = module_0.msubs(var_1, smart=var_1)
    with pytest.raises(ValueError):
        module_0.find_dynamicsymbols(var_3)


def test_case_21():
    var_0 = module_0.potential_energy()
    set_0 = {var_0, var_0, var_0}
    var_1 = var_0.replace(var_0, set_0, var_0)
    var_2 = module_0.msubs(var_1, smart=var_1)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "sympy.sets.sets.FiniteSet"
    )
    assert len(var_2) == 1
