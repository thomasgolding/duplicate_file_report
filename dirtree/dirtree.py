from typing import Union
from pathlib import Path

from dirtree.hash_file import hash_file

class DirTree:
    def __init__(self, rootpath: Union[str, Path]):
        if isinstance(rootpath, str):
            rp = Path(rootpath)
        else:
            rp = rootpath
        self.rootpath = rp
        
    def create_tree(self):
        self.tree = self.get_records(xdir=self.rootpath)
        return self.tree

    
    def get_records(self, xdir: Path):
        files  = [el.absolute() for el in xdir.iterdir() if el.is_file()]
        dirs = [el.absolute() for el in xdir.iterdir() if el.is_dir()]

        records = [
            {
                "parent_dir": str(el.parent),
                "filename": el.name,
                "pathstring": str(el),
                "size": el.lstat().st_size,
                "hash": hash_file(el)
            }
            for el in files
        ]

        rec_dir = [self.get_records(xdir=el) for el in dirs]
        rec_dir_flat = [rec for folder in rec_dir for rec in folder]
        records = records + rec_dir_flat

        return records






        



