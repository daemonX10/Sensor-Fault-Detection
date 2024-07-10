
# Sensor Fault Detection

This repository contains the source code for the Sensor Fault Detection system.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Sensor Fault Detection system is designed to monitor sensors and detect any faults. It uses advanced algorithms to ensure the accuracy and reliability of sensor data.

## Features

- Real-time sensor fault detection
- RESTful API for integrating with other systems
- Easy to deploy with Docker

## View the project
[video](https://drive.google.com/file/d/1yFZVNLQHuSQu5vOkE71K8dMvUH8G5rd4/view?usp=sharing)

<img src="./img/home page sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 2 sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 3 sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 4 sensor.png" alt="Your Image" width="1000" height="500")


<img src="./img/home page sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 2 sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 3 sensor.png" alt="Your Image" width="1000" height="500">
<img src="./img/page 4 sensor.png" alt="Your Image" width="1000" height="500">

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/daemonX10/Senser-Fault-Detection.git
   cd Senser-Fault-Detection
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```sh
   python app.py
   ```

4. **Using Docker:**
   ```sh
   docker build -t sensor-fault-detection .
   docker run -p 5000:5000 sensor-fault-detection
   ```

## Usage

The application provides a RESTful API to interact with the sensor fault detection system. Once the application is running, you can access the API endpoints at `http://127.0.0.1:5000`.

## API Endpoints

### Get System Status

- **URL:** `/status`
- **Method:** `GET`
- **Description:** Returns the status of the sensor fault detection system.
- **Response:**
  ```json
  {
      "status": {
          "system": "operational",
          "faults_detected": false
      }
  }
  ```

### Credit : Damodar Yadav (damodarryadav@gmail.com) @daemonX10

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


