from flask import Blueprint, render_template, request, flash, g, redirect, url_for, abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, created, author_id, username,'
        '(SELECT COUNT(*) FROM user_like WHERE post_id = p.id) AS likes_count'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)


@bp.route('/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id, check_author=False)

    user_liked = None

    if g.user is not None:
        # Check if the user liked the post
        user_liked = get_db().execute(
            'SELECT * FROM user_like WHERE user_id = ? AND post_id = ?',
            [g.user['id'], post['id']]
        ).fetchone() is not None

    return render_template('blog/post.html', post=post, user_liked=user_liked)


@bp.route('/like/<int:post_id>')
@login_required
def like_post(post_id):
    db = get_db()
    post = get_post(post_id, check_author=False)

    user_like = db.execute(
        'SELECT * FROM user_like WHERE user_id = ? AND post_id = ?',
        [g.user['id'], post['id']]
    ).fetchone()
    already_liked = user_like is not None

    if already_liked:
        # Remove the like
        db.execute(
            'DELETE FROM user_like WHERE user_id = ? AND post_id = ?',
            [g.user['id'], post['id']]
        )
        db.commit()
    else:
        # Add the like
        db.execute(
            'INSERT INTO user_like (user_id, post_id) VALUES (?, ?)',
            [g.user['id'], post['id']]
        )
        db.commit()

    return redirect(url_for('blog.post', post_id=post_id))


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'
        elif not body:
            error = 'Body is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' values (?, ?, ?)',
                [title, body, g.user['id']]
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update(post_id):
    post = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'
        elif not body:
            error = 'Body is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                [title, body, post_id]
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id):
    get_post(post_id)
    db = get_db()
    db.execute(
        'DELETE FROM post WHERE id = ?', [post_id]
    )
    db.commit()
    return redirect(url_for('blog.index'))


def get_post(post_id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        [post_id]
    ).fetchone()

    if post is None:
        abort(404, f"Post id {post_id} doesn't exist")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
