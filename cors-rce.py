"""
Author: Aleksa Zatezalo
Description: Obtains RCE on Concord servers through RCE.
Date: March 2024
"""

def constructYaml(lhost, lport):
    """
    Constructs a YAML file containing a workflow and RCE where lhost and lport are the
    ip and ports of the listener for an interactive shell found at lhost:lport.
    """
    
    pass

def constructCORS(lhost, lport, rhost):
    """
    Constructs an http page that abuses misconfigured cors in Concord servers.
    The function takes three arguments: lhost, a listening host; lport, a listening
    port; and rhost, the target url. Saves the ouput to the directory where the script is ran.
    """

    pass

def printLog(message):
    """
    Logs the string, message, to console with the appendage '[+] '.
    """

    pass

def parseServerMessage(message):
    """
    Parses server messages and logs them nicely to standard output.
    """

    pass

def startServer(lport):
    """
    Starts a local python server that listens on lport. It exists upon getting 
    a log mentioning that RCE was achived
    """

    pass

if __name__ == "__main__":
    pass