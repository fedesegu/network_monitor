# capture.py
# Captura de tráfico con PyShark

import pyshark

def capture_traffic(interface="Wi-Fi", count=100):
    """
    Captura tráfico de red en la interfaz especificada.
    :param interface: Nombre de la interfaz de red.
    :param count: Número de paquetes a capturar.
    :return: Lista de paquetes capturados o lista vacía si falla.
    """
    print(f"Capturando {count} paquetes en la interfaz {interface}...")
    try:
        capture = pyshark.LiveCapture(interface=interface)
        packets = [packet for packet in capture.sniff_continuously(packet_count=count)]
        print(f"Captura finalizada. {len(packets)} paquetes capturados.")
        return packets
    except Exception as e:
        print(f"Error capturando tráfico: {e}")
        return []  # Devuelve una lista vacía en caso de error