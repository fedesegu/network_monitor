# Integración de captura, extracción de características y detección de anomalías

from capture import capture_traffic
from features import extract_features
from model import train_model, predict_anomalies

def main():
    """
    Función principal para capturar tráfico, extraer características,
    entrenar el modelo y predecir anomalías.
    """
    interface = "Wi-Fi"  # Cambiar según la interfaz disponible
    count = 110
    
    packets = capture_traffic(interface, count)
    data = extract_features(packets)
    
    if data.empty:
        print("No se capturaron paquetes válidos.")
        return
    
    model = train_model(data)
    result = predict_anomalies(model, data)
    
    print("Detección de anomalías completada:")
    print(result)

if __name__ == "__main__":
    main()