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
    max_price, min_price, max_nights, min_nights = None, None, None, None
    count_tours = 0
    tour_id = 0
    tours_on_page = {}
    if departure not in departures:
        return page_not_found(404)
    departure_page_title = f'Летим {departures[departure]}'
    for tour in tours.values():
        tour_id += 1
        if departure == tour['departure']:
            count_tours += 1
            max_price = max(tour['price'], max_price) if max_price else tour['price']
            min_price = min(tour['price'], min_price) if min_price else tour['price']
            max_nights = max(tour['nights'], max_nights) if max_nights else tour['nights']
            min_nights = min(tour['nights'], min_nights) if min_nights else tour['nights']
            stats = {'count_tours': count_tours, 'max_price': max_price, 'min_price': min_price,
                     'max_nights': max_nights, 'min_nights': min_nights, }
            tours_on_page[tour_id] = tour
    return render_template('departure.html', departures=departures, departure_page_title=departure_page_title,
                           stats = stats, title=title,tours=tours_on_page)

@app.route('/tour/<tour_id>')
def render_tour(tour_id='1'):
    tour_id = int(tour_id)
    if tour_id not in tours:
        return page_not_found(404)
    return render_template('tour.html', tour=tours[tour_id], title=title, departures=departures)

@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'

if __name__ == '__main__':
    app.run()
