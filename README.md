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


## Repos

The repos analyzed were picked from the top 25 repos for the day on 03/12/2019 from C++, Java, Javascript, and Python. The commit hashes are available in the `repos.txt` file.

## Results

The results are stored in `results/` in the repo. The files are broken down per repo analyzed. 