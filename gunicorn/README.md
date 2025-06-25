
# SimpleHTTP Server

A lightweight, high-performance HTTP server built for modern web applications.

## Features

- **Fast and Efficient**: Optimized for high throughput and low latency
- **Modular Design**: Easily extend with custom middleware
- **Cross-Platform**: Runs on Linux, macOS, and Windows
- **WebSocket Support**: Built-in support for real-time communication
- **Static File Serving**: Efficiently serve static assets with proper caching
- **RESTful API Support**: First-class support for building RESTful services

## Installation

```bash
# Using pip
pip install simplehttp-server

# Using Docker
docker pull simplehttp/server:latest
```

## Quick Start

```python
from simplehttp import Server

app = Server()

@app.route('/')
def hello_world(request):
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

## Configuration

SimpleHTTP Server can be configured using environment variables or a configuration file:

```bash
# Set the port
export SIMPLEHTTP_PORT=9000

# Set the log level
export SIMPLEHTTP_LOG_LEVEL=debug
```

Or create a `config.yaml` file:

```yaml
server:
  port: 9000
  host: 0.0.0.0
  workers: 4
logging:
  level: debug
  format: json
```

## Contributing

We welcome contributions from the community! Here's how you can help:

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/simplehttp-server.git
   cd simplehttp-server
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Code Style

We follow PEP 8 with a few modifications. Run the linter before submitting:

```bash
make lint
```

### Testing

Please add tests for any new features or bug fixes:

```bash
# Run all tests
make test

# Run specific tests
pytest tests/test_routing.py
```

### Pull Request Process

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them with descriptive messages
3. Push your branch and create a pull request
4. Ensure CI passes on your PR
5. Wait for a maintainer to review your changes

### Code of Conduct

Please note that this project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Performance

SimpleHTTP Server has been benchmarked against other popular HTTP servers:

| Server | Requests/sec | Latency (ms) | Memory Usage (MB) |
|--------|--------------|--------------|-------------------|
| SimpleHTTP | 25,000 | 4.2 | 45 |
| Nginx | 23,500 | 4.5 | 60 |
| Node.js | 15,000 | 6.8 | 85 |

## License

SimpleHTTP Server is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2023 SimpleHTTP Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support

- [Documentation](https://simplehttp.readthedocs.io/)
- [Issue Tracker](https://github.com/simplehttp/server/issues)
- [Community Forum](https://community.simplehttp.io/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/simplehttp)

## Acknowledgements

SimpleHTTP Server is built on the shoulders of giants. We'd like to thank the following projects and their maintainers:

- [uvloop](https://github.com/MagicStack/uvloop)
- [httptools](https://github.com/MagicStack/httptools)
- [Jinja2](https://github.com/pallets/jinja)
