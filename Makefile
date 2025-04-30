all:
	python3 main.py

clean:
	rm -f main_transactions.csv

install:
	pip3 install -r requirements.txt
