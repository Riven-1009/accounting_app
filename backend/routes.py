from flask import Blueprint, request, jsonify
from models import db, Entry
from datetime import datetime

bp = Blueprint('api', __name__)

@bp.route('/entries', methods=['POST'])
def add_entry():
    data = request.json
    print('收到数据:', data)  # 调试用
    if not data:
        return jsonify({'error': '请求体为空或格式错误'}), 400
    # 其余代码...
    try:
        date_str = data.get('date', datetime.now().strftime('%Y-%m-%d'))
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        entry = Entry(
            type=data['type'],
            amount=data['amount'],
            category=data['category'],
            note=data.get('note', ''),
            date=date_obj
        )
        db.session.add(entry)
        db.session.commit()
        return jsonify({'message': 'Entry added'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@bp.route('/entries', methods=['GET'])
def get_entries():
    entries = Entry.query.all()
    return jsonify([{
        'id': e.id,
        'type': e.type,
        'amount': e.amount,
        'category': e.category,
        'note': e.note,
        'date': e.date
    } for e in entries])

@bp.route('/entries/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    data = request.json
    entry.type = data.get('type', entry.type)
    entry.amount = data.get('amount', entry.amount)
    entry.category = data.get('category', entry.category)
    entry.note = data.get('note', entry.note)
    entry.date = data.get('date', entry.date)
    db.session.commit()
    return jsonify({'message': 'Entry updated'})

@bp.route('/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entry deleted'})