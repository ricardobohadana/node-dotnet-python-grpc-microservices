using GrpcServer.Infrastructure.Contexts;
using GrpcServer.Interfaces.Repositories;
using GrpcServer.Protos;

namespace GrpcServer.Infrastructure.Repositories
{
    public class UserModelRepository : BaseRepository<UserModel>, IUserModelRepository
    {
        private readonly PostgreSqlContext _postgreSqlContext;

        public UserModelRepository(PostgreSqlContext postgreSqlContext) : base(postgreSqlContext)
        {
            _postgreSqlContext = postgreSqlContext;
        }

        public UserModel GetByEmail(string email)
        {
            return _postgreSqlContext.UserModels.Where(x => x.Email == email).FirstOrDefault();
        }

        public UserModel GetByEmailAndPassword(string email, string password)
        {
            return _postgreSqlContext.UserModels.Where(x => x.Email == email && x.Password.Equals(password)).FirstOrDefault();
        }
    }
}
