import queue


class InputQueue:

    def __init__(self, max_Size: int):
        self.input_queue = queue.Queue(max_Size)

    # Enqueues a value to the input queue.
    def enqeue_input(self, input):
        if input == None or not isinstance(input, str):
            raise ValueError("The value cannot be none and must be of type string.")

        if str(input).isspace() or input == "":
            return

        self.input_queue.put(input)

    # Dequeues a value from the input queue.
    def dequeue_input(self):
        if self.input_queue.empty():
            return False, None

        return True, self.input_queue.get()
