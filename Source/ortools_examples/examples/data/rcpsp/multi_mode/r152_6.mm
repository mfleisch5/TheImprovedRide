************************************************************************
file with basedata            : cr152_.bas
initial value random generator: 678112456
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  120
RESOURCES
  - renewable                 :  1   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19       12       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7   8
   3        3          2           8  11
   4        3          3          10  13  16
   5        3          2           6  11
   6        3          1           9
   7        3          2          10  11
   8        3          2          13  17
   9        3          2          10  14
  10        3          2          12  15
  11        3          3          12  13  14
  12        3          1          17
  13        3          1          15
  14        3          3          15  16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     2       9   10    6
         2     3       9    9    5
         3     5       8    7    4
  3      1     8       1    5    9
         2     8       0    3   10
         3     8       0    6    8
  4      1     1       0    7    7
         2     2       8    5    6
         3    10       0    4    2
  5      1     5       5    2    4
         2     7       4    1    4
         3     9       4    1    3
  6      1     4       3    3   10
         2     6       3    1   10
         3     6       2    2   10
  7      1     2       5    4    3
         2     6       0    3    3
         3     6       0    4    2
  8      1     2       0    5    6
         2     7       0    4    4
         3    10      10    2    4
  9      1     1       7   10    5
         2     3       5    8    5
         3     4       0    7    2
 10      1     3       0    9    9
         2     5       5    8    7
         3     8       4    7    5
 11      1     6       3    7    5
         2     7       0    7    3
         3     9       0    5    1
 12      1     2       0    7    8
         2     4       0    7    7
         3     8       7    6    7
 13      1     2       7    9    9
         2     5       0    6    9
         3     7       0    2    6
 14      1     2       0    6    6
         2     5       7    6    5
         3     7       0    6    5
 15      1     3       0    6    8
         2     3       0    7    7
         3     9       0    4    6
 16      1     1       4    6   10
         2     3       0    6    9
         3     8       3    5    9
 17      1     2       0   10    6
         2     3       0    5    5
         3     6       3    3    5
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  N 1  N 2
   24   98  104
************************************************************************
