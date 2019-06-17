import pytest
import seval

def test_unsafe():
    with pytest.raises(ValueError):
        seval.safe_eval('pow(2,3)')