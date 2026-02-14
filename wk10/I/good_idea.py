from abc import ABC, abstractmethod 

class printer:
    @abstractmethod
    def print(self):
        pass 

class scnner:
    @abstractmethod
    def scan(self):
        pass

class fax:
    @abstractmethod
    def fax(self):
        pass

class MultifunctionPrinter(printer, scnner, fax):
    def print(self):
        print("Printing document...")
    def scan(self):
        print("Scanning document...")
    def fax(self):
        print("Faxing document...")