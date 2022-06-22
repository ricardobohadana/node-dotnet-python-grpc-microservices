using GrpcServer.Infrastructure.Contexts;
using GrpcServer.Interfaces.Repositories;
using Microsoft.EntityFrameworkCore;

namespace GrpcServer.Infrastructure.Repositories
{
    public class BaseRepository<TEntity> : IBaseRepository<TEntity>
            where TEntity : class
    {

        private readonly PostgreSqlContext _postgreSqlContext;

        public BaseRepository(PostgreSqlContext postgreSqlContext)
        {
            _postgreSqlContext = postgreSqlContext;
        }

        public TEntity GetById(string id)
        {
            return _postgreSqlContext.Set<TEntity>().Find(id);
        }


        public void Insert(TEntity entity)
        {
            _postgreSqlContext.Entry(entity).State = EntityState.Added;
            _postgreSqlContext.SaveChanges();
        }

        
    }
}
