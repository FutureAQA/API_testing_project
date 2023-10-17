# API testing project

[![Allure-report](https://img.shields.io/badge/Allure%20Report-deployed-green)](https://futureaqa.github.io/API_testing_project/)

## How to work with this repository:

- Clone repository to your machine.
- Navigate to the root folder of the project.
- Create a virtual environment on Windows.
1. Here's the step-by-step guide on how to create a virtual environment in PyCharm for a project using the GUI on Windows:


    Open Your Project:
        Open PyCharm and load your project.

    Open Project Settings:
        In the top menu, go to "File" -> "Settings" (or "Ctrl+Alt+S").

    Configure Python Interpreter:
        In the left panel, select "Project: [Your Project]" -> "Python Interpreter."
        Click on the gear icon in the top right corner and choose "Add Interpreter"

    Create a New Virtual Environment:
        Choose "Virtualenv Environment" and click "Ok."
        Enter a name for the virtual environment folder and select its location. Click "Create."

    Specify the Python Interpreter:
        Select the newly created virtual environment from the dropdown list.
        Click "Ok."

    Confirm Changes:
        Close the settings window.
2. Creating a virtual environment using the terminal:

    In the project root, open the terminal and enter the command `python -m venv venv`

3. To activate the virtual environment, enter the following command in the terminal: `.\venv\Scripts\activate`.
   
4. When the virtual environment is activated, you will notice a change in the command line (or terminal) prompt. Typically, the name of the virtual environment will appear at the beginning of the prompt, indicating that you are inside an activated virtual environment.

    For instance, if you are using the Command Prompt in Windows, upon activating the virtual environment, you will observe a modification in the prompt:
: **(venv) Your\Project\Path>**

- Run command **pip install -r requirements.txt**
- After, execute **pytest -s -v** to run tests.


**To run a Docker container using the provided Dockerfile, follow these steps:**

    Ensure Docker is Installed:
        Install Docker on your computer if it's not already installed.
        https://www.docker.com/products/docker-desktop/

    Build the Docker Image:
        Open a terminal in the directory containing your Dockerfile.
        Enter the following command to build the Docker image:

        docker build -t my-python-app .

        Replace my-python-app with a unique name for your image.

    After building the image, run the Docker container with the following command:

        docker run my-python-app

    Review Test Results:

        Once the container completes execution, you will see the test results
