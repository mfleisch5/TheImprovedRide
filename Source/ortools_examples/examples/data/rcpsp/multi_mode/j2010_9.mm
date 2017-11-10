************************************************************************
file with basedata            : md330_.bas
initial value random generator: 1721760359
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  22
horizon                       :  144
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     20      0       18       16       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           8  11  17
   3        3          3           5   6  11
   4        3          1           6
   5        3          3           7   9  15
   6        3          3           7  13  15
   7        3          2           8  18
   8        3          3          10  12  16
   9        3          2          13  18
  10        3          1          14
  11        3          2          14  20
  12        3          1          19
  13        3          3          14  20  21
  14        3          1          19
  15        3          2          17  18
  16        3          1          19
  17        3          1          21
  18        3          2          20  21
  19        3          1          22
  20        3          1          22
  21        3          1          22
  22        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       5    0    0    5
         2     6       0    7    0    4
         3     7       0    4    6    0
  3      1     3       9    0    7    0
         2     5       0    2    5    0
         3     7       9    0    0    5
  4      1     1       7    0    0    7
         2     5       0    4    9    0
         3     9       0    1    9    0
  5      1     3       0    2    0   10
         2     8       0    1    5    0
         3     9       6    0    0    3
  6      1     2       3    0    0    8
         2     2       0    7    2    0
         3     3       3    0    0    7
  7      1     3       0    6    6    0
         2     7       0    5    3    0
         3    10       0    3    0    8
  8      1     2       0   10    0    4
         2     5      10    0    0    4
         3     6       0    9    0    4
  9      1     1       9    0    7    0
         2     8       7    0    4    0
         3     9       3    0    2    0
 10      1     4       0    6    0    8
         2     6       0    5    1    0
         3     9       0    2    0    5
 11      1     2       9    0    6    0
         2     9       9    0    4    0
         3    10       9    0    0    1
 12      1     3       8    0    0    7
         2     4       8    0    6    0
         3     5       7    0    0    7
 13      1     1       7    0    0    4
         2     3       7    0    1    0
         3     3       7    0    0    1
 14      1     1       5    0    0    8
         2     2       0    7    0    6
         3     2       5    0    0    2
 15      1     1       0    7    5    0
         2     4       3    0    1    0
         3     4       2    0    2    0
 16      1     4       0    6   10    0
         2     5       9    0   10    0
         3    10       0    5    0    4
 17      1     3       0    5    4    0
         2     3       0    6    0    7
         3     7       1    0    0    7
 18      1     7       0    8   10    0
         2    10       2    0    0    8
         3    10       0    8    8    0
 19      1     2       8    0    6    0
         2     4       8    0    0    9
         3     8       0    5    6    0
 20      1     1       0    7    8    0
         2     1       6    0    0    6
         3    10       5    0    0    6
 21      1     2       0    7   10    0
         2     3       3    0   10    0
         3     6       0    6    0    9
 22      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   15   14   56   62
************************************************************************
