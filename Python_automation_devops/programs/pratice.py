

import pytest

@pytest.fixture()
def sample_fixture():
    return [1,2,3]

def test_sum(sample_fixture):
    print(sum(sample_fixture))
