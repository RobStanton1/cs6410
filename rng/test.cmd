REM this script runs the rng for several test cases
REM the baseline script call for each distribution is as follows
REM python myRng.test.py 1000 5 Log 0.6
REM python myRng.test.py 1000 5 Kum 2 1
REM dist works correctly
REM running this script should result in no unhandled exceptions
REM or runtime errors

python myRng.py 1000 5 Log 0.66
python myRng.py 1000 5 Log 1
python myRng.py 1000 5 Log 0
python myRng.py 1000 5 Log -1
python myRng.py 0 5 Log 0.66
python myRng.py -1 5 Log 0.66
python myRng.py 1000 0.5 Log 0.66


python myRng.py 1000 5 Kum 2 1
python myRng.py 1000 5 Kum 0 1
python myRng.py 1000 5 Kum -1 1
python myRng.py 1000 5 Kum 2 0
python myRng.py 1000 5 Kum 2 -1
python myRng.py 0 5 Kum 2 1
python myRng.py -1 5 Kum 2 1
python myRng.py 1000 0.5 Kum 2 1