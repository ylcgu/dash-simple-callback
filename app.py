import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Try out a palindrome here!'
tabtitle = 'racecar'
sourceurl = 'https://codereview.stackexchange.com/questions/25679/create-palindrome-by-rearranging-letters-of-a-word'
githublink = 'https://github.com/austinlasseter/dash-simple-callback'

def my_function(letters):
    return(letters[::-1])


########### Define a cool function for palindromes
# Hat tip! https://codereview.stackexchange.com/users/1659/winston-ewert

# def my_function(letters):
#     """
#     Forms a palindrome by rearranging :letters: if possible,
#     throwing a :ValueError: otherwise.
#     :param letters: a suitable iterable, usually a string
#     :return: a string containing a palindrome
#     """
#     counter = Counter(letters)
#     sides = []
#     center = deque()
#     for letter, occurrences in counter.items():
#         repetitions, odd_count = divmod(occurrences, 2)
#         if not odd_count:
#             sides.append(letter * repetitions)
#             continue
#         if center:
#             return "no palindrome exists for '{}'".format(letters)
#         center.append(letter * occurrences)
#     center.extendleft(sides)
#     center.extend(sides)
#     return ''.join(center)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([dcc.Markdown('''
            _Suggestions you might try:_
            * A man, a plan, a canal: Panama!
            * Go hang a salami I'm a lasanga hog
            * God! Nate bit a Tibetan dog!
            ''')]),

    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),
    # html.Div(id='your_output_here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    palin=my_function(input_value)
    return f"You've entered '{input_value}', and your output is '{palin}'"

############ Deploy
if __name__ == '__main__':
    app.run_server()
