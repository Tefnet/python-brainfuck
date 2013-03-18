# python-brainfuck

Python parser and TCP/UDP/HTTP server for brainfuck language:
http://en.wikipedia.org/wiki/Brainfuck

## How To Use

#### Clone github code

    git clone https://github.com/Tefnet/python-brainfuck
    cd python-brainfuck

#### Create virtualenv

    virtualenv .

#### Run parser tests

    bin/python setup.py test

#### Install

    bin/python setup.py install


#### Run server

    bin/brainfuck_server

#### Test server

* TCP
    echo -n '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.' | nc  localhost 1982

* UDP
    echo -n '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.' | nc  localhost 1982

#### Test HTTP server

* Go to http://localhost:1983
* Paste your code and click submit button


