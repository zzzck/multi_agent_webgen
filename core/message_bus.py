class MessageBus:
    def __init__(self):
        self.storage = {}

    def publish(self, key, value):
        self.storage[key] = value

    def subscribe(self, key):
        return self.storage.get(key, None)

    def dump(self):
        return self.storage
