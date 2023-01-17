"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code , title , words, text):
        """Create story with words and template text."""
   
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        # pass template to here
        text = self.template
        
        # replace {} in template into value by using for loop
        for (key, val) in answers.items():        
            text = text.replace("{" + key + "}", val)          

        #  Then return the text , then move to the second loop do the same step
        #  Then pass the text variable to the post variable in def show_story() in routes.py        
        return text


# Here's a story to get you started

story1 = Story(
    "history",
    "A History Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "omg",
    "An Excited Adventure",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

# Make dict of {code:story, code:story, ...}
stories = {s.code: s for s in [story1, story2]}

# s will access to all data of story1 by first loop . 
# Then access to code parameter in s variable and assign it to dictonary by s.code {'history': story1 (all data inclued history code), 'omg': story2}
# stories = {}
# for s in [story1, story2]:
#     stories[s.code] = s
#     print(stories)
