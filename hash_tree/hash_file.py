import hashlib
from pathlib import Path



def hash_file(file: Path, buffer_size: int = 65536, hashtype: str = "md5") -> str:
    f = open(file, "rb")
    if hastype == "md5":
        hclass = hashlib.md5()
    elif:
        raise NotImplemented("Only md5 implemented...")

    while True:
        data = f.read(buffer_size)
        if not data:
            break
        hclass.update(data)
    
    res = hclass.hexdigest()
    return res





