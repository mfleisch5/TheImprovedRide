jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	5		2 3 4 5 11 
2	3	5		15 13 10 9 6 
3	3	3		12 9 7 
4	3	2		9 7 
5	3	2		8 7 
6	3	4		19 18 16 12 
7	3	6		23 19 18 17 15 14 
8	3	6		23 19 17 16 15 14 
9	3	6		24 23 19 18 17 16 
10	3	6		24 23 19 18 17 16 
11	3	5		23 18 17 16 15 
12	3	4		24 23 17 14 
13	3	3		23 22 14 
14	3	6		32 29 28 26 21 20 
15	3	6		29 26 25 24 22 21 
16	3	5		32 29 28 26 20 
17	3	5		32 29 28 25 21 
18	3	4		32 26 22 21 
19	3	3		32 28 20 
20	3	3		36 30 25 
21	3	5		40 36 31 30 27 
22	3	4		44 36 31 28 
23	3	6		40 35 34 33 32 30 
24	3	6		36 35 34 33 31 30 
25	3	3		40 31 27 
26	3	3		36 31 27 
27	3	5		44 38 35 34 33 
28	3	5		40 38 35 34 33 
29	3	2		31 30 
30	3	4		44 39 38 37 
31	3	3		47 39 37 
32	3	4		47 43 41 38 
33	3	5		51 47 45 43 41 
34	3	3		47 42 37 
35	3	5		51 50 45 43 42 
36	3	4		51 46 43 41 
37	3	4		51 50 45 43 
38	3	3		51 45 42 
39	3	2		46 41 
40	3	3		50 49 46 
41	3	2		50 42 
42	3	2		49 48 
43	3	2		49 48 
44	3	2		51 49 
45	3	1		46 
46	3	1		48 
47	3	1		48 
48	3	1		52 
49	3	1		52 
50	3	1		52 
51	3	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	
2	1	1	10	6	3	8	
	2	4	7	6	2	7	
	3	9	6	6	2	7	
3	1	6	5	1	4	7	
	2	8	5	1	3	5	
	3	10	5	1	2	5	
4	1	1	9	7	6	5	
	2	2	5	6	6	5	
	3	5	5	4	6	1	
5	1	5	6	3	8	8	
	2	7	4	3	6	7	
	3	10	4	3	5	6	
6	1	2	10	7	7	8	
	2	3	10	5	5	7	
	3	9	10	4	2	6	
7	1	1	9	5	6	3	
	2	2	7	4	4	3	
	3	5	7	3	3	1	
8	1	2	8	10	7	7	
	2	3	7	8	5	7	
	3	8	3	8	3	7	
9	1	4	10	7	8	9	
	2	5	7	7	7	9	
	3	6	3	7	6	9	
10	1	3	6	8	5	7	
	2	5	5	7	5	5	
	3	10	5	4	5	1	
11	1	5	8	10	8	5	
	2	6	6	7	7	3	
	3	9	5	5	5	3	
12	1	2	6	5	7	9	
	2	8	5	5	6	8	
	3	9	5	3	5	8	
13	1	5	7	3	5	8	
	2	8	4	3	3	7	
	3	10	2	3	1	3	
14	1	1	4	4	2	10	
	2	2	3	3	1	6	
	3	6	3	3	1	4	
15	1	1	5	5	8	6	
	2	5	4	5	8	3	
	3	7	4	3	6	3	
16	1	2	8	4	2	9	
	2	5	8	3	1	6	
	3	8	8	2	1	4	
17	1	4	6	1	10	8	
	2	8	4	1	9	8	
	3	9	1	1	8	8	
18	1	5	4	2	6	5	
	2	9	3	1	5	4	
	3	10	3	1	4	2	
19	1	2	5	3	8	8	
	2	8	3	3	6	6	
	3	10	2	3	3	5	
20	1	1	4	9	9	8	
	2	5	4	7	7	4	
	3	7	4	6	7	3	
21	1	1	8	8	8	7	
	2	9	5	8	7	6	
	3	10	5	8	7	5	
22	1	6	9	8	9	7	
	2	7	7	6	6	6	
	3	8	5	6	6	5	
23	1	4	3	4	9	10	
	2	8	3	4	7	9	
	3	9	3	2	6	9	
24	1	1	8	7	9	9	
	2	5	8	5	6	6	
	3	10	7	5	6	4	
25	1	4	7	9	6	5	
	2	7	6	9	6	5	
	3	8	5	9	1	3	
26	1	1	6	7	2	8	
	2	4	5	6	2	6	
	3	5	4	5	2	2	
27	1	3	8	8	9	5	
	2	5	4	6	9	4	
	3	9	4	3	9	3	
28	1	2	7	7	9	6	
	2	3	6	6	9	5	
	3	7	3	4	9	4	
29	1	1	3	6	9	6	
	2	8	3	3	3	3	
	3	10	1	3	2	2	
30	1	1	4	3	7	9	
	2	4	4	2	6	6	
	3	5	4	2	5	2	
31	1	4	8	9	7	4	
	2	7	7	7	4	3	
	3	9	7	1	4	2	
32	1	1	4	6	7	10	
	2	5	3	5	5	5	
	3	9	2	5	4	5	
33	1	1	8	9	7	5	
	2	3	5	9	6	4	
	3	10	5	8	6	3	
34	1	2	9	6	8	4	
	2	3	7	5	4	3	
	3	8	6	4	4	2	
35	1	2	7	5	8	6	
	2	4	7	4	4	6	
	3	5	6	4	2	3	
36	1	4	4	8	5	6	
	2	6	2	7	5	4	
	3	7	2	7	4	4	
37	1	2	8	9	9	8	
	2	4	5	9	8	8	
	3	9	5	9	6	8	
38	1	3	6	6	8	7	
	2	4	6	6	5	4	
	3	8	6	6	3	2	
39	1	2	8	6	10	10	
	2	4	7	4	6	8	
	3	9	4	4	4	6	
40	1	4	7	6	7	6	
	2	5	7	4	5	6	
	3	8	7	3	3	4	
41	1	2	7	5	8	8	
	2	4	6	5	5	8	
	3	10	4	4	4	6	
42	1	4	7	8	6	2	
	2	9	5	7	5	2	
	3	10	5	7	5	1	
43	1	3	4	7	6	5	
	2	4	2	5	5	3	
	3	6	2	1	3	2	
44	1	8	7	9	5	7	
	2	9	3	8	3	3	
	3	10	2	6	3	3	
45	1	4	8	8	9	8	
	2	7	7	7	8	8	
	3	8	5	6	7	8	
46	1	1	8	8	8	6	
	2	3	6	7	7	6	
	3	8	6	7	7	4	
47	1	1	6	2	8	5	
	2	6	6	2	8	4	
	3	7	6	2	8	3	
48	1	3	1	7	7	6	
	2	6	1	3	6	5	
	3	7	1	2	4	4	
49	1	2	5	6	5	10	
	2	5	4	4	4	7	
	3	6	4	3	2	6	
50	1	2	8	2	6	9	
	2	7	3	2	5	5	
	3	9	1	1	5	5	
51	1	1	6	8	9	9	
	2	7	2	4	9	4	
	3	9	1	4	9	2	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	33	34	256	245

************************************************************************
