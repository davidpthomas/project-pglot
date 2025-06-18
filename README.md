# Sherlock Project

<p align="center">
  <img src="docs/images/sherlock-logo.png" alt="Sherlock Logo" width="300"/>
  <br>
  <strong>Hunt down social media accounts by username across 400+ social networks</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/sherlock-project/"><img src="https://img.shields.io/pypi/v/sherlock-project.svg" alt="PyPI Version"></a>
  <a href="https://github.com/sherlock-project/sherlock/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/sherlock-project/sherlock/actions"><img src="https://github.com/sherlock-project/sherlock/workflows/Tests/badge.svg" alt="Tests"></a>
  <a href="https://codecov.io/gh/sherlock-project/sherlock"><img src="https://codecov.io/gh/sherlock-project/sherlock/branch/main/graph/badge.svg" alt="Coverage"></a>
</p>

## Overview

Sherlock is a powerful OSINT (Open Source Intelligence) tool that allows you to find usernames across social networks. With support for over 400 social networks, Sherlock can quickly identify where a specific username is registered, making it an invaluable tool for digital investigations, security research, and social media analysis.

## Features

- 🔍 **Comprehensive Search**: Check usernames across 400+ social networks
- ⚡ **Fast & Efficient**: Multi-threaded requests for rapid results
- 📊 **Multiple Output Formats**: Support for TXT, CSV, and XLSX formats
- 🌐 **Proxy Support**: Built-in support for HTTP/SOCKS proxies
- 🔒 **Tor Integration**: Optional Tor support for enhanced privacy
- 🎯 **Targeted Searches**: Ability to search specific sites only
- 📱 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🛡️ **WAF Detection**: Advanced Web Application Firewall bypass techniques

## Installation

### PyPI (Recommended)
```bash
pipx install sherlock-project
```

### Docker
```bash
docker pull sherlock/sherlock
```

### Package Managers
```bash
# Debian/Ubuntu (Kali, Parrot, Debian Testing and Sid)
apt install sherlock

# BlackArch
pacman -S sherlock

# Homebrew (macOS/Linux)
brew install sherlock
```

### From Source
```bash
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

Search for a single username:
```bash
sherlock john_doe
```

Search for multiple usernames:
```bash
sherlock user1 user2 user3
```

### Advanced Usage

Search with specific output file:
```bash
sherlock --output results.txt username
```

Search specific sites only:
```bash
sherlock --site Twitter --site Instagram username
```

Export results to CSV:
```bash
sherlock --csv username
```

Use proxy for requests:
```bash
sherlock --proxy socks5://127.0.0.1:1080 username
```

## Command Line Options

```
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT]
                [--output OUTPUT] [--tor] [--unique-tor] [--csv] [--xlsx]
                [--site SITE_NAME] [--proxy PROXY_URL] [--json JSON_FILE]
                [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color]
                [--browse] [--local] [--nsfw]
                USERNAMES [USERNAMES ...]

positional arguments:
  USERNAMES             One or more usernames to check with social networks

optional arguments:
  -h, --help            Show this help message and exit
  --version             Display version information and dependencies
  --verbose, -v         Display extra debugging information and metrics
  --folderoutput, -fo   Save results to specified folder (multiple usernames)
  --output, -o          Save results to specified file (single username)
  --tor, -t             Make requests over Tor (requires Tor installation)
  --unique-tor, -u      Use new Tor circuit for each request
  --csv                 Create Comma-Separated Values (CSV) file
  --xlsx                Create Excel spreadsheet file
  --site SITE_NAME      Limit analysis to specific sites
  --proxy, -p           Make requests over proxy (e.g., socks5://127.0.0.1:1080)
  --json, -j            Load data from JSON file or URL
  --timeout             Request timeout in seconds (default: 60)
  --print-all           Output sites where username was not found
  --print-found         Output sites where username was found
  --no-color            Disable colored terminal output
  --browse, -b          Open results in default browser
  --local, -l           Force use of local data.json file
  --nsfw                Include NSFW sites in search
```

## Development

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
```

2. Install development dependencies:
```bash
pip install -e .
pip install -r requirements-dev.txt
```

3. Install pre-commit hooks:
```bash
pre-commit install
```

### Running Tests

The project uses pytest for testing with comprehensive test coverage:

```bash
# Run all tests
pytest

# Run tests with coverage
coverage run --source=sherlock_project -m pytest -v
coverage report --show-missing

# Run only offline tests
pytest -v -m "not online"

# Run tests using tox (multiple Python versions)
tox
```

### Test Strategy

Following our organization's testing practices:
- **Test-Driven Development (TDD)** approach for new features
- **High test coverage** (80%+) especially for critical paths
- **Balanced test pyramid** with unit, integration, and end-to-end tests
- **Performance testing** for critical components
- **Edge case and failure scenario testing**

### Code Quality

The project maintains high code quality standards:

```bash
# Lint code with Ruff
ruff check

# Run all quality checks
tox -e lint
```

### Security Considerations

This project follows secure coding practices:
- **Input validation** for all user-provided data
- **Parameterized queries** to prevent injection attacks
- **Proper authentication** and authorization checks
- **Dependency management** with regular security updates
- **No hardcoded secrets** - uses environment variables
- **Secure logging** without exposing PII or secrets

## Architecture

### Core Components

- **`sherlock.py`**: Main application logic and CLI interface
- **`sites.py`**: Site information management and data loading
- **`result.py`**: Query result handling and status management
- **`notify.py`**: Output formatting and notification system
- **`parser.py`**: Command-line argument parsing

### Request ID Tracing

All methods support tracing with a `request_id` parameter for debugging and monitoring purposes.

### Data Protection

- Sensitive data is encrypted both in transit and at rest
- No PII or secrets are logged
- Proper access controls implemented for all data stores
- Environment variables used for configuration

## Contributing

We welcome contributions! Please see our [Contributing Guide](https://sherlockproject.xyz/contribute) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes following our coding standards
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Coding Standards

- Follow PEP 8 style guidelines
- Write comprehensive docstrings for all methods
- Include request_id parameter for tracing
- Add ASCII emoji descriptions in documentation
- Maintain high test coverage

## Supported Sites

Sherlock currently supports over 400 social networks and platforms. For a complete list, visit [sherlockproject.xyz/sites](https://sherlockproject.xyz/sites).

## Performance

- **Multi-threaded requests** for optimal performance
- **Configurable timeouts** to balance speed and reliability
- **Efficient memory usage** with streaming responses
- **Connection pooling** for reduced latency

## Privacy & Ethics

- **Responsible disclosure** of security vulnerabilities
- **Respect for rate limits** and terms of service
- **Educational and research purposes** only
- **No malicious use** - follow ethical guidelines

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Thank you to everyone who has contributed to Sherlock! ❤️

### Original Creator
- [Siddharth Dushantha](https://github.com/sdushantha)

### Current Maintainers
- [Paul Pfeister](https://github.com/ppfeister)
- [Matheus Felipe](https://github.com/matheusfelipeog)
- [Sondre Karlsen Dyrnes](https://github.com/Sondreespe)

### Contributors
<a href="https://github.com/sherlock-project/sherlock/graphs/contributors">
  <img src="https://contrib.rocks/image?&columns=25&max=10000&&repo=sherlock-project/sherlock" />
</a>

## Support

- 📖 **Documentation**: [sherlockproject.xyz](https://sherlockproject.xyz)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/sherlock-project/sherlock/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/sherlock-project/sherlock/discussions)
- 🔒 **Security**: See [SECURITY.md](SECURITY.md) for reporting vulnerabilities

## Star History

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=sherlock-project/sherlock&type=Date&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=sherlock-project/sherlock&type=Date" />
  <img alt="Sherlock Project Star History Chart" src="https://api.star-history.com/svg?repos=sherlock-project/sherlock&type=Date" />
</picture>

---

<p align="center">
  Made with ❤️ by the Sherlock Project team
  <br>
  🕵️‍♂️ Happy hunting! 🔍
</p>