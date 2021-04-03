from pathlib import Path
from tempfile import TemporaryDirectory

from shutil import copyfile
import pytest


@pytest.fixture(scope="session")
def dir_with_files(tmpdir_factory):
    tdir = tmpdir_factory.mktemp("data")
    files = [
        ("file1", "text1"), 
        ("file2", "text2"), 
        ("duplicate1", "text1")
    ]
    for el in files:            
        f = Path(tdir) / el[0]
        f.write_text(el[1])
    return tdir

@pytest.fixture(scope="session")
def dir_with_one_duplicate(tmpdir_factory, dir_with_files):
    tdir = tmpdir_factory.mktemp("with_duplicate")
    p = Path(dir_with_files)
    files = [el for el in p.iterdir()]
    for el in files:
        copyfile(el, Path(tdir) / el.name)
    f_src = files[0]
    p_dest = Path(tdir) / f"{el.name}2"
    f_dest = str(p_dest)
    copyfile(f_src, f_dest)
    return tdir


def test_filehash(dir_with_files):
    p = Path(dir_with_files)
    files = [el for el in p.iterdir()]
    assert len(files) == 3


def test_filehash_duplicate(dir_with_one_duplicate):
    p = Path(dir_with_one_duplicate)
    files = [el for el in p.iterdir()]
    assert len(files) == 4
    