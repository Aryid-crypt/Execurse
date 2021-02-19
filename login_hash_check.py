import hashlib

def login(username, password, password_hash):

    x = password + username
    
    xUtf8 = x.encode("utf-8")
    
    xHash = hashlib.md5( xUtf8 )
    
    xHex = xHash.hexdigest()
    
    if user_list[index_no][2] == xHex:
        return True
    else:
        return "The password was incorrect"


