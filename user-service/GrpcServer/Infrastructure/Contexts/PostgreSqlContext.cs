using GrpcServer.Infrastructure.Mappings;
using GrpcServer.Protos;
using Microsoft.EntityFrameworkCore;

namespace GrpcServer.Infrastructure.Contexts
{
    public class PostgreSqlContext : DbContext
    {
        public PostgreSqlContext(DbContextOptions<PostgreSqlContext> options) :
            base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new UserModelMap());
        }

        public DbSet<UserModel> UserModels { get; set; }
    }
}
