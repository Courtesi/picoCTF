import pyshark
import base64

# Load the pcap file
cap = pyshark.FileCapture('myNetworkTraffic.pcap')

# Iterate over each packet with retransmission
for pkt in cap:
    try:
        # Print timestamp and summary

        # If there's TCP payload
        if hasattr(pkt.tcp, 'payload'):
            payload_split = pkt.tcp.payload.split(":")
            #print(bytes.fromhex("".join(payload_split)))
            if payload_split[-1] == "3d" and payload_split[-2] == "3d":
                print(f"Time: {pkt.sniff_time}, Source: {pkt.ip.src}, Dest: {pkt.ip.dst}")
                print(f"TCP Seq: {pkt.tcp.seq}")

                decoded_str = base64.b64decode(bytes.fromhex("".join(payload_split))).decode("utf-8")
                print(decoded_str)
                print('-' * 40)
                print()
    except AttributeError as e:
        print(f"Skipping packet due to missing attribute: {e}")
