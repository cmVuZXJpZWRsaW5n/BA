# coding=utf-8
#!/bin/python


from flask import Flask, render_template, url_for
from elements import *


app = Flask(__name__)


questions = getQuestions()
attributes = getAttributes()
techniques = getTechniques()



@app.route("/")
def hello():
    return render_template('home_content.html', questions=questions, title="Security by Design")
#

if __name__ == '__main__':
		app.run(debug=True)



def lock(id):
    if id[:1] == 'q':
        for question in questions:
            if question['id'] == id:
                question['state'] = "deactivated"
    elif id[:1] == 'a':
        for attribute in attributes:
            if attribute['id'] == id:
                attribute['state'] = "deactivated"
    elif id[:1] == 't':
        for technique in techniques:
            if technique['id'] == id:
                technique['state'] = "deactivated"            


def printPentest():
    for attribute in attributes:
        if attribute['state'] == "activated":
            print(attribute['title'])

    for technique in techniques:
        if technique['state'] == "activated":
            print(technique['title'])
            

def askSub(id=""):
    if id != "":
        for question in questions:
            if question['state'] == "activated" and question['id'] == id:
                print(question['title'])
                for answer in question['answers']:
                    print("> "+ answer['text'])
            else:
                continue

            choice = raw_input('Enter your answer: ')
            for answer in question['answers']:
                if answer['text'] == choice:
                    for qlock in answer['qlocks']:
                        lock(qlock)
                    for alock in answer['alocks']:
                        lock(alock)
                    for atlock in answer['atlocks']:
                        lock(atlock)
                    for tlock in answer['tlocks']:
                        lock(tlock)
                    for squest in answer['subquestions']:
                        askSub(squest)
                else:
                    continue


def ask(id=""):
    if id == "":
        for question in questions:
            if question['state'] == "activated" and len(question['id']) == 2:
                print(question['title'])
                for answer in question['answers']:
                    print("> "+ answer['text'])
            else:
                continue

            choice = raw_input('Enter your answer: ')
            for answer in question['answers']:
                if answer['text'] == choice:
                    for qlock in answer['qlocks']:
                        lock(qlock)
                    for alock in answer['alocks']:
                        lock(alock)
                    for atlock in answer['atlocks']:
                        lock(atlock)
                    for tlock in answer['tlocks']:
                        lock(tlock)
                    for squest in answer['subquestions']:
                        askSub(squest)
                else:
                    continue
                     
ask()
printPentest()
