import kagglehub
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
# Download latest version
path = kagglehub.dataset_download("tawsifurrahman/covid19-radiography-database",
                                  output_dir=DATA_DIR)

print("Path to dataset files:", path)
