all:
	python3 main.py

clean:
	cd datasets
	rm -f *.csv
	cd ..

install:
	pip3 install -r requirements.txt
