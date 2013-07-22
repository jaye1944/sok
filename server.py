import socket
import datahandle
import pickle

#server data
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
#file info
CHUNK_SIZE = 100
WINDOW_SIZE = 5
SEND_FILE = "myfile.txt" #file name which going to send

#ACKS
ACKPOSITIVE = "1"

print("Server IP " + UDP_IP +" Srever port "+ str(UDP_PORT))
print("Window size is "+ str(WINDOW_SIZE))
print("Chunk size is "+ str(CHUNK_SIZE))
print("Ready to connect......")
def sendACK(first_data):
    while True:
        data, addr = sock.recvfrom(100) # buffer size is 1024 bytes
        if (data.decode('utf-8') == ACKPOSITIVE):
            sock2.sendto(first_data.encode('utf-8'), (UDP_IP, 5000))
            break

def WAIT():
    while True:
        data, addr = sock.recvfrom(100) # buffer size is 1024 bytes
        if (data.decode('utf-8') == ACKPOSITIVE):
            break

def Window_Ack():
    while True:
        data, addr = sock.recvfrom(100) # buffer size is 1024 bytes
        #print(data)
        return data.decode('utf-8')
        break

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
# resiver
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data_to_send = datahandle.get_data(SEND_FILE)#get data array
firstdata = datahandle.get_file_info(SEND_FILE, CHUNK_SIZE) + " " + str(WINDOW_SIZE)#first information

sendACK(firstdata)#check the connection of the server and send send data about the file

file_size = len(data_to_send)#get the size of the file from bytes
WAIT() #wait till the resiver ready to get data
packet = {} #data packet
pccount = 0
windowframe = 0
i =0
while True:
    if(windowframe == WINDOW_SIZE ):
        windowframe = 0
        k = Window_Ack()
        if(k!= ACKPOSITIVE):
            print("Negative ack resive")
            i = i - ((int(k) + WINDOW_SIZE) * CHUNK_SIZE )#re arrange the window in data buffer
        else:
            print("positive ack resive")
            k = ACKPOSITIVE
    data_part = data_to_send[i:i+CHUNK_SIZE]
    i += CHUNK_SIZE
    packet={windowframe:{data_part.__hash__():data_part}} #add data and metadata to dictionary
    send_packet = pickle.dumps(packet) #make one packet
    sock2.sendto(send_packet,(UDP_IP, 5000)) #send data
    print("frame " + str(windowframe) + " send")
    windowframe +=1
