import pandas as pd


def extract_features(packets):
    """
    Extrae características clave de los paquetes.
    """
    features = []
    prev_time = None  # Para calcular la diferencia de tiempo entre paquetes
    
    for packet in packets:
        try:
            timestamp = packet.sniff_time
            time_diff = (timestamp - prev_time).total_seconds() if prev_time else 0
            prev_time = timestamp
            
            features.append({
                "timestamp": timestamp,
                "length": int(packet.length),
                "protocol": packet.highest_layer,
                "src_ip": packet.ip.src if hasattr(packet, 'ip') else None,
                "dst_ip": packet.ip.dst if hasattr(packet, 'ip') else None,
                "src_port": int(packet.tcp.srcport) if hasattr(packet, 'tcp') else None,
                "dst_port": int(packet.tcp.dstport) if hasattr(packet, 'tcp') else None,
                "time_diff": time_diff,  # Diferencia de tiempo entre paquetes
            })
        except AttributeError:
            continue
    
    return pd.DataFrame(features)