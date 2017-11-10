************************************************************************
file with basedata            : cr340_.bas
initial value random generator: 263970756
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  130
RESOURCES
  - renewable                 :  3   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19        2       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   7
   3        3          2          10  11
   4        3          3           7   8  15
   5        3          2           8  10
   6        3          3          10  11  16
   7        3          2           9  12
   8        3          3           9  12  13
   9        3          2          16  17
  10        3          1          15
  11        3          2          12  15
  12        3          1          17
  13        3          1          14
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     4       9    5   10    4    9
         2     6       8    4    9    2    5
         3     8       5    3    9    1    4
  3      1     2       9    4    9    9    6
         2     5       7    2    9    8    3
         3     7       5    1    9    8    2
  4      1     1       9    6    5    8    5
         2     4       7    5    4    7    4
         3     5       4    5    1    4    4
  5      1     1       7   10    2    3    8
         2     3       6    8    1    3    8
         3    10       5    6    1    2    8
  6      1     8       4   10    5    8    8
         2     8       4    9    5    9    9
         3    10       4    9    5    7    8
  7      1     4       7    9   10    7    1
         2     8       6    8    8    4    1
         3     9       4    6    3    2    1
  8      1     2       8    7    6    6    8
         2     6       8    5    5    6    8
         3     8       8    2    3    6    8
  9      1     1       3    9    4    5    8
         2     9       3    7    3    1    6
         3     9       2    5    4    3    6
 10      1     2       9    9    6   10    4
         2     4       9    8    6   10    4
         3     9       9    7    4    9    3
 11      1     3       3    8    8    4    8
         2     5       2    7    5    3    8
         3     8       2    2    3    2    8
 12      1     1      10    3    7    7    7
         2     6       7    3    6    6    4
         3     7       5    1    4    6    2
 13      1     1       6    5    7    1    7
         2     2       5    2    5    1    4
         3     5       4    1    5    1    2
 14      1     5       7    2    3    7    6
         2     6       5    2    2    3    6
         3     6       1    1    3    3    3
 15      1     4       8    2    5    8    9
         2     8       8    2    5    6    8
         3    10       8    1    1    4    8
 16      1     3       8    9   10    7    9
         2     7       6    9    9    6    5
         3    10       6    8    9    4    1
 17      1     2       5    9    4    9    8
         2     6       5    6    2    9    8
         3     9       4    4    1    8    8
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  N 1  N 2
   27   29   24   77   85
************************************************************************
