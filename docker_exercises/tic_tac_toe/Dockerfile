# Use the official Python 3.12 image based on Alpine Linux (lightweight)
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Python game script from the host into the container
COPY tic_tac_toe.py .

# Set the default command to run the Tic-Tac-Toe game
CMD ["python3", "tic_tac_toe.py"]
