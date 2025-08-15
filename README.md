# Eureka SSRF

**A Proof of Concept to demonstrate SSRF vulnerability in Eureka service.**

> ⚠️ **Warning:** This PoC is for educational purposes only. Do **not** use it on systems you do not own or have explicit permission to test.

## Description

This script demonstrates how a malicious service can be registered on a Eureka server, potentially enabling **Server-Side Request Forgery (SSRF)**. It sends a crafted JSON payload to the Eureka API to register a custom service instance.

The PoC targets a Eureka service accessible from the Internet, allowing the tester to simulate internal requests through the vulnerable service.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/z3rodol/eureka-ssrf.git
cd eureka-ssrf
```

2. Install dependencies:

```bash
pip install requests
```
3. Configure the script:

EUREKA_URL : URL of the Eureka server (include credentials if necessary)

MY_IP : IP address where your malicious service is listening

TARGET_PORT : Port for the target internal service

4. Run the script:
```bash
python eureka_ssrf_poc.py
```

5. Check the output:

- [+] Malicious service successfully registered. – PoC worked

- [-] Failure (CODE) – PoC failed


6. Launch a listener

```bash
nc -lnvp 8081
```

# How it works

  1. The script sends a POST request to the Eureka server’s apps endpoint.

  2. It registers a new instance with custom IP and port.

  3. If the Eureka server is misconfigured or publicly accessible, this could be used to trigger SSRF towards internal services.

# Responsible Disclosure

This PoC should only be used in:

  - Your own testing environments

  - Security research labs

  - Authorized penetration tests

Do not attempt to target third-party services without permission.

