import argparse
from pathlib import Path

from duplicate_file_report.write_report import generate_report
from duplicate_file_report.write_report_dirs import write_duplicate_report_dirs


def cltool():
    parser = argparse.ArgumentParser(description="Duplicate file report.")
    parser.add_argument("rootdir", help="The rootdir for which to generate the report.")
    parser.add_argument("target", help="File where report is saved.")
    args = parser.parse_args()

    p = Path(args.rootdir)
    t = Path(args.target)
    if t.exists():
        print("Target must not exist.")
        return

    if p.is_dir() and p.exists():
        rep = generate_report(path=p)
        rep.to_csv(t)
        print(f"Report written in {t.name}")
    else:
        print("not valid rootdir.")


def cltool_dir():
    parser = argparse.ArgumentParser(description="Duplicate directory report.")
    parser.add_argument("csvdir", help="The directory containing csv reports.")
    args = parser.parse_args()

    p = Path(args.csvdir)

    if p.is_dir() and p.exists():
        write_duplicate_report_dirs(csvdir=args.csvdir)
