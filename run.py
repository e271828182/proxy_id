from proxypool.api import app
from proxypool.schedule import Schedule

def main():

    s = Schedule()
    s.run()
    app.run(host='0.0.0.0', port=5000, debug=True)




if __name__ == '__main__':
    main()

