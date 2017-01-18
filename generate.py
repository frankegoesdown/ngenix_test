from multiprocessing import cpu_count
import os.path
import random
import string
import uuid
import zipfile

from concurrent.futures import ProcessPoolExecutor
from xml.etree import ElementTree

from config import ZIP_DIR, COUNT_XMLS, COUNT_ZIPS, logger
from exception import ZipGenerateException


def generate_random_text(length):
    """Return string contains of uppercase symbols and digits without separators

    :length: integer length of returned string.

    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def create_xml():
    """Generate Xml

    Xml looks like:
    <root>
        <var name='id' value='random unique string value'/>
        <var name='level' value='random digit by 1 to 100'/>
        <objects>
            <object name='random string value'/>
            <object name='random string value'/>
            ...
        </objects>
    </root>

    """
    root = ElementTree.Element("root")
    var = ElementTree.SubElement(root, "var")
    var.attrib["name"] = "id"
    var.attrib["value"] = uuid.uuid4().hex

    var = ElementTree.SubElement(root, "var")
    var.attrib["name"] = "level"
    var.attrib["value"] = str(random.randint(1, 101))

    level = random.randint(1, 101)
    objects = ElementTree.SubElement(root, "objects")
    for i in range(level):
        obj = ElementTree.SubElement(objects, "object")
        obj.attrib["name"] = generate_random_text(random.randint(1, 11))

    return ElementTree.tostring(root, "utf-8")


def create_zip(zip_name):
    """Generate zip file with xmls files in ZIP_DIR

    :zip_name: string name of zip file.

    """
    path = os.path.join(ZIP_DIR, zip_name)

    try:
        with zipfile.ZipFile(path, "w") as zf:
            for it in range(COUNT_XMLS):
                filename = "{}.xml".format(it)
                xml = create_xml()
                zf.writestr(filename, xml)
    except IOError as er:
        raise ZipGenerateException(str(er))


def create_all_zips():
    """Generate all zips files in ZIP_DIR"""
    if not os.path.exists(ZIP_DIR):
        os.mkdir(ZIP_DIR)

    zip_names = [os.path.join(ZIP_DIR, "{}.zip".format(i)) for i in range(COUNT_ZIPS)]
    with ProcessPoolExecutor(cpu_count()) as executor:
        return executor.map(create_zip, zip_names)


if __name__ == "__main__":
    logger.info("Begin generate zips")
    create_all_zips()
    logger.info("All zip files generated in %s", ZIP_DIR)
