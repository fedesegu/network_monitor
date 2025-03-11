# capture.py
# Captura de tráfico con PyShark

import pyshark
import threading

def capture_traffic(interface="eth0", count=100, callback=None):
    """
    Captura tráfico de red y aplica un callback a cada paquete capturado.
    """
    print(f"Capturando {count} paquetes en la interfaz {interface}...")

    capture = pyshark.LiveCapture(interface=interface)

    def process_packet(packet):
        if callback:
            callback(packet)

    thread = threading.Thread(target=lambda: [process_packet(p) for p in capture.sniff_continuously(packet_count=count)])
    thread.start()
    thread.join()

    print(f"Captura finalizada.")