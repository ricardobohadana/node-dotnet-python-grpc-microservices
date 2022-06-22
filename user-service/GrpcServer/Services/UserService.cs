using Grpc.Core;
using GrpcServer.Interfaces.Repositories;
using GrpcServer.Protos;
using GrpcServer.Security;
using System.Net.Mail;

namespace GrpcServer.Services
{
    public class UserService : User.UserBase
    {
        private readonly ILogger<UserService> _logger;
        private readonly TokenController _tokenController;
        private readonly IUserModelRepository _userModelRepository;



        public UserService(ILogger<UserService> logger, TokenController tokenController, IUserModelRepository userModelRepository)
        {
            _logger = logger;
            _tokenController = tokenController;
            _userModelRepository = userModelRepository;
        }


        private bool IsValidEmail(string email)
        {
            var trimmedEmail = email.Trim();

            if (trimmedEmail.EndsWith("."))
            {
                return false; // suggested by @TK-421
            }
            try
            {
                var addr = new MailAddress(email);
                return addr.Address == trimmedEmail;
            }
            catch
            {
                return false;
            }
        }

        // VALIDATE TOKEN
        public override Task<AuthMiddlewareResponse> AuthMiddleware(AuthMiddlewareRequest request, ServerCallContext context)
        {
            var isValid = _tokenController.ValidateToken(request.Token);
            return Task.FromResult(new AuthMiddlewareResponse() { Authenticated = isValid });
        }

        // GET USER BY ID
        public override Task<GetUserByIdResponse> GetUserById(GetUserByIdRequest request, ServerCallContext context)
        {
            var user = _userModelRepository.GetById(request.Id);

            return Task.FromResult(
                new GetUserByIdResponse()
                {
                    User = user
                }
            );
        }

        // LOGIN USER
        public override Task<LoginResponse> Login(LoginRequest request, ServerCallContext context)
        {
            var errorResponse = Task.FromResult(new LoginResponse() { Token = "", User = new UserModel() });
            if (!IsValidEmail(request.Email))
                return errorResponse;

            var user = _userModelRepository.GetByEmailAndPassword(request.Email, request.Password);

            if (user == null)
                return errorResponse;

            var token = _tokenController.GenerateToken(user.Email);
            return Task.FromResult(new LoginResponse() { Token = token, User = user });
        }

        // LOGOUT USER
        public override Task<Empty> Logout(LogoutRequest request, ServerCallContext context)
        {
            return base.Logout(request, context);
        }

        // REGISTER USER
        public override Task<RegisterResponse> Register(RegisterRequest request, ServerCallContext context)
        {
            if (request.Password != request.PasswordConfirmation)
            {

                return Task.FromResult(
                    new RegisterResponse()
                    {
                        Success = false,
                        Message = "As senhas não são iguais."
                    }
                );
            }

            var user = new UserModel()
            {
                Id = Guid.NewGuid().ToString(),
                Email = request.Email,
                Name = request.Name,
                Password = request.Password,
            };

            _userModelRepository.Insert(user);

            return Task.FromResult(
                new RegisterResponse()
                {
                    Message = "Usuário cadastrado com sucesso!",
                    Success = true,
                }
            );
        }
    }
}
