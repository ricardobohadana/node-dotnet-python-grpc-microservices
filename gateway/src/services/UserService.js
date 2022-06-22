const load = require("../contracts/loader");

const serviceUrl = "dotnet-user-grpc:82";
// const serviceUrl = "0.0.0.0:82";

const UserService = load({
  service: "User",
  address: serviceUrl,
  file: "user",
});

module.exports = { UserService };
