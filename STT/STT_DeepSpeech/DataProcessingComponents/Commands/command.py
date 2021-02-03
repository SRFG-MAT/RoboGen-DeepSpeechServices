from command_interface import ICommand

class Command (ICommand):
    """Represents a basic implemenation of a command."""
    pass

    def __init__(self, command, target: str):
        """Initializes a new instance of the the Command class. The command represents an action which will be executed. The parameter for the command."""
        self.command = command
        self.target = target

    def execute(self) -> None:
        """Executes the injected command with specified parameter."""
        self.command(self.target)




