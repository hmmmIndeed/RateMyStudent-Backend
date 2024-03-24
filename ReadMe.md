Backend
Download all needed programs
    reference: https://code.visualstudio.com/docs/python/python-tutorial
    install python from python.org
    install VS Code
    install VS Code Python extension

Download the code
    download Git: https://git-scm.com/downloads
    open the folder the backend should be in
    type tjos command into the terminal:
git clone https://github.com/hmmmIndeed/RateMyStudent-Backend.git
    open the backend folder in VS Code

Set up venv in the backend folder
    press Ctrl+Shift+P to open the command runner
    search for and choose the "Python: Create Environment..." option
    choose the "Venv" option
    choose the "Python 3.11.8 64-bit /bin/python" option (any one of them is probably fine)
    select the "Terminal" menu at the top of the screen and choose "New Terminal"

Installing packages
    reference: https://realpython.com/python-virtual-environments-a-primer
    Windows:
    run these commands in the VS Code terminal:
python -m venv venv
venv\Scripts\activate
python -m pip install fastapi[all]
python -m pip install uvicorn
python -m pip install sqlalchemy
    also download sqlite3
    Linux:
    run these commands in the VS Code terminal:
python3 -m venv venv
source venv/bin/activate
python -m pip install fastapi[all]
python -m pip install uvicorn
python -m pip install sqlalchemy
    also make sure fastapi, uvicorn, sqlalchemy, and sqlite3 are all downloaded from your package manager on your local device

Running the backend
    navigate to main.py and run the file


#Frontend
Prerequisites for Running the Frontend

##NPM
NPM is needed to run the frontend part of RateMyStudent. To install npm, follow these steps:
1. Visit https://nodejs.org/en/download
2. Download the lts version of the installer
3. Run the installer

##Running the Frontend
1. Using an IDE of your choice, open up the project folder
2. Open up a terminal instance
3. Access the frontend folder by running
```cd frontend```
   in the terminal

##Installing the Dependencies

Inside of rateMyStudent/frontend, run the following commands

    npm install
    npm install react-router-dom
    npm install axios


Once those dependencies are done, you will be able to sucessfully run the frontend part of the application. However, before you launch it,
ensure that the backend server, backend/main.py is running in another terminal. Once you have verified that the backend server, run the following command:
    npm start

A browser should automatically open with the application running!


    open the folder the frontend should be in
    type this command into the terminal:
git clone zdfgxchvjkhcgxfzdfxchvjgkhl
    cd into the frontend folder
    run this command:
npm start
    launch the frontend in your web browser at http://localhost:3000/