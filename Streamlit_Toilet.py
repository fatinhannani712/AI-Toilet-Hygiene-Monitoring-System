# ========================================
# Real-Time Toilet Hygiene Prediction (Dense Model, No Buffer)
# ========================================

import streamlit as st
import numpy as np
import paho.mqtt.client as mqtt
import threading
import time
import joblib
from tensorflow.keras.models import load_model

# ----------------------------
# MQTT Config
# ----------------------------
mqtt_broker = "134.209.100.187"
mqtt_port = 1883
topics = {
    "ammonia": "esp32/BME680/PPM1",
    "temperature": "esp32/BME680/temperature1",
    "humidity": "esp32/BME680/humidity1",
    "iaq": "esp32/BME680/iaq1",
    "co2": "esp32/BME680/co21"
}

latest_data = {key: None for key in topics}

# ----------------------------
# Load Model + Tools
# ----------------------------
model = load_model("dense_multitask_cleanliness_forecast.h5", compile=False)
scaler_x = joblib.load("input_scaler.save")
scaler_y = joblib.load("sensor_scaler.save")
label_encoder = joblib.load("label_encoder.save")

# ----------------------------
# MQTT Setup
# ----------------------------
def on_connect(client, userdata, flags, rc):
    for topic in topics.values():
        client.subscribe(topic)

def on_message(client, userdata, msg):
    for key, topic in topics.items():
        if msg.topic == topic:
            try:
                latest_data[key] = float(msg.payload.decode())
            except:
                latest_data[key] = None

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, mqtt_port, 60)

mqtt_thread = threading.Thread(target=client.loop_forever)
mqtt_thread.start()

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Real-Time Toilet Hygiene", layout="wide")
st.title("🚽 Real-Time Toilet Hygiene Monitoring (Dense Model)")

col1, col2 = st.columns(2)

while True:
    with col1:
        st.subheader("📡 Live Sensor Values (MQTT)")
        for key, value in latest_data.items():
            st.metric(label=key.upper(), value=value if value is not None else "Waiting...")

    if all(v is not None for v in latest_data.values()):
        # Prepare input
        input_data = np.array([[latest_data["ammonia"],
                                latest_data["temperature"],
                                latest_data["humidity"],
                                latest_data["iaq"],
                                latest_data["co2"]]])
        scaled_input = scaler_x.transform(input_data)

        # Predict
        class_pred, future_sensor_scaled = model.predict(scaled_input)
        predicted_class_index = np.argmax(class_pred[0])
        predicted_label = label_encoder.inverse_transform([predicted_class_index])[0]
        confidence = float(np.max(class_pred[0]))

        # Forecast future sensor
        future_sensor = scaler_y.inverse_transform(future_sensor_scaled)[0]

        with col2:
            st.subheader("🧠 ML Prediction Output")
            st.metric("Cleanliness Status", f"{predicted_label} ✅")
            st.progress(confidence)
            st.text(f"Confidence: {confidence:.2f}")

            st.subheader("📈 Forecasted Sensor Values (Next 1 Hour)")
            st.write(f"Ammonia      : {future_sensor[0]:.2f} ppm")
            st.write(f"Temperature  : {future_sensor[1]:.2f} °C")
            st.write(f"Humidity     : {future_sensor[2]:.2f} %")
            st.write(f"IAQ          : {future_sensor[3]:.2f}")
            st.write(f"CO₂          : {future_sensor[4]:.2f} ppm")
    else:
        with col2:
            st.warning("Waiting for full sensor data from MQTT...")

    time.sleep(3)
    st.experimental_rerun()
