import pandas as pd

def extract_features(packets):
    """
    Extrae características relevantes de los paquetes capturados.
    :param packets: Lista de paquetes capturados.
    :return: DataFrame con características extraídas.
    """
    features = []
    
    for packet in packets:
        try:
            features.append({
                "timestamp": packet.sniff_time,
                "length": int(packet.length),
                "protocol": packet.highest_layer,
                "src_ip": packet.ip.src if hasattr(packet, 'ip') else None,
                "dst_ip": packet.ip.dst if hasattr(packet, 'ip') else None,
                "src_port": packet.tcp.srcport if hasattr(packet, 'tcp') else None,
                "dst_port": packet.tcp.dstport if hasattr(packet, 'tcp') else None,
            })
        except AttributeError:
            continue
    
    return pd.DataFrame(features)