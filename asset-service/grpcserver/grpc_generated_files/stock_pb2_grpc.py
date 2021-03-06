# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import stock_pb2 as stock__pb2


class StockStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStockLastPrice = channel.unary_unary(
                '/Stock/GetStockLastPrice',
                request_serializer=stock__pb2.Ticker.SerializeToString,
                response_deserializer=stock__pb2.GetStockLastPriceResponse.FromString,
                )
        self.GetStockHistoryPrice = channel.unary_unary(
                '/Stock/GetStockHistoryPrice',
                request_serializer=stock__pb2.Ticker.SerializeToString,
                response_deserializer=stock__pb2.GetStockHistoryResponse.FromString,
                )


class StockServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStockLastPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StockServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStockLastPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockLastPrice,
                    request_deserializer=stock__pb2.Ticker.FromString,
                    response_serializer=stock__pb2.GetStockLastPriceResponse.SerializeToString,
            ),
            'GetStockHistoryPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryPrice,
                    request_deserializer=stock__pb2.Ticker.FromString,
                    response_serializer=stock__pb2.GetStockHistoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Stock', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Stock(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStockLastPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Stock/GetStockLastPrice',
            stock__pb2.Ticker.SerializeToString,
            stock__pb2.GetStockLastPriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Stock/GetStockHistoryPrice',
            stock__pb2.Ticker.SerializeToString,
            stock__pb2.GetStockHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
