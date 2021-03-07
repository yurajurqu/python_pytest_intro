from readFromFile import readFromFile
from unittest.mock import MagicMock
import pytest


@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readLine = MagicMock(return_value='test line')
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr('builtins.open', mock_open)
    return mock_open

@pytest.mark.skip
def test_canCallReadFromFile():
    content = readFromFile('sample.txt')
    assert content == 'this is my sample text file'

def test_returnsCorrectString(mock_open,monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr('os.path.exists', mock_exists)
    result = readFromFile('blah')
    mock_open.assert_called_once_with('blah', 'r')
    assert result == 'test line'
    
def test_throwExceptionWithBadFile(mock_open,monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr('os.path.exists', mock_exists)
    with pytest.raises(Exception):
        result = readFromFile('blah')