class Device:
    def power_on(self):
        print("Device powered on")


class Printer(Device):
    def print_document(self):
        print("Printing...")


class Scanner(Device):
    def scan_document(self):
        print("Scanning...")


class MultiFunctionMachine(Printer, Scanner):
    pass


machine = MultiFunctionMachine()

machine.power_on()
machine.print_document()
machine.scan_document()