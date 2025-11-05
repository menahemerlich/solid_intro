from classes.exercies_o3.notifier import Notifier

class PushNotifier(Notifier):
    def send(self, message):
        print(f"warning: {message}")