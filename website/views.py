from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/more')
def more():
    return render_template("more.html")

@views.route('/team')
def team():
    return render_template("team.html")

@views.route('/contact')
def route():
    return render_template("contact.html")

@views.route('/quiz')
def quiz():
    return render_template("quiz.html")

@views.route('/secret')
def secret():
    return render_template("secret.html")

@views.route('/rule1')
def rule1():
    return render_template('rule1.html')

@views.route('/rule2')
def rule2():
    return render_template('rule2.html')

@views.route('/rule3')
def rule3():
    return render_template('rule3.html')

@views.route('/rule4')
def rule4():
    return render_template('rule4.html')

@views.route('/rule5')
def rule5():
    return render_template('rule5.html')

@views.route('/rule6')
def rule6():
    return render_template('rule6.html')

@views.route('/rule7')
def rule7():
    return render_template('rule7.html')

@views.route('/rule8')
def rule8():
    return render_template('rule8.html')
    