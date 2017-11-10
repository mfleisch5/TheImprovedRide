************************************************************************
file with basedata            : cm239_.bas
initial value random generator: 830803790
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  117
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       24        6       24
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        2          3          10  13  14
   3        2          2          11  13
   4        2          2           5  13
   5        2          2           6   7
   6        2          2          14  15
   7        2          2           8   9
   8        2          3          10  12  14
   9        2          2          11  12
  10        2          2          11  17
  11        2          2          15  16
  12        2          3          15  16  17
  13        2          1          17
  14        2          1          16
  15        2          1          18
  16        2          1          18
  17        2          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     6       3    2    8    7
         2     7       3    1    7    5
  3      1     5       8    6    5    7
         2     6       5    3    5    4
  4      1     1       9    6    7    4
         2     5       9    5    5    3
  5      1     3       7    6    9    7
         2    10       5    3    8    4
  6      1     3       4    5    8    6
         2     9       3    4    6    4
  7      1     2      10    7    5    4
         2     2       8    8    6    5
  8      1     5       8    9    2    8
         2     8       7    8    2    4
  9      1     4       5    9    7    6
         2     4       6    9    6    7
 10      1     2       4    9    4    2
         2     9       4    8    2    2
 11      1     1       4    7    2    6
         2     5       3    3    2    3
 12      1     6       9    7    8    5
         2    10       5    7    8    3
 13      1     5       8    8    8   10
         2     7       7    6    8    5
 14      1     2       4    7    4    5
         2    10       3    7    4    2
 15      1     5       7    7    4    7
         2     7       4    7    4    7
 16      1     5       5    2    8    8
         2     9       4    2    5    5
 17      1     7       6    6    9    9
         2     9       4    5    8    9
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   22   26   89   78
************************************************************************
