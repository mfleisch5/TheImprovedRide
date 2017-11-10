************************************************************************
file with basedata            : cn160_.bas
initial value random generator: 738944792
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  132
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  1   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18       10       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          14  15
   3        3          3          13  14  16
   4        3          3           5   7   9
   5        3          2           6  12
   6        3          1          11
   7        3          3           8  11  14
   8        3          3          10  12  17
   9        3          2          10  12
  10        3          1          13
  11        3          3          13  16  17
  12        3          2          15  16
  13        3          1          15
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     1       0    6    8
         2     4       0    5    6
         3     6       0    4    2
  3      1     1       0    8    7
         2     1       7    0    7
         3     9       0    8    5
  4      1     1       7    0    6
         2     2       4    0    6
         3     7       0    6    5
  5      1     1      10    0    6
         2     3       5    0    5
         3     6       3    0    5
  6      1     1       0    7    6
         2    10       0    7    4
         3    10       6    0    2
  7      1     3       9    0    5
         2     6       0    9    4
         3    10       9    0    1
  8      1     3       0    9    8
         2     9       0    8    7
         3     9       3    0    6
  9      1     3       0    9    6
         2    10       0    5    4
         3    10       4    0    3
 10      1     1       4    0    6
         2     9       3    0    4
         3    10       0    7    2
 11      1     7       0    6    8
         2     8       0    3    5
         3     8       4    0    6
 12      1     2       0    2    8
         2     4       4    0    7
         3     7       3    0    5
 13      1     5       0    9    6
         2     8       0    6    5
         3    10       0    5    4
 14      1     4       1    0   10
         2     6       0    8   10
         3    10       0    4    9
 15      1     2       6    0    6
         2     5       0   10    6
         3     6       5    0    5
 16      1     3       0    7    9
         2     4       0    7    8
         3     8       0    6    7
 17      1     1       0    3    8
         2     2       5    0    5
         3     6       0    3    2
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1
   23   25  113
************************************************************************
