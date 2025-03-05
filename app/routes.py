from flask import jsonify, abort, request
from . import app, db
from .models import Cards


@app.route('/api/all-cards', methods=['GET'])
def get_cards():
    cards = db.session.execute(db.select(Cards)).scalars().all()
    return jsonify([card.to_dict() for card in cards])


@app.route('/api/one-card/<int:uid>', methods=['GET'])
def get_one_card(uid):
    card = db.session.execute(db.select(Cards).filter_by(uid=uid)).scalar_one_or_none()

    if card is None:
        abort(404, description = "Card not found")

    return jsonify(card.to_dict())


@app.route('/api/add-card', methods=['POST'])
def add_card():
    if "order" not in request.form or "name" not in request.form or "link" not in request.form:
        return jsonify({"Error": "Incomplete data"}), 400
    
    order = request.form["order"]
    name = request.form["name"]
    link = request.form["link"]
    icon = request.files["icon"] 
    video = request.files["video"]

    if not icon or not video:
        return jsonify({"Error": "Missing file uploads"}), 400

    icon_data = icon.read()
    video_data = video.read()

    new_card = Cards(
        order=order,
        name=name,
        link=link,
        icon=icon_data,
        video=video_data
    )

    db.session.add(new_card)
    db.session.commit()
    
    return jsonify({"Message": "New Card is added"})


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
    data = request.get_json()

    if not data:
        return jsonify({"Error": "No data provided"})

    card = "" # TODO: filter the card

    if not card:
        return jsonify({"Error": "Card does not exist"})
    
    # TODO: update the card from here


    return jsonify(
            {
                "Message":"Card updated successfully",
                "card": data
            }
        )