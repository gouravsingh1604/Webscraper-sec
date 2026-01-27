import ssl, socket, requests
import nmap

def check_ssl_certificate(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return {"valid": True, "issuer": cert.get("issuer"), "subject": cert.get("subject")}
    except Exception as e:
        return {"valid": False, "error": str(e)}

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        important_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options"
        ]
        results = {}
        for h in important_headers:
            results[h] = headers.get(h, "Missing")
        return results
    except Exception as e:
        return {"error": str(e)}

def port_scan(hostname):
    scanner = nmap.PortScanner()
    try:
        scanner.scan(hostname, "1-1024")  # common ports
        return scanner[hostname]["tcp"]
    except Exception as e:
        return {"error": str(e)}
