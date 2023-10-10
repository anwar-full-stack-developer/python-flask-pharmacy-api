#  hospital_api/resource.py

from flask import request, make_response, abort
from flask_restful import Resource
from app_init import db
from .models import Medicine, medicineListSchema, medicineSchema

class MedicineListResource(Resource):
    def get(self):
        list = Medicine.query.all()
        return medicineListSchema.dump(list)
    
    def post(self): 
        data = request.get_json()
        ndata = medicineSchema.load(data)
        db.session.add(ndata)
        db.session.commit()
        return medicineSchema.dump(ndata), 201


class MedicineResource(Resource):
    def get(self, id):
        item = Medicine.query.get(id)
        if item is not None:
            return medicineSchema.dump(item)
        else:
            abort(404, f"Medicine with id {id} not found")

    def delete(self, id):
        item = Medicine.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return make_response(f"{id} successfully deleted", 200)
        else:
            abort(404, f"Medicine with id {id} not found")


    def put(self, id):
        xdata = Medicine.query.filter(Medicine.id == id).one_or_none()
        if xdata:
            data = medicineSchema.load(request.get_json())
            xdata.name = data.name
            xdata.image = data.image
            xdata.unit = data.unit
            xdata.details = data.details
            xdata.company = data.company
            xdata.gener_type = data.gener_type
            xdata.pot_type = data.pot_type
            db.session.merge(xdata)
            db.session.commit()
            return medicineSchema.dump(xdata), 201
        else:
            abort(404, f"Medicine with id {id} not found")
