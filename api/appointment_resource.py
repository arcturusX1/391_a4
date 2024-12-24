from flask_restful import Resource, reqparse
from flask import jsonify, request, flash
from flask_wtf.csrf import validate_csrf
from sqlalchemy.exc import IntegrityError


from blueprints.forms import UserForm


from model.database import User, Appointment, db

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
    
    def post(self):
        #manual CSRF validation
        #data from js comes here. look for csrf token in headers
        csrf = None
        mechanic_id = None
        if 'X-CSRFToken' in request.headers:
            csrf = request.headers['X-CSRFToken']
        try:
            validate_csrf(csrf)
        except Exception as e:
            return {'error': 'Invalid CSRF' }, 400
        
        form_data = request.get_json()
        print(form_data)
        form = UserForm(data=request.get_json())
        print(form)

        if not form.validate():
            return {'error': 'Validation error', 'errors': form.errors}, 400
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        phone = form.phone.data
        car_license = form.car_license.data
        car_engine = form.car_engine.data
        date = form.date.data
        
        mechanic_id = request.get_json().get('mechanic_id')


        #add data to db
        try:
            user = User(first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            car_license=car_license,
            car_engine=car_engine)

            db.session.add(user)
            db.session.commit()
            
            #try to book appointment
            if mechanic_id is not None:
                # Retrieve user by phone
                user = User.query.filter_by(phone=phone).first()
                if not user:
                    return {'error': 'User not found'}, 404

                user_id = user.id

                try:
                    # Create appointment
                    appointment = Appointment(
                        user_id=user_id,
                        mechanic_id=mechanic_id,
                        date=date
                    )
                    db.session.add(appointment)
                    db.session.commit()
                    print(f"Appointment created for User ID {user_id} and Mechanic ID {mechanic_id}")
                except IntegrityError:
                    db.session.rollback()
                    return {'error': 'Duplicate appointment for this user and mechanic'}, 400
                except Exception as e:
                    db.session.rollback()
                    print(f'Error: {e}')
                    return {'error': 'Server error'}, 500
            else:
                print('No mechanic ID provided')

            
            print(f'added {first_name}{last_name}')
        
        except Exception as e:
            db.session.rollback()
            print(f"error: {e}")

        return {'message': 'success', 'data': {'first-name': first_name, 'last-name': last_name}}, 201