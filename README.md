## Overview

This project is a backend service that serves as a proxy to fetch issues from a GitHub repository. It is implemented in Python and uses the built-in HTTP server. The service is containerized using Docker, and you can also run it without Docker for local development.

## Project Structure
- app_cmd/server/main.py: The entry point for the server.
- internal/api/handler.py: Contains the request handler logic.
- internal/github/client.py: Handles communication with the GitHub API.
- pkg/logger/logger.py: Implements a simple logging utility.
- pkg/constants/: Contains constant messages and error strings.
- pkg/config/config.py: Manages configuration settings.
- Dockerfile: Defines the Docker container for the service.
- docker-compose.yml: Sets up Docker Compose for running the service.
- requirements.txt: Lists Python dependencies.

## Requirements
- Python 3.8 or higher
- Docker (optional, for containerized deployment)

## Setup and Installation

1. **Clone the Repository**

    ```git clone https://github.com/Hmitchell433/presence-test-project.git```
    ```cd presence-test-project/app```

2. **Setup Environment Variables**

  Create a `.env` file in the app directory with the following content:

  ```SERVER_PORT=8080```

  Update the values as needed.

## Running the Service

### Without Docker

1. **Install Dependencies**

    Install the required Python packages using pip.

    ```pip install -r requirements.txt```

2. **Run the Server**

    ```python cmd/server/main.py ```

    The server will start and listen on the port specified in .env (default: 8080).

3. **Test the Service**

    You can test the service using curl or Postman. For example:

    ```curl "http://localhost:8080/?owner=your-repo-owner&repo=your-repo-name"```

### With Docker

1. **Build the Docker Image**
   ```docker-compose up --build  -d```

## Configuration
    Configuration settings are managed via the .env file. Ensure that the GITHUB_API_URL and SERVER_PORT are set according to your environment.

## Testing
  1. Testing without docker:
      ```pytest tests ```

  2. Testing with docker:
    ```docker-compose run --rm test```

## Logging
  The service includes basic logging. Logs are output to the console. You can adjust the logging level and format in pkg/logger/logger.py.

## Additional Information
- **CI/CD:** For continuous integration and deployment, you may set up pipelines in tools like CircleCI
