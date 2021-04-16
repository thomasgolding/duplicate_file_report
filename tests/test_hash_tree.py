from pathlib import Path

from hash_tree.hash_tree import HashTree

# from tests.test_fixtures import dir_with_one_duplicate

#  from tests.test_fixtures import dir_with_one_duplicate

hashtypes = ["md5"]


def test_filehash(dir_with_one_duplicate):
    p = Path(dir_with_one_duplicate)
    hashtree = HashTree(rootpath=p)
    tree = hashtree.get_tree()
    all_hashes = [el["hash"] for el in tree]
    all_filenames = [el["pathstring"] for el in tree]
    assert len(all_filenames) == len(set(all_filenames))
    assert len(all_hashes) == len(set(all_hashes)) + 1
