from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

appointments = []


@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()

    appointment = {
        "id": len(appointments) + 1,
        "patient_id": data["patient_id"],
        "doctor_id": data["doctor_id"],
        "date": data["date"],
        "time": data["time"]
    }

    appointments.append(appointment)

    return jsonify(appointment), 201


@app.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify(appointments)


@app.route("/")
def home():
    return jsonify({
        "service": "Appointment Service",
        "status": "running"
    })


@app.route("/appointment-details/<int:patient_id>/<int:doctor_id>", methods=["GET"])
def get_appointment_details(patient_id, doctor_id):
    patient_response = requests.get(
        f"http://patient-container:5001/patients/{patient_id}"
    )

    doctor_response = requests.get(
        f"http://doctor-container:5002/doctors/{doctor_id}"
    )

    return jsonify({
        "patient": patient_response.json(),
        "doctor": doctor_response.json()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)