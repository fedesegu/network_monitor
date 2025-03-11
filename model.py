# Entrenamiento del modelo de detección de anomalías

from sklearn.ensemble import IsolationForest

def train_model(data):
    """
    Entrena un modelo Isolation Forest para detectar anomalías en el tráfico de red.
    :param data: DataFrame con características extraídas.
    :return: Modelo entrenado.
    """
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data[["length"]])  # Se puede ampliar con más características
    return model

def predict_anomalies(model, data):
    """
    Predice anomalías en el tráfico de red.
    :param model: Modelo entrenado.
    :param data: DataFrame con características extraídas.
    :return: DataFrame con predicciones.
    """
    data["anomaly"] = model.predict(data[["length"]])
    return data