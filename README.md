# User Registration and Profile Image Upload API

## Description
This API provides endpoints for user registration and uploading profile images.

## Technologies Used
- Python
- FastAPI
- MongoDB (for storing user data)
- HTML/CSS (for front-end)
- JavaScript (for front-end interactions)

## Setup Instructions
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your MongoDB database and obtain the connection string.
4. Create a `.env` file and add the MongoDB connection string as `MONGO_URI`.
5. Run the FastAPI server using `uvicorn main:app --reload`.

## Endpoints
- `POST /register`: Endpoint for user registration.
  - Parameters:
    - `name`: User's name (string)
    - `email`: User's email address (string)
    - `password`: User's password (string)
    - `profile_image`: User's profile image (file)
  - Returns:
    - `200 OK` with user registration details if successful.
    - `400 Bad Request` if invalid data is provided.

## Usage
1. Send a `POST` request to `/register` with the required parameters.
2. Include the user's name, email, password, and profile image file in the request body.
3. Upon successful registration, the API will return the user's registration details.

