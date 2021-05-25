

- Activate your virtual environment for this project: 
   
    macOS/Linux: `source venv/bin/activate`
    
    Windows: `venv\Scripts\activate.bat`

- Point Flask to your application: 

    macOS/Linux:  `export FLASK_APP=main.py`
    
    Windows: `set FLASK_APP=main.py`
- Enable hot reloading, debug mode, and other useful features for local development:  

     macOS/Linux: `export FLASK_ENV=development`

    Windows: `set FLASK_ENV=development`
- run your flask application: 

    `flask run`





 what the app does:
 At the homepage you are forced to go through authentication. Only if you log in your allowed to try out the breed finder questionnair. The questionnair is made out of 4 placeholder questions. They are all yes no questions. Behind every "yes" there are 25 points. Behind the "no" there are 0 points. After the user has submitted the last answer the app prints out the score the user reached. The score is a number between 0 and 100. In a database there are dogbreeds with a min and max score. The app checks, which dog breed is suited for the user, by figuring out if the user score is in range of the min_score and max_score.


