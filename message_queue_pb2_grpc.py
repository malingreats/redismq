# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import message_queue_pb2 as message__queue__pb2


class MessageQueueStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send_msg = channel.unary_unary(
        '/messagequeue.MessageQueue/send_msg',
        request_serializer=message__queue__pb2.SendRequest.SerializeToString,
        response_deserializer=message__queue__pb2.SendResponse.FromString,
        )
    self.recv_rsp = channel.unary_unary(
        '/messagequeue.MessageQueue/recv_rsp',
        request_serializer=message__queue__pb2.ReceiveRequest.SerializeToString,
        response_deserializer=message__queue__pb2.ReceiveResponse.FromString,
        )
    self.get_rsp = channel.unary_unary(
        '/messagequeue.MessageQueue/get_rsp',
        request_serializer=message__queue__pb2.GetRequest.SerializeToString,
        response_deserializer=message__queue__pb2.GetResponse.FromString,
        )
    self.ack_rsp = channel.unary_unary(
        '/messagequeue.MessageQueue/ack_rsp',
        request_serializer=message__queue__pb2.AcknowledgeRequest.SerializeToString,
        response_deserializer=message__queue__pb2.AcknowledgeResponse.FromString,
        )
    self.recv_msg = channel.unary_unary(
        '/messagequeue.MessageQueue/recv_msg',
        request_serializer=message__queue__pb2.ReceiveRequest.SerializeToString,
        response_deserializer=message__queue__pb2.ReceiveResponse.FromString,
        )
    self.get_msg = channel.unary_unary(
        '/messagequeue.MessageQueue/get_msg',
        request_serializer=message__queue__pb2.GetRequest.SerializeToString,
        response_deserializer=message__queue__pb2.GetResponse.FromString,
        )
    self.ack_msg = channel.unary_unary(
        '/messagequeue.MessageQueue/ack_msg',
        request_serializer=message__queue__pb2.AcknowledgeRequest.SerializeToString,
        response_deserializer=message__queue__pb2.AcknowledgeResponse.FromString,
        )
    self.send_rsp = channel.unary_unary(
        '/messagequeue.MessageQueue/send_rsp',
        request_serializer=message__queue__pb2.SendRequest.SerializeToString,
        response_deserializer=message__queue__pb2.SendResponse.FromString,
        )


class MessageQueueServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def send_msg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def recv_rsp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_rsp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ack_rsp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def recv_msg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_msg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ack_msg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def send_rsp(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessageQueueServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send_msg': grpc.unary_unary_rpc_method_handler(
          servicer.send_msg,
          request_deserializer=message__queue__pb2.SendRequest.FromString,
          response_serializer=message__queue__pb2.SendResponse.SerializeToString,
      ),
      'recv_rsp': grpc.unary_unary_rpc_method_handler(
          servicer.recv_rsp,
          request_deserializer=message__queue__pb2.ReceiveRequest.FromString,
          response_serializer=message__queue__pb2.ReceiveResponse.SerializeToString,
      ),
      'get_rsp': grpc.unary_unary_rpc_method_handler(
          servicer.get_rsp,
          request_deserializer=message__queue__pb2.GetRequest.FromString,
          response_serializer=message__queue__pb2.GetResponse.SerializeToString,
      ),
      'ack_rsp': grpc.unary_unary_rpc_method_handler(
          servicer.ack_rsp,
          request_deserializer=message__queue__pb2.AcknowledgeRequest.FromString,
          response_serializer=message__queue__pb2.AcknowledgeResponse.SerializeToString,
      ),
      'recv_msg': grpc.unary_unary_rpc_method_handler(
          servicer.recv_msg,
          request_deserializer=message__queue__pb2.ReceiveRequest.FromString,
          response_serializer=message__queue__pb2.ReceiveResponse.SerializeToString,
      ),
      'get_msg': grpc.unary_unary_rpc_method_handler(
          servicer.get_msg,
          request_deserializer=message__queue__pb2.GetRequest.FromString,
          response_serializer=message__queue__pb2.GetResponse.SerializeToString,
      ),
      'ack_msg': grpc.unary_unary_rpc_method_handler(
          servicer.ack_msg,
          request_deserializer=message__queue__pb2.AcknowledgeRequest.FromString,
          response_serializer=message__queue__pb2.AcknowledgeResponse.SerializeToString,
      ),
      'send_rsp': grpc.unary_unary_rpc_method_handler(
          servicer.send_rsp,
          request_deserializer=message__queue__pb2.SendRequest.FromString,
          response_serializer=message__queue__pb2.SendResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'messagequeue.MessageQueue', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))