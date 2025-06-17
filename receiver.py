import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    ##receiver ke ander ip add receiver ka he aayega
    #hamesha and receiver ka hi aayega khud ka
    ip_add = "192.168.137.241"
    port = 8888
    complete_add = (ip_add,port)
    s.bind(complete_add)

    while True:
        message , sender_address = s.recvfrom(1024)

        print("Raw Message",message)
        print("sender Address", sender_address)

        decoded_msg = message.decode("ascii")
        print("message",decoded_msg)
except Exception as e:
 print("an error occured",e)