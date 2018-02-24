import socket
import threading
import win32clipboard as clipboard
import os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

"""
def connect():
	i = True
	while i:
		bind_ip = raw_input("Please enter an IP to use: ")
		try:
			socket.inet_aton(bind_ip)
			i = False
		except socket.error:
			print "That was not a valid IP"
			i = True
	i = True
	while i:
		bind_port = raw_input("Please enter a port to use: ")
		try:
			
	target_host = 
	target_port = 
#Future feature of optional IPs
"""
bind_ip = "localhost"
bind_port = 8080
target_host = "localhost"
target_port = 8080
command = ""
incoming_paste = ""

def listen():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((bind_ip, bind_port))
	server.listen(5)
	print "[*] Listening on %s:%d" % (bind_ip,bind_port)
	# this is our client-handling thread
	def handle_client(client_socket):
		# print out what the client sends
		request = client_socket.recv(1024)
		print "[*] Received this(type paste to use): %s" % request
		# send back a packet
		client_socket.send("Received: " + request)
		client_socket.close()
		incoming_paste = request
		command = ""
		return

	while True:
		client, addr = server.accept()
		print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
		# spin up our client thread to handle incoming data
		client_handler = threading.Thread(target=handle_client,args=(client,))
		client_handler.start()
		return


def paste():
	clipboard.OpenClipboard()
	clipboard.EmptyClipboard()
	clipboard.SetClipboardText(incoming_paste, clipboard.CF_TEXT) #this does not seem to be working
	clipboard.CloseClipboard()
	command = ""
	return

def copy():
	# create a socket object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clipboard.OpenClipboard() #opens the clipboard for use
	print clipboard.GetClipboardData()
	# connect the client
	client.connect((target_host,target_port))
	# send some data
	client.send(clipboard.GetClipboardData())
	clipboard.CloseClipboard()
	# receive some data
	response = client.recv(4096)
	print response
	command = ""
	return

def help():
	clear()
	print "Use 'connect' to open the connection prompt"
	print "Use 'paste' to paste from the connected client"
	print "Use 'copy' to copy from your computer's clipboard"
	print "Use 'listen' to listen for an imcoming paste from the connected computer"
	command = ""
	return

while command != "exit":
	command = raw_input("What would you like to do?: ").lower()

	if command == "help": help()
	elif command == "copy": copy()
	elif command == "listen": listen() 
	elif command == "paste": paste()
	#elif command == "connect": connect()





#Also, would like to add many of this code was inspired by stuff in Black Hat Python, so credit where it is due