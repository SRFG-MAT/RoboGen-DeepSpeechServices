import os
from TTS.vocoder.utils.io import load_checkpoint as load_vocoder_checkpoint
from TTS.vocoder.utils.generic_utils import setup_generator
from TTS.tts.utils.io import load_checkpoint
from TTS.utils.audio import AudioProcessor
from TTS.utils.io import load_config
from TTS.tts.utils.text.symbols import symbols, phonemes
from TTS.tts.utils.synthesis import synthesis
from TTS.tts.utils.generic_utils import setup_model
from scipy.io.wavfile import write
import IPython
import time
import torch


class TTSLib:
    def tts(self, model, text, CONFIG, use_cuda, ap, use_gl, figures=True):
        t_1 = time.time()
        waveform, alignment, mel_spec, mel_postnet_spec, stop_tokens, inputs = synthesis(model, text, CONFIG, use_cuda, ap, self.speaker_id, style_wav=None,
                                                                                         truncated=False, enable_eos_bos_chars=CONFIG.enable_eos_bos_chars)
        # mel_postnet_spec = ap._denormalize(mel_postnet_spec.T)
        if not use_gl:
            waveform = self.vocoder_model.inference(
                torch.FloatTensor(mel_postnet_spec.T).unsqueeze(0))
            waveform = waveform.flatten()
        if use_cuda:
            waveform = waveform.cpu()
        waveform = waveform.numpy()
        rtf = (time.time() - t_1) / (len(waveform) / ap.sample_rate)
        tps = (time.time() - t_1) / len(waveform)
        print(waveform.shape)
        print(" > Run-time: {}".format(time.time() - t_1))
        print(" > Real-time factor: {}".format(rtf))
        print(" > Time per step: {}".format(tps))
        IPython.display.display(IPython.display.Audio(
            waveform, rate=CONFIG.audio['sample_rate']))
        write("../Audio/audio.wav",
              CONFIG.audio['sample_rate'], waveform)
        return alignment, mel_postnet_spec, stop_tokens, waveform

    def __init__(self):
        # # runtime settings
        self.use_cuda = False

        # LOAD TTS MODEL
        # multi speaker
        self.speaker_id = None
        self.speakers = []
        self.ap_vocoder = None
        self.model = None
        self.vocoder_model = None
        self.setup()
        self.language = "de"

        self.TTS_MODEL = f"./tts_model.pth.tar"
        self.TTS_CONFIG = f"./config.json"
        self.VOCODER_MODEL = f"./vocoder_model.pth.tar"
        self.VOCODER_CONFIG = f"./config_vocoder.json"

    def setup(self):
        # load configs
        self.TTS_CONFIG = load_config(self.TTS_CONFIG)
        self.VOCODER_CONFIG = load_config(self.VOCODER_CONFIG)

        # load the audio processor
        self.ap = AudioProcessor(**self.TTS_CONFIG.audio)

        # load the model
        num_chars = len(
            phonemes) if self.TTS_CONFIG.use_phonemes else len(symbols)
        self.model = setup_model(num_chars, len(
            self.speakers), self.TTS_CONFIG)

        self.model, _ = load_checkpoint(
            self.model, self.TTS_MODEL, use_cuda=self.use_cuda)
        self.model.eval()

        # LOAD VOCODER MODEL
        self.vocoder_model = setup_generator(self.VOCODER_CONFIG)
        self.vocoder_model, _ = load_vocoder_checkpoint(
            self.vocoder_model, checkpoint_path=self.VOCODER_MODEL)
        self.vocoder_model.remove_weight_norm()
        self.vocoder_model.inference_padding = 0

        self.ap_vocoder = AudioProcessor(**self.VOCODER_CONFIG['audio'])
        if self.use_cuda:
            self.vocoder_model.cuda()
        self.vocoder_model.eval()

    def generateAudio(self, sentenceToTranslate, language):
        self.language = language
        align, spec, stop_tokens, wav = self.tts(
            self.model, sentenceToTranslate, self.TTS_CONFIG, self.use_cuda, self.ap, use_gl=False, figures=True)
