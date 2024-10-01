from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
@app.route("/page2")
def render_page2():
    first = request.args['first'] 
    last = request.args['last']
    city = request.args['city']
    adress = request.args['adress']
    pnum = request.args['pnum']
    email = request.args['email']
    return render_template('page2.html', response1 = first, response2 = last, response3 = city, response4 = adress, response5 = pnum, response6 = email)
if __name__=="__main__":
    app.run(debug=False)
