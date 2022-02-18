from concurrent import futures
import grpc

import proto.main_pb2 as chat_proto
import proto.main_pb2_grpc as chat_grpc


class ChattingService(chat_grpc.ChattingServicer):
    def __init__(self):
        self.chat = []

    def MessageStream(self, request, context: grpc.ServicerContext):
        last_read = len(self.chat) - 1
        while context.is_active():
            while last_read < len(self.chat) - 1:
                last_read += 1
                message = self.chat[last_read]
                yield message

    def SendMessage(self, message: chat_proto.Message, context):
        print(f'[{message.author}] {message.text}')
        self.chat.append(message)
        return chat_proto.Empty()

class ChatServer:

    def __init__(self, port=5000, host='[::]', max_workers=10):
        self._port = port
        self._host = host
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        chat_grpc.add_ChattingServicer_to_server(ChattingService(), self._server)

    def serve(self):
        self._server.add_insecure_port(f'{self._host}:{self._port}')
        self._server.start()
        try:
            self._server.wait_for_termination()
        except KeyboardInterrupt:
            self._server.stop(None)

if __name__ == '__main__':
    chat = ChatServer(5000, '[::]')
    chat.serve()