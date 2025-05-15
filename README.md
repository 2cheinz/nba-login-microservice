NBA Login Microservice 

This is a Flask-based login service with token generation for my teammate's NBA Journaling Application.

Features:
- POST / login - accepts a username and returns a session token
- POST / validate - accepts token and returns either true or false
- Uses Python's 'secrets' module to generate a hex token