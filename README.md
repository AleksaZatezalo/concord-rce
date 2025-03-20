# Concord RCE

This repository contains a Python exploit targeting a serise of vulnerabilities in the open-source Concord Workflow Server (developed by Walmart). The exploit obtains remote code execution.

## Vulnerabilities Exploited

The exploit leverages three authentication bypass vulnerabilities:

1. CORS Misconfiguration (Information Disclosure)
2. Cross-Site Request Forgery (CSRF) Attack
3. Default User Accounts with Undocumented API Keys

## Exploit Workflow

1. **CORS Exploitation**
Abuse permissive CORS settings to extract sensitive API keys and authentication tokens.

2. **CSRF Attack** 
Craft malicious requests to execute unauthorized actions on behalf of an authenticated user.

3. **Default User & API Key Abuse** 
Gain access to hardcoded API keys, escalate privileges, and achieve full RCE.

## Prerequisites

1. Python 3.x
2. requests library (pip install requests)
3. A vulnerable instance of Concord Workflow Server

### Disclaimer

This exploit is intended for educational and authorized penetration testing purposes only. Unauthorized use against live systems is illegal and unethical. The authors are not responsible for misuse.