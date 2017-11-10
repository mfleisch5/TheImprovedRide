************************************************************************
file with basedata            : md94_.bas
initial value random generator: 1661737052
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  105
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       14        6       14
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   7   8
   3        3          2           6  12
   4        3          2           5   7
   5        3          3           6   8   9
   6        3          2          11  13
   7        3          3           9  11  13
   8        3          3          10  11  13
   9        3          1          10
  10        3          1          12
  11        3          1          14
  12        3          1          14
  13        3          1          14
  14        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     4       4    4   10    0
         2     5       3    4    9    0
         3     9       3    4    0    8
  3      1     1       8    4    7    0
         2     6       7    4    0    6
         3     9       4    3    0    4
  4      1     3       9   10    0    7
         2     8       8    7    0    7
         3    10       5    5    3    0
  5      1     5       8    5    0    3
         2     5       6    4    0    4
         3     8       5    4    6    0
  6      1     2       7    5    0    6
         2     5       7    5    5    0
         3     9       7    4    3    0
  7      1     4       5    6    0    6
         2     7       5    5    0    3
         3     9       5    5    8    0
  8      1     1       6    6    0    8
         2     6       4    5    0    7
         3    10       3    3    4    0
  9      1     1       2    3    8    0
         2     3       2    2    0    7
         3     8       2    1    0    6
 10      1     1       7    7    0    8
         2     5       6    6    0    8
         3     7       5    6    3    0
 11      1     4       7    9    8    0
         2     8       6    5    0    7
         3     9       1    3    7    0
 12      1     3       7    8    0   10
         2     7       4    7    8    0
         3     8       4    5    0    9
 13      1     4       3    9    0    3
         2     5       3    7    3    0
         3     9       2    7    0    2
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   14   17   73   80
************************************************************************
