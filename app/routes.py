from flask import render_template, session
from app import app

@app.route('/')
@app.route('/base')
def base():
    return render_template('storyBase.html', previous = "previous", next = "next")

paragraphs = [  'blah blah blah 1',
                'blah blah blah 2',
                'blah blah 3']
links = ['1', '2', '3']

current = 0

@app.route('/novel')
def novel():
    return render_template('storyBase.html', body_text = paragraphs[current], previous = findPrevious(current), next = links[current + 1])

@app.route('/increment', methods=['POST'])
def increment():
    count = session.get('count', 0)
    session['count'] = count + 1

def findPrevious(num):
    if (num - 1) < 0:
        return links[0]
    else :
        return links[num - 1]