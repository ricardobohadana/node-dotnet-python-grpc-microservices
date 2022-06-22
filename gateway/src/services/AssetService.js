const load = require("../contracts/loader");

const serviceUrl = "python-stock-grpc:80";
// const serviceUrl = "0.0.0.0:80";

const AssetService = load({
  service: "Stock",
  address: serviceUrl,
  file: "stock",
});

module.exports = { AssetService };
