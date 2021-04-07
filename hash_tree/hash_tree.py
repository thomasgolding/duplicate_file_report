from typing import Union
from pathlib import Path

from hash_tree.hash_file import hash_file

class HashTree:
    def __init__(self, rootpath: Union[str, Path], buffer_size: int = 65536, hashtype: str = "md5"):
        if isinstance(rootpath, str):
            rp = Path(rootpath)
        else:
            rp = rootpath
        self.rootpath = rp
        self.hashtype = hashtype
        self.buffer_size = buffer_size
        

    def get_tree(self):
        self.tree = self._get_records(xdir=self.rootpath)
        return self.tree


    def get_file_hash(self, file: Path):
        bz = self.buffer_size
        ht = self.hashtype
        file_hash = hash_file(file=file, buffer_size=bz, hashtype=ht)
        return file_hash
        

    def _get_records(self, xdir: Path):
        
        files  = [el.absolute() for el in xdir.iterdir() if el.is_file()]
        dirs = [el.absolute() for el in xdir.iterdir() if el.is_dir()]

        records = [
            {
                "parent_dir": str(el.parent),
                "filename": el.name,
                "pathstring": str(el),
                "size": el.lstat().st_size,
                "hash": self.get_file_hash(el)
            }
            for el in files
        ]

        rec_dir = [self._get_records(xdir=el) for el in dirs]
        rec_dir_flat = [rec for folder in rec_dir for rec in folder]
        records = records + rec_dir_flat

        return records
    
    