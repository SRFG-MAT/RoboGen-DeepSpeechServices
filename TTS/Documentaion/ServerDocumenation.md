# Server

The server runs over Flask and therefore offers several Get-Requests which can be requested by the Q.BO.

## Setup Flask

```ps
pip3 install flask
```

Create an fileName.py with base structure below and execute with:

```python
import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/audio', methods=['GET'])
def getData():
    return jsonify('data': data)

app.run(host='0.0.0.0')
```

This structure offers now a requests like for example `127.0.0.1:5000/audio`, which returns a Json. Return value has to of the type "`response`, `json`, `string`".

```ps
sudo python3 fileName.py
```

## Gernerl Concept

To make the server "public" (accessable/visible within the network) you need to use `app.run(host='0.0.0.0')`.
Trought this you can make requests to the port 5000 (default). The IP-Adress is the default IP-Adress of the maschine.

The server offers two differnet get requests. `audio` and `text`.

**Audio** --> Audio is used to get an request, with a specifyed text. The text will be converted to a .wav file and will save it on the server as temp. <br>
Which will be the response of the server. The data will be transferd as bytes. <br>
Those bytes will be rebuild as .mp3 on the client side (Q.Bo). This file will be played as audio.<br>
Possible **arguments** for the request are `text` (the text to translate) and `language`. Currently supported languages are english and german.
Currently

## References

https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://de.wikipedia.org/wiki/Flask
https://www.fullstackpython.com/flask.html
https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
<br>
<br>
<br>

# Client

```
pip install requests
```

## Request Setup

```py
import argparse
import requests
```

The argparser offers a lot of different options to use commandline argument and to handle them pretty easy.
Below the configuring of the commandline arguments and how you can access them:

```py
argsparser = argparse.ArgumentParser(description="Started Client")
argsparser.add_argument("-host", "--hostname", required=True, help="Hostname is required!")

response = getAudioRequest(args.hostname, args.port, args.text, args.language)
```

How to make an request is shown below:

```py
return requests.get(f'http://127.0.0.1:5000/audio', params={'text': "Text to translate", 'language': "de"})
```

The request returns a resonse. You can validate the status of the request, like if it was 200 (Success), or any 4xx status code. Depending on the status code you can handle the result.

The json content of the result can be used like this:

```py
response.json()['data']
```

## References

https://realpython.com/api-integration-in-python/
https://stackoverflow.com/questions/6787233/python-how-to-read-bytes-from-file-and-save-it
https://realpython.com/python-requests/
https://pypi.org/project/requests/
https://docs.python.org/3/library/argparse.html
https://docs.python.org/3/howto/argparse.html
https://realpython.com/command-line-interfaces-python-argparse/
