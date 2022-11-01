from flask import Flask, render_template, redirect
import scrape

app = Flask(__name__, static_folder = "assets")


new_papers = []

@app.route("/")
def index():
    return render_template("index.html", new_papers = new_papers)


@app.route("/scrape")
def scraper():
    new_papers = scrape.scrape()
    
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
