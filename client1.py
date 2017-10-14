from scapy import*
import sys

packet= sniff(count=100)
for pkts in packet:
	if(str(pkts.getlayer(IP).src=="10.10.111.108") and pkts.haslayer(TCP)):
		port=int(pkts.getlayer(TCP).dport)
		if(port==12):
			letters=chr(pkts.getlayer(IP).id)
			sys.stdout.write(letters)
