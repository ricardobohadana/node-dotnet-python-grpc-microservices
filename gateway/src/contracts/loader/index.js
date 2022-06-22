const path = require("path");
const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
const { promisify } = require("util");

const protoConfig = require("../../config/proto.config");

module.exports = function load({
  service,
  file,
  address,
  credentials = grpc.credentials.createInsecure(),
}) {
  const protoDef = protoLoader.loadSync(
    path.resolve(__dirname, "..", `${file}.proto`),
    protoConfig
  );

  const proto = grpc.loadPackageDefinition(protoDef);

  const client = new proto[service](address, credentials);

  // promisify all client methods
  Object.entries(client.__proto__).map(([prop, value]) => {
    if (value.originalName !== undefined) {
      client[prop] = promisify(value);
    }
  });

  // console.log(client);

  return client;
};
