from function import get_stock_price
from grpc_generated_files import stock_pb2
from grpc_generated_files import stock_pb2_grpc

    
    
class StockServicer(stock_pb2_grpc.StockServicer):
    def GetStockLastPrice(self, request, context):
        response = stock_pb2.GetStockLastPriceResponse()
        stock_data = get_stock_price.get_stock_price(request.ticker)
        response.ticker = stock_data['ticker']
        response.price = stock_data['price']
        return response

    def GetStockHistoryPrice(self, request, context):
        response = stock_pb2.GetStockHistoryResponse()
        stock_data = get_stock_price.get_stock_history_price(request.ticker)
        response.ticker = stock_data['ticker']
        for data in stock_data['data']:
            response.data.add(
                High=data['High'],
                Low=data['Low'],
                Open=data['Open'],
                Close=data['Close'],
                Date=data['Date']
            )            
        return response