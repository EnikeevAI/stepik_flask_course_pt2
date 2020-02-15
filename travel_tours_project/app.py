from flask import Flask


app = Flask(__name__)

@app.route('/')
def main():
    return 'main page'

@app.route('/departure/<departure>')
def departure(departure):
    return 'departure page'

@app.route('/tour/<tour_id>')
def tour(tour_id=1):
    return 'tour page'

@app.errorhandler(404)
def page_not_found(error):
    return 'Такой страницы нет'

if __name__ == '__main__':
    app.run()