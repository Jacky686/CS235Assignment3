from flask import Blueprint, render_template

import flix.adapters.repository as repo
import flix.browse.services as services

browse_blueprint = Blueprint('browse_bp', __name__)


@browse_blueprint.route('/browse', methods=['GET'])
def browse():
    movies = services.get_movies(repo.repo_instance)
    length = len(movies)
    return render_template(
        'browse/browse.html', movies=movies, length=length
    )
