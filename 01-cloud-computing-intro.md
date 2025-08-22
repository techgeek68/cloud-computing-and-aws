# Introduction to Cloud Computing & Deployment Model

---

## What is Cloud Computing?

Cloud Computing is the on-demand delivery of computing power, database, storage, applications, and other IT resources via the internet, with pay-as-you-go pricing.

---

## Categories of Cloud Services

### 1. Compute
- **Purpose:** Enables processing power to run applications & services.
- **Examples:**
  - Virtual Machines (VMs)
  - Containers (e.g., Docker, Kubernetes)
  - Serverless Computing (e.g., AWS Lambda)

#### Practical Example

See [`compute-demo.py`](compute-demo.py) for a demonstration of running a serverless function using AWS Lambda.

---

### 2. Storage
- **Purpose:** Provides space to store, backup, and retrieve data.
- **Examples:**
  - Amazon S3: Object storage
  - Amazon EBS: Block storage for EC2
  - Amazon EFS: Scalable file storage
  - AWS Glacier: Long-term, archival storage

#### Practical Example

See [`storage-demo.py`](storage-demo.py) for uploading and retrieving files in Amazon S3.

---

### 3. Networking
- **Purpose:** Enables connectivity between cloud resources and external networks.
- **Examples:**
  - Amazon VPC: Virtual private cloud
  - Elastic Load Balancing (ELB)
  - Amazon Route 53: DNS
  - AWS CloudFront: CDN

#### Practical Example

See [`networking-demo.tf`](networking-demo.tf) for provisioning a VPC and configuring networking using Terraform.

---

### 4. Database
- **Purpose:** Managed services for storing & accessing structured/unstructured data.
- **Examples:**
  - Amazon RDS: Managed relational database
  - Amazon DynamoDB: NoSQL key-value store
  - Amazon Redshift: Data warehousing
  - Amazon Aurora: High-performance relational database

#### Practical Example

See [`database-demo.py`](database-demo.py) for basic operations with Amazon DynamoDB.

---

### 5. Development, Messaging, & Deployment
- **Purpose:** Tools for building, deploying, and managing applications.
- **Examples:**
  - AWS CodePipeline: CI/CD
  - Amazon SQS: Messaging
  - Amazon SNS: Notification
  - AWS CloudFormation: Infrastructure as Code

#### Practical Example

See [`deployment-demo.yml`](deployment-demo.yml) for a simple AWS CloudFormation template.

---

### 6. Migration & Transfer
- **Purpose:** Moving workloads to the cloud.
- **Examples:**
  - AWS DMS: Database Migration Service
  - AWS Snowball: Data transfer device
  - AWS Migration Hub: Migration tracking
  - AWS Transfer Family: Managed file transfer (SFTP, FTPS, FTP)

#### Practical Example

See [`migration-demo.md`](migration-demo.md) for a walkthrough of data migration using AWS DMS.

---

### 7. AI & ML
- **Purpose:** Services for training models, predictions, automation.
- **Examples:**
  - Amazon SageMaker: ML models
  - Amazon Rekognition: Image/video analysis
  - Amazon Comprehend: NLP
  - Amazon Lex: Chatbot service

#### Practical Example

See [`ml-demo.py`](ml-demo.py) for running a simple inference using Amazon Comprehend.

---

### 8. Auditing, Monitoring & Logging
- **Purpose:** Tracks cloud activity for performance, compliance, and security.
- **Examples:**
  - Amazon CloudWatch: Monitoring & alerts
  - AWS CloudTrail: Auditing API activity
  - AWS Config: Resource monitoring
  - AWS X-Ray: Distributed tracing

#### Practical Example

See [`monitoring-demo.py`](monitoring-demo.py) for creating a CloudWatch metric and alarm.

---

### 9. Security, Compliance & Governance
- **Purpose:** Data protection, privacy, regulatory adherence.
- **Examples:**
  - AWS IAM: Identity & access management
  - AWS KMS: Key management/encryption
  - Amazon GuardDuty: Threat detection
  - AWS WAF: Web Application Firewall

#### Practical Example

See [`security-demo.py`](security-demo.py) for setting up an IAM user and policy.

---

### 10. Pricing, Billing & Support
- **Purpose:** Cost management, usage monitoring, support.
- **Examples:**
  - AWS Budgets
  - AWS Cost Explorer
  - AWS Support Plans
  - AWS Trusted Advisor

#### Practical Example

See [`billing-demo.py`](billing-demo.py) for querying billing data using AWS Cost Explorer.

---

## Traditional Computing Model vs Cloud Computing Model

### Traditional Computing
- Hardware solutions require physical space, staff, security, planning, and capital expenditure.
- Long hardware procurement cycles.
- Capacity provisioned by guessing maximum peaks.

### Cloud Computing
- Infrastructure as software.
- Flexible, cost-effective, easily changed.
- Eliminates undifferentiated heavy-lifting tasks.

#### Practical Analysis

See [`comparison.md`](comparison.md) for a breakdown of cost and resource management between traditional and cloud computing models.

---

## Similarities between AWS & Traditional IT

| Category      | On-premises IT                 | AWS Equivalent                |
|---------------|-------------------------------|-------------------------------|
| Security      | Firewalls, ACLs, Admins        | Security Groups, Network ACLs, IAM |
| Networking    | Routers, Switches              | ELB, VPC                      |
| Compute       | Physical servers               | EC2 Instances, AMI            |
| Storage/DB    | DAS, SAN, NAS, RDBMS          | EBS, EFS, S3, RDS             |

---

## CapEx vs. OpEx

| Model         | CapEx         | OpEx        |
|---------------|---------------|-------------|
| On-Premises   | Yes           | Yes         |
| Cloud         | No            | Yes         |

- **On-Premises:** Upfront hardware/software costs (CapEx), ongoing operations (OpEx).
- **Cloud:** No large upfront investment, pay-as-you-go (OpEx).

---

## Cloud Computing Advantages

- Speed: Fast resource setup
- Agility: Easy upgrades
- Economies of scale: Pay-as-you-go
- Elasticity: Use resources as needed
- Durability: No aging hardware

---

## Cloud Service Models

### IaaS (Infrastructure as a Service)
- **Features:** Scalable resources, pay-as-you-go, control over infrastructure
- **Examples:** AWS EC2, Azure VMs, Google Compute Engine, AWS S3
- **App Example:** Dropbox (storage)

#### Practical Example

See [`iaas-demo.tf`](iaas-demo.tf) for deploying an EC2 instance using Infrastructure as Code.

---

### PaaS (Platform as a Service)
- **Features:** Development tools, auto-scaling, simplifies deployment
- **Examples:** Heroku, Google App Engine, Azure App Service, AWS Elastic Beanstalk
- **App Example:** Netflix (content delivery)

#### Practical Example

See [`paas-demo.py`](paas-demo.py) for deploying a simple web app on AWS Elastic Beanstalk.

---

### SaaS (Software as a Service)
- **Features:** Accessible via browser, automatic updates, multi-tenancy
- **Examples:** Google Workspace, Salesforce, Slack, AWS Chime

#### Practical Example

See [`saas-demo.md`](saas-demo.md) for SaaS integration and usage.

---

## Cloud Computing Deployment Models

### 1. Public Cloud
- Managed by third-party provider, available to general public, scalable.
- **Providers:** AWS, Oracle Cloud, IBM Cloud, Azure, GCP
- **Disadvantages:** Shared resources, security/privacy concerns, reliability issues.

#### Practical Example

See [`public-cloud-demo.md`](public-cloud-demo.md) for a deployment scenario in AWS public cloud.

---

### 2. Private Cloud
- Dedicated to one organization, managed in-house or by third party, customizable, secure.
- **Examples:** VMware vCloud, OpenStack, Microsoft System Center
- **Disadvantages:** High cost, maintenance, training, limited scalability.

#### Practical Example

See [`private-cloud-demo.md`](private-cloud-demo.md) for setting up OpenStack.

---

### 3. Hybrid Cloud
- Combination of public and private clouds, flexible, secure, cost-effective.
- **Examples:** AWS, Azure, GCP, HPE
- **Disadvantages:** Complex integration, suitable for multiple use cases.

#### Practical Example

See [`hybrid-cloud-demo.md`](hybrid-cloud-demo.md) for integrating on-premises and AWS resources.

---

### 4. Community Cloud
- Shared by organizations with similar interests, collaborative.
- **Examples:** NIH Biomedical Research Cloud, NASA HEC Program
- **Disadvantages:** Higher cost, limited popularity, lower bandwidth/storage.

#### Practical Example

See [`community-cloud-demo.md`](community-cloud-demo.md) for a collaborative research scenario.

---

## Advantages of Cloud Computing

1. Trade capital expenses for variable expenses
2. Massive economies of scale
3. Stop guessing capacity
4. Increase speed & agility
5. Reduce data center spending
6. Go global in minutes

---

# Introduction to Amazon Web Services (AWS)

## What are Web Services?

- Software applications accessible over the internet, interoperable across platforms.
- Use standardized formats (XML/JSON) for data exchange.
- Operate through APIs (rules for software interaction).

---

## What is AWS?

- Secure cloud platform with global products.
- On-demand access to compute, storage, network, database, and management tools.
- Pay only for what you use; services work together like building blocks.

---

## Interacting with AWS

1. **AWS Management Console:** Graphical interface.
2. **Command Line Interface (AWS CLI):** Commands or scripts.
3. **Software Development Kits (SDKs):** Code integration (Java, Python, etc.).

#### Practical Example

See [`awscli-demo.sh`](awscli-demo.sh) for basic AWS CLI usage.

---

## AWS Global Infrastructure

- Designed for flexibility, reliability, scalability, and security.
- **Global Infrastructure Map:** [AWS Global Infrastructure Map](https://aws.amazon.com/about-aws/global-infrastructure/#AWS_Global_Infrastructure_Map)
- **Regions and Availability Zones:** [Regions & AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

### AWS Regions
- Geographical areas with AWS data centers.
- Full redundancy and connectivity.
- Each region has multiple Availability Zones (AZs).

### AWS Data Centers
- Secure, redundant power, networking, connectivity.
- 50k-80k physical servers per center.

### Choosing an AWS Region
- Data governance/legal requirements
- Proximity to customers (latency)
- Service availability
- Costs

### AWS Points of Presence (PoPs)
- **Edge Locations:** Serve cached content (CloudFront CDN)
- **Regional Edge Caches:** For less frequently accessed content

---

## AWS Infrastructure Features

- **Elasticity:** Dynamically adjusts capacity.
- **Scalability:** Grows with demand.
- **Fault-tolerance:** No single point of failure.
- **High availability:** Minimizes downtime.

#### Practical Example

See [`infra-features-demo.md`](infra-features-demo.md) for a scenario using Auto Scaling and Multi-AZ deployments.

---

## Regions vs Availability Zones vs Edge Locations

| Type             | Description                                                                              |
|------------------|-----------------------------------------------------------------------------------------|
| Regions          | Virtual geographic areas with multiple availability zones. Geographic redundancy.        |
| Availability Zones | Separate clusters for fault tolerance and high availability. Host servers, apps, etc.   |
| Edge Locations   | Small data centers for caching and content delivery close to users.                     |

---

## AWS Services and Service Category

### AWS Foundational Services

#### Applications Layer
- **Virtual Desktops:** Amazon WorkSpaces
- **Collaboration:** Amazon Chime

#### Platform Services Layer
- **Databases:** RDS (relational), DynamoDB (NoSQL)
- **Caching:** ElastiCache
- **Analytics:** Kinesis, Redshift, Glue
- **Application Services:** SQS (queue), Step Functions (orchestration), AppStream 2.0, MediaConvert, SES (email)
- **Deployment & Management:** ECS/EKS (containers), CodePipeline (DevOps), CloudFormation (templates), CloudWatch (monitoring)
- **Mobile Services:** Cognito (identity), Pinpoint (analytics/notifications)

#### Foundation Services Layer
- **Compute:** EC2, Lambda
- **Networking:** VPC, Route 53
- **Storage:** S3 (object), EBS (block), Glacier (archive)

#### Infrastructure Layer
- **Regions:** e.g., US-East-1
- **Availability Zones:** e.g., North Virginia (6 AZs)
- **Edge Locations:** CloudFront CDN

---

## Introduction to Frameworks

### Cloud Adoption Framework (CAF)

- Set of best practices/tools for cloud adoption.
- Helps manage risks, costs, and compliance.
- Optimizes governance/security.

#### Perspective & Foundational Capabilities

| Perspective | Capability Examples        |
|-------------|---------------------------|
| Security    | Infra protection, governance, incident response |
| Platform    | Architecture, engineering, CI/CD                |
| Governance  | Program management, financial mgmt, risk mgmt   |
| People      | Culture, workforce, leadership, org design       |

#### Cloud Transformation Domain

- Domains: Technology, Process, Organization, Product
- Capabilities: Business, People, Governance, Platform, Security, Operations
- Outcomes: Reduced risk, improved ESG, revenue growth, efficiency

#### Cloud Transformation Journey

**Phases:**
1. **Envision:** Link cloud to business outcomes, prioritize opportunities.
2. **Align:** Identify gaps, dependencies, stakeholder alignment.
3. **Launch:** Pilot initiatives, learn & adjust.
4. **Scale:** Expand pilots, associate business benefits with scaling.

---

## AWS Well-Architected Framework

Helps architects build secure, performant, resilient, and efficient infrastructure. Six pillars:

1. **Security:** Protect data, systems, assets; compliance & risk management.
   - *Example:* Use CloudTrail for logging.
2. **Operational Excellence:** Manage/monitor operations, improve processes.
   - *Example:* Use CodeCommit for version control.
3. **Reliability:** Recover from failures, maintain performance.
   - *Example:* Multi-AZ RDS deployments.
4. **Performance Efficiency:** Optimize resources, adapt to change.
   - *Example:* Use Lambda for serverless.
5. **Cost Optimization:** Avoid unnecessary costs, maximize ROI.
   - *Example:* S3 Intelligent-Tiering.
6. **Sustainability:** Environmentally responsible architecture.
   - *Example:* EC2 Auto Scaling.

### General Design Principles

- **Stop guessing capacity:** Scale automatically.
- **Test at production scale:** Create test envs on demand.
- **Automate:** Create/replicate workloads efficiently.
- **Evolutionary architectures:** Design for change.
- **Data-driven architecture:** Use data for improvement.
- **Game days:** Simulate events to improve resilience.

#### Practical Example

See [`wellarchitected-demo.md`](wellarchitected-demo.md) for a sample secure and scalable AWS architecture.

---

## Sign up for AWS Account

- Go to [AWS Sign Up](https://portal.aws.amazon.com/billing/signup)
- Follow the instructions.
- Create root user, then assign admin access to another user.

---

## Create a User with Administrative Access

1. Log in to AWS Management Console.
2. Turn on MFA.
3. Enable IAM Identity Center.
4. Add user, assign group, set permissions.

---

## Getting Started with the AWS Management Console

- **Features:** Service navigation, search, customization, notifications, cost/usage monitoring, favorites, CloudShell.
- **Dashboard:** Widgets for health, cost, favorites, recent services, Trusted Advisor.
- **Navigation Bar:** Account info, region selector, service selector, search, CloudShell.

---

## AWS CLI

- **Install:** [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- **Commands:**
  - `aws --version`
  - `aws help`
  - `aws ec2 describe-instances`
- **Documentation:** [EC2 CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/)

#### Practical Example

See [`awscli-demo.sh`](awscli-demo.sh).

---

*End of Introduction to Cloud Computing & AWS*