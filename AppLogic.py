import socket
import platform
import psutil
import wmi
import urllib.request


class AppLogic:
    @staticmethod
    def fetch_ipv4_info():
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        is_static = socket.gethostbyaddr(ip)
        interface = None
        if "Wi-Fi" in platform.platform():
            interface = "Wi-Fi"
        elif "Ethernet" in platform.platform():
            interface = "Ethernet"
        result = f"IPv4 Address: {ip}\nStatic: {is_static}\nNetwork Interface: {interface}"
        return result

    @staticmethod
    def check_proxy_info():
        proxy_handler = urllib.request.ProxyHandler()
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("http://www.google.com", timeout=5)
            is_proxy_enabled = True
        except Exception:
            is_proxy_enabled = False

        proxy_status = "Proxy is enabled" if is_proxy_enabled else "Proxy is disabled"
        return proxy_status

    @staticmethod
    def retrieve_system_info():
        os_version = platform.platform()
        os_architecture = platform.architecture()
        num_cores = psutil.cpu_count(logical=False)
        ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
        result = f"Operating System Version: {os_version}\nArchitecture: {os_architecture}\nCPU Cores: {num_cores}\nRAM: {ram} GB"
        return result

    @staticmethod
    def fetch_bios_info():
        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        result = f"BIOS Manufacturer: {bios.Manufacturer}\nBIOS Version: {bios.Version}\nBIOS Release Date: {bios.ReleaseDate}"
        return result

    @staticmethod
    def get_host_name():
        hostname = socket.gethostname()
        return f"Hostname: {hostname}"
