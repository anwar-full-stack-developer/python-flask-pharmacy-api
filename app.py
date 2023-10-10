import app_init
db=app_init.db
# do not use this
# app=app_init.connex_app
# use this ...
app=app_init.app
api = app_init.api


# Create the endpoints.
from pharmacy_api.resource import  MedicineGenerTypeListResource, MedicineGenerTypeResource
from pharmacy_api.pot_type_resource import MedicinePotTypeResource, MedicinePotTypeListResource
from pharmacy_api.company_resource import MedicineCompanyResource, MedicineCompanyListResource
from pharmacy_api.medicine_resource import Medicine, MedicineListResource, MedicineResource


# Pharmacy api
api.add_resource(MedicineGenerTypeListResource, '/pharmacy/geners')
api.add_resource(MedicineGenerTypeResource, '/pharmacy/gener/<id>')

api.add_resource(MedicinePotTypeListResource, '/pharmacy/pots')
api.add_resource(MedicinePotTypeResource, '/pharmacy/pot/<id>')

api.add_resource(MedicineCompanyListResource, '/pharmacy/companies')
api.add_resource(MedicineCompanyResource, '/pharmacy/company/<id>')

api.add_resource(MedicineListResource, '/pharmacy/medicines')
api.add_resource(MedicineResource, '/pharmacy/medicine/<id>')



if __name__ == '__main__':
    # Create the database tables.
    with app.app_context():
        db.create_all()
    # Start the Flask development web server.
    app.run(host="0.0.0.0", port=8000, debug=True)
