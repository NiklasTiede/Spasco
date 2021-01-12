import spasco.spasco2 as sp2

import pytest
pytest.fixture()


def test_main():
    """Dummy test in order to make conda build pass"""

    sp2.hello_name('Niklas')
    assert sp2.hello_name('Niklas') == 'Hello, Niklas!'
    # out, err = capsys.readouterr()
    # assert out == 'Hello, Niklas!'
    # assert err == ''
