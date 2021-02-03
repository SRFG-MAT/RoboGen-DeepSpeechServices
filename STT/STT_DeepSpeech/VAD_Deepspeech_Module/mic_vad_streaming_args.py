class VADArgs:

    def __init__(self, model, scorer, vad_aggressiveness, device, rate, file, nospinner, savewav, on_data_received_emitter):
        self.model = model
        self.scorer = scorer
        self.vad_aggressiveness = vad_aggressiveness
        self.device = device
        self.rate = rate
        self.file = file
        self.nospinner = nospinner
        self.savewav = savewav
        self.eventEmitter = on_data_received_emitter
