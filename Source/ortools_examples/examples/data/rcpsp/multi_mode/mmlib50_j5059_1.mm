jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	11		2 3 4 5 7 8 9 11 12 14 23 
2	3	6		21 19 18 16 13 6 
3	3	5		27 20 17 15 10 
4	3	6		29 27 25 24 21 13 
5	3	6		32 22 18 16 15 13 
6	3	5		36 27 25 20 10 
7	3	8		36 34 33 29 28 25 24 21 
8	3	4		32 24 18 15 
9	3	9		41 37 36 35 34 33 28 25 20 
10	3	7		34 32 30 29 28 24 22 
11	3	6		36 32 28 26 25 17 
12	3	6		37 34 33 27 25 24 
13	3	6		40 36 34 30 28 17 
14	3	4		33 29 26 19 
15	3	8		41 40 37 36 34 33 31 25 
16	3	8		51 50 41 39 37 35 33 26 
17	3	10		51 50 49 47 41 39 37 35 33 31 
18	3	7		51 50 37 36 33 31 26 
19	3	7		51 50 49 41 35 34 28 
20	3	6		50 39 32 31 30 26 
21	3	7		50 49 41 39 32 31 30 
22	3	8		51 50 49 48 47 40 39 33 
23	3	7		51 50 49 48 47 39 31 
24	3	3		35 31 26 
25	3	5		50 49 46 43 30 
26	3	9		49 48 47 46 45 44 43 40 38 
27	3	6		49 47 43 41 40 35 
28	3	3		48 47 31 
29	3	6		50 48 47 44 43 37 
30	3	6		51 48 47 45 44 42 
31	3	5		46 45 44 43 38 
32	3	5		47 45 44 43 42 
33	3	4		45 44 43 38 
34	3	4		45 43 42 39 
35	3	2		48 42 
36	3	2		44 43 
37	3	1		38 
38	3	1		42 
39	3	1		46 
40	3	1		42 
41	3	1		46 
42	3	1		52 
43	3	1		52 
44	3	1		52 
45	3	1		52 
46	3	1		52 
47	3	1		52 
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
2	1	2	9	8	0	4	
	2	4	9	6	0	4	
	3	5	7	2	0	4	
3	1	8	10	6	6	0	
	2	10	9	5	0	2	
	3	10	9	4	2	0	
4	1	1	8	7	0	2	
	2	2	7	5	0	2	
	3	4	6	1	0	2	
5	1	2	6	4	0	4	
	2	4	5	2	5	0	
	3	6	3	1	0	4	
6	1	2	5	5	0	8	
	2	8	5	3	2	0	
	3	9	5	3	0	4	
7	1	3	5	8	9	0	
	2	5	4	7	7	0	
	3	5	4	4	0	4	
8	1	3	7	6	0	7	
	2	5	7	6	10	0	
	3	9	7	6	0	6	
9	1	5	6	10	3	0	
	2	6	4	5	0	6	
	3	6	4	2	3	0	
10	1	4	7	8	0	9	
	2	6	5	7	8	0	
	3	6	5	4	0	7	
11	1	3	9	1	0	5	
	2	6	7	1	0	4	
	3	8	6	1	0	3	
12	1	2	8	8	0	3	
	2	7	4	6	5	0	
	3	8	1	5	3	0	
13	1	2	5	5	2	0	
	2	3	4	4	2	0	
	3	6	4	4	1	0	
14	1	3	4	7	0	8	
	2	6	4	4	0	7	
	3	9	4	4	3	0	
15	1	4	7	10	0	9	
	2	8	7	6	7	0	
	3	10	3	6	3	0	
16	1	4	9	10	5	0	
	2	7	9	9	4	0	
	3	9	9	9	3	0	
17	1	4	8	5	0	8	
	2	5	6	3	0	8	
	3	8	3	2	0	8	
18	1	2	10	8	0	10	
	2	4	10	5	0	4	
	3	5	10	3	0	1	
19	1	1	3	8	4	0	
	2	5	3	6	0	6	
	3	9	3	5	0	6	
20	1	1	3	3	7	0	
	2	7	3	3	0	5	
	3	8	3	3	6	0	
21	1	4	6	3	9	0	
	2	8	4	3	0	6	
	3	8	4	3	8	0	
22	1	3	6	5	8	0	
	2	7	5	5	6	0	
	3	10	3	2	3	0	
23	1	4	5	7	4	0	
	2	5	4	7	3	0	
	3	10	4	2	0	1	
24	1	1	9	2	0	7	
	2	2	5	1	5	0	
	3	5	3	1	0	2	
25	1	1	7	7	7	0	
	2	3	6	4	0	6	
	3	7	3	4	0	6	
26	1	2	5	7	0	7	
	2	4	4	3	8	0	
	3	7	3	3	7	0	
27	1	4	9	9	0	6	
	2	6	9	4	6	0	
	3	6	9	2	0	2	
28	1	2	6	8	9	0	
	2	6	4	7	8	0	
	3	9	2	7	0	1	
29	1	4	3	10	6	0	
	2	5	3	8	3	0	
	3	9	3	5	0	4	
30	1	3	10	3	9	0	
	2	4	9	2	9	0	
	3	9	7	2	9	0	
31	1	2	6	10	5	0	
	2	7	5	10	0	7	
	3	10	3	10	2	0	
32	1	2	5	9	9	0	
	2	3	5	7	0	4	
	3	4	4	7	9	0	
33	1	4	4	4	4	0	
	2	5	4	4	3	0	
	3	5	3	4	0	8	
34	1	6	8	2	3	0	
	2	7	7	1	0	6	
	3	10	6	1	2	0	
35	1	1	9	8	0	8	
	2	1	7	5	5	0	
	3	8	7	3	0	8	
36	1	3	6	6	9	0	
	2	4	6	5	5	0	
	3	9	6	5	0	3	
37	1	6	8	2	0	6	
	2	10	6	2	0	2	
	3	10	6	1	5	0	
38	1	6	7	3	9	0	
	2	7	4	3	0	3	
	3	8	3	2	0	2	
39	1	3	8	8	0	6	
	2	3	4	8	3	0	
	3	10	3	7	3	0	
40	1	1	8	5	9	0	
	2	3	7	4	0	8	
	3	7	6	2	0	7	
41	1	2	8	6	0	7	
	2	4	8	5	0	4	
	3	6	8	2	0	3	
42	1	1	4	6	0	6	
	2	2	2	5	0	6	
	3	3	1	5	0	2	
43	1	2	8	7	0	7	
	2	7	6	5	0	5	
	3	10	6	5	0	4	
44	1	5	8	3	7	0	
	2	7	7	2	6	0	
	3	8	7	2	0	10	
45	1	1	8	5	0	6	
	2	3	6	4	2	0	
	3	7	4	2	2	0	
46	1	2	4	7	7	0	
	2	4	3	6	3	0	
	3	7	3	4	0	2	
47	1	6	6	4	0	2	
	2	8	5	3	0	2	
	3	10	4	3	0	2	
48	1	5	6	6	0	6	
	2	6	4	6	2	0	
	3	7	3	6	2	0	
49	1	2	7	7	0	8	
	2	4	5	7	5	0	
	3	5	3	6	0	8	
50	1	2	7	8	0	3	
	2	3	4	7	0	2	
	3	7	1	7	0	2	
51	1	4	9	9	0	9	
	2	5	5	8	0	8	
	3	6	2	8	0	8	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	43	41	177	207

************************************************************************
