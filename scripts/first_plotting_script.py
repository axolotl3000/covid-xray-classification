from covidxray.plotting import plot_image, read_image
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RESULTS_DIR = ROOT / "results"

# Image import
img = read_image(DATA_DIR / "COVID-19_Radiography_Dataset" / "COVID" / "images" / "COVID-125.png")

print(img.shape)


fig, ax = plot_image(img, title="COVID-19 X-ray Image")
fig.savefig(RESULTS_DIR / "test_plot.png")
