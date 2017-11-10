************************************************************************
file with basedata            : md222_.bas
initial value random generator: 2084686078
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  126
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19       10       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   8   9
   3        3          3           5   8  10
   4        3          3           7   9  14
   5        3          3           9  15  16
   6        3          2          10  11
   7        3          1          11
   8        3          3          11  14  17
   9        3          1          17
  10        3          1          12
  11        3          2          15  16
  12        3          1          13
  13        3          2          14  17
  14        3          2          15  16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       6    7    8    0
         2     2       4    6    0    5
         3     4       3    4    3    0
  3      1     4       6    3    0   10
         2     6       2    3    4    0
         3     6       2    2    0   10
  4      1     3       7    8   10    0
         2     6       6    6    5    0
         3     7       6    5    4    0
  5      1     3      10    7    0    7
         2     8       8    3    8    0
         3    10       7    2    8    0
  6      1     1       4    9    0    4
         2     4       3    8    0    4
         3     8       3    7    1    0
  7      1     3       8    4    0    4
         2     7       6    3    7    0
         3     9       3    3    0    4
  8      1     1       5    8    0    9
         2     1       4    7    6    0
         3    10       2    6    0   10
  9      1     4       8   10    0    9
         2     6       7    9    9    0
         3     9       6    9    0    6
 10      1     6       6    8    8    0
         2     7       5    5    0    6
         3     7       5    7    6    0
 11      1     3       9    6    0    2
         2     4       8    4    4    0
         3    10       5    3    1    0
 12      1     1       9    1    0    6
         2     1       9    1    2    0
         3     7       7    1    2    0
 13      1     6       3    3    0    6
         2     6       3    3   10    0
         3     8       2    1    8    0
 14      1     1       4    3    7    0
         2     5       3    3    7    0
         3     6       1    3    7    0
 15      1     1       5    5    7    0
         2     5       4    3    6    0
         3     8       4    1    0    7
 16      1     1       5    9    3    0
         2     9       2    8    2    0
         3     9       2    6    3    0
 17      1     2       5    9    0    6
         2     4       5    7    0    5
         3     8       4    6    6    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   18  100   82
************************************************************************
