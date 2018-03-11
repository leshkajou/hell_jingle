from bottle import post, get, run, static_file, request

from player import Player

p = Player(3)
#p.start()

@post('/play')
def play():
    print(request.json)
    p.start()
    p.play(request.json)
    p.stop()
    return "Hello World!"

@get('/')
def index():
    return static_file('index.html', root='./static')

@get('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='0.0.0.0', port=8080, debug=True)
