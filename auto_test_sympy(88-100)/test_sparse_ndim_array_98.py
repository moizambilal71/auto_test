# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sparse_ndim_array as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    mutable_sparse_n_dim_array_0.__eq__(mutable_sparse_n_dim_array_0)


def test_case_1():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(ValueError):
        mutable_sparse_n_dim_array_0.tomatrix()


def test_case_2():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_3():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    mutable_sparse_n_dim_array_0.__setitem__(
        mutable_sparse_n_dim_array_0, mutable_sparse_n_dim_array_0
    )


@pytest.mark.xfail(strict=True)
def test_case_4():
    module_0.SparseNDimArray()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 131
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 1
    var_0.__setitem__(list_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    mutable_sparse_n_dim_array_0.__getitem__(mutable_sparse_n_dim_array_0)


def test_case_7():
    dict_0 = {}
    list_0 = [dict_0]
    sparse_n_dim_array_0 = module_0.SparseNDimArray(*list_0)
    assert (
        f"{type(sparse_n_dim_array_0).__module__}.{type(sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(sparse_n_dim_array_0) == 0


@pytest.mark.xfail(strict=True)
def test_case_8():
    int_0 = 2
    list_0 = [int_0, int_0]
    list_1 = [list_0, list_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_1)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 4
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 4
    var_1 = mutable_sparse_n_dim_array_0.tomatrix()
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.matrices.sparse.MutableSparseMatrix"
    )
    assert len(var_1) == 4
    var_2 = var_0.__eq__(var_0)
    var_3 = var_2.__eq__(int_0)
    mutable_sparse_n_dim_array_0.__setitem__(var_0, var_2)


@pytest.mark.xfail(strict=True)
def test_case_9():
    int_0 = 4
    list_0 = [int_0, int_0]
    str_0 = "x)uJ=I+0-N$|Ypz!(a*"
    dict_0 = {str_0: list_0, str_0: list_0}
    module_0.MutableSparseNDimArray(*list_0, **dict_0)


def test_case_10():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    int_0 = 3
    list_0 = [
        mutable_sparse_n_dim_array_0,
        mutable_sparse_n_dim_array_0,
        int_0,
        mutable_sparse_n_dim_array_0,
    ]
    with pytest.raises(ValueError):
        mutable_sparse_n_dim_array_0.reshape(*list_0)


def test_case_11():
    int_0 = 131
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_12():
    int_0 = 2
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 1
    mutable_sparse_n_dim_array_1 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_1).__module__}.{type(mutable_sparse_n_dim_array_1).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_1) == 0
    var_1 = var_0.as_mutable()
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(var_1) == 1
    none_type_0 = None
    mutable_sparse_n_dim_array_1.__setitem__(none_type_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    int_0 = 85
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 1
    mutable_sparse_n_dim_array_1 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_1).__module__}.{type(mutable_sparse_n_dim_array_1).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_1) == 0
    var_1 = var_0.copy()
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_1) == 1
    mutable_sparse_n_dim_array_1.__new__()


def test_case_14():
    int_0 = 131
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.__eq__(list_0)
    var_1 = mutable_sparse_n_dim_array_0.__setitem__(
        var_0, mutable_sparse_n_dim_array_0
    )


@pytest.mark.xfail(strict=True)
def test_case_15():
    int_0 = 2
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    mutable_sparse_n_dim_array_0.reshape(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    int_0 = 0
    list_0 = [int_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 1
    var_1 = mutable_sparse_n_dim_array_0.__setitem__(int_0, int_0)
    var_1.sort_key()


@pytest.mark.xfail(strict=True)
def test_case_17():
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray()
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 0
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    bool_0 = False
    tuple_0 = (bool_0, bool_0, mutable_sparse_n_dim_array_0)
    mutable_sparse_n_dim_array_0.__setitem__(tuple_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    int_0 = 2
    list_0 = [int_0]
    var_0 = list_0.count(list_0)
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_0)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 1
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_1 = var_0.__eq__(var_0)
    var_2 = mutable_sparse_n_dim_array_0.__setitem__(var_0, var_0)
    var_2.sort_key()


def test_case_19():
    int_0 = 2
    list_0 = [int_0]
    list_1 = [list_0, list_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_1)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 2
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.as_immutable()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.ImmutableSparseNDimArray"
    )
    assert len(var_0) == 2
    with pytest.raises(ValueError):
        mutable_sparse_n_dim_array_0.tomatrix()


def test_case_20():
    int_0 = 2
    list_0 = [int_0]
    list_1 = [list_0, list_0]
    mutable_sparse_n_dim_array_0 = module_0.MutableSparseNDimArray(*list_1)
    assert (
        f"{type(mutable_sparse_n_dim_array_0).__module__}.{type(mutable_sparse_n_dim_array_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(mutable_sparse_n_dim_array_0) == 2
    assert (
        f"{type(module_0.MutableSparseNDimArray.free_symbols).__module__}.{type(module_0.MutableSparseNDimArray.free_symbols).__qualname__}"
        == "builtins.property"
    )
    var_0 = mutable_sparse_n_dim_array_0.reshape(*list_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sparse_ndim_array.MutableSparseNDimArray"
    )
    assert len(var_0) == 2
    with pytest.raises(ValueError):
        mutable_sparse_n_dim_array_0.tomatrix()
