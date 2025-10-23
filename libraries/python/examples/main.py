import argparse
import pathlib
import tojson


parser = argparse.ArgumentParser()
parser.add_argument("config_file", type=pathlib.Path)
args = parser.parse_args()

print(tojson.load_config(args.config_file))
