import csv
import json
import os
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    @staticmethod
    def read_xml(path):
        records = ET.parse(path).getroot()
        reports = list()
        for record in records:
            report = dict()
            for children in record:
                report[children.tag] = children.text
            reports.append(report)
        return reports

    @staticmethod
    def read_csv(path):
        with open(path, encoding="utf-8") as file:
            reports = csv.DictReader(file, delimiter=",", quotechar='"')
            return [report for report in reports]

    @staticmethod
    def read_json(path):
        with open(path, encoding="utf-8") as file:
            reports = json.load(file)
            return reports

    @staticmethod
    def import_data(path, type):
        __root, extesion = os.path.splitext(path)

        extesions = {
          ".csv": Inventory.read_csv,
          ".json": Inventory.read_json,
          ".xml": Inventory.read_xml
        }
        if type == 'simples':
            return SimpleReport.generate(extesions[extesion](path))
        return CompleteReport.generate(extesions[extesion](path))
