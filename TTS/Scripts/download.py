import gdown

# 2.7
# operation = raw_input()("Choose one operation below")


def switchDownload(operation):
    switcher = {
        1: downloadTTSModel,
        2: downloadTTSConfigFile,
        3: downloadVocoderModel,
        4: downloadVocoderConfigModel,
        5: downloadScaleStats,
        9: downloadAll,
    }

    switcher.get(operation, lambda: "Invalid Argument")()


def downloadTTSModel():
    # download tts model
    url1 = 'https://drive.google.com/uc?id=1VG0EI7J6S1bk3h0q1VBc9ALExkdZdeVm'
    output1 = 'tts_model.pth.tar'
    gdown.download(url1, output1, quiet=False)
    print("Download Finished!")


def downloadTTSConfigFile():
    # download tts config file
    url2 = 'https://drive.google.com/uc?id=1s1GcSihlj58KX0LeA-FPFvdMWGMkcxKI'
    output2 = 'config.json'
    gdown.download(url2, output2, quiet=False)
    print("Download Finished!")


def downloadVocoderModel():
    # download vocoder model
    url3 = 'https://drive.google.com/uc?id=1zYFHElvYW_oTeilvbZVLMLscColWRbck'
    output3 = 'vocoder_model.pth.tar'
    gdown.download(url3, output3, quiet=False)
    print("Download Finished!")


def downloadVocoderConfigModel():
    # download vocoder config file
    url4 = 'https://drive.google.com/uc?id=1ye9kVDbatAKMncRMui7watrLQ_5DaJ3e'
    output4 = 'config_vocoder.json'
    gdown.download(url4, output4, quiet=False)
    print("Download Finished!")


def downloadScaleStats():
    # download scale stats
    url5 = 'https://drive.google.com/uc?id=1QD40bU_M7CWrj9k0MEACNBRqwqVTSLDc'
    output5 = 'scale_stats.npy'
    gdown.download(url5, output5, quiet=False)
    print("Download Finished!")


def downloadAll():
    downloadTTSModel()
    downloadTTSConfigFile()
    downloadVocoderModel()
    downloadVocoderConfigModel()
    downloadScaleStats()


print("[1] --> Download TTSModel")
print("[2] --> Download TTSConfigFile")
print("[3] --> Download VocoderModel")
print("[4] --> Download VocoderConfigModel")
print("[5] --> Download ScaleStats")
print("[9] --> Download All")
print("[0] --> Exit")

operation = ""

while operation != 0 or operation != 0:
    operation = input("Choose one operation below: ")
    switchDownload(int(operation))
