
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

### start with python main.py
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:z0h3T0WC84KLoN0I@tonelessly-contiguous-terrapin.data-1.use1.tembo.io:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

### Models

class NecktieCategory(db.Model):
    __tablename__ = 'necktie_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class NecktieDistrict(db.Model):
    __tablename__ = 'necktie_districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class NecktieDoctor(db.Model):
    __tablename__ = 'necktie_doctors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('necktie_categories.id'), nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey('necktie_districts.id'), nullable=False)
    price_range_low = db.Column(db.Integer)
    price_range_high = db.Column(db.Integer)
    languages = db.Column(db.JSON)
    bio = db.Column(db.Text)

    category = db.relationship('NecktieCategory')
    district = db.relationship('NecktieDistrict')


### Routes

@app.route('/doctor', methods=['POST'])
def create_doctor():
    data = request.get_json()

    doctor = NecktieDoctor(
        first_name=data['first_name'],
        last_name=data['last_name'],
        category_id=data['category_id'],
        district_id=data['district_id'],
        price_range_low=data.get('price_range_low'),
        price_range_high=data.get('price_range_high'),
        languages=data.get('languages', []),
        bio=data.get('bio', '')
    )
    db.session.add(doctor)
    db.session.commit()

    return jsonify({"message": "Doctor created", "id": doctor.id}), 201


@app.route('/doctor/<int:id>', methods=['GET'])
def get_doctor(id):
    doctor = NecktieDoctor.query.get_or_404(id)
    return jsonify({
        "id": doctor.id,
        "first_name": doctor.first_name,
        "last_name": doctor.last_name,
        "category": doctor.category.name,
        "district": doctor.district.name,
        "price_range_low": doctor.price_range_low,
        "price_range_high": doctor.price_range_high,
        "languages": doctor.languages,
        "bio": doctor.bio
    })


@app.route('/doctor', methods=['GET'])
def list_doctors():
    query = NecktieDoctor.query

    # Optional filters
    district = request.args.get('district')
    category = request.args.get('category')
    price_min = request.args.get('price_min', type=int)
    price_max = request.args.get('price_max', type=int)
    language = request.args.get('language')

    if district:
        query = query.join(NecktieDistrict).filter(NecktieDistrict.name.ilike(f'%{district}%'))
    if category:
        query = query.join(NecktieCategory).filter(NecktieCategory.name.ilike(f'%{category}%'))
    if price_min is not None:
        query = query.filter(NecktieDoctor.price_range_low >= price_min)
    if price_max is not None:
        query = query.filter(NecktieDoctor.price_range_high <= price_max)
    ## far cannot fix problem with jsonb with languages. does not exists on stackoverflow
    ##if language:
    ##
    ##    query = query.filter(NecktieDoctor.languages.contains([language]))

    doctors = query.all()

    return jsonify([
        {
            "id": d.id,
            "first_name": d.first_name,
            "last_name": d.last_name,
            "category": d.category.name,
            "district": d.district.name,
            "price_range_low": d.price_range_low,
            "price_range_high": d.price_range_high,
            "languages": d.languages
        } for d in doctors
    ])


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Necktie Doctor API!"})


if __name__ == '__main__':
    app.run(debug=True)