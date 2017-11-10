************************************************************************
file with basedata            : md297_.bas
initial value random generator: 1430447782
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  135
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       13        3       13
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7  19
   3        3          3           6  14  19
   4        3          3          12  13  14
   5        3          2           8   9
   6        3          2          10  11
   7        3          1           9
   8        3          3          10  11  14
   9        3          1          12
  10        3          2          15  16
  11        3          2          13  16
  12        3          1          17
  13        3          2          15  18
  14        3          2          15  16
  15        3          1          17
  16        3          2          17  18
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0    4    5   10
         2     6       0    4    5    6
         3     9       0    4    5    5
  3      1     3       0    5    8    4
         2     4       8    0    8    3
         3     9       5    0    5    3
  4      1     4       0    9    5    6
         2     7       4    0    3    4
         3     9       4    0    1    4
  5      1     2       0    2    3    5
         2     2       7    0    3    5
         3     5       5    0    3    4
  6      1     2       0    5    4    6
         2     2       6    0    5    7
         3     8       3    0    1    6
  7      1     3       0    7    7    8
         2     4       7    0    6    7
         3     6       7    0    4    7
  8      1     4       7    0   10    3
         2     4       0    4    9    2
         3     7       7    0    7    1
  9      1     3       0    5    2    7
         2     8       5    0    2    5
         3    10       0    3    1    5
 10      1     3       7    0    4    3
         2     7       6    0    3    3
         3    10       0    9    2    2
 11      1     1       0    5    5    8
         2     2       0    3    5    7
         3     3       6    0    4    7
 12      1     1       0    3    7    4
         2     3       2    0    7    3
         3     8       0    2    5    3
 13      1     3       0    8    5    8
         2     7       3    0    5    7
         3    10       0    7    4    6
 14      1     1       0    7    9    8
         2     5       9    0    7    7
         3     6       5    0    5    7
 15      1     1       0    6    2    5
         2     5       0    4    2    5
         3     8      10    0    1    4
 16      1     1       3    0    8    6
         2     4       0    7    8    6
         3     8       0    6    8    4
 17      1     1       5    0    4    6
         2     3       0   10    2    3
         3     3       0    6    1    5
 18      1     1       4    0    7    4
         2     7       2    0    6    2
         3     7       0    2    5    3
 19      1     2       8    0    8    4
         2     5       2    0    8    3
         3     9       0    9    7    2
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
    8   12   87   91
************************************************************************
