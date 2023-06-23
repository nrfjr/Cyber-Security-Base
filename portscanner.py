import sys
import socket

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
         print(p)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('usage: python %s address min_port max_port' % sys.argv[0])
    else:
        main(sys.argv)