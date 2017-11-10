jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	11		2 3 4 6 7 8 9 11 12 14 16 
2	3	6		33 27 19 18 15 10 
3	3	9		42 30 27 24 22 21 18 17 13 
4	3	3		18 13 5 
5	3	8		42 32 30 26 24 22 21 17 
6	3	8		42 32 27 26 24 22 21 18 
7	3	6		33 32 24 22 20 17 
8	3	4		22 21 18 13 
9	3	6		32 26 24 22 18 17 
10	3	5		42 32 22 20 17 
11	3	3		42 25 15 
12	3	5		33 30 27 22 18 
13	3	8		41 40 36 32 29 26 25 23 
14	3	7		40 30 29 28 27 25 21 
15	3	4		36 32 30 17 
16	3	9		51 41 38 33 31 29 28 26 24 
17	3	8		50 41 40 39 37 31 29 23 
18	3	7		50 40 37 36 31 29 23 
19	3	6		41 38 30 28 26 25 
20	3	7		50 49 40 36 31 28 26 
21	3	6		51 48 41 38 33 31 
22	3	3		48 38 25 
23	3	6		51 49 48 38 35 28 
24	3	7		49 48 45 39 37 36 34 
25	3	5		50 49 45 39 31 
26	3	5		48 45 37 35 34 
27	3	6		50 49 48 47 44 37 
28	3	4		47 46 45 34 
29	3	4		48 45 35 34 
30	3	3		48 45 34 
31	3	2		46 34 
32	3	3		50 49 47 
33	3	3		49 45 43 
34	3	2		44 43 
35	3	2		44 43 
36	3	2		46 44 
37	3	1		46 
38	3	1		43 
39	3	1		47 
40	3	1		45 
41	3	1		47 
42	3	1		43 
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
2	1	2	9	9	5	4	
	2	9	8	8	4	4	
	3	10	8	8	4	3	
3	1	1	9	8	5	7	
	2	6	8	7	4	6	
	3	7	5	5	2	3	
4	1	6	8	1	7	6	
	2	6	6	1	5	7	
	3	7	6	1	5	6	
5	1	2	3	9	5	9	
	2	9	3	7	4	8	
	3	10	1	7	4	7	
6	1	2	5	6	9	5	
	2	4	5	5	6	4	
	3	6	4	3	6	4	
7	1	4	5	5	5	4	
	2	5	4	4	3	2	
	3	10	3	3	1	1	
8	1	4	8	6	10	4	
	2	7	8	6	8	2	
	3	8	6	5	7	2	
9	1	3	7	9	5	6	
	2	9	7	6	4	3	
	3	10	7	4	4	2	
10	1	5	6	6	8	8	
	2	6	6	5	7	6	
	3	7	4	5	6	4	
11	1	2	5	3	9	8	
	2	3	4	1	8	8	
	3	10	3	1	6	8	
12	1	2	9	3	9	8	
	2	4	7	3	9	6	
	3	5	7	2	9	3	
13	1	1	8	9	1	6	
	2	3	6	5	1	6	
	3	4	6	3	1	2	
14	1	2	8	9	6	9	
	2	3	5	9	5	7	
	3	9	5	9	4	7	
15	1	1	5	8	7	6	
	2	2	4	6	5	5	
	3	4	2	4	5	4	
16	1	4	4	7	4	5	
	2	6	2	6	2	5	
	3	7	2	5	2	4	
17	1	2	6	6	7	4	
	2	3	5	3	6	4	
	3	8	1	1	4	2	
18	1	2	9	4	5	5	
	2	4	8	3	4	3	
	3	6	8	3	3	3	
19	1	1	5	4	6	6	
	2	3	4	4	6	6	
	3	4	3	4	4	6	
20	1	4	8	5	10	1	
	2	6	8	4	6	1	
	3	7	8	4	5	1	
21	1	2	5	7	8	9	
	2	3	3	6	8	9	
	3	5	2	5	8	9	
22	1	4	6	9	8	3	
	2	5	4	8	6	2	
	3	10	3	8	4	2	
23	1	4	7	7	4	9	
	2	5	7	7	3	7	
	3	8	6	6	3	6	
24	1	4	7	3	8	7	
	2	5	7	2	8	5	
	3	10	7	1	6	3	
25	1	3	3	8	5	6	
	2	4	3	6	5	3	
	3	5	3	4	5	2	
26	1	1	7	10	7	7	
	2	2	7	4	7	7	
	3	3	5	4	3	7	
27	1	3	5	6	4	1	
	2	5	5	5	4	1	
	3	6	5	5	2	1	
28	1	2	10	9	6	6	
	2	7	8	7	5	5	
	3	9	6	3	3	5	
29	1	1	9	6	8	9	
	2	9	6	5	7	8	
	3	10	5	5	7	6	
30	1	3	8	8	5	3	
	2	4	7	7	5	2	
	3	5	2	5	3	2	
31	1	1	3	5	5	8	
	2	7	2	4	4	7	
	3	8	2	3	2	6	
32	1	1	8	9	9	5	
	2	5	7	8	8	3	
	3	9	5	8	7	3	
33	1	2	3	5	4	10	
	2	5	3	4	3	10	
	3	6	2	3	2	10	
34	1	4	5	8	5	4	
	2	6	4	8	5	4	
	3	10	3	7	5	4	
35	1	2	10	5	8	8	
	2	4	8	4	8	5	
	3	5	7	4	8	3	
36	1	2	7	3	6	8	
	2	9	5	3	6	6	
	3	10	5	2	4	6	
37	1	3	6	3	10	8	
	2	8	6	2	7	7	
	3	10	5	2	1	4	
38	1	5	10	6	4	3	
	2	8	9	5	2	3	
	3	9	9	4	2	2	
39	1	3	3	6	3	8	
	2	5	2	6	3	8	
	3	7	2	1	2	6	
40	1	2	5	4	6	7	
	2	3	4	3	5	7	
	3	4	3	3	5	7	
41	1	5	3	1	2	8	
	2	8	3	1	2	4	
	3	9	3	1	2	2	
42	1	3	6	8	7	6	
	2	4	4	6	3	6	
	3	10	3	6	3	5	
43	1	2	8	7	10	4	
	2	3	7	4	9	2	
	3	9	4	4	9	1	
44	1	8	4	2	4	6	
	2	9	3	2	4	4	
	3	10	1	2	4	3	
45	1	2	3	4	8	10	
	2	5	3	4	7	7	
	3	8	3	4	7	6	
46	1	1	9	9	10	5	
	2	4	7	7	8	4	
	3	7	7	5	8	2	
47	1	1	2	7	7	5	
	2	5	2	7	6	4	
	3	7	2	7	6	3	
48	1	3	8	6	8	9	
	2	5	5	5	5	7	
	3	6	1	5	3	7	
49	1	1	9	7	5	6	
	2	2	6	6	4	4	
	3	8	6	5	1	3	
50	1	6	8	8	7	8	
	2	7	7	8	7	8	
	3	8	4	8	7	8	
51	1	3	4	2	8	8	
	2	4	3	2	8	8	
	3	6	3	2	8	7	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	26	24	247	240

************************************************************************
