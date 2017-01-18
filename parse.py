import csv
from multiprocessing import cpu_count
import os.path
from xml.etree import ElementTree
import zipfile

from concurrent.futures import ProcessPoolExecutor

from config import ZIP_DIR, CSV_DIR, LEVELS_CSV, OBJECTS_CSV, logger
from exception import CsvGenerateException, ZipDirectoryException
from service import check_dir


def parse_xml(xml):
    """Parse single xml file in zip archive

    :xml: string xml file.

    """
    tree = ElementTree.fromstring(xml)
    name = tree.findall("./var[@name='id']")[0]
    level = tree.findall("./var[@name='level']")[0]
    if len(name) or len(level):
        logger.warning("Missing level or name in XML")

    return {
        'id': name.attrib['value'],
        'level': level.attrib['value'],
        'objects': [obj.attrib['name'] for obj in tree.findall('./objects/object')]
    }


def extract_xml(path_to_zip):
    """Write all data from xml files in zip archive to csv file

    :path_to_zip: string path to zip file.

    """
    levels, objects = [], []
    with zipfile.ZipFile(path_to_zip, 'r') as zf:
        for filename in zf.namelist():
            if filename.endswith('.xml'):
                with zf.open(filename, 'r') as xml:
                    parsed_data = parse_xml(xml.read())
                    levels.append('{} {}'.format(parsed_data['id'], parsed_data['level']))
                    for obj in parsed_data["objects"]:
                        objects.append('{} {}'.format(parsed_data['id'], obj))

    write_to_csv(LEVELS_CSV, levels)
    write_to_csv(OBJECTS_CSV, objects)


def write_to_csv(csv_path, data):
    """Write data to csv file

    :csv_path: string path to csv file.
    :data: string data to write in csv file.

    """
    try:
        with open(csv_path, 'ab') as cf:
            writer = csv.writer(cf, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar="|")
            writer.writerows(data)
    except IOError as err:
        logger.exception("Something went wrong with CSV files")
        raise CsvGenerateException(str(err))


def create_csvs():
    """Create all csv files in CSV_DIR and write data"""
    try:
        zip_names = [os.path.join(ZIP_DIR, zip_name) for zip_name in os.listdir(ZIP_DIR) if zip_name.endswith(".zip")]
    except OSError as err:
        logger.exception("Can't find zip files")
        raise ZipDirectoryException(str(err))

    check_dir(CSV_DIR)
    logger.info("Run parse XMLs")
    with ProcessPoolExecutor(cpu_count()) as executor:
        return executor.map(extract_xml, zip_names)

if __name__ == "__main__":
    logger.info("Begin parse zips")
    create_csvs()
    logger.info("All csv files generated in %s", CSV_DIR)
