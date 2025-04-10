# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src.flask.sessions as module_0
import datetime as module_1


def test_case_0():
    session_interface_0 = module_0.SessionInterface()


def test_case_1():
    secure_cookie_session_0 = module_0.SecureCookieSession()
    assert (
        f"{type(secure_cookie_session_0).__module__}.{type(secure_cookie_session_0).__qualname__}"
        == "src.flask.sessions.SecureCookieSession"
    )
    assert len(secure_cookie_session_0) == 0
    assert module_0.SecureCookieSession.modified is False
    assert module_0.SecureCookieSession.accessed is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.get_expiration_time(var_0, var_0)
    dict_0 = {session_interface_0: session_interface_0, var_1: var_1}
    var_2 = var_0.__ior__(var_0)
    var_3 = session_interface_0.should_set_cookie(dict_0, var_2)
    assert var_3 is True
    tzinfo_0 = module_1.tzinfo()
    str_0 = "?u^&f%<~2qq7P3\x0c\nFx"
    var_4 = var_0.__eq__(session_interface_0)
    var_4.setdefault(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    null_session_0 = module_0.NullSession()
    assert (
        f"{type(null_session_0).__module__}.{type(null_session_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(null_session_0) == 0
    str_0 = "}w>1^\r~0pg\rx"
    null_session_0.__getitem__(str_0)


def test_case_4():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.get_expiration_time(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    secure_cookie_session_0 = module_0.SecureCookieSession()
    assert (
        f"{type(secure_cookie_session_0).__module__}.{type(secure_cookie_session_0).__qualname__}"
        == "src.flask.sessions.SecureCookieSession"
    )
    assert len(secure_cookie_session_0) == 0
    assert module_0.SecureCookieSession.modified is False
    assert module_0.SecureCookieSession.accessed is False
    secure_cookie_session_0.setdefault(secure_cookie_session_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    null_session_0 = module_0.NullSession()
    assert (
        f"{type(null_session_0).__module__}.{type(null_session_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(null_session_0) == 0
    none_type_0 = None
    null_session_0.setdefault(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    session_interface_0 = module_0.SessionInterface()
    session_interface_0.get_cookie_name(session_interface_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    session_interface_0 = module_0.SessionInterface()
    session_interface_0.get_cookie_domain(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.get_expiration_time(var_0, var_0)
    var_2 = session_interface_0.should_set_cookie(session_interface_0, var_0)
    assert var_2 is False
    session_interface_0.get_cookie_httponly(var_2)


@pytest.mark.xfail(strict=True)
def test_case_10():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.get_expiration_time(var_0, var_0)
    var_2 = session_interface_0.should_set_cookie(session_interface_0, var_0)
    assert var_2 is False
    tzinfo_0 = module_1.tzinfo()
    session_interface_0.get_cookie_secure(tzinfo_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "jnD3EHn("
    secure_cookie_session_0 = module_0.SecureCookieSession()
    assert (
        f"{type(secure_cookie_session_0).__module__}.{type(secure_cookie_session_0).__qualname__}"
        == "src.flask.sessions.SecureCookieSession"
    )
    assert len(secure_cookie_session_0) == 0
    assert module_0.SecureCookieSession.modified is False
    assert module_0.SecureCookieSession.accessed is False
    session_interface_0 = module_0.SessionInterface()
    session_interface_0.get_cookie_samesite(str_0)


def test_case_12():
    none_type_0 = None
    session_interface_0 = module_0.SessionInterface()
    with pytest.raises(NotImplementedError):
        session_interface_0.open_session(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    session_interface_0.get_cookie_partitioned(session_interface_0)


def test_case_14():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.should_set_cookie(session_interface_0, var_0)
    assert var_1 is False


def test_case_15():
    session_interface_0 = module_0.SessionInterface()
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.get_expiration_time(var_0, var_0)
    var_2 = session_interface_0.should_set_cookie(session_interface_0, var_0)
    assert var_2 is False
    with pytest.raises(NotImplementedError):
        session_interface_0.save_session(var_2, var_2, var_1)


@pytest.mark.xfail(strict=True)
def test_case_16():
    session_interface_0 = module_0.SessionInterface()
    bool_0 = session_interface_0.is_null_session(session_interface_0)
    var_0 = session_interface_0.make_null_session(session_interface_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "src.flask.sessions.NullSession"
    )
    assert len(var_0) == 0
    var_1 = session_interface_0.should_set_cookie(session_interface_0, var_0)
    assert var_1 is False
    session_interface_0.get_cookie_httponly(session_interface_0)
