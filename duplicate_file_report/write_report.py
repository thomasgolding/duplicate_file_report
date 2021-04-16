from pathlib import Path

import pandas as pd

from hash_tree.hash_tree import HashTree


def generate_report(path: Path):
    hashtree = HashTree(rootpath=path)
    tree = hashtree.get_tree()
    df = pd.DataFrame.from_records(tree)
    hashcol = df["hash"].value_counts()
    # hashcol=hashcol[hashcol>1]
    hashcol.name = "duplicates"
    res = df.merge(hashcol, left_on="hash", right_index=True)
    res.sort_values(by=["duplicates", "hash"], ascending=False, inplace=True)
    return res
