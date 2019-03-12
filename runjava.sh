for filename in repos/java/*; do
	echo "Working on ${filename}"
	filename="${filename##*/}"
	python3 main.py -d repos/java/${filename} -l .java --csv > results/java/${filename}.csv
	echo "Finished"
done
