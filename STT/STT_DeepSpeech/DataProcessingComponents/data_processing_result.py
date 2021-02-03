
class DataProcessingResult:
    def __init__(self, success: bool, is_wake_up_word : bool, sentence : str, guess : str):
        self.success = success
        self.is_wake_up_word = is_wake_up_word
        self.sentence = sentence
        self.guess = guess
