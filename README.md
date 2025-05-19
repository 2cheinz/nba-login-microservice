NBA Login Microservice 

This is a Flask-based login service with token generation for my teammate's NBA Journaling Application.

Features:
- POST / login - accepts a username and returns a session token
- POST / validate - accepts token and returns either true or false
- Uses Python's 'secrets' module to generate a hex token

How to run the program:
- Open terminal (after Python and Flask have been installed) and do "python3 login.py" to begin running this program on the localhost:5001 port

How to use the Login Endpoint:
- Use the URL http://localhost:5001/login
- Use a POST request
- A JSON format for the body such as: {"username": "casey"}
- An Example respone would be: {"token": "593fgja349fgkl9"}

How to use the Validate Endpoint:
- Use the URL http://localhost:5001/login
- Use a POST request
- A JSON format for the body such as: {"token": "593fgja349fgkl9"}
- An Example respone would be: {"valid": "true"}

Example Call Using Python:

URL = "http://localhost:5001"

# Login
- username = input("Enter your username to login: ")
- login_response = requests.post(f"{URL}/login", json={"username": username})
- token = login_response.json().get("token")
- print(f"Token received: {token}")

# Validate
- validate_response = requests.post(f"{URL}/validate", json={"token": token})
- print("Validation response:", validate_response.json())

