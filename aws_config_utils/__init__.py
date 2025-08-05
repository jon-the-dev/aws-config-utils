"""AWS Config Utils - Utilities for working with AWS Config resource types."""

from .core import get_config_resource_types, get_config_services

__version__ = "0.1.0"
__all__ = ["get_config_resource_types", "get_config_services"]
