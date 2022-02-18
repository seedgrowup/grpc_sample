import threading
import grpc

import proto.main_pb2 as chat_proto
import proto.main_pb2_grpc as chat_grpc

class ChatClient:

    def __init__(self, port=5000, host='127.0.0.1'):
        self._port = port
        self._host = host
        self._on_message_receive = None
        self._channel = grpc.insecure_channel(f'{self._host}:{self._port}')
        self._chat_service = chat_grpc.ChattingStub(self._channel)

    def start_listen_messages(self, message_received):
        self._on_message_receive = message_received
        threading.Thread(target=self._listen_for_messages, daemon=True).start()

    def _listen_for_messages(self):
        for message in self._chat_service.MessageStream(chat_proto.Empty()):
            self._on_message_receive(message)

    def send_message(self, username, text):
        message = chat_proto.Message()
        message.author = username
        message.text = text
        self._chat_service.SendMessage(message)

    def close(self):
        self._channel.close()

class Chat:

    def __init__(self, chat_client: ChatClient):
        self.username = ''
        self._chat_client = chat_client

    def start(self):
        self._get_username()
        self._chat_client.start_listen_messages(self._message_received)
        self._get_inputs()

    def _get_username(self):
        while not self.username:
            self.username = input('Enter Username: ')

    def _message_received(self, message):
        print(f'[{message.author}]: {message.text}')

    def _get_inputs(self):
        try:
            text = input()
            while True:
                if text:
                    self._chat_client.send_message(self.username, text)
                text = input()
        except KeyboardInterrupt:
            pass
        self._chat_client.close()

if __name__ == '__main__':
    chat = Chat(ChatClient(5000, '127.0.0.1'))
    chat.start()