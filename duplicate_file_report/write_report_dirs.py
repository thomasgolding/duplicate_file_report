from pathlib import Path

import pandas as pd


def read_subreports(csvdir: str) -> pd.DataFrame:
    p = Path(csvdir)
    csvfiles = [el for el in p.iterdir() if ".csv" in el.name]
    df_raw = pd.concat([pd.read_csv(p) for p in csvfiles])
    df_raw.reset_index(drop=True, inplace=True)
    return df_raw


def transform(df_raw: pd.DataFrame) -> pd.DataFrame:
    hash_per_folder = df_raw.groupby("parent_dir").apply(lambda r: r["hash"].tolist())
    n_files = hash_per_folder.apply(len)
    n_files.name = "n_files"
    hash_per_folder_sets = hash_per_folder.apply(frozenset)
    hash_per_folder_sets.name = "hash_set"

    df_tmp = pd.DataFrame(hash_per_folder_sets).reset_index()

    dirs = df_tmp.groupby(by=["hash_set"]).apply(
        lambda r: frozenset(r["parent_dir"].tolist())
    )
    dirs.name = "duplicated_dirs"
    df_res = pd.DataFrame(dirs).reset_index()
    df_res["n_unique_files"] = df_res.apply(lambda r: len(r["hash_set"]), axis=1)
    df_res["n_dirs"] = df_res.apply(lambda r: len(r["duplicated_dirs"]), axis=1)
    df_res["list_duplicated_dirs"] = df_res.apply(
        lambda r: list(r["duplicated_dirs"]), axis=1
    )
    df_res.sort_values(by=["n_dirs", "n_unique_files"], ascending=False, inplace=True)
    return df_res


def write_duplicate_report_dirs(csvdir: str):
    p_csvdir = Path(csvdir)
    if not p_csvdir.exists():
        return

    resdir = p_csvdir / "result"
    result = resdir / "result.csv"
    if not resdir.exists():
        resdir.mkdir()

    df_raw = read_subreports(csvdir=csvdir)
    df_res = transform(df_raw=df_raw)
    df_res.to_csv(result)
