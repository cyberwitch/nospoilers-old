from json import dumps

from flask import Flask, render_template, request

from nospoilers.tmdbutils import TMDBUtils


app = Flask(__name__)
tmdb = TMDBUtils('1c9fdf67f8e8f9df79a09809f463bc25')

@app.route('/suggestions/<search_text>')
def suggestions(search_text):
    return dumps(tmdb.search(search_text, True))

@app.route('/search')
def search():
    query = request.args.get('query')

    if query:
        return render_template('search.html', query=query, shows=tmdb.search(query))
    else:
        return render_template('search.html')

@app.route('/show/<tmdb_id>')
def show(tmdb_id):
    show = tmdb.get_show(tmdb_id)
    return render_template('show.html', show=show)

@app.route('/show/<tmdb_id>/season/<season_number>')
def show_season(tmdb_id, season_number):
    return dumps(tmdb.get_season(tmdb_id, season_number))

if __name__ == '__main__':
    app.run(debug=True)
