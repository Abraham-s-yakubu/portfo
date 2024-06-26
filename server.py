from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_section>")
def html_page(page_section=None):
    return render_template(page_section)


def write_to_file(data):
    with open("Database.txt", mode="a") as file_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = file_database.write(f"\n email:{email}, subject:{
                                   subject}, message:{message}")


def write_to_csv(data):
    with open("database.csv", newline='', mode="a") as csv_database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            csv_database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "did not save to database"
    else:
        return "somethiing went wrong try again"
