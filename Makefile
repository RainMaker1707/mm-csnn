default: run clean

run:
	python3 ./main.py

clean:
	rm -rf ./*/__pycache__
	rm -rf ./*/*/__pycache__