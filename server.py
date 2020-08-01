"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all.
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

PUPPIES = {'1': 'http://cdn1-www.dogtime.com/assets/uploads/gallery/30-impossibly-cute-puppies/impossibly-cute-puppy-2.jpg',
           '2': 'http://pictures.4ever.eu/data/download/animals/dogs/husky-puppies,-two-puppies-147859.jpg',
           '3': 'http://www.cutestpaw.com/wp-content/uploads/2012/12/Three-pups-just-hanging-around.jpg',
           'lots': 'http://www.lifedaily.com/wp-content/uploads/2015/09/puppy-pile-5-terriblycute.com_.jpg'}


@app.route('/')
def show_index():
    """Show the index page"""

    return render_template('index.html')


@app.route('/practice')
def show_practice():
    """Show the practice page."""

    return render_template('js-practice.html')


@app.route('/api/puppies')
def get_puppies():
    """Return a URL linking to a photo of the requested number of puppies."""

    # Get the form data from the AJAX request
    num_puppies = request.args.get('num-puppies')

    # Get the appropriate URL
    puppy_url = PUPPIES.get(num_puppies)

    # Package everything up in a dictionary, jsonify it, and return it
    return jsonify({'url': puppy_url})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
