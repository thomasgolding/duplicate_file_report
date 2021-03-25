import hashlib
from pathlib import Path



def hash_file(file: Path, buffer_size: int = 65536):
    f = open(file, "rb")
    hclass = hashlib.md5()

    while True:
        data = f.read(buffer_size)
        if not data:
            break
        hclass.update(data)
    
    res = hclass.hexdigest()
    return res





