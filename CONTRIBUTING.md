# How to Contribute

Thank you for your interest in improving this project for encrypted ZIP backups with automatic upload to Google Drive! This document describes how you can contribute code, report bugs, or suggest improvements. Please read it carefully to understand the contribution process.

## Contribution Process

To contribute to the code, follow these general steps:

- **Fork** the official repository on GitHub to create your own personal copy.  
- **Clone your fork** to your local machine (`git clone <your-fork-url>`).  
- **Create a branch** for your changes (`git checkout -b my-new-feature`) with a descriptive name.  
- **Make your changes** in that branch following the project’s coding style. Be sure to test and ensure your code works properly.  
- **Add and commit** your changes with clear and concise messages (e.g., “Add support for multiple folders” or “Fix file encryption bug”).  
- **Push** your branch with the commits to your remote GitHub repository (`git push origin my-new-feature`).  
- **Open a Pull Request (PR)** from your branch in your fork to the `main` branch of the original project. In the PR, describe the changes you’re proposing and why they are useful.  

The maintainers will review your PR. They may request changes or improvements before merging. Please respond kindly to comments and keep the PR updated with new commits if needed. Once accepted, your PR will be merged into the project.

## Code Style

Code consistency is essential. This project follows Python’s style conventions (PEP 8). It is recommended to use tools such as:

- **Black**: auto-formatter (`black .`)
- **Flake8**: static code analyzer (`flake8`)

Use descriptive names for variables, functions, and classes. Add explanatory comments and docstrings to new functions.

## Reporting Bugs and Suggesting Improvements

Use the repository’s *Issues* section to:

1. **Check if a similar issue** already exists.
2. **Open a new one** with a clear title and detailed description.
3. Tag it as “bug” or “enhancement” if you have permission.

Please follow the code of conduct and maintain respectful communication.

## Ideas to Expand the Project

Some improvement ideas:

- Support for multiple folders.
- JSON/YAML configuration file.
- Web interface (Streamlit, Flask).
- Upload to other services (Dropbox, S3, etc.).
- Notifications after backup completion.
- Incremental backups.
- Internal scheduled tasks.

If you have other ideas, open an issue or propose a PR.

## Acknowledgements

Thank you for your interest in contributing! This project grows better thanks to contributors like you. If you have any questions, open an issue or contact the maintainers.
