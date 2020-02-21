from flask import Flask, render_template, request, url_for, redirect
from data import title, subtitle, description, departures, tours
import random

app = Flask(__name__)


def create_tours_on_page(tours_id_list, tours_dict=tours):
    tours_on_page = {}
    for tour_id in tours_id_list:
        tours_on_page[tour_id] = tours_dict[tour_id]
    return tours_on_page

@app.route('/')
def main():
    random_tours = random.sample(list(tours), 6)
    tours_on_page = create_tours_on_page(random_tours)
    return render_template('index.html', tours=tours_on_page, title=title, subtitle=subtitle, description=description,
                           departures=departures)

@app.route('/departure/<departure>')
def render_departure(departure):
    departure = departure
    if departure not in departures:
        return page_not_found(404)
    departure_page_title = 'Летим {}'.format(departures[departure])
    found_tours = []
    tours_price_values = []
    tours_number_of_nights = []
    for tour in tours:
        if departure == tours[tour]['departure']: found_tours.append(tour)
    tours_on_page = create_tours_on_page(found_tours)
    for tour in tours_on_page:
        tours_price_values.append(tours_on_page[tour]['price'])
        tours_number_of_nights.append(tours_on_page[tour]['nights'])
    return render_template('departure.html', title=title, departures=departures,
                       departure_page_title=departure_page_title, tours=tours_on_page,
                       tours_price=tours_price_values, tours_nights=tours_number_of_nights)

@app.route('/tour/<tour_id>')
def render_tour(tour_id='1'):
    tour_id = int(tour_id)
    if tour_id not in tours:
        return page_not_found(404)
    tour_title = tours[tour_id]['title']
    tour_picture = tours[tour_id]['picture']
    tour_description = tours[tour_id]['description']
    tour_price_msg = 'Купить тур за {}'.format(tours[tour_id]['price'])
    tour_text = None
    for departure in departures:
        if departure == tours[tour_id]['departure']:
            tour_text = '{country_to} {country_from} {night_number} ночей'.format(
                country_to=tours[tour_id]['country'],
                country_from=departures[tours[tour_id]['departure']],
                night_number=tours[tour_id]['nights'])
    return render_template('tour.html', tour_title=tour_title, tour_text=tour_text, tour_picture=tour_picture,
                           tour_description=tour_description, tour_price_msg=tour_price_msg, title=title,
                           departures=departures)

@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'

if __name__ == '__main__':
    app.run()
