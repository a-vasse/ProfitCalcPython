from flask import Flask, g, request, render_template
app = Flask(__name__)

from decimal import Decimal
from calculator import calculate_net, currency_places

@app.route('/', methods=['GET','POST'])
def index():
    error = None
    result = None
    show_form = True

    if request.method == 'POST':
        try:
            result = calculate_net(request.form['revenue'], request.form['expenses'])
            show_form = False
        except ValueError as err:
            error = str(err)

    g.currency_places = currency_places
    return render_template('index.html', error=error, result=result, show_form=show_form)
