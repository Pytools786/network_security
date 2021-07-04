import hashlib

design_text = '''
   _____  ____________  ____  __   ____
  / _ \ \/ /_  __/ __ \/ __ \/ /  / __/
 / ___/\  / / / / /_/ / /_/ / /___\ \  
/_/    /_/ /_/  \____/\____/____/___/  
                                       
                                         coded by shivraj patil
'''
print(design_text)


msg = input("Enter text to produce hashes : ")

# encode it to bytes using UTF-8 encoding
message = msg.encode()

# hash with MD5 
print("MD5 : ", hashlib.md5(message).hexdigest())

# hash with SHA-256
print("SHA-256 : ", hashlib.sha256(message).hexdigest())


#hash with BLAKE2b
print("BLAKE2b : ", hashlib.blake2b(message).hexdigest())