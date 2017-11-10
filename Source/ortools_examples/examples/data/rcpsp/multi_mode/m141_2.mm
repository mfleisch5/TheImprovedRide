************************************************************************
file with basedata            : cm141_.bas
initial value random generator: 151971114
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  75
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       30        8       30
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2           7   9
   3        1          2           5  16
   4        1          3           6   7   8
   5        1          3           8  10  15
   6        1          3           9  10  13
   7        1          2          12  15
   8        1          2          11  14
   9        1          2          16  17
  10        1          2          12  14
  11        1          1          12
  12        1          1          17
  13        1          3          14  15  16
  14        1          1          17
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       0    2    1   10
  3      1     7       0   10    5    6
  4      1     7       4    0    3    2
  5      1     2       8    0    4    1
  6      1     5       8    0    9    5
  7      1    10       0    2   10    6
  8      1     3       3    0    6    8
  9      1     2       9    0   10    9
 10      1     7       0    6    6    5
 11      1     4       9    0    7    9
 12      1     2       0    8    1    7
 13      1     8       6    0    6    7
 14      1     2       0   10    6    1
 15      1     1       5    0    6    5
 16      1    10       0    2    8    5
 17      1     2       0    5    5    5
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   13   13   93   91
************************************************************************
