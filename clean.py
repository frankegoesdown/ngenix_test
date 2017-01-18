import os.path
import shutil

from config import ZIP_DIR, CSV_DIR


def remove_all_temp_folders():
    if os.path.exists(ZIP_DIR):
        shutil.rmtree(ZIP_DIR)
    if os.path.exists(CSV_DIR):
        shutil.rmtree(CSV_DIR)

if __name__ == "__main__":
    remove_all_temp_folders()
