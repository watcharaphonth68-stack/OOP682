class machine:
    def print(self):
        pass
    def scan(self):
        pass
    def fax(self):
        pass

class OldPrinter(machine):
    def print(self):
        print("Printing document...")
    def scan(self):
        raise NotImplementedError("This printer cannot scan.")
    def fax(self):
        raise NotImplementedError("This printer cannot fax.")