
from abc import ABC, abstractmethod


# Abstract Parent Class
class SecurityScanner(ABC):

    def __init__(self, scanner_name):
        self.scanner_name = scanner_name

    @abstractmethod
    def scan(self, target):
        pass

    def display_scanner(self):
        print(f"Scanner={self.scanner_name}")
        pass


# Child Class 1
class NetworkScanner(SecurityScanner):

    def scan(self, target):
        # Check whether target contains "suspicious"
        if "suspicious" in target.lower():
            print("Threat deteced network not safe")
        else:
            print("the network is safe")


# Child Class 2
class MalwareScanner(SecurityScanner):

    def scan(self, target):
        if ".exe" in target.lower():
            print("not safe")
        else:
            print("safe")


# Child Class 3
class PhishingScanner(SecurityScanner):

    def scan(self, target):
        if "fake" in target.lower():
            print("not safe")
        else:
            print("safe")


# Main Program

scanner1 = NetworkScanner("Network Scanner")
scanner2 = MalwareScanner("Malware Scanner")
scanner3 = PhishingScanner("Phishing Scanner")

scanners = [scanner1, scanner2, scanner3]

targets = [
    "suspicious_traffic",
    "unknown_file.exe",
    "https://example.com/fake-login"
]

for scanner, target in zip(scanners, targets):

    scanner.display_scanner()
    scanner.scan(target)
    print("-----------------------")
