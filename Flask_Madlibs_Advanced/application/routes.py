from application import app
from flask import Flask, render_template, request
from stories import stories

@app.route("/")
def ask_story():
        
    # Access and return all the values of each story by stories.values()
    return render_template("select-story.html",stories=stories.values())
   

@app.route("/questions")
def ask_questions():
    """Generate and show form to ask words."""
    story_id = request.args["story_id"]
    story = stories[story_id]   
    prompts = story.prompts    

    return render_template("questions.html",
                           story_id=story_id,
                           title=story.title,
                           prompts=prompts)


@app.route("/story")
def show_story():
    """Show story result."""
    story_id = request.args["story_id"]
    story = stories[story_id]

    # access all the key-value pairs in URL parameters by request.args then convert into dictionary 
    # Then using the items() method in stories.py to access key-value
    # Get data the text variable from generate function in stories.py 
    post = story.generate(request.args)    

    # Assign the title and text to story.html
    return render_template("story.html",
                           title=story.title,
                           text=post)