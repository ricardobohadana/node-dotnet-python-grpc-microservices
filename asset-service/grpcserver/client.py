import grpc
from grpc_generated_files import stock_pb2
from grpc_generated_files import stock_pb2_grpc

# Step 1: Create a Channel
channel = grpc.insecure_channel('localhost:80')

# Step 2: Create a stub
stub = stock_pb2_grpc.StockStub(channel)

# Step 3: Create a request calling the API
ticker = stock_pb2.Ticker(ticker='AAPL')
# response = stub.GetStockLastPrice(ticker)
# print("Calling GetStockLastPrice:")
# print(response)

response = stub.GetStockHistoryPrice(ticker)
print("Calling GetStockHistoryPrice:")
print(response)