from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Ticket

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/book', methods=['POST'])
@login_required
def book():
    name = request.form['name']
    route = request.form['route']
    ticket = Ticket(name=name, route=route, user_id=current_user.id)
    db.session.add(ticket)
    db.session.commit()
    return "Booking successful!"

@routes.route('/admin')
@login_required
def admin():
    if current_user.username != 'admin':
        return redirect(url_for('routes.index'))
    tickets = Ticket.query.all()
    return render_template('admin.html', tickets=tickets)
