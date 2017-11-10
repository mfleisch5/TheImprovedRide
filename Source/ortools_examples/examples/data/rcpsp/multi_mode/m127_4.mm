************************************************************************
file with basedata            : cm127_.bas
initial value random generator: 1355009694
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  96
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       33        6       33
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2          10  11
   3        1          3           9  10  12
   4        1          3           5   6   7
   5        1          3           8  13  14
   6        1          2           8   9
   7        1          3          10  13  14
   8        1          2          12  15
   9        1          2          13  17
  10        1          2          16  17
  11        1          1          16
  12        1          2          16  17
  13        1          1          15
  14        1          1          15
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       9    0    4    0
  3      1    10       3    0    0    8
  4      1     4       6    0    4    0
  5      1    10       1    0    2    0
  6      1     9       0    2    0    3
  7      1    10       7    0    6    0
  8      1     9       0    6   10    0
  9      1     9       7    0    0   10
 10      1     1       0    2    0    4
 11      1     7       0    3    0    6
 12      1     1       0    7    0    4
 13      1     9       6    0    0    2
 14      1     6       0    7    0    5
 15      1     2       0    4    0    4
 16      1     4       0    4    6    0
 17      1     2       6    0    0    5
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   16   13   32   51
************************************************************************
