# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src.flask.logging as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x11\x93\xbc>\xee\xefz\xac\x95\xc5\xb5\xc5"
    module_0.create_logger(bytes_0)
