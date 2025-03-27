from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login
from flask_login import current_user
from . import model
from . import db
from datetime import date, timedelta

bp = Blueprint("manager", __name__)

@bp.route("/schedule")
@flask_login.login_required
def schedule():
    projections, num_results = manager_reservations_auxiliar()
    return render_template("manager_schedule.html", packed=zip(projections, num_results), projections=projections)

def manager_reservations_auxiliar():
    current_day = date.today()
    future = current_day + timedelta(weeks=1)
    past = current_day - timedelta(weeks=1)
    projections = model.Projection.query.filter(model.Projection.day <= future, model.Projection.day >= past).order_by(model.Projection.day.asc(), model.Projection.time.asc()).all()
    num_results = []
    for proj in projections:
        num_results.append(proj.screen.num_total_seats - compute_reserved_seats(proj.id))
    return projections, num_results

def compute_reserved_seats(id):
    projection = model.Projection.query.filter(model.Projection.id == id).one()
    sum_result = db.session.query(
        db.func.sum(model.Reservation.num_seats).label('reserved')
    ).filter(
        model.Reservation.projection == projection
    ).one()
    num_reserved_seats = sum_result.reserved if sum_result.reserved else 0
    num_free_seats = projection.screen.num_total_seats - num_reserved_seats
    return num_free_seats
