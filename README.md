# AWS Config Utils

A Python utility library for working with AWS Config resource types. This package provides easy access to AWS Config supported resource types and allows filtering by AWS service.

## Installation

```bash
pip install aws-config-utils
```

## Usage

### Command Line Interface

After installation, you can use the command line interface:

```bash
# List all AWS Config supported resource types
aws-config-utils list

# List resource types for a specific service
aws-config-utils list --service EC2

# List all supported AWS services
aws-config-utils services

# Get help
aws-config-utils --help
```

### Python API

You can also use the library programmatically:

```python
from aws_config_utils import get_config_resource_types, get_config_services

# Get all resource types
all_resources = get_config_resource_types()

# Get resource types for a specific service
ec2_resources = get_config_resource_types(service="EC2")

# Get all supported services
services = get_config_services()
```

## Features

- Complete list of AWS Config supported resource types
- Filter resource types by AWS service
- Command line interface for easy access
- Python API for programmatic use

## Requirements

- Python 3.7+

## License

MIT License
