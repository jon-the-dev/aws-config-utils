"""Tests for core functionality."""

import pytest
from aws_config_utils.core import get_config_resource_types, get_config_services


def test_get_all_resource_types():
    """Test getting all resource types."""
    resources = get_config_resource_types()
    assert isinstance(resources, list)
    assert len(resources) > 0
    assert "AWS::EC2::Instance" in resources


def test_get_resource_types_by_service():
    """Test filtering resource types by service."""
    ec2_resources = get_config_resource_types(service="EC2")
    assert isinstance(ec2_resources, list)
    assert len(ec2_resources) > 0
    assert all(resource.startswith("AWS::EC2::") for resource in ec2_resources)
    assert "AWS::EC2::Instance" in ec2_resources


def test_get_resource_types_nonexistent_service():
    """Test filtering by non-existent service."""
    resources = get_config_resource_types(service="NonExistentService")
    assert isinstance(resources, list)
    assert len(resources) == 0


def test_get_config_services():
    """Test getting all services."""
    services = get_config_services()
    assert isinstance(services, list)
    assert len(services) > 0
    assert "EC2" in services
    assert "S3" in services
    assert "IAM" in services
    # Should be sorted
    assert services == sorted(services)


def test_service_consistency():
    """Test that services returned match those in resource types."""
    services = get_config_services()
    all_resources = get_config_resource_types()
    
    # Extract services from resource types
    resource_services = set()
    for resource in all_resources:
        parts = resource.split("::")
        if len(parts) >= 2:
            resource_services.add(parts[1])
    
    assert set(services) == resource_services
