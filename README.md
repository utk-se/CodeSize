# CodeSize

Codesize depends on these repos:
* https://github.com/terryyin/lizard


## Python Script

To use:

```
python3 main.py

-f [file]
-d [directory] 
-l [extension]

--csv
```


With the `-f` flag, you can specify a specific file to analyze.

With the `-d` flag, you can specify a specific directory to analyze. 

With the `-l` flag, you can specify a specific file extension. You can use this flag to specify multiple extensions (ex. `-l .cpp -l .cc`).

The `--csv` flag will specify the output to be csv friendly. Without this, it will be much easier on the eyes to view, although not so great for analysis.

The code will ignore all functions with a width more than 999 characters long, as this was considered a major outlier.


## Repos

The repos analyzed were picked from the top 25 repos for the day on 03/12/2019 from C++, Java, Javascript, and Python. The link and commit hash for each repo is available in the `repos.txt` file. 100 repos were downloaded, but only 95 repos were used (5 of the repos did not contain any code).

## Results

The results are stored in `results/` in the repo. The files are broken down per repo analyzed. The .csv file is what was genereated by the script, and the excel file contains the statistics for each repo. There are 100 total .xlsx files - 95 for each repo, 4 for language overalls, and 1 for everything overall.