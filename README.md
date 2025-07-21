# Python CI/CD Project using Jenkins | 3-Tier Architecture

This project demonstrates a simple 3-tier application setup that includes:
- **Backend**: Python Flask app
- **Frontend**: Static HTML file
- **Database**: MySQL
- **CI/CD**: Jenkins pipeline for automated testing, linting, building

## Jenkins CI/CD Setup
- Create a New Pipeline Job in Jenkins
- Go to Jenkins Dashboard -> New Item -> Name: Python-CI-CD-pipeline -> Choose: Pipeline -> Click OK

## Connect GitHub Repo
- Under Pipeline -> Definition, select Pipeline script from SCM
- SCM: Git: Repo URL: https://github.com/vaishnavipadwal/Python-CI-CD-project.git -> Branch: main -> Script Path: Jenkinsfile

## Run the Pipeline
- Click Build Now: Jenkins will execute the following steps:
- Clone your GitHub repo
- Set up Python environment
- Install backend dependencies
- Run unit tests
- Run static code analysis using flake8
- Build Docker image for backend

---

# The difference between using Docker and not using Docker in your project in the context of this python CI/CD 3-tier setup.

##  1. **Without Docker (Non-Docker Setup)**

### How it works:

* Your app runs directly on the local machine or Jenkins agent.
* Jenkins creates a Python virtual environment, installs dependencies, and runs the code natively.
* The database (MySQL) needs to be installed and running on your local/remote machine or configured separately.
* Jenkins just runs shell commands like python, pip, pytest, flake8.

### Pros:

* Easier to understand for beginners.
* No container setup required.
* Faster initial setup in Jenkins.

### Cons:

* Works only if the environment (OS, Python version, dependencies) is identical across machines.
* Higher chance of "it works on my machine" issues.
* Jenkins server must have Python and all tools installed manually.
* Deployment and environment isolation are harder to manage.

---

##  2. **With Docker (Dockerized Setup)**

### How it works:

* You define everything the app needs inside a Dockerfile.
* Jenkins builds a Docker image of your backend using that Dockerfile.
* Optionally, use Docker Compose to spin up backend, frontend, and MySQL DB in containers.
* Your app becomes containerized — runs the same way everywhere: locally, in Jenkins, in production.

### Pros:

* Environment consistency: same result on any machine, including Jenkins, staging, or production.
* No need to install Python or MySQL manually on Jenkins or local.
* Clean isolation: app, dependencies, and runtime all inside the container.
* Makes deployment easier (e.g., to ECS, Kubernetes, or EC2).
* Allows multi-tier orchestration via docker-compose.

### Cons:

* Slightly more complex to understand and set up.
* Jenkins must have Docker installed and configured properly.
* Build time is a bit longer because of Docker image creation.

---

- i will create project  with docker means Dockerzied setup in my next project (This will be my future work to improve environment consistency and deployment.)
