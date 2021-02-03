from STT_DeepSpeech.ApplicationComponents.application import App
import argparse

# modelFile = "E:\\PyCharm\\Projects\\output_graph_from_koh-osug.tflite"
# scorerFile = "E:\\PyCharm\\Projects\\kenlm.scorer"
# wake_up_word = "aufwachen"

if __name__ == "__main__":
    argsParser = argparse.ArgumentParser(description="Starting streaming from microphone to deepspeech using VAD")

    argsParser.add_argument("-wup", "--wake_up_word", required=True,
                        help="Set the wake-up word for the Qbo.")
    argsParser.add_argument("-m", "--model", required=True,
                        help="Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)")
    argsParser.add_argument("-s", "--scorer", required=True,
                        help="Path to the external scorer file.")
    argsParser.add_argument('-w', '--savewav',
                        help="Save .wav files of utterences to given directory")

    ARGS = argsParser.parse_args()
    if str(ARGS.wake_up_word).isspace():
        raise ValueError("The wake up word must cannot be empty.")

    app = App(ARGS.wake_up_word, ARGS.model, ARGS.scorer)
    app.run()