# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, url_for, jsonify
from werkzeug.utils import redirect
from ideas.models import Ideas

app = Flask(__name__)

app.secret_key = 'FEEDBACK-SECRET'


@app.route("/", methods=['GET'])
def index():
    output = []

    ideas = sorted(Ideas.find_all(), key=lambda x: x.vote, reverse=True)
    for idea in ideas:
        output.append({'id': idea.id, 'title': idea.title, 'description': idea.description, 'vote': idea.vote})

    return render_template("index.html", titulo="Dasa Box", ideas=output)


@app.route("/ideas", methods=['POST'])
def ideas():
    title = request.form.get('title')
    description = request.form.get('description')
    Ideas.save(title, description)

    flash('Ideia registrada')
    return redirect(url_for('index'))


@app.route("/vote/<int:_id>", methods=['POST'])
def vote(_id):
    item = Ideas.find_by_id(_id)
    Ideas.make_vote(item)

    return jsonify({"message": 'Feedback registrado com sucesso!'})


app.run(debug=True, port=8090)
