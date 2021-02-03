from abc import  ABC, abstractmethod

class ICommand(ABC):

    def __init__(self, command):
        self.command = command
        super().__init__()

    @abstractmethod
    def execute(self) -> None:
        pass
