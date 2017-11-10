************************************************************************
file with basedata            : cn362_.bas
initial value random generator: 1530491044
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  123
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       24        6       24
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   9  16
   3        3          3          11  13  17
   4        3          1           5
   5        3          3           6   7   8
   6        3          1          10
   7        3          3           9  11  13
   8        3          3           9  10  13
   9        3          1          14
  10        3          2          12  14
  11        3          2          15  16
  12        3          1          17
  13        3          2          15  16
  14        3          2          15  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     2       2    4    9    8    8
         2     3       2    3    9    7    7
         3     4       2    2    9    4    6
  3      1     1       4   10    7    4    9
         2     6       4   10    7    4    8
         3     6       4   10    6    4    9
  4      1     1       6    2    7    3    6
         2     6       3    1    7    2    6
         3    10       2    1    6    1    3
  5      1     6      10    8    6    6    4
         2     9       8    7    4    6    3
         3    10       7    4    4    3    2
  6      1     2       9    4    9    9    6
         2     7       9    4    8    8    5
         3    10       8    4    8    8    5
  7      1     4       9    9    2    8    6
         2    10       9    6    2    5    2
         3    10       9    5    2    7    2
  8      1     2       9    8    1    8    3
         2     3       9    7    1    8    2
         3     5       9    7    1    7    2
  9      1     3       7   10    6   10    5
         2     4       4    6    5    8    5
         3     5       3    5    5    7    4
 10      1     4       4    9   10    7    6
         2     6       3    8    7    7    5
         3    10       2    7    4    7    5
 11      1     4       9    4   10    8    9
         2     7       7    3   10    6    8
         3     9       2    3    9    4    4
 12      1     8       4    7    5    9    5
         2     9       4    3    5    7    2
         3     9       3    5    4    7    3
 13      1     1       7    5    8    8    5
         2     3       7    5    5    5    4
         3     8       7    2    2    4    3
 14      1     2       6    7   10   10    2
         2     5       5    7   10    4    2
         3    10       3    6    9    1    1
 15      1     8       7    7    4    7    8
         2     9       6    2    3    7    8
         3     9       6    2    4    5    8
 16      1     1       8    5    6    9    7
         2     2       7    3    5    9    5
         3     4       6    2    5    7    4
 17      1     1       2    8    9    3    7
         2     2       2    7    9    2    5
         3     4       1    7    8    1    3
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
   18   19  109  117   96
************************************************************************
