************************************************************************
file with basedata            : md207_.bas
initial value random generator: 1607094084
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  111
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17        2       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5  11
   3        3          2           5  11
   4        3          1           7
   5        3          2           6   8
   6        3          3          10  12  14
   7        3          3          11  12  14
   8        3          2           9  12
   9        3          3          10  14  17
  10        3          2          15  16
  11        3          1          13
  12        3          2          13  16
  13        3          2          15  17
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
  2      1     2       6    4    0    5
         2     4       5    4    2    0
         3     5       2    4    0    3
  3      1     4      10    9    0    2
         2     7       7    7    8    0
         3     8       4    5    8    0
  4      1     1      10    8    8    0
         2     6       9    6    0    4
         3     7       8    4    0    3
  5      1     1      10    3    0    7
         2     5       7    3    9    0
         3     8       6    3    2    0
  6      1     2       2    8    5    0
         2     3       2    5    0    9
         3     9       2    2    5    0
  7      1     1       4   10    0    9
         2     4       3    9    0    9
         3     8       3    7    0    8
  8      1     2       9    3    0    7
         2     5       8    2    0    5
         3     5       9    2    3    0
  9      1     1       8    6    6    0
         2     8       7    6    6    0
         3    10       3    5    3    0
 10      1     3       8    5    0    8
         2     4       7    5    0    4
         3     6       7    5    0    3
 11      1     2       9    7    6    0
         2     5       6    5    0    4
         3     6       5    2    0    3
 12      1     3       9    4    6    0
         2     3       9    5    0    5
         3     5       7    4    5    0
 13      1     3       7    7    0    7
         2     7       6    6    0    5
         3     8       5    5    0    4
 14      1     1       7    6    6    0
         2     6       6    4    3    0
         3     8       4    3    0   10
 15      1     4       7    8    8    0
         2     6       5    5    0    4
         3     8       4    3    5    0
 16      1     1       4    5    0    7
         2     3       4    4    0    4
         3     4       4    3    7    0
 17      1     2      10   10    0    8
         2     5       8    8    8    0
         3     6       5    8    7    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   22   19   43   56
************************************************************************
