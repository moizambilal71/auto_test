# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import _classifier as module_0


def test_case_0():
    classifier_0 = module_0._Classifier()


@pytest.mark.xfail(strict=True)
def test_case_1():
    classifier_0 = module_0._Classifier()
    classifier_1 = module_0._Classifier()
    classifier_1.score(classifier_1, classifier_1)
