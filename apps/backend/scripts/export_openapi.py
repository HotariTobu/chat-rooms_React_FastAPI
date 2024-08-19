import argparse
import json
from pathlib import Path

from src.main import app

parser = argparse.ArgumentParser(description="Export OpenAPI schema file.")
parser.add_argument(
    "output_path", type=Path, help="Path to the output OpenAPI schema file"
)
args = parser.parse_args()

output_path: Path = args.output_path

with output_path.open("w") as f:
    json.dump(app.openapi(), f)
