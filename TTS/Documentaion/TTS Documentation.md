# TTS Documentation

## Introduction

We use the free available library of "Mozilla/TTS". These provide many standalone functions for the conversion of written word to spoken language by a computer.
We use Tacotron2 and ParallelWaveGAN models and Thorsten_DE dataset.

Tacotron2 is trained using Double Decoder Consistency (DDC) only for 130K steps (3 days) with a single GPU.
Note 1: That model performance can be improved with more training.
Note 2: Due to a mistake at training configuration, this models does not read numbers written in digit form.
Note 3: The minimum required version of python is >=3.6

## Manual

### Step 1 (Setup Vm)

```sh
sudo apt-get install python3-pip
sudo apt-get install git
sudo apt-get install espeak
```

### Step 2 (Download)

```
git clone https://github.com/mozilla/TTS
```

### Step 3 (Additions)

```sh
git checkout 540d811
sudo pip3 install -r requirements.txt
sudo python3 setup.py install
sudo pip3 install IPython
```

Incase "sudo pip3 install -r requirements.txt" returns the errors move to "Step 4"

### Step 4 (Correction of Packages)

The requirements can differ from the setup so we need to do a small correction:

```sh
sudo pip3 install numpy==1.18
sudo pip3 install scipy==1.4.1
```

### Step 5 (Execution)

One of those:

```
python3 loadDE.py
python3 loadEN.py
```

## Usage

### Get Requests

**Audio request**

- Get Request --> GetAudioFromText(textToSpeak) --> .mp3
- Get Request --> GetAudioFromText(textToSpeak, language [de | deutsch | german | en | english]) --> .mp3
<!-- 
**Text requests**


- Get Request -> GetTextFromAudio(text) -> string
- Get Request -> GetTextFromAudio(text, language [de | deutsch | german | en | english]) -> string -->

## References

- Guide --> https://colab.research.google.com/drive/1SPl226SwzrfMZltrVagIXya_ax4CsMh-?usp=sharing#scrollTo=4dnpE0-kvTsu
- TSS Lib --> https://github.com/mozilla/TTS
- Tutorials --> https://github.com/mozilla/TTS/wiki/TTS-Notebooks-and-Tutorials
- General Info --> https://github.com/mozilla/TTS/wiki/FAQ

### German Downloads

    * https://drive.google.com/uc?id=1VG0EI7J6S1bk3h0q1VBc9ALExkdZdeVm
    * https://drive.google.com/uc?id=1s1GcSihlj58KX0LeA-FPFvdMWGMkcxKI
    * https://drive.google.com/uc?id=1zYFHElvYW_oTeilvbZVLMLscColWRbck
    * https://drive.google.com/uc?id=1ye9kVDbatAKMncRMui7watrLQ_5DaJ3e
    * https://drive.google.com/uc?id=1QD40bU_M7CWrj9k0MEACNBRqwqVTSLDc

### English Downloads

    * https://drive.google.com/uc?id=1dntzjWFg7ufWaTaFy80nRz-Tu02xWZos
    * https://drive.google.com/uc?id=18CQ6G6tBEOfvCHlPqP8EBI4xWbrr9dBc
    * https://drive.google.com/uc?id=1Ty5DZdOc0F7OTGj9oJThYbL5iVu_2G0K
    * https://drive.google.com/uc?id=1Rd0R_nRCrbjEdpOwq6XwZAktvugiBvmu
    * https://drive.google.com/uc?id=11oY3Tv0kQtxK_JPgxrfesa99maVXHNxU

### Addtional Information

The "use_cuda" option can be enabled in case the NVIDIA Drivers are installed and the GPU is avaible

### Own Scripts

- downloadEN.py --> Provides a function to download each file from the section "Downloads" for the english models
- downloadDE.py --> Provides a function to download each file from the section "Downloads" for the german models
- loadEN.py --> Creates the setup for the model
- loadDE.py --> Creates the setup for the model
- server.py --> Provides the request (api) for the client
- client.py --> The client, which can make requests
