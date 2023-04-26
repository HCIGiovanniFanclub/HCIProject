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
def quiz():
    return render_template("quiz.html", user=current_user)

@views.route('/end')
def end():
    return render_template("end.html", user=current_user)

@views.route('/hiscores')
def hiscores():
    return render_template("hiscores.html", user=current_user)

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

@views.route('/glossary')
def glossary():
    return render_template('glossary.html', user=current_user)

@views.route('/rule1bad')
def rule1bad():
    return render_template('rule1bad.html', user=current_user)

@views.route('/rule2bad')
def rule2bad():
    return render_template('rule2bad.html', user=current_user)

@views.route('/rule3bad')
def rule3bad():
    return render_template('rule3bad.html', user=current_user)

@views.route('/rule4bad')
def rule4bad():
    return render_template('rule4bad.html', user=current_user)

@views.route('/rule5bad')
def rule5bad():
    return render_template('rule5bad.html', user=current_user)

@views.route('/rule6bad')
def rule6bad():
    return render_template('rule6bad.html', user=current_user)
   
@views.route('/rule7bad')
def rule7bad():
    return render_template('rule7bad.html', user=current_user)

@views.route('/rule8bad')
def rule8bad():
    return render_template('rule8bad.html', user=current_user)

    