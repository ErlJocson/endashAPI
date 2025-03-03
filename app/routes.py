from flask import jsonify, abort, request
from . import app, db
from .models import Cards


@app.route('/api/all-cards', methods=['GET'])
def get_cards():
    cards = db.session.execute(db.select(Cards).order_by(Cards.order)).scalars().all()
    return jsonify([card.to_dict() for card in cards])


@app.route('/api/one-card/<int:uid>', methods=['GET'])
def get_one_card(uid):
    card = db.session.execute(db.select(Cards).filter_by(uid=uid)).scalar_one_or_none()

    if card is None:
        abort(404, description = "Card not found")

    return jsonify(card.to_dict())


@app.route('/api/add-card', methods=['POST'])
def add_card():
    if request.method == "POST":
        data = request.get_json()

        if not data:
            return jsonify({"Error":"Data are missing"})

        if "order" not in data or "name" not in data or "link" not in data or "icon" not in data or "video" not in data:
            return jsonify({"Error":"Incomplete data"})
        
        new_card = Cards(
            order   = data['order'],
            name    = data['name'],
            link    = data['link'],
            icon    = data['icon'],
            video   = data['video']
        )

        db.session.add(new_card)
        db.session.commit()
        return jsonify({"Message":"New Card is added"})


@app.route('/api/delete-card/<int:uid>', methods=['DELETE'])
def delete_card(uid):
    card = Cards.query.filter_by(uid=uid).first()
    if card:
        db.session.delete(card)
        db.session.commit()
        return jsonify({"Message":"Card Deleted Successfully"})
    return jsonify({"Error":"Card Not Found"})


@app.route('/api/update-card/<int:uid>', methods=['PUT'])
def update_card(uid):
    return

