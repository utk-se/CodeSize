for filename in repos/cpp/*; do
	echo "Working on ${filename}"
	filename="${filename##*/}"
	python3 main.py -d repos/cpp/${filename} -l .cc -l .cpp -l .cx --csv > results/cpp/${filename}.csv
	echo "Finished"
done
