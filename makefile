#Makefile for CodeSize Project

EXECUTABLES = main

lock: main.py
	cp main.py main
	chmod 755 main

clean:
	rm -f $(EXECUTABLES)
