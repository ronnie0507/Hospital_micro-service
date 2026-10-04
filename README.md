# Hospital Microservices

A containerized hospital management application developed using three independent microservices: Patient Service, Doctor Service, and Appointment Service.

The project demonstrates microservice development, Docker containerization, service-to-service communication, workload testing, resource monitoring, and performance analysis under different workload levels.

## 2. Objectives

- Develop three independent microservices.
- Implement REST APIs for the services.
- Containerize each microservice using Docker.
- Establish communication between the services.
- Deploy the services as separate containers.
- Generate different workload levels.
- Measure response time and throughput.
- Monitor CPU and memory utilization.
- Analyze application performance under increasing concurrency.

  ## 3. System Architecture

                         Client
                           |
                           v
                +----------------------+
                | Appointment Service  |
                |      Port 5003       |
                +----------+-----------+
                           |
                 +---------+---------+
                 |                   |
                 v                   v
        +----------------+   +----------------+
        | Patient Service|   | Doctor Service |
        |    Port 5001   |   |    Port 5002   |
        +----------------+   +----------------+

## 4. Microservices

### Patient Service

- **Port:** 5001
- **Purpose:** Manages patient information.
- **Technology:** Flask
- **Docker Container:** `patient-container`

### Doctor Service

- **Port:** 5002
- **Purpose:** Manages doctor information.
- **Technology:** Flask
- **Docker Container:** `doctor-container`

### Appointment Service

- **Port:** 5003
- **Purpose:** Manages appointments and communicates with the Patient and Doctor Services.
- **Technology:** Flask
- **Docker Container:** `appointment-container`

## 5. Technologies Used

- **Python** — Microservice development
- **Flask** — REST API development
- **Docker** — Containerization and deployment
- **Docker Network** — Communication between microservices
- **Ubuntu WSL** — Workload testing environment
- **wrk** — Load and workload testing

## 6. Docker Deployment

Each microservice was containerized and run as a separate Docker container.

### Docker Images

- `patient-service`
- `doctor-service`
- `appointment-service`

### Docker Containers

- `patient-container`
- `doctor-container`
- `appointment-container`

### Docker Network

The three containers were connected using the Docker network:

`hospital-network`

The Docker network allows the services to communicate with each other using their container names.

## 7. Service-to-Service Communication

The communication was tested using the following endpoint:

```text
http://127.0.0.1:5003/appointment-details/1/1
```

 Response
```text
{
  "doctor": {
    "available": true,
    "id": 1,
    "name": "Dr. Kumar",
    "specialization": "Cardiology"
  },
  "patient": {
    "age": 25,
    "gender": "Male",
    "id": 1,
    "name": "Rahul"
  }
}

```

## 8. Workload Testing

The Appointment Service was selected for workload testing.

The `wrk` load-testing tool was used to generate different levels of concurrent requests.

Five workload levels were tested:

| Workload | Concurrent Requests |
|----------|---------------------|
| W1 | 1 |
| W2 | 2 |
| W3 | 4 |
| W4 | 8 |
| W5 | 16 |

Each workload was tested for 30 seconds.

The number of threads was kept at 1 while the number of concurrent requests was varied.
## 9. Performance Results

The workload tests produced the following results:

| Workload | Concurrent Requests | Average Response Time (ms) | Throughput (req/s) | Failed Requests |
|----------|---------------------|----------------------------|---------------------|-----------------|
| W1 | 1 | 1.97 | 487.03 | 1 |
| W2 | 2 | 3.65 | 535.38 | 0 |
| W3 | 4 | 8.38 | 472.42 | 0 |
| W4 | 8 | 15.31 | 518.83 | 0 |
| W5 | 16 | 29.39 | 542.11 | 0 |

## 10. Workload Test Results

### W1 and W2

![W1 and W2 Results](grahs/W1-W2.png)

### W3 and W4


![W3 and W4 Results](grahs/W3-W4.png)

### W5

![W5 Results](grahs/W5.png)

## 11. CPU and Memory Utilization

The resource utilization of all three containers was monitored using Docker Stats.

### CPU Utilization

![CPU Utilization](grahs/CPU_utilization.png)

### Memory Utilization

![Memory Utilization](grahs/Memory_utilization.png)

The observed resource utilization was:

| Service | CPU Utilization | Memory Utilization |
|---------|-----------------|--------------------|
| Appointment Service | 0.08% | 57.02 MiB |
| Doctor Service | 0.08% | 45.46 MiB |
| Patient Service | 0.07% | 58.23 MiB |

The resource measurements show that all three services operated with low CPU utilization and moderate memory usage during the observation.

## 12. Performance Analysis

The workload results were analyzed by comparing response time and throughput at different concurrency levels.

- Response time increased as the number of concurrent requests increased.
- The lowest response time was observed at W1 with 1.97 ms.
- At W5 with 16 concurrent requests, the response time increased to 29.39 ms.
- Throughput remained around 470–542 requests per second across the tested workloads.
- No request failures were observed from W2 to W5.
- The resource utilization of all three services remained low during the observation.

## 13. Conclusion

The hospital microservice application was successfully developed using three independent services and deployed using Docker containers.

The services communicated successfully through a Docker network. Workload testing with five concurrency levels showed that response time increased as concurrency increased, while throughput remained relatively stable.

The experiment also demonstrated how container resource utilization can be monitored and how application performance changes under different workloads.
