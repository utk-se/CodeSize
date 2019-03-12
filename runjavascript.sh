for filename in repos/javascript/*; do
	echo "Working on ${filename}"
	filename="${filename##*/}"
	python3 main.py -d repos/javascript/${filename} -l .js --csv > results/javascript/${filename}.csv
	echo "Finished"
done
