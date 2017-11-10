jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	9		2 3 4 5 7 8 10 11 12 
2	6	11		30 28 26 25 24 23 22 21 20 19 13 
3	6	8		24 22 21 20 19 17 16 9 
4	6	4		26 21 14 6 
5	6	9		31 29 28 27 26 25 24 21 19 
6	6	7		28 27 25 23 22 20 19 
7	6	7		30 27 26 24 22 21 15 
8	6	5		34 31 30 18 14 
9	6	6		36 31 30 29 28 27 
10	6	6		34 30 29 25 24 19 
11	6	5		31 29 28 25 21 
12	6	5		31 29 28 26 21 
13	6	5		37 34 31 29 18 
14	6	8		51 44 43 42 36 33 29 28 
15	6	8		51 44 43 42 36 33 29 28 
16	6	5		51 43 34 28 25 
17	6	7		49 44 37 36 32 31 30 
18	6	9		51 49 44 42 41 40 36 33 32 
19	6	9		49 44 42 41 40 37 36 35 32 
20	6	6		42 41 35 34 32 31 
21	6	10		51 49 48 44 43 42 40 37 35 34 
22	6	7		43 42 39 36 35 34 29 
23	6	6		49 43 40 37 35 32 
24	6	10		51 50 49 48 47 44 43 40 39 38 
25	6	7		50 44 42 41 40 39 36 
26	6	7		50 49 43 41 39 36 34 
27	6	5		44 41 40 34 33 
28	6	4		49 37 35 32 
29	6	5		49 47 41 40 38 
30	6	5		46 42 41 39 38 
31	6	4		51 43 40 39 
32	6	4		50 48 47 46 
33	6	2		39 35 
34	6	2		47 46 
35	6	1		38 
36	6	1		38 
37	6	1		39 
38	6	1		45 
39	6	1		45 
40	6	1		46 
41	6	1		48 
42	6	1		47 
43	6	1		45 
44	6	1		46 
45	6	1		52 
46	6	1		52 
47	6	1		52 
48	6	1		52 
49	6	1		52 
50	6	1		52 
51	6	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	3	5	4	13	15	11	16	
	2	10	4	3	13	14	11	14	
	3	15	4	2	10	14	11	12	
	4	16	4	2	7	14	10	11	
	5	17	4	1	5	14	10	7	
	6	18	4	1	3	14	9	5	
3	1	9	2	3	6	19	10	8	
	2	10	2	3	5	14	10	6	
	3	12	2	3	4	14	10	6	
	4	17	2	3	3	9	10	6	
	5	18	2	3	3	7	10	5	
	6	19	2	3	2	6	10	4	
4	1	1	2	5	17	12	12	11	
	2	4	1	4	16	12	12	10	
	3	8	1	3	14	12	12	7	
	4	11	1	3	13	11	12	7	
	5	16	1	3	12	11	12	3	
	6	19	1	2	12	10	12	3	
5	1	2	2	1	11	14	13	6	
	2	4	2	1	11	13	11	5	
	3	8	2	1	9	12	9	4	
	4	9	2	1	7	12	8	3	
	5	17	2	1	4	12	6	2	
	6	20	2	1	3	11	5	2	
6	1	4	3	3	11	2	20	16	
	2	6	3	3	9	2	19	15	
	3	7	3	3	7	2	18	14	
	4	8	2	3	7	2	18	11	
	5	12	1	3	5	2	18	9	
	6	15	1	3	3	2	17	6	
7	1	5	1	5	11	8	20	5	
	2	6	1	4	8	8	19	5	
	3	9	1	4	8	7	17	5	
	4	10	1	4	6	6	16	4	
	5	14	1	4	6	3	15	3	
	6	15	1	4	4	2	15	3	
8	1	5	4	4	9	14	12	16	
	2	8	4	4	9	14	11	14	
	3	9	3	4	6	14	11	13	
	4	13	3	4	6	13	10	11	
	5	14	2	4	2	13	8	10	
	6	17	1	4	2	12	7	7	
9	1	2	5	4	14	5	14	18	
	2	10	4	4	12	5	14	18	
	3	11	4	3	10	3	13	17	
	4	14	4	3	8	2	12	17	
	5	19	3	3	4	1	11	16	
	6	20	3	2	4	1	10	15	
10	1	5	3	4	15	8	8	15	
	2	8	2	4	14	8	7	15	
	3	10	2	4	13	8	5	13	
	4	12	2	4	11	8	5	12	
	5	13	2	4	11	7	3	10	
	6	14	2	4	10	7	2	9	
11	1	2	4	4	2	8	6	12	
	2	3	3	4	2	7	6	10	
	3	5	3	4	2	6	6	8	
	4	9	3	4	2	5	6	8	
	5	13	2	3	2	4	5	6	
	6	18	2	3	2	2	5	5	
12	1	5	4	3	8	13	12	15	
	2	6	4	3	8	12	11	12	
	3	14	4	3	7	12	9	10	
	4	15	3	2	6	12	7	9	
	5	19	3	2	5	12	7	6	
	6	20	3	2	4	12	5	5	
13	1	2	4	3	19	15	18	18	
	2	7	3	3	18	12	16	17	
	3	11	3	3	18	10	14	14	
	4	12	2	3	17	8	9	12	
	5	18	2	2	17	6	8	8	
	6	19	2	2	17	4	6	7	
14	1	13	4	3	11	18	19	13	
	2	14	4	3	10	17	18	12	
	3	16	4	3	9	17	16	10	
	4	17	4	3	9	16	15	7	
	5	18	3	3	8	15	13	7	
	6	19	3	3	8	14	13	4	
15	1	2	3	4	17	19	4	11	
	2	3	3	4	16	17	4	11	
	3	4	3	3	15	15	4	10	
	4	5	3	3	14	13	3	7	
	5	9	3	1	13	13	3	6	
	6	13	3	1	13	12	3	6	
16	1	10	4	5	8	10	17	18	
	2	12	3	4	8	9	16	14	
	3	13	2	4	7	9	13	12	
	4	14	2	4	7	7	12	11	
	5	17	2	4	6	5	8	9	
	6	18	1	4	5	5	8	7	
17	1	1	3	4	10	13	16	6	
	2	7	3	4	9	13	16	5	
	3	8	3	4	9	13	13	5	
	4	9	3	4	8	13	7	5	
	5	10	3	4	8	13	7	4	
	6	18	3	4	8	13	4	3	
18	1	1	5	2	6	13	15	12	
	2	4	4	1	5	12	15	12	
	3	6	4	1	4	11	13	8	
	4	11	3	1	2	9	12	6	
	5	14	2	1	2	7	11	5	
	6	17	2	1	1	7	11	3	
19	1	1	4	4	17	13	19	5	
	2	2	3	3	15	11	17	5	
	3	3	3	3	11	10	17	4	
	4	4	3	3	9	8	16	4	
	5	5	3	3	6	4	14	4	
	6	14	3	3	3	4	14	3	
20	1	4	2	4	3	11	10	14	
	2	5	2	4	2	9	10	12	
	3	9	2	3	2	7	9	9	
	4	16	2	3	2	6	8	9	
	5	18	2	2	2	4	6	5	
	6	20	2	1	2	3	5	5	
21	1	1	2	3	19	16	16	17	
	2	3	2	3	16	14	15	16	
	3	4	2	3	15	13	15	15	
	4	14	2	3	14	10	13	11	
	5	15	2	2	11	4	11	8	
	6	16	2	2	10	4	11	8	
22	1	1	4	2	15	9	17	9	
	2	2	3	2	12	7	15	9	
	3	3	2	2	10	7	15	7	
	4	12	2	2	9	6	12	5	
	5	13	1	2	8	6	10	4	
	6	18	1	2	7	5	9	2	
23	1	6	2	4	19	11	17	16	
	2	7	2	3	19	10	13	15	
	3	8	2	3	19	10	12	14	
	4	9	1	3	19	10	10	14	
	5	10	1	3	19	10	9	12	
	6	16	1	3	19	10	6	12	
24	1	2	5	5	16	12	17	11	
	2	7	5	4	13	9	16	11	
	3	8	5	4	11	9	14	11	
	4	11	5	3	10	8	13	10	
	5	16	5	2	7	6	13	10	
	6	17	5	2	6	5	11	10	
25	1	3	5	4	8	9	13	10	
	2	4	4	4	8	7	12	10	
	3	8	3	3	8	7	12	9	
	4	9	3	3	8	5	11	7	
	5	15	3	3	8	5	8	7	
	6	20	2	2	8	4	7	6	
26	1	6	3	1	15	11	7	13	
	2	7	2	1	11	9	6	13	
	3	8	2	1	10	9	5	12	
	4	12	2	1	7	8	3	12	
	5	15	1	1	6	8	3	11	
	6	17	1	1	3	7	1	11	
27	1	7	1	2	11	16	14	4	
	2	10	1	2	9	13	12	4	
	3	11	1	2	9	13	8	4	
	4	12	1	2	7	10	7	4	
	5	13	1	2	6	8	4	4	
	6	19	1	2	5	4	3	4	
28	1	1	3	3	15	16	17	12	
	2	3	2	3	12	15	15	12	
	3	10	2	2	11	15	15	11	
	4	11	2	2	6	15	14	10	
	5	19	1	2	5	15	13	10	
	6	20	1	1	2	15	12	9	
29	1	1	5	4	14	4	4	15	
	2	5	4	4	11	4	3	14	
	3	8	3	4	11	3	3	13	
	4	13	2	4	9	3	2	13	
	5	16	2	4	9	3	1	12	
	6	18	1	4	7	2	1	12	
30	1	3	3	3	15	17	12	13	
	2	10	2	3	15	13	11	13	
	3	12	2	2	14	12	11	13	
	4	13	1	2	14	10	11	13	
	5	14	1	1	13	10	10	13	
	6	16	1	1	13	7	9	13	
31	1	1	5	2	15	17	18	8	
	2	3	5	2	14	16	17	8	
	3	9	5	2	13	14	17	7	
	4	18	5	2	10	11	17	7	
	5	19	5	2	8	11	16	6	
	6	20	5	2	7	8	16	6	
32	1	2	4	2	13	19	15	18	
	2	3	3	2	11	18	14	16	
	3	6	3	2	11	18	14	15	
	4	8	3	2	9	18	14	15	
	5	9	3	2	8	18	14	14	
	6	16	3	2	5	18	14	13	
33	1	2	4	4	11	18	9	8	
	2	5	3	4	9	17	7	7	
	3	11	3	4	9	17	7	6	
	4	13	3	4	8	16	5	4	
	5	16	3	3	5	16	5	4	
	6	18	3	3	5	15	3	2	
34	1	1	3	4	16	14	14	15	
	2	4	3	3	12	12	13	12	
	3	5	3	3	12	12	11	10	
	4	10	3	2	9	11	11	7	
	5	19	3	1	9	9	9	5	
	6	20	3	1	6	8	9	5	
35	1	3	5	5	16	13	7	14	
	2	4	4	4	15	10	6	13	
	3	10	4	4	14	10	6	12	
	4	14	4	4	14	9	5	12	
	5	17	3	3	12	7	4	12	
	6	19	3	3	12	6	3	11	
36	1	9	4	1	15	13	10	17	
	2	10	3	1	15	12	9	17	
	3	11	3	1	14	12	8	17	
	4	12	2	1	13	12	8	16	
	5	13	1	1	13	12	7	16	
	6	15	1	1	12	12	7	16	
37	1	5	5	4	3	4	18	6	
	2	6	4	4	2	4	17	6	
	3	10	4	4	2	4	16	6	
	4	11	4	4	2	3	16	6	
	5	12	4	4	2	2	16	6	
	6	17	4	4	2	2	15	6	
38	1	2	4	5	18	14	13	14	
	2	3	4	4	15	13	13	13	
	3	14	4	4	13	11	10	13	
	4	16	3	4	10	8	9	12	
	5	17	3	3	10	8	8	11	
	6	18	2	3	7	6	7	9	
39	1	6	3	4	10	20	16	18	
	2	7	3	4	9	18	16	17	
	3	8	3	3	8	14	16	16	
	4	11	3	3	7	14	15	16	
	5	12	3	2	5	11	15	14	
	6	19	3	2	5	10	15	12	
40	1	2	3	3	13	13	18	9	
	2	3	3	3	13	13	17	8	
	3	9	3	3	13	13	16	8	
	4	10	3	2	13	13	15	8	
	5	13	2	1	13	13	13	7	
	6	18	2	1	13	13	13	6	
41	1	2	2	1	15	12	14	19	
	2	5	1	1	12	11	13	15	
	3	9	1	1	11	10	11	14	
	4	14	1	1	9	9	9	13	
	5	18	1	1	9	8	7	10	
	6	19	1	1	7	8	7	8	
42	1	1	4	4	8	15	18	7	
	2	3	3	4	8	14	17	6	
	3	12	3	4	7	12	17	5	
	4	15	3	3	7	11	14	5	
	5	16	3	3	7	8	14	3	
	6	17	3	3	6	7	11	3	
43	1	2	5	5	17	20	11	20	
	2	3	5	4	17	15	11	19	
	3	4	5	4	17	15	10	19	
	4	17	5	4	17	10	10	19	
	5	19	5	4	17	9	9	18	
	6	20	5	4	17	7	9	18	
44	1	2	3	5	11	17	9	17	
	2	5	2	4	10	16	9	12	
	3	6	2	4	8	15	8	11	
	4	9	2	3	6	14	8	9	
	5	19	2	3	6	12	7	5	
	6	20	2	3	5	12	6	5	
45	1	4	4	5	20	16	17	15	
	2	8	4	4	19	16	15	13	
	3	11	4	3	17	16	13	13	
	4	16	4	2	17	15	8	13	
	5	17	4	2	16	15	5	12	
	6	18	4	1	15	15	4	11	
46	1	7	5	1	11	11	15	18	
	2	8	4	1	9	10	15	16	
	3	14	4	1	7	10	15	16	
	4	18	4	1	5	9	15	13	
	5	19	3	1	3	6	14	12	
	6	20	3	1	2	6	14	9	
47	1	2	5	3	3	13	19	5	
	2	3	4	2	3	13	17	4	
	3	13	3	2	3	12	15	3	
	4	17	3	2	3	11	15	3	
	5	18	1	1	3	11	14	3	
	6	19	1	1	3	10	11	2	
48	1	3	5	5	8	19	10	19	
	2	6	5	3	8	18	9	16	
	3	8	5	3	7	16	9	15	
	4	13	5	2	7	14	9	12	
	5	18	5	1	7	13	8	10	
	6	19	5	1	6	11	8	9	
49	1	6	2	4	13	11	5	19	
	2	8	1	4	12	9	3	16	
	3	9	1	4	10	8	3	13	
	4	12	1	4	10	6	2	9	
	5	14	1	4	8	5	2	8	
	6	16	1	4	7	5	1	5	
50	1	1	3	2	11	13	16	13	
	2	5	3	2	10	10	15	11	
	3	10	2	2	9	8	13	9	
	4	13	2	1	9	8	10	8	
	5	16	1	1	7	6	6	7	
	6	19	1	1	7	5	4	6	
51	1	2	5	5	13	17	17	13	
	2	3	3	4	11	16	16	11	
	3	10	3	4	10	15	16	10	
	4	15	2	3	9	14	16	9	
	5	17	1	3	7	12	15	9	
	6	18	1	2	7	11	14	7	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2	N 3	N 4
	29	30	546	594	614	575

************************************************************************
