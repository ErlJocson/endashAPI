from flask import jsonify, abort
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
    return


@app.route('/api/delete-card/<int:uid>', methods=['DELETE'])
def delete_card(uid):
    return


@app.route('/api/update-card/<int:uid>', methods=['PUT'])
def update_card(uid):
    return

