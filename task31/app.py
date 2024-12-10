from flask import request, render_template, redirect, url_for
from task31_model import User, db, app

@app.route("/")
def site_():
    return redirect(url_for('cv'))

@app.route("/cv")
def cv():
    user = User.query.all()
    return render_template('cv.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)