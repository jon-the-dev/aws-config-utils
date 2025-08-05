"""Tests for CLI functionality."""

import pytest
from unittest.mock import patch
from aws_config_utils.cli import main
import sys
from io import StringIO


def test_cli_list_all():
    """Test CLI list command without service filter."""
    with patch('sys.argv', ['aws-config-utils', 'list']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main()
            output = mock_stdout.getvalue()
            assert result == 0
            assert "All AWS Config supported resource types:" in output
            assert "AWS::EC2::Instance" in output
            assert "Total:" in output


def test_cli_list_with_service():
    """Test CLI list command with service filter."""
    with patch('sys.argv', ['aws-config-utils', 'list', '--service', 'EC2']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main()
            output = mock_stdout.getvalue()
            assert result == 0
            assert "AWS Config resource types for EC2:" in output
            assert "AWS::EC2::Instance" in output


def test_cli_list_invalid_service():
    """Test CLI list command with invalid service."""
    with patch('sys.argv', ['aws-config-utils', 'list', '--service', 'InvalidService']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main()
            output = mock_stdout.getvalue()
            assert result == 1
            assert "No resource types found for service: InvalidService" in output


def test_cli_services():
    """Test CLI services command."""
    with patch('sys.argv', ['aws-config-utils', 'services']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main()
            output = mock_stdout.getvalue()
            assert result == 0
            assert "AWS services with Config-supported resource types:" in output
            assert "EC2" in output
            assert "Total:" in output


def test_cli_no_command():
    """Test CLI with no command shows help."""
    with patch('sys.argv', ['aws-config-utils']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main()
            output = mock_stdout.getvalue()
            assert result == 1
            assert "usage:" in output
