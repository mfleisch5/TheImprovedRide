************************************************************************
file with basedata            : cr19_.bas
initial value random generator: 1610064318
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  127
RESOURCES
  - renewable                 :  1   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       26       12       26
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           7  10  17
   3        3          3           9  10  11
   4        3          3           5   6   8
   5        3          3           9  11  12
   6        3          2           9  12
   7        3          2          15  16
   8        3          2          10  13
   9        3          1          14
  10        3          2          15  16
  11        3          1          13
  12        3          1          13
  13        3          2          14  15
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     1       0    5    0
         2     4       0    2    0
         3     4       9    0    6
  3      1     3       3    3    0
         2     6       0    3    0
         3     9       0    0    8
  4      1     4       0    8    0
         2     6       0    0    4
         3    10       8    0    1
  5      1     6       5    4    0
         2     8       0    0    8
         3     8       0    4    0
  6      1     4       0    9    0
         2     5       0    0    3
         3    10       1    8    0
  7      1     1       5    6    0
         2     3       0    0    5
         3     8       3    0    3
  8      1     3       0    0   10
         2     9       0    0    8
         3    10       0    5    0
  9      1     2       4    7    0
         2     4       3    0    6
         3     5       3    5    0
 10      1     5       0    0   10
         2     8       9    8    0
         3     9       7    0    9
 11      1     6      10    4    0
         2     7      10    0    6
         3     8       9    0    5
 12      1     3       5    2    0
         2     6       5    0    8
         3     7       0    0    7
 13      1     4       0    0    9
         2     4       0    4    0
         3     5       5    0    8
 14      1     1       3    7    0
         2     5       2    0    7
         3     9       0    5    0
 15      1     2      10    8    0
         2     5       0    0    8
         3     8       8    5    0
 16      1     2       0    0    5
         2     5       0    8    0
         3     9       0    6    0
 17      1     5       0    0    9
         2     6       3    0    7
         3     8       2    6    0
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  N 1  N 2
   14   47   56
************************************************************************
