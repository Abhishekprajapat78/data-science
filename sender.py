import socket
try:
    ##creating socket 
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #dgram -- datagram
    print("socket created")
    ip_add = "192.168.137.241"
    
    port = 8888
    target_add = (ip_add,port)
    message = input("Enter the massage : 😂 ")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg,target_add)
    print("message send success")
    s.close()
except Exception as e:
    print("AN ERROR OCCURED",e) 