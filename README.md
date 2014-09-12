scheduler
=========

Python script scheduler

USAGE
=====
Put files inside scripts folder, and to specify when to run each script, change the name to scriptname-XXs.py, XX is amount of seconds, can be any number-
Make a script that calls this script every X amount of time so it checks and runs everything as needed

EXAMPLE
=======
Imagine you wanna scrape some sites, you would put this files in the scripts folder: scraper1-20s.py scraper2-300s.py scraper3-15s.py
what you would get is scraper1 running every 20 seconds, scraper 2 every 5 minutes and scraper3 every 15 seconds

REQUIREMENTS
============
You'll need screen installed in your server, since every script runs in its own screen
