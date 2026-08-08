import socket 

# Target host to scan 
target = input("Enter IP or website to scan: ")

#List of common ports high school CS projects usually check
ports = [21,22,80,443,3306,8080] 

print(f"---Starting scan on {target} ---")

for port in posts: 
     try:
       # Create a basic socket connection
       s = sockt.socket(socket.AF_INET,socket.SOCK_SREAM)
       s.settimeout(1.0)

       # connect_ex returns 0 if connrction succeeds
       result = s.connect_ex((Target,port))

       if result ==0:
          print(f"[+] Port{port} is OPEN!")
      else:
          print(f"[-] Port {port} is closed")

      s.close()
    except:
      print(f"Error scanning port {port}")
print("Done scanning")
