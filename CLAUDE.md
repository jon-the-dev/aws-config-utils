# aws-config-utils

A Python utility library for working with AWS Config resource types.

## Project Overview

This is a lightweight Python package that provides a complete list of AWS Config supported resource types (400+) with the ability to filter by AWS service. It offers both a CLI and Python API for easy access to AWS Config resource type information.

## Tech Stack

- **Language**: Python 3.7+
- **Build System**: setuptools with pyproject.toml (PEP 517/518)
- **Testing**: pytest with pytest-cov
- **Code Quality**: black, flake8, mypy
- **Distribution**: twine for PyPI publishing

## Project Structure

```
aws-config-utils/
├── aws_config_utils/           # Main package
│   ├── __init__.py            # Package exports
│   ├── core.py                # Core logic with resource type database
│   └── cli.py                 # Command-line interface
├── tests/                     # Test suite
│   ├── test_core.py          # Core functionality tests
│   └── test_cli.py           # CLI tests
├── setup.py                  # Setup configuration
├── pyproject.toml            # Project metadata
└── requirements-dev.txt      # Development dependencies
```

## Development Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Install package in development mode:
   ```bash
   pip install -e .
   ```

## Testing & Code Quality

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov
```

Format code:
```bash
black .
```

Lint code:
```bash
flake8 .
```

Type checking:
```bash
mypy .
```

## CLI Usage

List all resource types:
```bash
aws-config-utils list
```

Filter by service:
```bash
aws-config-utils list --service EC2
```

List all services:
```bash
aws-config-utils services
```

## Python API Usage

```python
from aws_config_utils import get_config_resource_types, get_config_services

# Get all resource types
all_types = get_config_resource_types()

# Get resource types for specific service
ec2_types = get_config_resource_types(service="EC2")

# Get all services
services = get_config_services()
```

## Key Files

- **aws_config_utils/core.py**: Contains CONFIG_RESOURCE_IDS list and core functions
- **aws_config_utils/cli.py**: Command-line interface implementation
- **tests/**: Comprehensive test coverage for both core and CLI functionality

## Dependencies

**Runtime**: None (standard library only)

**Development**: pytest, pytest-cov, black, flake8, mypy, build, twine

## Publishing

See PUBLISHING.md for instructions on publishing to PyPI.
