from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/gallery/<int:post>")
def post(post):
    if(post == 1):
        src='img/hacker-man-0.png'
        title="Posing"
        msg="Casually posing with my super micro computer (ceramic paper weight)."
    elif(post == 2):
        src='img/hacker-man-1.png'
        title="Posing (serious)"
        msg="Time to pose for real and win the Halloween competition and score some babes."
    elif(post == 3):
        src='img/hacker-man-2.png'
        title="Asking for my Phone Back"
        msg="Paul (camera operator) was asked to hand over the phone. He refused. Tensions escalated. Combat all but ensured."
    elif(post == 4):
        src='img/hacker-man-3.png'
        title="Demanding for my Phone Back"
        msg="Paul (camera operator) would not give my phone back because he was having too much fun. This was serious business and hacker man could not handle the disrespect."
    else:
        src='img/question_mark.svg'
        title="Post not found!"
        msg="Uh oh!"
    return render_template("post.html", image=src, title=title,message=msg)

if __name__ == "__main__":
    print("\n--- Starting Server at http://127.0.0.1:5000 ---")
    app.run(debug=True)