from flask import Flask, render_template, request, url_for, redirect
from data import title, subtitle, description, departures, tours
import random

app = Flask(__name__)


@app.route('/')
def main():
    random_tours = random.sample(list(tours), 6)
    tours_on_page = {}
    for tour in random_tours:
        tours_on_page[tour] = tours[tour]
    return render_template('index.html', tours=tours_on_page, title=title, subtitle=subtitle, description=description,
                           departures=departures)


@app.route('/departure/<departure>')
def render_departure(departure):
    departure = departure
    departure_link = '/departure/{}'.format(departure)
    return render_template('departure.html', title=title, departures=departures, link=departure_link)


@app.route('/tour/<tour_id>')
def render_tour(tour_id='1'):
    tour_id = int(tour_id)
    if tour_id in tours:
        for tour in tours:
            if tour == tour_id:
                tour_title = tours[tour]['title']
                for departure in departures:
                    if departure == tours[tour]['departure']:
                        tour_text = '{country_to} {country_from} {night_number} ночей'.format(
                            country_to=tours[tour]['country'],
                            country_from=departures[tours[tour]['departure']],
                            night_number=tours[tour]['nights'])
                tour_picture = tours[tour]['picture']
                tour_description = tours[tour]['description']
                tour_price_msg = 'Купить тур за {}'.format(tours[tour]['price'])
    else: return page_not_found(404)

    return render_template('tour.html', tour_title=tour_title, tour_text=tour_text, tour_picture=tour_picture,
                           tour_description=tour_description, tour_price_msg=tour_price_msg, title=title,
                           departures=departures)


@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'


if __name__ == '__main__':
    app.run()
