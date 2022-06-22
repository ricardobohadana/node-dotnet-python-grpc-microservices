const { Router } = require("express");
const AssetController = require("./controllers/AssetController");
const UserController = require("./controllers/UserController");

const router = Router();

router.use("/stock", UserController.AuthMiddleware);
router.get("/stock/price/:ticker", AssetController.getLatestPrice);
router.get("/stock/history/:ticker", AssetController.getHistoryPrice);

router.get("/user/:id", UserController.getUserById);
router.post("/user/login", UserController.login);
router.post("/user/register", UserController.register);
router.get("/user/logout", UserController.logout);

module.exports = { router };
