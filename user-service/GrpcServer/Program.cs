using GrpcServer.Services;

using GrpcServer.Infrastructure.Contexts;
using GrpcServer.Infrastructure.Repositories;
using GrpcServer.Interfaces.Repositories;
using Microsoft.EntityFrameworkCore;
using GrpcServer.Security;
using System.Text;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;

var builder = WebApplication.CreateBuilder(args);

// JWT
var settings = builder.Configuration.GetSection("TokenSettings");
builder.Services.Configure<TokenSettings>(settings);
var section = settings.Get<TokenSettings>();
var key = Encoding.ASCII.GetBytes(section.SecretKey);

//builder.Services.AddAuthentication(auth =>
//{
//    auth.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
//    auth.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
//}).AddJwtBearer(bearer =>
//{
//    bearer.RequireHttpsMetadata = false;
//    bearer.SaveToken = true;
//    bearer.TokenValidationParameters = new TokenValidationParameters()
//    {
//        ValidateIssuerSigningKey = true,
//        IssuerSigningKey = new SymmetricSecurityKey(key),
//        ValidateIssuer = false,
//        ValidateAudience = false,
//    };
//});

builder.Services.AddTransient(map => new TokenController(section));

// Connection to database
string connectionString = builder.Configuration.GetConnectionString("Postgres");
builder.Services.AddDbContext<PostgreSqlContext>(builder => builder.UseNpgsql(connectionString));

// Dependency injection
builder.Services.AddTransient<IUserModelRepository, UserModelRepository>();

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<UserService>();
app.MapGet("/", () => "Running");

using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;

    var context = services.GetRequiredService<PostgreSqlContext>();
    if (context.Database.GetPendingMigrations().Any())
    {
        context.Database.Migrate();
    }
}

app.Run();
