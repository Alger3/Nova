import pytest
from pathlib import Path

from tools.file_tools import read_file, write_file


@pytest.mark.asyncio
async def test_write_and_read_file(tmp_path: Path):
    test_file = tmp_path / "test.txt"
    await write_file(str(test_file), "hello")
    content = await read_file(str(test_file))
    assert content == "hello"
