import pytest
from click.testing import CliRunner
from binary import cli


@pytest.fixture
def runner():
    return CliRunner()

