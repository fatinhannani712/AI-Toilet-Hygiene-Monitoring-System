# AI-Toilet-Hygiene-Monitoring-System using CNN-LSTM
AI-powered IoT system for real-time toilet hygiene monitoring using a hybrid CNN-LSTM deep model and environmental sensors.

 **Project Status:** 🎓 Final Year Project | Portfolio Edition

An AI-powered IoT monitoring system developed as my Final Year Project at Universiti Putra Malaysia (UPM). The system predicts toilet hygiene conditions using real-time environmental sensor data and a hybrid CNN-LSTM deep learning model.

## Disclaimer

This repository is a portfolio edition of my Final Year Project and is shared for academic and professional portfolio purposes only.

To respect project confidentiality, collaborative contributions, and intellectual property, the complete source code, datasets, configuration files, credentials, and deployment resources are not included. Certain components have been simplified or omitted.

The contents of this repository are intended to demonstrate the system architecture, implementation approach, and the technical skills applied throughout the development of the project.


## Project Overview

Maintaining public toilet cleanliness through manual inspection is inefficient and time-consuming. This project integrates Internet of Things (IoT) and Artificial Intelligence (AI) technologies to monitor environmental conditions and predict toilet hygiene levels in real time.

The system collects data from multiple sensors, processes the information using a hybrid CNN-LSTM model, stores data in a cloud database, and visualizes results through an interactive dashboard.

---

## Key Features

- Real-time environmental monitoring
- Hybrid CNN-LSTM prediction model
- Streamlit dashboard
- Cloud database integration
- Telegram notification system
- IoT sensor network
- Historical data visualization

---

## Technologies Used

### Programming Languages

- Python
- C++

### Machine Learning

- TensorFlow
- Keras
- Scikit-learn
- Pandas
- NumPy

### IoT

- ESP32
- MQTT
- LoRaWAN
  <img width="700" height="550" alt="Screenshot 2025-07-13 133346" src="https://github.com/user-attachments/assets/e8943998-e91d-44e3-a960-8bc681015807" />



### Dashboard

- Streamlit 
<img width="1000" height="600" alt="Screenshot 2025-07-14 061056" src="https://github.com/user-attachments/assets/97f4f7c5-7a58-4a94-9b55-f1fa1331a630" />


### Database

- InfluxDB Cloud
<img width="500" height="400" alt="Screenshot 2025-07-12 155055" src="https://github.com/user-attachments/assets/e6f109b0-8adc-43a6-bbb1-cdc75d875c70" />


---

## Hardware Components

- ESP32
- BME680 Environmental Sensor
- MQ-135 Gas Sensor
- PIR Motion Sensor
- IR Counter Sensor

---

## Machine Learning

Model Architecture:

- Hybrid CNN-LSTM

<img width="808" height="420" alt="Screenshot 2025-07-13 161043" src="https://github.com/user-attachments/assets/e4b63ffa-d4b6-4ca4-b306-dc372af48406" />


Performance:

- R² Score: 0.90
- MAE: 0.05
- <img width="600" height="200" alt="Screenshot 2025-07-12 182604" src="https://github.com/user-attachments/assets/9cce8f77-b633-4c25-b777-df2694a32f41" />

- <img width="600" height="200" alt="Screenshot 2025-07-12 184952" src="https://github.com/user-attachments/assets/574b485d-0e6d-4e49-b669-02fb84e3ca89" />

---

## System Workflow

1. Environmental sensors collect data.
2. ESP32 transmits sensor readings.
3. Data is sent through MQTT and LoRaWAN.
4. Sensor data is stored in InfluxDB Cloud.
5. The CNN-LSTM model predicts toilet hygiene levels.
6. Predictions are displayed on the Streamlit dashboard.
7. Telegram notifications are sent when cleaning is required.

---

## Project Gallery

### Dashboard

<img width="1200" height="600" alt="Screenshot 2025-07-14 061056" src="https://github.com/user-attachments/assets/b5a66d35-f09f-4aba-96b5-559ded250924" />
<img width="1200" height="600" alt="Screenshot 2025-07-14 061007" src="https://github.com/user-attachments/assets/51fb96ad-3b3f-47dc-a409-76374b4f4f66" />
<img width="1200" height="600" alt="Screenshot 2025-07-14 061336" src="https://github.com/user-attachments/assets/77464c5f-0077-451d-947e-db45753cc560" />



### System Architecture

<img width="1000" height="700" alt="Screenshot 2025-08-07 095428" src="https://github.com/user-attachments/assets/7343eb4c-6628-4a21-937b-0c695093b489" />

<img width="1000" height="600" alt="Screenshot 2025-07-12 172118" src="https://github.com/user-attachments/assets/c7d073a6-c201-4e8c-bc2b-8f85b226577c" />

### Hardware Setup
<img width="1200" height="600" alt="Screenshot 2025-07-12 231626" src="https://github.com/user-attachments/assets/7a102968-608e-452d-be64-d293e3233cb8" />!

<img width="900" height="600" alt="Screenshot 2025-07-14 082444" src="https://github.com/user-attachments/assets/935933e8-4a7f-4654-9756-a4c9a7fa5e33" />


---

## Skills Demonstrated

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Internet of Things (IoT)
- Data Analytics
- Python Programming
- Dashboard Development
- Cloud Database
- Embedded Systems

---

