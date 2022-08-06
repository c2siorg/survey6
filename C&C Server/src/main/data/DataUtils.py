def clientToArchive(client):
    # error handling -> if empty 
    if(len(client) == 0):
        raise Exception("No user found")
    
    client = client[0]
    archive = {'hostname': client[1],'lastActiveTime': client[3]}
    return archive
    
