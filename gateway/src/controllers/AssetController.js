const { AssetService } = require("../services/AssetService");

class AssetController {
  async getLatestPrice(request, response) {
    const { ticker } = request.params;
    const grpcResponse = await AssetService.GetStockLastPrice({ ticker });
    return response.json(grpcResponse);
  }

  async getHistoryPrice(request, response) {
    const { ticker } = request.params;
    const grpcResponse = await AssetService.GetStockHistoryPrice({ ticker });
    return response.json(grpcResponse);
  }
}

module.exports = new AssetController();
