# Publishing to PyPI

This document provides step-by-step instructions for publishing the aws-config-utils package to PyPI.

## Prerequisites

1. **PyPI Account**: Create accounts on both [TestPyPI](https://test.pypi.org/) and [PyPI](https://pypi.org/)
2. **API Tokens**: Generate API tokens for both TestPyPI and PyPI
3. **Required Tools**: Install the required publishing tools:
   ```bash
   pip install build twine
   ```

## Configuration

### 1. Update Package Information

Before publishing, update the following files with your information:

- `setup.py`: Update author name, email, and URL
- `pyproject.toml`: Update author name, email, and repository URLs
- `LICENSE`: Update copyright holder name

### 2. Configure Twine

Create a `.pypirc` file in your home directory:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = your-pypi-api-token

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your-testpypi-api-token
```

## Publishing Process

### Option 1: Using the Automated Script

Run the provided publishing script:

```bash
python publish.py
```

This script will:
- Clean previous builds
- Run tests
- Build the package
- Check the package for issues

### Option 2: Manual Steps

1. **Clean previous builds**:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   ```

2. **Run tests**:
   ```bash
   python -m pytest tests/ -v
   ```

3. **Build the package**:
   ```bash
   python -m build
   ```

4. **Check the package**:
   ```bash
   python -m twine check dist/*
   ```

5. **Upload to TestPyPI** (recommended first):
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

6. **Test the TestPyPI installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ aws-config-utils
   aws-config-utils --help
   ```

7. **Upload to PyPI** (if TestPyPI works):
   ```bash
   python -m twine upload dist/*
   ```

## Version Management

Update the version number in both:
- `setup.py`
- `pyproject.toml`
- `aws_config_utils/__init__.py`

Follow [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (e.g., 1.0.0)
- Increment MAJOR for incompatible API changes
- Increment MINOR for backwards-compatible functionality additions
- Increment PATCH for backwards-compatible bug fixes

## Post-Publishing

After successful publishing:

1. **Create a Git tag**:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```

2. **Test installation**:
   ```bash
   pip install aws-config-utils
   aws-config-utils --help
   ```

3. **Update documentation** if needed

## Troubleshooting

### Common Issues

1. **Package already exists**: Increment the version number
2. **Authentication failed**: Check your API tokens in `.pypirc`
3. **Package validation errors**: Run `twine check dist/*` for details
4. **Import errors**: Ensure all dependencies are properly specified

### Useful Commands

- Check package metadata: `python setup.py check`
- Validate package: `python -m twine check dist/*`
- List package contents: `tar -tzf dist/aws-config-utils-*.tar.gz`

## Security Notes

- Never commit API tokens to version control
- Use API tokens instead of passwords
- Consider using environment variables for tokens
- Regularly rotate your API tokens
