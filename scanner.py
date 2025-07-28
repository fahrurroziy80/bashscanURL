import socket
from urllib.parse import urlparse

def get_ip_from_url(url):
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc or parsed_url.path
        ip = socket.gethostbyname(hostname)
        print(f"[+] IP address dari {hostname} adalah {ip}")
        return ip
    except socket.gaierror:
        print("[-] Gagal mendapatkan IP. Cek URL-nya.")
        return None

def port_scan(ip, ports=[21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]):
    print(f"[+] Memulai pemindaian port di IP: {ip}")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Timeout 1 detik
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[OPEN] Port {port} terbuka")
            s.close()
        except Exception as e:
            print(f"[ERROR] Tidak bisa memindai port {port}: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL website (contoh: https://example.com): ")
    ip = get_ip_from_url(url)
    if ip:
        port_scan(ip)
