import os

from flask import Flask, request, render_template, jsonify

from flask_socketio import SocketIO, emit, send, leave_room, join_room

from flask_sqlalchemy import SQLAlchemy

from flask_session import Session

from flask_mail import Mail, Message

# Email settings!

app = Flask(__name__, template_folder="./templates")

socketio = SocketIO(app)



mail_settings = {

"MAIL_SERVER": "smtp.gmail.com",
"MAIL_PORT" : 465,
"MAIL_USE_TLS" : False,
"MAIL_USE_SSL" : True,
"MAIL_USERNAME" : "olusegunpopoola4real@gmail.com",
"MAIL_PASSWORD" : "prayer1020!",
"MAIL_DEFAULT_SENDER" : "olusegunpopoola4real@gmail.com"

}

app.config.update(mail_settings)
mail = Mail(app)

app.config["SQLALCHEMY_DATABASE_URI"] = ""
app.config["SECRET_KEY"] = "skjgbsku thgvsothgi ghi tgoishgohstoiughoug hghdfoghsiutgfiskghgbvsfk"
app.config["SQLACLHEMY_TRACK_MODIFICATION"] = False


@app.route("/")
def mailss():
    return render_template("email.html")


@app.route("/send", methods = ["POST", "GET"])
def send():
    if request.method == "POST":
        Email = request.form.get("Email")
        msg = Message (
        subject = "Welcome to DesignPro!",
        recipients = [Email],
        body = "This is a email i sent using python and Flask",
        html = render_template("index.html")
        )
        mail.send(msg)
        return render_template("success.html")
    else:
        return "An error occured!"
#@app.route("/bulk_send", methods=["POST", "GET"])
#def bulk_send():
#    with mail.connect() as conn:
#    for user in users:
#        message = '...'
#        subject = "hello, %s" % user.name
#        msg = Message(recipients=[user.email],
#                      body=message,
#                      subject=subject)
#        conn.send(msg)
@app.route("/start", methods=["POST", "GET"])
def start():
    return render_template("test_chat.html")
#@app.route("/done", methods=["POST", "GET"])
#def sd():
#    FullName = request.form.get("Name")
#    Commented = request.form.get("name")
#    @socketio.on("responses")
#    def commented(FullName, Commented):
#        print("recieved!")
#        emit("Commenteds", FullName, Commented)
#    return render_template("test_chat.html", FullName=FullName, Commented=Commented)


@socketio.on("my event")
def sends(data):
    print('recieved message: ' + str(data))
    emit("response", data)
@socketio.on("responses")
def commented(FullName, Commented):
    print(str(FullName), str(Commented))
    emit("Commenteds", FullName, Commented)
socketio.run(app)
app.run()
