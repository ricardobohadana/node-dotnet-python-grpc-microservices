namespace GrpcServer.Interfaces.Repositories
{
    public interface IBaseRepository<TEntity>
        where TEntity : class
    {
        TEntity GetById(string id);
        void Insert(TEntity entity);
    }
}
