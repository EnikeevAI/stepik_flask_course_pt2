from flask import Flask, render_template, request, url_for, redirect
from data import title, subtitle, description, departures, tours


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', title=title, subtitle=subtitle, description=description)

@app.route('/departure/<departure>')
def departure(departure):
    return render_template('departure.html')

@app.route('/tour/<tour_id>')
def tour(tour_id=1):
    return render_template('tour.html')

@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'

if __name__ == '__main__':
    app.run()