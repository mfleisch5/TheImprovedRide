************************************************************************
file with basedata            : c2132_.bas
initial value random generator: 2088283212
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  125
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18        3       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   9
   3        3          3           7  10  13
   4        3          3           5   8  14
   5        3          2           7  10
   6        3          3           7   8  14
   7        3          2          12  17
   8        3          3          11  12  13
   9        3          3          11  13  14
  10        3          2          11  12
  11        3          3          15  16  17
  12        3          1          16
  13        3          2          15  16
  14        3          2          15  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       7    6    2    0
         2     5       5    6    2    0
         3    10       4    5    2    0
  3      1     1       2    8    0    6
         2     1       2   10    0    5
         3     9       1    5    0    5
  4      1     1       9    9    7    0
         2     2       8    8    0    5
         3     6       7    8    7    0
  5      1     5       9   10    0    6
         2     7       4   10    5    0
         3     8       3   10    0    2
  6      1     2       7    4    7    0
         2     8       7    3    4    0
         3    10       6    2    4    0
  7      1     2       3    6    4    0
         2     8       3    5    2    0
         3    10       3    5    0    6
  8      1     2       7    7   10    0
         2     5       5    3    5    0
         3     7       3    1    3    0
  9      1     1       8    5    4    0
         2     2       4    5    0    4
         3     6       3    5    0    4
 10      1     6       4    6    0   10
         2     7       3    6    0   10
         3     8       3    6    0    9
 11      1     2       3    7    8    0
         2     9       2    6    5    0
         3    10       2    4    0    2
 12      1     2       3    7    0    2
         2     4       2    6    0    1
         3    10       1    6    4    0
 13      1     1       8    7    0    3
         2     5       8    6    0    3
         3     7       8    5    0    3
 14      1     3       7    5    9    0
         2     4       5    5    4    0
         3     4       6    5    0   10
 15      1     2       9    3    0    8
         2     5       8    1    0    7
         3     5       8    2    4    0
 16      1     2       5   10    4    0
         2     4       3    6    4    0
         3     8       3    3    3    0
 17      1     2       7    5    0    8
         2     2       4    6    0    7
         3     7       1    3    5    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   24   25   73   70
************************************************************************
