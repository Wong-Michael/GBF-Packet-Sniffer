import scapy.all as scapy
from scapy.layers import http


def sniff(interface): 
    scapy.sniff(iface=interface, store=False , prn= process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPResponse):
        print(packet[http.HTTPResponse].payload)

def main():
    sniff('Ethernet 6')

if __name__ == "__main__":
    main()