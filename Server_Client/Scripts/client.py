import requests
import argparse


def writeBytesToFile(dataToWrite):
    fileStreamWrite = open("./clientAudio.mp3", "wb")
    fileStreamWrite.write(dataToWrite)
    fileStreamWrite.close()


def saveReceivedAudioFile(resp):
    if resp.status_code != 200:
        print(f"{resp.status_code}: {resp.json()['Message']}!")
        return

    writeBytesToFile(bytearray(resp.json()['data']))
    print("Audio file saved")


def getAudioRequest(hostName, port, text, language):
    return requests.get(f'http://{hostName}:{port}/audio', params={'text': text, 'language': language})


if __name__ == "__main__":
    argsparser = argparse.ArgumentParser(description="Started Client")
    argsparser.add_argument("-host", "--hostname",
                            required=True, help="Hostname is required!")
    argsparser.add_argument(
        "-p", "--port", help="Port is optional!", default=5000)

    argsparser.add_argument("-t", "--text", required=True,
                            help="Text to translate is required!")

    argsparser.add_argument("-l", "--language",
                            help="Language of speaker is in default German! Supported --> [en | de]!", default="de")

    args = argsparser.parse_args()

    response = getAudioRequest(
        args.hostname, args.port, args.text, args.language)
    saveReceivedAudioFile(response)
