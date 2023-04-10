import sys
import argparse
import zipfile
import os

DEFAULT_OUTPUT = "output.zip"

def getargs(args=sys.argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", nargs="+", required=True)
    parser.add_argument("-o", "--output", help="output path", default=os.path.join(".", DEFAULT_OUTPUT))

    return parser.parse_args()

def compresslist(files: list, output: str, compression: int = zipfile.ZIP_DEFLATED) -> None:
    try:
        if os.path.isdir(output):
            output = os.path.join(output, DEFAULT_OUTPUT)
        zf = zipfile.ZipFile(output, mode="w")
        for file in files:
            zf.write(file, os.path.basename(file), compress_type=compression)
        zf.close()

    except (FileNotFoundError, PermissionError) as e:
        print(f"[ERROR] {e}")

if __name__=="__main__":
    args = getargs()
    files = args.input
    if os.path.isdir(args.input[0]):
        files = [ent.path for ent in os.scandir(args.input[0]) if ent.is_file()]
    
    compresslist(files, args.output)