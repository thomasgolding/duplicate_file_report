from pathlib import Path
import pytest
from shutil import copyfile

from tests.data_files import files0


def _helper_write_file(directory: str, files: list = files0) -> None:
    for el in files:
        f = Path(directory) / el[0]
        f.write_text(el[1])
    return


@pytest.fixture
def dir_with_files(tmpdir_factory):
    tdir = tmpdir_factory.mktemp("data")
    _helper_write_file(directory=tdir)
    return tdir


@pytest.fixture
def dir_with_one_duplicate(tmpdir_factory):
    tdir = tmpdir_factory.mktemp("with_duplicate")
    _helper_write_file(directory=tdir, files=files0)

    p = Path(tdir)
    pfiles = [el for el in p.iterdir()]
    f_src = pfiles[0]
    p_dest = Path(tdir) / f"{f_src.name}2"
    f_dest = str(p_dest)
    copyfile(f_src, f_dest)
    return tdir


