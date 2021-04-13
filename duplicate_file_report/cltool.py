from pathlib import Path
import argparse

from duplicate_file_report.write_report import generate_report

    
def cltool():
    parser = argparse.ArgumentParser(description='Duplicate file report.')
    parser.add_argument("rootdir", help="The rootdir for which to generate the report.")
    args = parser.parse_args()

    p = Path(args.rootdir)
    if p.is_dir() and p.exists():
        rep = generate_report(path=p)
        print(rep)
    else:
        print("not valid rootdir.")
    


if __name__ == __name__:
    cltool()