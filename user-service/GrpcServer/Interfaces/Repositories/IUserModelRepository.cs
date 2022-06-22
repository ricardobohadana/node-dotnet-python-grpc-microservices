using GrpcServer.Protos;

namespace GrpcServer.Interfaces.Repositories
{
    public interface IUserModelRepository: IBaseRepository<UserModel>
    {
        UserModel GetByEmail(string email);

        UserModel GetByEmailAndPassword(string email, string password);
    }
}
