************************************************************************
file with basedata            : cr424_.bas
initial value random generator: 2103791086
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  137
RESOURCES
  - renewable                 :  4   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       28        5       28
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          11  15
   3        3          3           5   9  13
   4        3          3           6   8  11
   5        3          3           7  10  17
   6        3          2          12  13
   7        3          3          11  12  14
   8        3          2           9  15
   9        3          1          10
  10        3          2          12  14
  11        3          1          16
  12        3          1          16
  13        3          3          14  15  17
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0
  2      1     4       3    7    5    7    0    2
         2     7       3    4    3    5    5    0
         3    10       3    4    3    1    4    0
  3      1     5       9    9    7    7    0    7
         2    10       7    4    5    7    5    0
         3    10       5    1    6    7    7    0
  4      1     6      10    8    8    7    9    0
         2     6      10    8    8    7    0    3
         3    10      10    7    7    5    0    3
  5      1     4       2    4    5   10    8    0
         2     5       2    4    3    9    8    0
         3     6       2    3    3    9    8    0
  6      1     3       8    5    2    9    0    8
         2     6       8    5    1    9    6    0
         3     7       6    5    1    9    0    3
  7      1     2       6    8    8    1    5    0
         2     8       3    4    5    1    0    8
         3     9       2    3    2    1    3    0
  8      1     6       8    8    2    8    0    6
         2     7       6    8    2    8    8    0
         3     9       3    8    1    8    4    0
  9      1     1       9    5    6    9    9    0
         2     8       4    3    4    8    0    4
         3     8       7    3    3    8    3    0
 10      1     5       9    6    6    2    0    8
         2     7       4    6    5    1    0    6
         3     9       4    6    4    1    6    0
 11      1     3       8    3    9    8    9    0
         2     7       8    3    8    7    7    0
         3    10       7    3    7    6    6    0
 12      1     1       9    6    2    8    2    0
         2     2       6    6    1    6    0    3
         3     9       4    6    1    6    0    2
 13      1     1       9    7    1    5    0    6
         2     2       8    4    1    3    0    5
         3     8       8    3    1    3    0    5
 14      1     6      10    8    8    8    6    0
         2    10       7    8    5    6    0    5
         3    10       7    8    5    8    6    0
 15      1     5       3    7    7    3    8    0
         2     6       2    6    5    3    5    0
         3     7       2    6    3    2    5    0
 16      1     4       7   10    6    8    0    7
         2     6       5   10    3    7    0    6
         3     8       3   10    3    7    0    6
 17      1     1      10    9    2    9    5    0
         2     5       8    6    1    9    0    9
         3     7       7    5    1    8    0    3
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
   24   25   22   27   75   60
************************************************************************
