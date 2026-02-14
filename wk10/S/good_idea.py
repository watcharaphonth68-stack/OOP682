class PDFReportgenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        pass

class ExcelReportgenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        pass
class EmailSender:
    def __init__(self, recipient):
        self.recipient = recipient
    def send_email(self, report):
        pass