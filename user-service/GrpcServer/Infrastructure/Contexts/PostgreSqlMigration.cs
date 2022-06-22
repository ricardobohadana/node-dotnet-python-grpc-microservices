using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace GrpcServer.Infrastructure.Contexts
{
    public class PostgreSqlMigration: IDesignTimeDbContextFactory<PostgreSqlContext>
    {
        public PostgreSqlContext CreateDbContext(string[] args)
        {
            var configurationBuilder = new ConfigurationBuilder();
            var path = Path.Combine(Directory.GetCurrentDirectory(), "appsettings.json");
            configurationBuilder.AddJsonFile(path,false);
            var root = configurationBuilder.Build();
            var connectionString = root.GetSection("ConnectionStrings").GetSection("Postgres").Value;
            var builder = new DbContextOptionsBuilder<PostgreSqlContext>();
            builder.UseNpgsql(connectionString);
            return new PostgreSqlContext(builder.Options);
        }
    }
}
