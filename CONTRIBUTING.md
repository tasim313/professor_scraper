# Contributing to Professor Scraper

## Thank you for your interest in contributing to Professor Scraper! Whether you're fixing bugs, adding new features, or improving documentation, your contributions are greatly appreciated. This document provides guidelines to help you make your contributions effectively.

### Table of Contents
    - Code of Conduct
    - Getting Started
    - How to Contribute
    - Code Guidelines
    - Pull Request Process
    - Reporting Issues
    - Additional Resources

### Code of Conduct
```bash
This project adheres to the Code of Conduct. By participating, you agree to maintain a respectful and inclusive environment for all contributors. Please report any violations to [tasim.swe@gmail.com].
```

### Getting Started

```bash
Fork and Clone the Repository
git clone https://github.com/tasim313/professor_scraper.git

Set Up Your Environment
pip install -r requirement/development.text

Run the Application Locally
Apply migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

```

### How to Contribute

```bash
Reporting Bugs
Search the issues to see if the bug has already been reported.
If not, create a new issue with detailed steps to reproduce the problem.

Suggesting Features
Check existing feature requests before suggesting a new one.
Provide a clear use case and benefits of the feature in your issue.

Implementing Changes
Create a new branch for your work:
git checkout -b feature/your-feature-name
```

### Code Guidelines
```bash
   Code Style
   Follow PEP 8 for Python code style.
   Use Black for code formatting:
   flake8
   black .
   Testing
   Add or update tests for any new features or bug fixes.
   Run tests to ensure everything works:    
```

### Pull Request Process

```bash
Ensure Tests Pass: Verify that all tests and lint checks pass locally.
Provide a Clear Description: Include:
    - The purpose of the pull request.
    - Related issue numbers (e.g., "Fixes #123").
    - A summary of the changes made.
Submit the Pull Request: Push your branch and create a pull request against the main branch:
git push origin feature/your-feature-name

```

### Reporting Issues

```bash
When reporting an issue:
    - Include a descriptive title.
    - Provide steps to reproduce the problem.
    - Mention the expected vs. actual behavior.
    - Attach relevant logs or screenshots if applicable.
```
