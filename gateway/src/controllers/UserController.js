const { UserService } = require("../services/UserService");

class UserController {
  async login(request, response) {
    const grpcResponse = await UserService.Login(request.body);
    return response.json({
      token: grpcResponse.token,
      user: {
        ...grpcResponse.user,
        password: "",
      },
    });
  }

  async logout(request, response) {}

  async register(request, response) {
    const { email, password, passwordConfirmation, name } = request.body;
    const grpcResponse = await UserService.Register({
      name,
      email,
      password,
      passwordConfirmation,
    });
    console.log(grpcResponse);
    const { success, message } = grpcResponse;

    if (success) {
      return response.status(201).json({ success, message });
    } else {
      return response.status(400).json({ success, message });
    }
  }

  async getUserById(request, response) {
    const { id } = request.params;
    const grpcResponse = await UserService.GetUserById({ id });
    return response.json({
      token: grpcResponse.token,
      user: {
        ...grpcResponse.user,
        password: "",
      },
    });
  }

  async AuthMiddleware(request, response, next) {
    const auth = request.headers.authorization;
    const [, token] = auth.split(" ");
    const grpcResponse = await UserService.AuthMiddleware({ token });
    if (grpcResponse.authenticated) {
      next();
    }
  }
}

module.exports = new UserController();
