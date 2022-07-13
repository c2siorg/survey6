def clientToArchive(client):
    # error handling -> if empty or if more than one values 
    client = client[0]
    archive = {'hostname': client[1],'lastActiveTime': client[3]}
    return archive
    
