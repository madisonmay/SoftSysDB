SoftSysDB
=========

Homework 03 -- Experiment with Redis

Setup
-----

Parse imdb compressed files and dump into .jl files
```
python imdb.py
```

Generate intermediate representation and save as .jl files
```
python parse.py && python merge.py
```

Dump final representation into redis
```
python redis_save.py
```

Run a python version of the bidirectional shortest path search algorithm.
The file can be edited to find the path between different actor pairs.
```
python sps.py
```

Compile C file that demonstrates basic C functionality
```
gcc sps.c -o sps -I hiredis -L hiredis -lhiredis -lm
```

Run the demo C file and find actors/actresses 1 edge away from a given actor/actress
```
./sps
```




