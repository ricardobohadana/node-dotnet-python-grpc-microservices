try:
    import grpc
    from concurrent import futures
    import time
    from function import get_stock_price
    from grpc_generated_files import stock_pb2
    from grpc_generated_files import stock_pb2_grpc
    from services import stock_service
except:
    print('Error loading modules!')
    
    



def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stock_pb2_grpc.add_StockServicer_to_server(stock_service.StockServicer(), server)
    print('Starting server. Listening on port 80.')
    server.add_insecure_port('[::]:80')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
            pass
    except KeyboardInterrupt:
        server.stop(0)
        print('Server stopped.')
        
        
        
if __name__ == '__main__':
    run()