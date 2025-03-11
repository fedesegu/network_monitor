from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

def train_model(data):
    """
    Entrena un modelo Isolation Forest para detectar anomalías.
    """
    # Convertir variables categóricas a numéricas
    label_enc = LabelEncoder()
    data["protocol"] = label_enc.fit_transform(data["protocol"].astype(str))
    
    # Seleccionar características relevantes
    features = ["length", "time_diff", "protocol"]
    
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data[features])
    
    return model

def predict_anomalies(model, data):
    """
    Predice anomalías usando el modelo entrenado.
    """
    features = ["length", "time_diff", "protocol"]
    data["anomaly"] = model.predict(data[features])
    
    # Convertir -1 a 1 para anomalías
    data["anomaly"] = data["anomaly"].apply(lambda x: 1 if x == -1 else 0)
    
    return data