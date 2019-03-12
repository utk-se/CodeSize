for filename in repos/python/*; do
	echo "Working on ${filename}"
	filename="${filename##*/}"
	python3 main.py -d repos/python/${filename} -l .py --csv > results/python/${filename}.csv
	echo "Finished"
done
