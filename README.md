# Introduction: Cloud Computing and AWS 

![License](https://img.shields.io/github/license/techgeek68/cloud-computing-aws-intro-demo)
![CI](https://github.com/techgeek68/cloud-computing-aws-intro-demo/actions/workflows/lint.yml/badge.svg)
![Issues](https://img.shields.io/github/issues/techgeek68/cloud-computing-aws-intro-demo)

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Folder Structure](#folder-structure)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Contribution Guidelines](#contribution-guidelines)
- [License & Credits](#license--credits)
- [References](#references)

---

## Overview

This repository provides hands-on demonstrations and documentation for foundational cloud computing concepts using AWS. It's designed for learners and professionals exploring compute, storage, networking, security, and more, with practical examples and clear explanations.

---

## Key Features

- **Modular Demos:** Step-by-step guides for AWS services (EC2, S3, RDS, IAM, etc.).
- **Conceptual Docs:** Explanations for SaaS, PaaS, IaaS, and deployment models.
- **Infrastructure as Code:** Terraform examples for reproducibility.
- **Scripts:** Automation for setup and cleanup.
- **Diagrams & References:** Visual architecture and curated resources.
- **CI/CD:** GitHub Actions for code quality and style checks.

---

## Folder Structure

```plaintext
docs/         # Conceptual documentation, diagrams, references
demos/        # Hands-on AWS service demos by topic
terraform/    # Infrastructure-as-code examples
scripts/      # Automation scripts (setup, cleanup)
.github/      # GitHub-specific files (workflows, contributing)
assets/       # Static assets (badges, images)
```

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/techgeek68/cloud-computing-aws-intro-demo.git
   cd cloud-computing-aws-intro-demo
   ```

2. **Set up AWS CLI and credentials**
   - [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
   - Configure with `aws configure`

3. **(Optional) Install Terraform**
   - [Terraform Install Guide](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

---

## Usage Guide

- **Explore Concepts:**  
  Browse `docs/concepts/` for foundational cloud computing knowledge.

- **Run Demos:**  
  Each folder in `demos/` includes step-by-step instructions and sample code.

- **Deploy with Terraform:**  
  Navigate to `terraform/` for infrastructure automation examples.

- **Scripts:**  
  Use `scripts/setup.sh` to initialize resources and `scripts/cleanup.sh` to tear them down.

---

## Contribution Guidelines

We welcome contributions!

- Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) before making pull requests.
- Follow naming conventions and code style defined in this repo.
- All contributions are subject to code review and CI checks.

---

## License & Credits

Distributed under the [MIT License](LICENSE).

**Credits:**  
- [techgeek68](https://github.com/techgeek68)  
- [AWS Documentation](https://docs.aws.amazon.com/)
- Contributors listed in [CONTRIBUTING.md](.github/CONTRIBUTING.md)

---

## References

See [docs/references.md](docs/references.md) for further learning resources.

---
