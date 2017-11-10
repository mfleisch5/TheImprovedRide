************************************************************************
file with basedata            : cr441_.bas
initial value random generator: 108945133
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  130
RESOURCES
  - renewable                 :  4   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19        5       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6  10  13
   3        3          3           5   7   8
   4        3          2           9  10
   5        3          2           6  17
   6        3          3           9  12  14
   7        3          2          11  16
   8        3          2           9  14
   9        3          2          15  16
  10        3          3          12  14  17
  11        3          1          13
  12        3          1          15
  13        3          2          15  17
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
  2      1     3       5    0    8    0    6    6
         2     9       3    2    0    7    4    3
         3     9       0    3    0    6    5    2
  3      1     2       0    7    0    0    7    6
         2     2       7    7    0    5    6    8
         3     8       5    0    6    1    5    5
  4      1     1      10    4    4   10    6    9
         2    10       9    2    3    9    5    2
         3    10       0    4    0    0    5    4
  5      1     1       3    0    0    8    7    7
         2     5       0    0    7    8    5    5
         3     5       2    0    7    8    6    4
  6      1     5       9    0    4    3    2    2
         2     7       5    7    3    0    2    2
         3     8       4    5    0    0    2    1
  7      1     3       9    0    0    0    6    2
         2     4       6    0    9    4    4    1
         3     6       5    0    0    0    3    1
  8      1     4       0    5    0   10    7    4
         2     8       3    4    0    0    6    3
         3     9       0    0    3    0    4    3
  9      1     5       0    6    0    2    8   10
         2    10      10    0    3    0    7    7
         3    10       9    0    4    0    7    8
 10      1     1       0    0    7    0   10    8
         2     3       6    0    5    1    8    5
         3     7       0    5    2    0    7    5
 11      1     2       8    0    6    0    7    9
         2     7       0    0    5    7    7    8
         3     8       0    0    0    5    5    7
 12      1     6       0    0    0    8    7    6
         2     7       0    7    6    5    7    6
         3     8       0    0    5    0    6    5
 13      1     3       0    0    5    2    7    8
         2     4       0    6    0    1    5    7
         3     7       0    0    0    1    4    7
 14      1     1       0    0    8    0    3    7
         2     6       3    4    5    0    3    6
         3    10       3    0    0    8    2    4
 15      1     5       0    0    6    9    8    5
         2     8       0    4    0    7    8    5
         3     9       0    2    2    3    7    5
 16      1     2       0    5    0    3    8    6
         2     3       0    4    8    0    7    5
         3     7       7    0    0    0    7    5
 17      1     3       0    0    0    7    5    9
         2     4       0    0    4    0    3    8
         3     9       0    0    0    7    3    8
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
   11    6    7   13   90   89
************************************************************************
