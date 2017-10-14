# Covert-Communication-
Covert Communication between server and client using TCP channel.
A covert channel is created between them in such a way that the other hosts on the network are not aware of the data exchange between them. I have used IP packets for this type of communication with TCP as the transport layer. I have injected data in the IP header of the packet at the server which is sent to the client using the Covert Channel.
I have injected data in the Identification filed of the IP header which is encoded in the form of the ASCII value of that letter and the same is decoded at the server to get back the alphabets.
I have used two programs, one for the Server and other for the client that is attached with this pdf file.
