namespace GrpcServer.Security
{
    public class TokenSettings
    {
        public string SecretKey { get; set; }
        public int ExpirationInHours { get; set; }
    }
}
