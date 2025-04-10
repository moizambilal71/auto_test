# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import numpy as module_0
import mlxtend.classifier.ensemble_vote as module_1
import inspect as module_2
import sklearn.exceptions as module_3
import numpy.f2py.crackfortran as module_4
import numpy.f2py as module_5


def test_case_0():
    none_type_0 = None
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    with pytest.raises(ValueError):
        ensemble_vote_classifier_0.fit(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_2.currentframe()
    var_0.get_params()


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.EnsembleVoteClassifier(
        none_type_0, use_clones=none_type_0, fit_base_estimators=none_type_0
    )


def test_case_3():
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    with pytest.raises(module_3.NotFittedError):
        ensemble_vote_classifier_0.predict_proba(var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    ensemble_vote_classifier_0.get_params()


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    var_0 = module_4.setkindselector(none_type_0, none_type_0)
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {}
    assert ensemble_vote_classifier_0.named_clfs == {}
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {}
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    var_1 = ensemble_vote_classifier_0.get_params()
    var_1.__getattr__(none_type_0)


def test_case_6():
    none_type_0 = None
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    with pytest.raises(module_3.NotFittedError):
        ensemble_vote_classifier_0.predict(none_type_0)


def test_case_7():
    none_type_0 = None
    none_type_1 = None
    var_0 = module_4.setkindselector(none_type_0, none_type_1)
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {}
    assert ensemble_vote_classifier_0.named_clfs == {}
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {}
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    with pytest.raises(ValueError):
        ensemble_vote_classifier_0.fit(none_type_1, none_type_1)


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    var_0 = module_4.setkindselector(none_type_0, none_type_0)
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {}
    assert ensemble_vote_classifier_0.named_clfs == {}
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {}
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    var_1 = ensemble_vote_classifier_0.__sklearn_clone__()
    assert var_1.voting == "hard"
    assert var_1.verbose == 0
    var_2 = ensemble_vote_classifier_0.get_params()
    var_0.getstate()


@pytest.mark.xfail(strict=True)
def test_case_9():
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    ensemble_vote_classifier_0.transform(ensemble_vote_classifier_0)


def test_case_10():
    none_type_0 = None
    var_0 = module_0.geterr()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(
        var_0, none_type_0, verbose=var_0, use_clones=none_type_0
    )
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "divide",
        "str-2": "over",
        "str-3": "under",
        "str-4": "invalid",
    }
    assert ensemble_vote_classifier_0.voting is None
    assert ensemble_vote_classifier_0.weights is None
    assert ensemble_vote_classifier_0.verbose == {
        "divide": "warn",
        "over": "warn",
        "under": "ignore",
        "invalid": "warn",
    }
    assert ensemble_vote_classifier_0.use_clones is None
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    with pytest.raises(ValueError):
        ensemble_vote_classifier_0.fit(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    var_0 = module_5.__dir__()
    ensemble_vote_classifier_0 = module_1.EnsembleVoteClassifier(var_0, weights=var_0)
    assert (
        f"{type(ensemble_vote_classifier_0).__module__}.{type(ensemble_vote_classifier_0).__qualname__}"
        == "mlxtend.classifier.ensemble_vote.EnsembleVoteClassifier"
    )
    assert ensemble_vote_classifier_0.clfs == [
        "test",
        "__all__",
        "__spec__",
        "warnings",
        "__dir__",
        "__file__",
        "auxfuncs",
        "symbolic",
        "subprocess",
        "func2subr",
        "__loader__",
        "f2py2e",
        "__cached__",
        "f90mod_rules",
        "__path__",
        "cfuncs",
        "diagnose",
        "run_main",
        "capi_maps",
        "sys",
        "get_include",
        "common_rules",
        "VisibleDeprecationWarning",
        "__doc__",
        "__version__",
        "__builtins__",
        "__getattr__",
        "os",
        "cb_rules",
        "__name__",
        "_isocbind",
        "_backends",
        "rules",
        "main",
        "use_rules",
        "crackfortran",
        "__package__",
    ]
    assert ensemble_vote_classifier_0.named_clfs == {
        "str-1": "test",
        "str-2": "__all__",
        "str-3": "__spec__",
        "str-4": "warnings",
        "str-5": "__dir__",
        "str-6": "__file__",
        "str-7": "auxfuncs",
        "str-8": "symbolic",
        "str-9": "subprocess",
        "str-10": "func2subr",
        "str-11": "__loader__",
        "str-12": "f2py2e",
        "str-13": "__cached__",
        "str-14": "f90mod_rules",
        "str-15": "__path__",
        "str-16": "cfuncs",
        "str-17": "diagnose",
        "str-18": "run_main",
        "str-19": "capi_maps",
        "str-20": "sys",
        "str-21": "get_include",
        "str-22": "common_rules",
        "str-23": "VisibleDeprecationWarning",
        "str-24": "__doc__",
        "str-25": "__version__",
        "str-26": "__builtins__",
        "str-27": "__getattr__",
        "str-28": "os",
        "str-29": "cb_rules",
        "str-30": "__name__",
        "str-31": "_isocbind",
        "str-32": "_backends",
        "str-33": "rules",
        "str-34": "main",
        "str-35": "use_rules",
        "str-36": "crackfortran",
        "str-37": "__package__",
    }
    assert ensemble_vote_classifier_0.voting == "hard"
    assert ensemble_vote_classifier_0.weights == [
        "test",
        "__all__",
        "__spec__",
        "warnings",
        "__dir__",
        "__file__",
        "auxfuncs",
        "symbolic",
        "subprocess",
        "func2subr",
        "__loader__",
        "f2py2e",
        "__cached__",
        "f90mod_rules",
        "__path__",
        "cfuncs",
        "diagnose",
        "run_main",
        "capi_maps",
        "sys",
        "get_include",
        "common_rules",
        "VisibleDeprecationWarning",
        "__doc__",
        "__version__",
        "__builtins__",
        "__getattr__",
        "os",
        "cb_rules",
        "__name__",
        "_isocbind",
        "_backends",
        "rules",
        "main",
        "use_rules",
        "crackfortran",
        "__package__",
    ]
    assert ensemble_vote_classifier_0.verbose == 0
    assert ensemble_vote_classifier_0.use_clones is True
    assert ensemble_vote_classifier_0.fit_base_estimators is True
    ensemble_vote_classifier_0.fit(var_0, var_0)
