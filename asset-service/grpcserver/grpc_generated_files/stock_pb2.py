# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstock.proto\"\x18\n\x06Ticker\x12\x0e\n\x06ticker\x18\x01 \x01(\t\"Q\n\tStockData\x12\x0c\n\x04High\x18\x01 \x01(\x02\x12\x0b\n\x03Low\x18\x02 \x01(\x02\x12\x0c\n\x04Open\x18\x03 \x01(\x02\x12\r\n\x05\x43lose\x18\x04 \x01(\x02\x12\x0c\n\x04\x44\x61te\x18\x05 \x01(\t\":\n\x19GetStockLastPriceResponse\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\"C\n\x17GetStockHistoryResponse\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x18\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\n.StockData2\x80\x01\n\x05Stock\x12:\n\x11GetStockLastPrice\x12\x07.Ticker\x1a\x1a.GetStockLastPriceResponse\"\x00\x12;\n\x14GetStockHistoryPrice\x12\x07.Ticker\x1a\x18.GetStockHistoryResponse\"\x00\x62\x06proto3')



_TICKER = DESCRIPTOR.message_types_by_name['Ticker']
_STOCKDATA = DESCRIPTOR.message_types_by_name['StockData']
_GETSTOCKLASTPRICERESPONSE = DESCRIPTOR.message_types_by_name['GetStockLastPriceResponse']
_GETSTOCKHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['GetStockHistoryResponse']
Ticker = _reflection.GeneratedProtocolMessageType('Ticker', (_message.Message,), {
  'DESCRIPTOR' : _TICKER,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:Ticker)
  })
_sym_db.RegisterMessage(Ticker)

StockData = _reflection.GeneratedProtocolMessageType('StockData', (_message.Message,), {
  'DESCRIPTOR' : _STOCKDATA,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:StockData)
  })
_sym_db.RegisterMessage(StockData)

GetStockLastPriceResponse = _reflection.GeneratedProtocolMessageType('GetStockLastPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTOCKLASTPRICERESPONSE,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:GetStockLastPriceResponse)
  })
_sym_db.RegisterMessage(GetStockLastPriceResponse)

GetStockHistoryResponse = _reflection.GeneratedProtocolMessageType('GetStockHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTOCKHISTORYRESPONSE,
  '__module__' : 'stock_pb2'
  # @@protoc_insertion_point(class_scope:GetStockHistoryResponse)
  })
_sym_db.RegisterMessage(GetStockHistoryResponse)

_STOCK = DESCRIPTOR.services_by_name['Stock']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TICKER._serialized_start=15
  _TICKER._serialized_end=39
  _STOCKDATA._serialized_start=41
  _STOCKDATA._serialized_end=122
  _GETSTOCKLASTPRICERESPONSE._serialized_start=124
  _GETSTOCKLASTPRICERESPONSE._serialized_end=182
  _GETSTOCKHISTORYRESPONSE._serialized_start=184
  _GETSTOCKHISTORYRESPONSE._serialized_end=251
  _STOCK._serialized_start=254
  _STOCK._serialized_end=382
# @@protoc_insertion_point(module_scope)
