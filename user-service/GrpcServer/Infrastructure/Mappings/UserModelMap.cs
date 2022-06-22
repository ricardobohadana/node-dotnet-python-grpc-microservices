using GrpcServer.Protos;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace GrpcServer.Infrastructure.Mappings
{
    public class UserModelMap : IEntityTypeConfiguration<UserModel>
    {
        public void Configure(EntityTypeBuilder<UserModel> builder)
        {
            builder.ToTable("USER");

            builder.HasKey(x => x.Id);

            builder.Property(x => x.Name).HasColumnName("Name").IsRequired();
            builder.Property(x => x.Email).HasColumnName("Email").IsRequired();
            builder.HasIndex(x => x.Email).IsUnique();
            builder.Property(x => x.Password).HasColumnName("Password").IsRequired();
        }
    }
}
