from flask import Flask, render_template
from coding_projects import PROJECTS
from works_list import PIECE_CATEGORIES

project_classes = ["project-even", "project-odd"]


app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html', piece_categories=PIECE_CATEGORIES)

@app.route('/coding')
def portfolio():
    return render_template('projects.html', projects=list(PROJECTS.values()),
    project_classes=project_classes)

@app.route('/discord')
def score():
    return render_template('score.html')

@app.route('/discore_part')
def part():
    return render_template('for_performers.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

if __name__ == '__main__':
   app.run(debug=True)
