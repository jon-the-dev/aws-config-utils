#!/usr/bin/env python3
"""Command line interface for aws-config-utils."""

import argparse
import sys
from .core import get_config_resource_types, get_config_services


def list_resources(args):
    """List AWS Config resource types."""
    if args.service:
        resources = get_config_resource_types(service=args.service)
        if not resources:
            print(f"No resource types found for service: {args.service}")
            print(f"Available services: {', '.join(get_config_services())}")
            return 1
        print(f"AWS Config resource types for {args.service}:")
    else:
        resources = get_config_resource_types()
        print("All AWS Config supported resource types:")
    
    for resource in resources:
        print(f"  {resource}")
    
    print(f"\nTotal: {len(resources)} resource types")
    return 0


def list_services(args):
    """List all AWS services with Config support."""
    services = get_config_services()
    print("AWS services with Config-supported resource types:")
    for service in services:
        resource_count = len(get_config_resource_types(service=service))
        print(f"  {service} ({resource_count} resource types)")
    
    print(f"\nTotal: {len(services)} services")
    return 0


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AWS Config Utils - Utilities for working with AWS Config resource types",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  aws-config-utils list                    # List all resource types
  aws-config-utils list --service EC2      # List EC2 resource types
  aws-config-utils services                # List all supported services
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser(
        'list', 
        help='List AWS Config resource types'
    )
    list_parser.add_argument(
        '--service', 
        type=str,
        help='Filter by AWS service (e.g., EC2, S3, IAM)'
    )
    list_parser.set_defaults(func=list_resources)
    
    # Services command
    services_parser = subparsers.add_parser(
        'services',
        help='List all AWS services with Config support'
    )
    services_parser.set_defaults(func=list_services)
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command is provided, show help
    if not args.command:
        parser.print_help()
        return 1
    
    # Execute the command
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
