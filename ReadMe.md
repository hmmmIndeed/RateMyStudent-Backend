# OSC Hackathon: Rate My Student
Hello! This project is a Rate My Professor-inspired website that allows teachers to "rate" their students, giving them the ability to pass on their experience with a student to the students' future teachers. Teachers describe their students and fill in fields to give future teachers an idea of their future students' strengths and weaknesses.

This project is split into two parts which must be downloaded separately.
## Backend
### Download all needed programs
The first step is to download all the needed programs used to run this app. You can reference this to download everything needed for the backend: https://code.visualstudio.com/docs/python/python-tutorial. Follow these three steps that are also in the article.
1. install python from https://python.org
2. install VS Code from https://code.visualstudio.com/
3. install VS Code Python extension from the VS Code extension marketplace

(on Linux, the first two can be downloaded by your package manager)

### Download the code
Download Git from https://git-scm.com/downloads or your package manager on Linux. Then, in the terminal, cd into the folder the backend should be in. 

Type this command into the terminal:
```git clone https://github.com/hmmmIndeed/RateMyStudent-Backend.git```


### Set up venv in the backend folder
Open the backend folder in VS Code. Press Ctrl+Shift+P to open the command runner. Search for and choose the "Python: Create Environment..." option. Then choose the "Venv" option. Right after, choose the "Python 3.11.8 64-bit /bin/python" option (any one of them is probably fine). Lastly, select the "Terminal" menu at the top of the screen and choose "New Terminal".

### Installing packages
You can use this as reference when installing the Python packages: https://realpython.com/python-virtual-environments-a-primer.

Windows:

Run these commands in the VS Code terminal:

    python -m venv venv
    venv\Scripts\activate
    python -m pip install fastapi[all]
    python -m pip install uvicorn
    python -m pip install sqlalchemy

Also download sqlite3: https://www.sqlite.org/download.html.

Linux:

Run these commands in the VS Code terminal:

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install fastapi[all]
    python -m pip install uvicorn
    python -m pip install sqlalchemy

Also make sure fastapi, uvicorn, sqlalchemy, and sqlite3 are all downloaded from your package manager on your local device.

### Running the backend
Navigate to main.py and run the file.


## Frontend
Prerequisites for Running the Frontend

### NPM
NPM is needed to run the frontend part of RateMyStudent. To install npm, follow these steps:
1. Visit https://nodejs.org/en/download
2. Download the lts version of the installer
3. Run the installer

### Running the Frontend
1. Using an IDE of your choice, open up the project folder
2. Open up a terminal instance
3. Access the frontend folder by running
```cd frontend```
   in the terminal

### Installing the Dependencies

Inside of rateMyStudent/frontend, run the following commands

    npm install
    npm install react-router-dom
    npm install axios


Once those dependencies are done, you will be able to sucessfully run the frontend part of the application. However, before you launch it,
ensure that the backend server, backend/main.py is running in another terminal. Once you have verified that the backend server, run the following command:

    npm start

A browser should automatically open with the application running!


Open the folder the frontend should be in and type this command into the terminal:

    git clone zdfgxchvjkhcgxfzdfxchvjgkhl

cd into the frontend folder and run this command:

    npm start

Launch the frontend in your web browser at http://localhost:3000/
