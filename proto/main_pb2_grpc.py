# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.main_pb2 as main__pb2


class ChattingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MessageStream = channel.unary_stream(
                '/grpc.Chatting/MessageStream',
                request_serializer=main__pb2.Empty.SerializeToString,
                response_deserializer=main__pb2.Message.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/grpc.Chatting/SendMessage',
                request_serializer=main__pb2.Message.SerializeToString,
                response_deserializer=main__pb2.Empty.FromString,
                )


class ChattingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MessageStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChattingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MessageStream': grpc.unary_stream_rpc_method_handler(
                    servicer.MessageStream,
                    request_deserializer=main__pb2.Empty.FromString,
                    response_serializer=main__pb2.Message.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=main__pb2.Message.FromString,
                    response_serializer=main__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.Chatting', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chatting(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MessageStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpc.Chatting/MessageStream',
            main__pb2.Empty.SerializeToString,
            main__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.Chatting/SendMessage',
            main__pb2.Message.SerializeToString,
            main__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)