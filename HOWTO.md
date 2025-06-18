# How to Run Sherlock

This guide provides comprehensive instructions on how to install, configure, and run the Sherlock application for finding usernames across social networks.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Methods](#installation-methods)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Configuration](#configuration)
6. [Output Formats](#output-formats)
7. [Troubleshooting](#troubleshooting)
8. [Performance Optimization](#performance-optimization)
9. [Security Considerations](#security-considerations)

## Prerequisites

### System Requirements

- **Python**: Version 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 512MB RAM (1GB+ recommended for large searches)
- **Network**: Internet connection required

### Python Version Check

Verify your Python version:
```bash
python --version
# or
python3 --version
```

If you need to install Python 3.8+, visit [python.org](https://python.org/downloads/).

## Installation Methods

### Method 1: PyPI Installation (Recommended)

Install using pipx (preferred):
```bash
pipx install sherlock-project
```

Or using pip:
```bash
pip install sherlock-project
```

### Method 2: Docker Installation

Pull the Docker image:
```bash
docker pull sherlock/sherlock
```

### Method 3: Package Manager Installation

**Debian/Ubuntu (Kali, Parrot, Debian Testing and Sid):**
```bash
sudo apt update
sudo apt install sherlock
```

**BlackArch:**
```bash
sudo pacman -S sherlock
```

**Homebrew (macOS/Linux):**
```bash
brew install sherlock
```

### Method 4: From Source

Clone and install from source:
```bash
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip install -r requirements.txt
```

## Basic Usage

### Running Your First Search

Search for a single username:
```bash
sherlock john_doe
```

Search for multiple usernames:
```bash
sherlock alice bob charlie
```

### Running from Different Installation Methods

**PyPI Installation:**
```bash
sherlock username
```

**Docker:**
```bash
docker run --rm -t sherlock/sherlock username
```

**From Source:**
```bash
python -m sherlock_project username
# or
python sherlock_project/sherlock.py username
```

### Understanding the Output

When you run Sherlock, you'll see output like:
```
[*] Checking username john_doe on:
[+] Facebook: https://facebook.com/john_doe
[+] Instagram: https://instagram.com/john_doe
[-] Twitter: Not Found!
[+] GitHub: https://github.com/john_doe
```

- `[+]` indicates the username was found
- `[-]` indicates the username was not found
- `[*]` indicates informational messages

## Advanced Usage

### Targeting Specific Sites

Search only specific social networks:
```bash
sherlock --site Twitter --site Instagram --site GitHub username
```

### Using Proxies

Route requests through a proxy:
```bash
# HTTP proxy
sherlock --proxy http://127.0.0.1:8080 username

# SOCKS5 proxy
sherlock --proxy socks5://127.0.0.1:1080 username
```

### Tor Integration

**Note**: Tor support is deprecated but still available.

Install Tor support:
```bash
pip install 'sherlock-project[tor]'
```

Use Tor for requests:
```bash
sherlock --tor username
```

Use unique Tor circuit for each request:
```bash
sherlock --unique-tor username
```

### Timeout Configuration

Set custom timeout (default is 60 seconds):
```bash
sherlock --timeout 30 username
```

### Verbose Output

Enable detailed debugging information:
```bash
sherlock --verbose username
```

### Pattern Matching

Search for usernames with variations:
```bash
# This will search for user_name, user-name, and user.name
sherlock "user{?}name"
```

## Configuration

### Environment Variables

Set environment variables for configuration:
```bash
export SHERLOCK_TIMEOUT=30
export SHERLOCK_PROXY=socks5://127.0.0.1:1080
```

### Custom Data Sources

Use a custom JSON file for site data:
```bash
sherlock --json custom_sites.json username
```

Use local data file:
```bash
sherlock --local username
```

### Including NSFW Sites

Include adult/NSFW sites in search:
```bash
sherlock --nsfw username
```

## Output Formats

### Text Output (Default)

Results are saved to `username.txt`:
```bash
sherlock username
```

### Custom Output File

Specify output file for single username:
```bash
sherlock --output results.txt username
```

### Folder Output for Multiple Users

Save results to a specific folder:
```bash
sherlock --folderoutput ./results user1 user2 user3
```

### CSV Format

Export results to CSV:
```bash
sherlock --csv username
```

### Excel Format

Export results to Excel spreadsheet:
```bash
sherlock --xlsx username
```

### Browser Integration

Open found profiles in default browser:
```bash
sherlock --browse username
```

### Print Options

Control what gets printed:
```bash
# Print all results (found and not found)
sherlock --print-all username

# Print only found results (default)
sherlock --print-found username

# Disable colored output
sherlock --no-color username
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Python Version Error
```
Error: Sherlock requires Python 3.8+
```
**Solution**: Upgrade Python to version 3.8 or higher.

#### 2. Module Not Found Error
```
ModuleNotFoundError: No module named 'sherlock_project'
```
**Solution**: Reinstall Sherlock or check your Python path.

#### 3. Connection Timeout
```
Timeout Error: Request timed out
```
**Solutions**:
- Increase timeout: `sherlock --timeout 120 username`
- Use a proxy: `sherlock --proxy http://proxy:port username`
- Check your internet connection

#### 4. Too Many Requests (Rate Limiting)
```
HTTP Error 429: Too Many Requests
```
**Solutions**:
- Add delays between requests
- Use a proxy or VPN
- Reduce concurrent requests

#### 5. Permission Denied (Docker)
```
Permission denied while trying to connect to Docker
```
**Solution**: Add your user to the docker group or use sudo.

### Debug Mode

Enable verbose output for troubleshooting:
```bash
sherlock --verbose --dump-response username
```

### Request ID Tracing

For debugging purposes, all methods support request ID tracing. Enable verbose mode to see request IDs in logs.

## Performance Optimization

### Optimizing Search Speed

1. **Use specific sites** instead of searching all:
   ```bash
   sherlock --site Twitter --site Instagram username
   ```

2. **Adjust timeout** for faster results:
   ```bash
   sherlock --timeout 30 username
   ```

3. **Use local data** to avoid downloading site information:
   ```bash
   sherlock --local username
   ```

### Memory Usage

For large-scale searches:
- Process usernames in batches
- Use folder output to organize results
- Monitor system resources

### Network Optimization

- Use a fast, stable internet connection
- Consider using a proxy for better routing
- Avoid peak hours for better response times

## Security Considerations

### Privacy Protection

1. **Use Tor** for anonymous searches:
   ```bash
   sherlock --tor username
   ```

2. **Use proxies** to hide your IP:
   ```bash
   sherlock --proxy socks5://127.0.0.1:1080 username
   ```

### Responsible Usage

- **Respect rate limits** and terms of service
- **Don't abuse** the tool for malicious purposes
- **Follow ethical guidelines** for OSINT research
- **Obtain proper authorization** before investigating individuals

### Data Protection

- Results may contain sensitive information
- Store output files securely
- Consider encrypting results for sensitive investigations
- Follow your organization's data handling policies

## Examples

### Basic Examples

```bash
# Simple username search
sherlock johndoe

# Multiple usernames
sherlock alice bob charlie

# Search with custom timeout
sherlock --timeout 45 username
```

### Advanced Examples

```bash
# Search specific sites with CSV output
sherlock --site GitHub --site Twitter --csv developer_username

# Anonymous search through Tor with verbose output
sherlock --tor --verbose --output secure_results.txt target_user

# Batch search with folder organization
sherlock --folderoutput ./investigation_results user1 user2 user3

# Pattern search with Excel output
sherlock --xlsx "company{?}name"

# Proxy search with browser opening
sherlock --proxy socks5://127.0.0.1:1080 --browse username
```

### Docker Examples

```bash
# Basic Docker usage
docker run --rm -t sherlock/sherlock username

# Docker with volume mounting for output
docker run --rm -t -v $(pwd):/opt/sherlock/results sherlock/sherlock --folderoutput /opt/sherlock/results username

# Docker with custom options
docker run --rm -t sherlock/sherlock --csv --timeout 30 username
```

## Getting Help

### Command Line Help

View all available options:
```bash
sherlock --help
```

### Version Information

Check your Sherlock version:
```bash
sherlock --version
```

### Additional Resources

- **Documentation**: [sherlockproject.xyz](https://sherlockproject.xyz)
- **GitHub Issues**: [Report bugs](https://github.com/sherlock-project/sherlock/issues)
- **Community**: [GitHub Discussions](https://github.com/sherlock-project/sherlock/discussions)

---

**Happy hunting! 🕵️‍♂️**

*Remember to use Sherlock responsibly and ethically. Always respect privacy, terms of service, and applicable laws when conducting username reconnaissance.*

🔍 ASCII Art Detective Badge - For those who seek the truth in digital footprints!