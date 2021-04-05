from pathlib import Path
from typing import Tuple
import pytest


from shutil import copyfile

files = [
    ("file1", "text1"), 
    ("file2", "text2")
]

@pytest.fixture(scope="session")
def dir_with_files(tmpdir_factory):
    tdir = tmpdir_factory.mktemp("data")
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


def get_dircontent(xdir: str) -> Tuple:
    p = Path(xdir)
    read_files = [el for el in p.iterdir()]
    filenames = [el.name for el in read_files]
    filecontent = [el.read_text() for el in read_files]
    return read_files, filenames, filecontent

    
def test_dir_with_files(dir_with_files):
    read_files, filenames, filecontent = get_dircontent(xdir=dir_with_files)
    assert len(read_files) == len(files)
    assert len(set(filenames)) == len(set(filecontent))


def test_dir_with_one_duplicate(dir_with_one_duplicate):
    read_files, filenames, filecontent = get_dircontent(xdir=dir_with_one_duplicate)
    assert len(read_files) == len(files) + 1
    assert len(set(filenames)) == len(set(filecontent)) + 1
