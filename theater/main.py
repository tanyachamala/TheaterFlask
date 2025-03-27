from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import current_user, login_required
from . import db
from .model import Movie, Projection

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    current_day = date.today()
    future = current_day + timedelta(weeks=1)
    nmovies = Movie.query.filter(Projection.day > current_day, Projection.day <= future).order_by(Projection.day.asc(), Projection.time.asc()).all()
    tmovies = Movie.query.filter(Projection.day == current_day).order_by(Projection.time.asc()).all()
    
    return render_template("main/index.html", next_projections=nmovies, today_projections=tmovies)

# Add more routes as needed
