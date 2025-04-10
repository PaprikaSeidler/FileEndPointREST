from os import listdir
from os.path import isfile, join
import requests
import socket

myPath = "C:/p2pTemp" #Path to the directory containing the files
myip = "192.168.0.111" #IP address of the server
myport = 7000 #Port of the server
onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))] #List of files in the directory

api_url = "https://localhost:7001/api/FileEndpoint" #API URL of the file endpoint
for filename in onlyFiles: #Iterate over the files in the directory
    myobject = {"Ipadress": myip, "port": myport} #Create a JSON object with the IP address and port
    response = requests.post(api_url + "/" + filename, json= myobject) #Send a POST request to the API with the filename and JSON object
    print(response) #Print the response from the API
    print(response.json()) #Print the JSON response from the API
    
s = socket.socket() # Create a socket object
s.bind(('',myport))  # Bind to the port 
s.listen(5) # Listen for incoming connections and allow 5 connections
while True: # Infinite loop to keep the server running
    connectionSocket, addr = s.accept() # Accept a connection from a client
    
    print('Got connection from', addr)
    filename = connectionSocket.recv(1024).decode()
    print("Opening file... ", filename)
    file = open("Opening file... ", filename)
    file_data = file.read(1024)
    while (file_data):
        print("Sending data...")
        connectionSocket.send(file_data) # Send the file data to the client
        file_data = file.read(1024)
    file.close() # Close the file
    print("File sent successfully")
    connectionSocket.shutdown(socket.SHUT_WR) # Shutdown the connection

for filename in onlyFiles: #Iterate over the files in the directory
    myobject = {"Ipadress": myip, "port": myport} #Create a JSON object with the IP address and port
    response = requests.delete(api_url + "/" + filename, json= myobject) #Send a DELETE request to the API with the filename and JSON object
    print(response) #Print the response from the API
    print(response.json()) #Print the JSON response from the API












