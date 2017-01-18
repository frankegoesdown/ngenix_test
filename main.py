from clean import remove_all_temp_folders
from generate import create_zips
from parse import create_csvs

if __name__ == "__main__":
    remove_all_temp_folders()
    create_zips()
    create_csvs()
