
# Complex subclass
class CPU:
    def os(self):
        print("initializing OS")

class Memory:
    def load(self):
        print("load memory")

class HardDrive:
    def read(self, data):
        print(f"{data}")


# Facade
class ComputerFacade:

    def __init__(self):
        self.cpu = CPU()
        self.load = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.os()
        self.load.load()
        self.hard_drive.read(20)


my_pc = ComputerFacade()
my_pc.start_computer()
