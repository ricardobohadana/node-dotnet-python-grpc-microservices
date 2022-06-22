const express = require("express");
const { router } = require("./routes");

const app = express();

app.use(express.json());

app.use(router);

app.listen("81", () => console.log("Server started on port 81"));
