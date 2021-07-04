import hashlib

design_text = '''
   _____  ____________  ____  __   ____
  / _ \ \/ /_  __/ __ \/ __ \/ /  / __/
 / ___/\  / / / / /_/ / /_/ / /___\ \  
/_/    /_/ /_/  \____/\____/____/___/  
                                       
                                         coded by shivraj patil
'''
print(design_text)


text = input(" enter text tou want to encrypt : ")

#input string to encrypt

hash_object = hashlib.md5(text.encode())

print("encryption Type " + hash_object.name)

md5_hash = hash_object.hexdigest()


print("md5 encrypted data: " + md5_hash)

#print the encrypted string data
