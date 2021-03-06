from devjobs import app
from flask import render_template, session


@app.route('/c/search', methods=['GET'])
def c_search():
    from pojo import CompanyAuthBean
    bean = CompanyAuthBean()
    if not bean.verify_token(session["X-Auth-Token"]):
        session.clear()
        return render_template("companies/index.html")
    return render_template("companies/dashboard.html")
