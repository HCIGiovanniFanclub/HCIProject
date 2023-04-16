from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/more')
def more():
    return render_template("more.html", user=current_user)

@views.route('/team')
def team():
    return render_template("team.html", user=current_user)

@views.route('/contact')
def route():
    return render_template("contact.html", user=current_user)

@views.route('/quiz')
@login_required
def quiz():
    return render_template("quiz.html", user=current_user)

@views.route('/secret')
@login_required
def secret():
    return render_template("secret.html", user=current_user)

@views.route('/rule1')
def rule1():
    return render_template('rule1.html', user=current_user)

@views.route('/rule2')
def rule2():
    return render_template('rule2.html', user=current_user)

@views.route('/rule3')
def rule3():
    return render_template('rule3.html', user=current_user)

@views.route('/rule4')
def rule4():
    return render_template('rule4.html', user=current_user)

@views.route('/rule5')
def rule5():
    return render_template('rule5.html', user=current_user)

@views.route('/rule6')
def rule6():
    return render_template('rule6.html', user=current_user)

@views.route('/rule7')
def rule7():
    return render_template('rule7.html', user=current_user)

@views.route('/rule8')
def rule8():
    return render_template('rule8.html', user=current_user)
    