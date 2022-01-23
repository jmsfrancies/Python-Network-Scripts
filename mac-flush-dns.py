# file that clears the DNS cache for the MacOS
import os, subprocess

def main():
    os.system("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder")
main()