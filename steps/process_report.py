import json

from steps.step import AbstractStep


class ProcessReportStep(AbstractStep):
    def __init__(self, doc_id, report_file, reports_repository):
        self._doc_id = doc_id
        self._report_file = report_file
        self._reports_repository = reports_repository

    def process(self):
        with open(self._report_file.full_path(), 'r') as f:
            report = json.load(f)

            report_doc = {
                '_id': self._doc_id,
                'report': report
            }

            self._reports_repository.insert_document(report_doc)

            return report
