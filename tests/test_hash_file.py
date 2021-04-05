from pathlib import Path
import hashlib 
import pytest

from hash_tree.hash_file import hash_file
from tests.test_fixtures import dir_with_files, files


hashtypes = ["md5"]

def test_filehash(dir_with_files):
    p = Path(dir_with_files)
    read_files = [el for el in p.iterdir()]
    for f in read_files:
        bytecontent = f.read_bytes()
        for ht in hashtypes:
            hash1 = hash_file(file=f, hashtype=ht)
            hasher = hashlib.md5()
            hasher.update(bytecontent)
            hash2 = hasher.hexdigest()
            assert hash1 == hash2
        
