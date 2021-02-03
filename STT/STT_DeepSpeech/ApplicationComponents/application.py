import pyaudio
from pymitter import EventEmitter
import STT_DeepSpeech.VAD_Deepspeech_Module.mic_vad_streaming as vadToDeepSpeechTool
from STT_DeepSpeech.VAD_Deepspeech_Module import mic_vad_streaming_args
from STT_DeepSpeech.DataProcessingComponents import data_processing_unit, data_processing_result


class App:

    # Give us access to the input and output devices.
    audio_manager = pyaudio.PyAudio()


    # The sensitivity for the VAD.
    vad_aggression_factor = 3

    # Sample rate for the VAD tool.
    sample_rate = 16000

    #
    nospinner = True

    # The path for the saved audio files.
    savewav = None


    file_path = None
    # wake up word =
    command_set = { "commands" : ["hilfe", "anrufen", "schmerzen", "ich habe schmerzen", "ich brauche hilfe", "hallo"] }

    # Initializes a new instance of the app class.
    def __init__(self, wake_up_word, model_file, scorer_file):
        self.command_set["wake_up_word"] = wake_up_word
        self.model_file = model_file
        self.scorer_file = scorer_file
        self.input_device = pyaudio.PyAudio.get_default_input_device_info(self.audio_manager)
        self.input_device_index = self.input_device.get("index")

    def notify_client(self, data : data_processing_result.DataProcessingResult):
        print("Eingabe:", "\n", "Cubo ist bereit:", data.is_wake_up_word, "\n", "Verstanden:", data.sentence, "\n", "Vermutung:", data.guess, "\n" )

    # Callback for the onDataReceived event.
    # @on_data_received_emitter.on("handle_received_data")
    # def handleData(self, data):
    #     print("Received data: %s" % data)

    # Runs the app.
    def run(self):
        # Fired when input is available.

        self.on_data_received_emitter = EventEmitter()
        self.on_notification_emitter = EventEmitter()
        self.on_notification_emitter.on("notify_client", self.notify_client)

        self.data_processing_unit = data_processing_unit.DataProcessingUnit(self.on_data_received_emitter,
                                                                            self.on_notification_emitter,
                                                                            self.command_set)
        self.data_processing_unit.start_processing()

        args = mic_vad_streaming_args.VADArgs(self.model_file, self.scorer_file, self.vad_aggression_factor, self.input_device_index,
                                              self.sample_rate, self.file_path, self.nospinner, self.savewav, self.on_data_received_emitter)
        vadToDeepSpeechTool.main(args)