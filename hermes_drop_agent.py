"""
The Magic Walnut Plant Shoppe — Hermes Weekly Drop Agent Utility
Location: H:\\The Magic Walnut Plants Sales\\website\\hermes_drop_agent.py

Usage by Hermes Agent or Dustin:
1. Drop your weekly plant photos into a folder (e.g., H:\\The Magic Walnut Plants Sales\\10-28-2026)
2. Run:
   python hermes_drop_agent.py --folder "H:\\The Magic Walnut Plants Sales\\10-28-2026" --manifest "Monstera Albo|115|IMG_1670.JPG,IMG_1662.JPG;Thai Constellation|75|IMG_1686.JPG"
   OR simply drop a `drop.txt` file inside the photo folder where each line is:
   Plant Name | Price | Category | img1.jpg, img2.jpg | Description
"""

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

WEBSITE_DIR = Path(__file__).resolve().parent
CATALOG_PATH = WEBSITE_DIR / "catalog.json"
ASSETS_PLANTS_DIR = WEBSITE_DIR / "assets" / "plants"


def load_catalog() -> dict:
    if CATALOG_PATH.exists():
        return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return {"shopInfo": {}, "plants": [], "merch": []}


def save_catalog(data: dict) -> None:
    CATALOG_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[Hermes Drop Agent] Saved updated catalog -> {CATALOG_PATH}")


def ingest_weekly_drop(source_folder: Path, manifest_str: str = "", wipe_previous: bool = False) -> None:
    ASSETS_PLANTS_DIR.mkdir(parents=True, exist_ok=True)
    catalog = load_catalog()

    if wipe_previous:
        catalog["plants"] = []

    entries = []
    drop_txt = source_folder / "drop.txt"
    if manifest_str:
        entries = [line.strip() for line in manifest_str.split(";") if line.strip()]
    elif drop_txt.exists():
        entries = [
            line.strip()
            for line in drop_txt.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]

    for idx, entry in enumerate(entries, start=1):
        parts = [p.strip() for p in entry.split("|")]
        name = parts[0]
        price = int(float(parts[1])) if len(parts) > 1 else 50
        image_names = [img.strip() for img in parts[2].split(",") if img.strip()] if len(parts) > 2 else []
        category = parts[3] if len(parts) > 3 else "Monstera"
        desc = parts[4] if len(parts) > 4 else "1-of-1 exact sanctuary plant photographed this week."

        rel_images = []
        for img_name in image_names:
            src_img = source_folder / img_name
            if src_img.exists():
                dest_img = ASSETS_PLANTS_DIR / src_img.name
                shutil.copy2(src_img, dest_img)
                rel_images.append(f"assets/plants/{src_img.name}")

        plant_id = f"mw-{datetime.now().strftime('%m%d')}-{idx:03d}"
        catalog["plants"].insert(
            0,
            {
                "id": plant_id,
                "name": name,
                "botanical": f"{category} sanctuary specimen",
                "price": price,
                "type": "WYSIWYG",
                "category": category,
                "status": "available",
                "stock": 1,
                "potSize": '4" Clear Sanctuary Cup',
                "rootStatus": "Rooted in Chunky Aroid Mix",
                "light": "Bright Indirect",
                "badge": "1-OF-1 EXACT PLANT",
                "description": desc,
                "images": rel_images or ["assets/logos/2.png"],
            },
        )

    catalog.setdefault("shopInfo", {})["dropDate"] = datetime.now().strftime("%Y-%m-%d")
    save_catalog(catalog)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hermes Weekly Plant Drop Publisher")
    parser.add_argument("--folder", type=str, required=True, help="Path to weekly plant photos folder")
    parser.add_argument("--manifest", type=str, default="", help="Semicolon-separated 'Name|Price|img1,img2|Category|Desc'")
    parser.add_argument("--wipe", action="store_true", help="Archive/clear previous week's plants before publishing")
    args = parser.parse_args()

    ingest_weekly_drop(Path(args.folder), args.manifest, args.wipe)
