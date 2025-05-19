NBA Login Microservice 

This is a Flask-based login service with token generation for my teammate's NBA Journaling Application.

Features:
- POST / login - accepts a username and returns a session token
- POST / validate - accepts token and returns either true or false
- Uses Python's 'secrets' module to generate a hex token


How to Use the Login Endpoint:
- Use the URL http://localhost:5001/login
- Use a POST request
- A JSON format for the body such as: {"username": casey}

