## Organization Practices

### Documentation

All documentation for methods must be written in the english language
The last line of all documentation for methods should include a random, single line ascii emoji with it's description next to it

### Request ID Tracing

All methods must support tracing with a `request_id` parameter

## Security Practices
### Secure Coding
- Validate all inputs from untrusted sources
- Sanitize data before displaying or storing it
- Use parameterized queries to prevent SQL injection
- Implement proper authentication and authorization checks
- Follow the principle of least privilege for all components
- Keep dependencies updated to patch known vulnerabilities

### Data Protection
- Encrypt sensitive data both in transit and at rest
- Never hard-code secrets (API keys, passwords, etc.) in source code
- Use environment variables or secret management services for credentials
- Implement proper access controls for all data stores
- Have a data classification policy to identify sensitive information
- Implement proper logging without exposing PII or secrets

### Testing Practices
## Test Strategy
- Adopt test-driven development (TDD) where appropriate
- Aim for high test coverage (typically 80%+), especially for critical paths
- Balance unit, integration, and end-to-end tests (Test Pyramid)
- Include performance testing for critical components
