from flask_restful import Resource
from model.database import Appointment

class AppointmentResource(Resource):
    def get(self, id):
        # Query appointments for the given mechanic ID
        appointments = Appointment.query.filter_by(mechanic_id=id).all()
        print(appointments)
        if not appointments:
            return {"error": "No appointments found for this mechanic"}, 404

        # Extract dates from appointments
        booked_dates = [
            appointment.date.strftime('%Y-%m-%d-%H-%M')
            for appointment in appointments
        ]
        return {"dates": booked_dates}