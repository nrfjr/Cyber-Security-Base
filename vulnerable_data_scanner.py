import requests
import sys

#This script tries to connect using the IP Address and Port
#you'll be providing and return the vulnerable data after successful attempt.

def scan_vulnerability(ip_address, port):

  url = "http://{}:{}/".format(ip_address, port)
  response = requests.get(url)
  return response

def main(argv):

    try:
    
      ip_address = sys.argv[1]
      port = int(sys.argv[2])

      vulnerable_data = scan_vulnerability(ip_address, port)

      print("Connection Status: {}".format(vulnerable_data))
      print("Heres the vulnerable data on {}:{}: ".format(ip_address,port))
      print(vulnerable_data.content)

    except Exception as e:

      print("Unable to connect using {}:{}".format(ip_address, port))
      print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Too few args.')
    else:
        main(sys.argv)