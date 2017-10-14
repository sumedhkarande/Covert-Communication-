from scapy.all import*

while True:
	message=raw_input('Enter the string:')
	print message
	for character in message:
		ASCII= ord(character)
		print ASCII
		packet=IP(dst="10.10.111.255",id=ASCII)/TCP(dport=12)
		send(packet)
	
