Client Server Calculator

This repository contains programs simulating sending data using various transmission protocols; TCP, Simulated unreliable UDP, and Reliable UDP

All programs send information on a local host network.

Each protocol implements a server-side calculator that accepts data from a client program in "operator number number" form (e.g. * 4 8) and returns the result of the equation back to the client.

Each protocol also handles invalid inputs, timeouts, and dead server cases.

To run the protocols, first create a txt file with your desired inputs. Any number of inputs can be run on new lines. See test.txt for example.
Run server: python3 server.py
Run client with inputs: python3 client.py test.txt


