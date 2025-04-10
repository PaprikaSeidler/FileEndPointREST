import requests
import socket

api_url = "https://localhost:7001/api/FileEndpoint"

response = requests.get(api_url) # Get the list of files from the server
data = response.json() # Parse the JSON response

fileName = data[0] # Get the first file name from the list
print(fileName) # Print the file name

response = requests.get(api_url + "/" + fileName) # Get the file details from the server
data = response.json() # Parse the JSON response

#serverIP = data[0]["ipAddress"] # Get the server IP address from the response
#serverPort = data[0]["port"] # Get the server port from the response

serverIP = "localhost" # IP address of the server
serverPort = 7000 # Port of the server
fileName = "cheddar2.jpg" # Name of the file to be downloaded

my_socket = socket.socket() # Create a socket object
my_socket.connect((serverIP, serverPort)) # Connect to the server
my_socket.send(fileName.encode()) # Send the file name to the server

file = open('C:/p2pTempOutput' + fileName, 'wb') # Open a file to write the received data

file_data = my_socket.recv(1024) # Receive the file data from the server
while (file_data): # While there is data to receive
    print("Receiving...")   # Print a message indicating that data is being received
    file.write(file_data) # Write the received data to the file
    file_data = my_socket.recv(1024) # Receive more data from the server
file.close() # Close the file

print("Done Sending") # Print a message indicating that the file has been received successfully
my_socket.close() # Close the socket connection
