import sys
import socket

"""

    scan_port - this function allows you to scan 1 address and port at a time.
                it can be used in main function like scan_port(<address>, <port>)
    
    read_port_data - this function reads the data from an address, make sure that the 
                address with corresponding port is open using scan_port for this function
                to connect and get the available data. usage is same as scan_port.
    
    get_accessible_port - iterates through a range of ports from minimum port to maximum
                (ie: from port 1 to port 65535) while using scan_port method for each iteration
                then returns tha array of iteration.

"""

def scan_port(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = (ip, port)
        sock.connect(server_address)
        return True
    except:
        pass
    finally:
        sock.close()

    return False

def read_port_data(address, port):
    
    s = socket.socket()
    s.connect((address, port))
    data = s.recv(1024) 
    
    return str(data)


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    for port in range(min_port, max_port):
        found_ports += [dict(
            ip = address,
            port = port,
            is_open = scan_port(address, port)
        )]
    
    return found_ports


def main(argv):
    address = sys.argv[1]
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    ports = get_accessible_ports(address, min_port, max_port)
    for p in ports:
         if p['is_open'] == True:
            print("IP: "+str(p["ip"])+", Port: "+str(p["port"])+", Status: "+str(p["is_open"]))
            print("Message: " + read_port_data(p["ip"], p["port"]))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)
