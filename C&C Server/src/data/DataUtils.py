from multiprocessing.connection import Client


def clientToArchive(client):
    # error handling -> if empty or if more than one values 
    if(len(client) == 0):
        raise Exception("No user found")
    
    client = client[0]
    archive = {'hostname': client[1],'lastActiveTime': client[3]}
    return archive
    
