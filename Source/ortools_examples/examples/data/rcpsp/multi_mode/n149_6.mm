************************************************************************
file with basedata            : cn149_.bas
initial value random generator: 1447453970
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  141
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  1   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       25        5       25
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           7  10  11
   3        3          3           6   8  10
   4        3          2           5  14
   5        3          3          12  15  16
   6        3          1          13
   7        3          1           8
   8        3          2           9  15
   9        3          2          13  14
  10        3          3          12  13  14
  11        3          2          12  15
  12        3          1          17
  13        3          2          16  17
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     5       8    0    9
         2     6       0    4    8
         3    10       0    2    8
  3      1     2       0    8    6
         2     7       6    0    6
         3     9       0    7    6
  4      1     2       5    0    5
         2     5       0    2    5
         3     8       2    0    4
  5      1     1       0    5    7
         2     2       0    4    5
         3    10       2    0    2
  6      1     1       0    7    3
         2     2       7    0    2
         3    10       7    0    1
  7      1     1       2    0    9
         2     6       2    0    5
         3     7       1    0    4
  8      1     5       4    0    3
         2     7       0    2    3
         3     9       2    0    3
  9      1     7       0    2   10
         2     8       5    0    9
         3     9       2    0    9
 10      1     4       7    0    6
         2     6       3    0    6
         3     8       3    0    4
 11      1     2       0    5    3
         2     6       0    2    3
         3     9       9    0    3
 12      1     1       0    1    9
         2     6       4    0    9
         3     7       0    1    8
 13      1     4       0   10    1
         2     9       6    0    1
         3    10       0    9    1
 14      1     3       0    4    9
         2     6       1    0    9
         3     7       0    4    8
 15      1     4       3    0    7
         2    10       2    0    3
         3    10       0    3    4
 16      1     1       0    3    8
         2     3       8    0    7
         3     8       0    3    6
 17      1     3       0    7    5
         2     8       9    0    4
         3    10       8    0    3
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1
   10    4   93
************************************************************************
