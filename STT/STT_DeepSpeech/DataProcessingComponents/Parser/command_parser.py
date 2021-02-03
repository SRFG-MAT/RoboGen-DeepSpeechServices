from ..Commands.command_interface import ICommand
from ..Commands.command import Command

class CommandParser:
    def __init__(self, commandSet : list, notifyClient):
        self.commandSet = commandSet
        self.notifyClient = notifyClient
        self.generate_command_pairs()

    def generate_command_pairs(self, commandSet : list):
        self.commandPairs = {}
        for commandName in commandSet:
            self.commandPairs[commandName] = Command(self.notifyClient, commandName)

    def parse(self, input) -> bool:
        if self.commandPairs.get(input) == None:
            return False

        return True