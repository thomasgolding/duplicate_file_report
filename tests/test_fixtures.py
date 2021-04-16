from pathlib import Path
from typing import Tuple

from tests.data_files import files0


def get_dircontent(xdir: str) -> Tuple:
    p = Path(xdir)
    read_files = [el for el in p.iterdir()]
    filenames = [el.name for el in read_files]
    filecontent = [el.read_text() for el in read_files]
    return read_files, filenames, filecontent


def test_dir_with_files(dir_with_files):
    read_files, filenames, filecontent = get_dircontent(xdir=dir_with_files)
    assert len(read_files) == len(files0)
    assert len(set(filenames)) == len(set(filecontent))


def test_dir_with_one_duplicate(dir_with_one_duplicate):
    read_files, filenames, filecontent = get_dircontent(xdir=dir_with_one_duplicate)
    assert len(read_files) == len(files0) + 1
    assert len(set(filenames)) == len(set(filecontent)) + 1
