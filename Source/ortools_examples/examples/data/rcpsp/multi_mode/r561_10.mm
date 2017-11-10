************************************************************************
file with basedata            : cr561_.bas
initial value random generator: 569286736
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  128
RESOURCES
  - renewable                 :  5   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18        9       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3          10  12  14
   3        3          2           9  14
   4        3          1           5
   5        3          3           6   7   9
   6        3          2           8  16
   7        3          3          10  12  17
   8        3          3          11  12  14
   9        3          2          15  16
  10        3          2          13  16
  11        3          2          13  17
  12        3          1          13
  13        3          1          15
  14        3          2          15  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  R 5  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0    0
  2      1     7       9    7    6    8    5    7    7
         2     9       8    6    6    7    4    7    7
         3     9       9    4    6    6    4    7    7
  3      1     1       5    3    3    9    6    7    6
         2     7       4    3    3    5    6    5    6
         3    10       4    2    2    4    4    3    6
  4      1     2       4    6    8    5    5    5    2
         2     3       4    5    8    5    3    5    2
         3     4       4    3    7    5    2    2    1
  5      1     3       7    3    9    8    7    5    9
         2     8       6    3    4    5    7    1    9
         3     8       6    2    4    7    6    1    8
  6      1     2       9    2    7    6    4    9    4
         2     3       6    2    7    4    2    8    3
         3     9       2    2    7    3    1    8    2
  7      1     1       7    9    3    9    8    2    8
         2     7       5    8    3    8    7    2    8
         3     9       2    6    2    7    7    2    8
  8      1     1       6    5    4    8    7    5    9
         2     2       6    3    4    4    4    3    9
         3     2       6    5    3    5    4    2    9
  9      1     3       7    8    7    9    6   10    8
         2     4       6    8    6    7    5    9    5
         3     7       6    6    4    7    4    8    4
 10      1     4       4    9    4    6    4    9    7
         2     4       4   10    4    5    6    7    7
         3     9       3    8    3    3    2    2    7
 11      1     1       6    8    4    4    6    9    5
         2     4       6    8    4    3    5    8    3
         3     9       3    7    4    2    4    8    3
 12      1     6       8    6    9    8    4   10    8
         2     7       5    4    6    8    4    9    7
         3     9       3    3    3    6    3    9    6
 13      1     2       9    2   10    5    7    7    7
         2     3       7    2    9    5    6    7    6
         3     9       6    1    9    4    3    7    5
 14      1     5       6    7    4    7    8    9    4
         2     7       5    4    3    7    5    9    2
         3    10       4    3    2    6    3    9    1
 15      1     2       9   10    9    2    7    8    3
         2     4       6    8    7    2    6    7    3
         3    10       3    6    5    1    5    7    2
 16      1     6       7    6   10    3    8    7    6
         2     7       7    6   10    2    5    7    5
         3     8       7    6    9    2    3    7    5
 17      1     4       9    5    8    6    6    5    6
         2     4       9    3    8    9    6    4    7
         3     6       7    3    8    2    5    3    3
 18      1     0       0    0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  R 5  N 1  N 2
   14   14   14   13   11  114  100
************************************************************************
