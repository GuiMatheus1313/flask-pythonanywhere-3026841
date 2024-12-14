from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db #está voltando duas pastas
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #...código inutil
        return redirect(url_for('main.index'))
    return render_template('formularioTeste.html', form = form, name = session.get('name'), checkemail = session.get('checkemail'), pessoa = False)