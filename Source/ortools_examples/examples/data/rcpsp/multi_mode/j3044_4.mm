************************************************************************
file with basedata            : mf44_.bas
initial value random generator: 347947031
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  32
horizon                       :  235
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     30      0       31       13       31
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5  10  26
   3        3          3           5  10  21
   4        3          3           7  15  16
   5        3          3           6  13  16
   6        3          3           8   9  20
   7        3          2          13  14
   8        3          2          11  25
   9        3          1          31
  10        3          1          12
  11        3          1          18
  12        3          3          15  22  23
  13        3          1          27
  14        3          3          17  18  19
  15        3          2          18  30
  16        3          1          25
  17        3          3          21  25  26
  18        3          2          24  29
  19        3          2          21  24
  20        3          2          24  28
  21        3          3          23  27  28
  22        3          1          28
  23        3          1          29
  24        3          1          31
  25        3          1          27
  26        3          2          30  31
  27        3          1          30
  28        3          1          29
  29        3          1          32
  30        3          1          32
  31        3          1          32
  32        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0    7    2   10
         2     6       0    3    2    8
         3     7       8    0    2    6
  3      1     1       0    6    9    7
         2     3       5    0    6    6
         3     6       5    0    6    2
  4      1     1       0    3    5    7
         2     6       9    0    1    6
         3     6       7    0    2    4
  5      1     1       0    6    5    2
         2     3       0    2    3    1
         3     3       8    0    4    1
  6      1     3       4    0    8   10
         2     8       4    0    7    9
         3     9       3    0    7    9
  7      1     2       8    0    5    2
         2     5       0    1    3    2
         3     6       3    0    2    2
  8      1     7       0    6    5    7
         2    10       0    6    4    6
         3    10      10    0    5    4
  9      1     4       0    5    8   10
         2     5       9    0    4   10
         3     9       1    0    1   10
 10      1     8       0    7    5    7
         2     8       7    0    5   10
         3     9       0    9    5    5
 11      1     1      10    0   10    5
         2     2       8    0    9    3
         3     8       0    2    9    2
 12      1     3       8    0    9    7
         2     7       8    0    9    4
         3     9       8    0    8    3
 13      1     3       5    0    4   10
         2     3       0    6    4   10
         3     9       4    0    4   10
 14      1     1       0    5    5    5
         2     8       0    4    5    5
         3    10       4    0    4    5
 15      1     3       0    8    4   10
         2     6       0    3    4    9
         3    10       3    0    3    9
 16      1     6       3    0    7    9
         2     7       0    9    7    8
         3    10       0    8    7    7
 17      1     4       0    6    6    9
         2     8       9    0    4    9
         3     9       5    0    1    7
 18      1     8       0    6    5    7
         2     9       5    0    4    4
         3     9       3    0    5    5
 19      1     2       0    5   10    7
         2     5       0    3    8    5
         3     9       0    1    5    2
 20      1     3       0    9    7    7
         2     4       0    8    5    7
         3     9       0    5    2    6
 21      1     1       8    0    6    3
         2     2       7    0    6    2
         3     7       0   10    4    1
 22      1     2       9    0   10    4
         2     6       4    0   10    4
         3     7       2    0    9    3
 23      1     4       0    8    6   10
         2     7       0    5    5   10
         3     8       3    0    3   10
 24      1     2       0    7    5    8
         2     6       0    6    5    8
         3     7       0    2    5    6
 25      1     1       5    0    6    2
         2     2       5    0    4    2
         3     2       0    8    4    2
 26      1     2       3    0    5    8
         2     2       0    4    6    8
         3     7       5    0    4    8
 27      1     5       0    8    9    6
         2     5       4    0    9    6
         3     7       0    8    8    6
 28      1     1       0    7   10    3
         2     3       0    6    9    3
         3     5       0    6    8    3
 29      1     2       4    0    5    9
         2     2       0    4    6    6
         3    10       4    0    4    2
 30      1     5       0    3    6    7
         2     6       2    0    6    7
         3     8       2    0    5    7
 31      1     6       0    7    1    7
         2     9       8    0    1    6
         3    10       6    0    1    3
 32      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   34   55  162  179
************************************************************************
