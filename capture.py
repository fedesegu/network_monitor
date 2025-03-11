# capture.py
# Captura de tráfico con PyShark

import pyshark

def capture_traffic(interface="eth0", count=100):
    """
    Captura tráfico de red en la interfaz especificada.
    :param interface: Nombre de la interfaz de red (por defecto "eth0").
    :param count: Número de paquetes a capturar.
    :return: Lista de paquetes capturados.
    """
    print(f"Capturando {count} paquetes en la interfaz {interface}...")
    capture = pyshark.LiveCapture(interface=interface)
    packets = []
    
    for packet in capture.sniff_continuously(packet_count=count):
        packets.append(packet)
    
    print(f"Captura finalizada. {len(packets)} paquetes capturados.")
    return packets