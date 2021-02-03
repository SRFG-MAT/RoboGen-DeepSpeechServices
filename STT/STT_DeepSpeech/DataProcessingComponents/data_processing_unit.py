from STT_DeepSpeech.DataProcessingComponents.input_queue import InputQueue
from STT_DeepSpeech.DataProcessingComponents.input_validator import Validator
from multiprocessing import Process
from threading import Thread
import time

class DataProcessingUnit:

    # Fired when input is available.

    def __init__(self, on_data_received_emitter, on_notification_emitter, validCommandSet: dict):
        self.command_set = validCommandSet
        self.on_data_received_emitter = on_data_received_emitter
        self.on_data_received_emitter.on("handle_data", self.handle_data)
        self.on_notification_emitter = on_notification_emitter
        self.input_queue = InputQueue(100)
        self.validator = Validator(validCommandSet)
        self.running = False
        self.wakeUp = False


    # Callback for the onDataReceived event.
    def handle_data(self, data):
        self.input_queue.enqeue_input(data)



    def start_processing(self):

        if not self.running:
            self.running = True
            self.queue_worker = Thread(target=self.worker, args=(self.input_queue,))
            self.queue_worker.setDaemon(True)
            self.queue_worker.start()



    def stop_processing(self):
        if self.running:
            self.queue_worker.join()
            self.running = False

    def worker (self, input_queue):

        while self.running:
            item = input_queue.dequeue_input()
            if not item[0]:
                time.sleep(0.1)
                continue

            sentence = item[1]
            result = self.validator.validate_input(sentence)
            if result.is_wake_up_word:
                self.wakeUp = True

            result.is_wake_up_word = self.wakeUp
            self.on_notification_emitter.emit("notify_client", result)
