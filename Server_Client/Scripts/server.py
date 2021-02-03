import flask
from flask import request, jsonify
from flask_api import status

from EN.loadEN import TTSLib as TTSEN
from DE.loadDE import TTSLib as TTSDE

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# different instances for different languages
ttsEN = TTSEN()
ttsDE = TTSDE()


def readBytesOfFile(pathToFile):
    fileStreamRead = open(pathToFile, "rb")
    data = fileStreamRead.read()
    fileStreamRead.close()
    return data


def checkIfArgumentsAreValid(language):
    listOfStrings = ['de', 'deutsch', 'en', 'english']
    if language in listOfStrings:
        return True

    return False


def createAudioFile(receivedText, language):
    if "en" in language:
        ttsEN.generateAudio(receivedText)

    if "de" in language:
        ttsDE.generateAudio(receivedText)


def getByteList(data):
    byteList = []

    for byte in data:
        byteList.append(byte)

    return byteList


@app.route('/audio', methods=['GET'])
def getAudioFromFile():

    receivedText = request.args.get("text")
    language = request.args.get("language")

    # https://www.flaskapi.org/api-guide/status-codes/
    if not checkIfArgumentsAreValid(language):
        content = {'Message': "Invalid language selection!"}
        return content, status.HTTP_400_BAD_REQUEST

    print("[GET-Request]: Data received: ", receivedText)
    createAudioFile(receivedText, language)
    byteList = getByteList(readBytesOfFile("./Audio/serverAudio.wav"))

    return jsonify({'data': byteList})


app.run(host='0.0.0.0')
