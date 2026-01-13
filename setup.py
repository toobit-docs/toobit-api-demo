"""
TooBit API SDK Installation Configuration
"""

from setuptools import setup, find_packages

import os

# Read long description from README.md
readme_path = "README.md"
if not os.path.exists(readme_path):
    readme_path = "README.md" # Fallback or handle error

with open(readme_path, "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="toobit-api-sdk",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="TooBit Cryptocurrency Trading All API SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/toobit-api-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "toobit-sdk=open_api_sdk.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="toobit, cryptocurrency, trading, api, sdk",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/toobit-api-sdk/issues",
        "Source": "https://github.com/yourusername/toobit-api-sdk",
        "Documentation": "https://github.com/yourusername/toobit-api-sdk#readme",
    },
) 