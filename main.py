"""Simple Hello World script.

This script prints a customized greeting message when executed.

Usage:
    python main.py [--name NAME]
    
Arguments:
    --name: Optional name to greet (default: World)
"""
import argparse


def main():
    """Print personalized greeting message using CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()