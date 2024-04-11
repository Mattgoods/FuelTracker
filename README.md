# FuelTracker

## Description

FuelTracker is a web application designed to provide a comprehensive analysis of gas prices. The web app offers users the ability to explore various factors that influence gas prices through trend queries. By focusing on trend queries, the web app allows users to investigate how gas prices correlate with different variables over time, providing a dynamic and interactive way to understand these relationships.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+ (https://www.python.org/downloads/)
- Docker (https://docs.docker.com/engine/install/)
- Git
- Visual Studio Code (highly recommmended)

### Setup (Recommend doing everything in VS Code using their terminal)

1. **Clone the Repository**
   
   git clone https://github.com/Mattgoods/FuelTracker.git
   cd FuelTracker

2. **Setup Python Virtual Environment**

   python3 -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`

3. **Install Dependencies**

   pip install -r requirements.txt

4. **Environment Variables**
   - Not sure what this step is, was recommended by Chat-GPT, probably something we have to do later on once we set up the database.
   - Copy the `.env.example` file to a new file named `.env`.
   - Modify the `.env` file with the database credentials and other configurations.

5. **Docker Setup**
   - Ensure Docker Desktop is running.
   - Build the Docker image:

     docker-compose build

   - Start the Docker container:

     docker-compose up

### Running the Application

- **Using Docker**:
  You can use Docker to run the application. This ensures that the environment is consistent across all team members' machines:

  docker-compose up

  This command will start the application and you can go to `http://localhost:5001` to see the website. Changes will update live as long as you save files.

- **Local Development**:
  This way is probably a little easier but might as well use Docker since it's already set up for the project.
  Start the Flask application by running:

  python run.py

  Access the application at `http://localhost:5001`.

### Testing

- Run the automated tests for this system:

  python -m unittest discover
