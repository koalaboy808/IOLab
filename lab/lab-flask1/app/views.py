from app import myapp
from flask import request,render_template

@myapp.route('/')
@myapp.route('/index')
def index():
    # print "This is a log ..comes on your console"
    # return "Hello  - this the page for your form !!"
    return render_template("index.html");
@myapp.route('/submitform', methods=['GET','POST'])
def shitty():
    # print "This is a log ..comes on your console"
    # return "Hello  - this the page for your form !!"
    # return "rendered!"
    

    f = open('workfile', 'w')
    name=request.args.get('name')
    email=request.args.get('email')
    f.write("my name is " + name + ", and I like my email: " + email)

    return "your name sucks, " + name + " just like your stupid " + email
