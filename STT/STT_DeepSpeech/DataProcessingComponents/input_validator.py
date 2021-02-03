import fuzzy
import Levenshtein
from STT_DeepSpeech.DataProcessingComponents.data_processing_result import DataProcessingResult


class Validator:

    soundex = fuzzy.Soundex(4)
    def __init__(self, key_sentences : dict):
        self.key_sentences = key_sentences





    def validate_phonetic_similarities(self, input_text : str, key_sentence : str):
        key_length = len(key_sentence)
        if key_length <= 5:
            levenshtein_max_op = 2
        else:
            levenshtein_max_op = 4

        if Levenshtein.distance(input_text, key_sentence) <= levenshtein_max_op:
            return True

        # if self.soundex(key_sentence) == self.soundex(input_text):
        #     return True

        return False


    def validate_wakeupword(self, input_sentence : str):
        self.wake_up_word = self.key_sentences.get("wake_up_word")
        return self.validate_phonetic_similarities(input_sentence, self.wake_up_word)


    def validate_input(self, input_text):
        if not isinstance(input_text, str):
            return DataProcessingResult(success=False, is_wake_up_word=False, sentence=input_text, guess="Invalid")

        if self.validate_wakeupword(input_text):
            return DataProcessingResult(success=True, is_wake_up_word=True, sentence=input_text, guess=self.wake_up_word)

        for key_sentence in self.key_sentences.get("commands"):
            if self.validate_phonetic_similarities(input_text, key_sentence):
                return DataProcessingResult(success=True, is_wake_up_word=False, sentence=input_text, guess=key_sentence)

        return DataProcessingResult(success=False, is_wake_up_word=False, sentence=input_text, guess="No guess")
