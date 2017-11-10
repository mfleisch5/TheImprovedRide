jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	7		2 3 4 5 8 10 15 
2	9	4		22 13 7 6 
3	9	10		27 26 24 21 20 18 16 14 13 12 
4	9	7		26 24 23 22 14 11 7 
5	9	6		27 26 24 22 16 9 
6	9	7		34 30 29 26 24 17 16 
7	9	9		35 31 29 28 25 21 20 19 18 
8	9	9		39 30 29 27 26 24 23 19 18 
9	9	7		34 30 29 25 23 21 13 
10	9	6		34 31 30 26 24 14 
11	9	8		51 40 38 33 32 30 27 21 
12	9	7		42 40 39 33 31 30 25 
13	9	3		42 33 17 
14	9	6		51 42 39 33 29 25 
15	9	6		40 34 32 31 30 21 
16	9	4		49 35 25 23 
17	9	5		51 39 38 31 28 
18	9	8		51 50 49 48 40 36 33 32 
19	9	8		50 49 47 42 38 36 34 32 
20	9	7		47 41 40 38 34 32 30 
21	9	7		50 49 47 42 39 37 36 
22	9	7		51 49 48 47 40 37 36 
23	9	6		51 50 48 37 36 33 
24	9	6		49 47 42 40 37 36 
25	9	5		50 47 38 36 32 
26	9	7		50 49 48 45 41 37 35 
27	9	7		50 49 48 45 41 37 35 
28	9	5		50 49 47 36 32 
29	9	8		50 49 47 46 45 44 41 38 
30	9	7		50 49 48 46 45 44 43 
31	9	5		49 47 45 44 41 
32	9	3		45 43 37 
33	9	3		47 46 45 
34	9	3		46 44 43 
35	9	3		47 44 43 
36	9	2		44 41 
37	9	2		46 44 
38	9	2		48 43 
39	9	2		45 43 
40	9	2		45 43 
41	9	1		43 
42	9	1		48 
43	9	1		52 
44	9	1		52 
45	9	1		52 
46	9	1		52 
47	9	1		52 
48	9	1		52 
49	9	1		52 
50	9	1		52 
51	9	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	
2	1	3	29	25	24	26	
	2	9	26	23	24	25	
	3	10	25	21	24	22	
	4	11	22	21	24	16	
	5	12	20	17	24	15	
	6	14	20	15	24	11	
	7	20	16	15	24	10	
	8	23	16	11	24	6	
	9	30	13	9	24	3	
3	1	1	21	26	22	30	
	2	5	19	25	19	29	
	3	6	16	23	18	27	
	4	7	14	23	16	26	
	5	8	13	22	13	26	
	6	9	13	21	13	26	
	7	11	11	19	9	24	
	8	13	9	19	9	24	
	9	19	6	18	6	23	
4	1	3	11	27	21	21	
	2	7	11	24	21	20	
	3	12	11	23	21	20	
	4	13	11	20	20	19	
	5	14	11	20	20	18	
	6	15	11	18	20	19	
	7	17	11	16	19	19	
	8	19	11	14	19	18	
	9	21	11	13	19	18	
5	1	2	13	9	13	29	
	2	6	12	8	11	26	
	3	7	10	7	11	21	
	4	10	8	6	9	18	
	5	14	8	6	8	15	
	6	15	6	5	8	15	
	7	18	5	3	6	10	
	8	20	4	3	6	7	
	9	24	3	2	4	4	
6	1	5	25	29	24	18	
	2	11	23	28	24	16	
	3	13	21	25	24	15	
	4	14	18	25	24	13	
	5	16	14	21	23	10	
	6	17	12	20	23	9	
	7	19	11	20	23	7	
	8	24	6	18	23	3	
	9	25	6	15	23	3	
7	1	11	22	15	3	26	
	2	13	21	14	2	20	
	3	14	20	13	2	18	
	4	15	19	11	2	17	
	5	16	19	11	1	14	
	6	20	18	10	1	10	
	7	23	17	7	1	7	
	8	25	16	6	1	5	
	9	28	16	6	1	1	
8	1	1	21	26	29	21	
	2	11	20	26	28	20	
	3	12	20	25	28	18	
	4	14	19	23	28	17	
	5	17	19	23	28	15	
	6	18	19	22	28	12	
	7	20	18	21	28	9	
	8	27	17	20	28	8	
	9	28	17	19	28	5	
9	1	2	24	21	29	18	
	2	3	20	19	27	15	
	3	4	19	19	26	15	
	4	6	18	18	25	13	
	5	14	16	17	24	10	
	6	16	16	17	24	9	
	7	20	13	17	22	8	
	8	27	12	15	21	5	
	9	28	10	15	21	5	
10	1	14	24	26	19	27	
	2	19	22	24	17	26	
	3	21	20	23	17	26	
	4	23	19	22	15	26	
	5	26	16	19	14	26	
	6	27	13	17	11	26	
	7	28	12	15	11	26	
	8	29	8	14	10	26	
	9	30	7	10	8	26	
11	1	1	27	26	17	27	
	2	7	26	20	17	27	
	3	9	26	18	17	27	
	4	16	25	15	16	27	
	5	17	23	14	15	26	
	6	18	22	12	15	26	
	7	20	21	8	15	26	
	8	21	21	5	14	25	
	9	23	19	3	14	25	
12	1	7	19	30	12	7	
	2	10	18	29	12	7	
	3	12	17	27	12	6	
	4	13	15	27	12	5	
	5	14	14	26	12	5	
	6	17	13	25	12	4	
	7	23	12	24	12	3	
	8	27	9	23	12	3	
	9	28	8	22	12	2	
13	1	8	27	26	18	23	
	2	15	27	24	16	21	
	3	16	27	23	15	20	
	4	17	27	22	13	19	
	5	18	26	19	12	17	
	6	19	26	19	12	16	
	7	24	26	18	9	14	
	8	28	25	17	9	13	
	9	29	25	15	7	11	
14	1	5	26	22	27	28	
	2	6	26	19	24	25	
	3	8	25	17	22	22	
	4	9	25	17	21	17	
	5	12	24	16	18	15	
	6	13	24	14	17	13	
	7	21	23	12	15	8	
	8	22	22	11	13	6	
	9	30	22	10	11	5	
15	1	2	25	14	13	28	
	2	8	25	13	12	28	
	3	12	25	13	11	28	
	4	13	25	13	10	27	
	5	22	25	13	9	27	
	6	27	24	13	8	26	
	7	28	24	13	8	25	
	8	28	24	13	6	26	
	9	29	24	13	6	25	
16	1	2	30	29	18	5	
	2	3	24	29	17	5	
	3	4	24	29	15	5	
	4	6	20	29	14	5	
	5	7	15	29	14	5	
	6	11	13	29	14	5	
	7	12	12	29	12	5	
	8	16	8	29	12	5	
	9	17	4	29	11	5	
17	1	2	26	29	14	19	
	2	4	24	24	12	16	
	3	5	23	20	12	15	
	4	11	22	19	10	15	
	5	14	22	15	8	13	
	6	18	22	14	8	13	
	7	19	21	11	5	11	
	8	21	20	7	4	11	
	9	30	19	4	4	9	
18	1	3	28	17	23	27	
	2	4	26	16	21	26	
	3	11	24	15	19	25	
	4	14	22	13	17	25	
	5	15	21	13	14	24	
	6	17	20	11	12	24	
	7	18	19	11	8	23	
	8	28	18	9	3	23	
	9	30	16	9	2	23	
19	1	6	15	18	28	23	
	2	11	14	16	25	23	
	3	15	13	15	24	21	
	4	17	11	14	24	20	
	5	18	8	14	21	18	
	6	20	8	13	21	17	
	7	26	7	13	19	16	
	8	29	5	11	16	14	
	9	30	4	11	15	13	
20	1	6	21	30	28	19	
	2	8	21	28	27	17	
	3	9	19	27	26	17	
	4	13	19	27	26	16	
	5	16	18	26	25	12	
	6	21	17	26	24	12	
	7	25	15	24	24	10	
	8	26	14	23	24	8	
	9	29	14	23	23	6	
21	1	6	28	13	27	21	
	2	10	27	11	26	19	
	3	15	25	10	26	17	
	4	16	24	9	26	15	
	5	19	24	6	25	14	
	6	20	22	6	25	13	
	7	21	21	5	25	11	
	8	27	21	4	25	9	
	9	29	20	2	25	8	
22	1	7	28	27	14	8	
	2	10	24	26	13	7	
	3	11	23	24	13	6	
	4	12	22	21	12	5	
	5	15	17	21	10	5	
	6	19	15	18	9	4	
	7	22	12	16	8	4	
	8	24	11	14	7	3	
	9	30	7	12	6	3	
23	1	4	22	19	24	23	
	2	5	20	17	20	23	
	3	6	17	17	18	22	
	4	7	17	17	17	22	
	5	10	15	15	12	20	
	6	18	12	15	12	20	
	7	21	10	15	9	20	
	8	25	9	14	6	19	
	9	28	5	13	4	18	
24	1	3	24	26	29	6	
	2	4	23	25	24	6	
	3	11	23	22	23	6	
	4	12	21	21	22	5	
	5	13	21	18	20	4	
	6	24	20	16	16	4	
	7	26	19	15	16	3	
	8	27	18	13	12	3	
	9	28	18	11	10	3	
25	1	1	12	19	27	25	
	2	5	11	17	26	24	
	3	12	11	14	26	24	
	4	13	11	13	25	24	
	5	17	10	11	25	23	
	6	19	10	9	25	23	
	7	24	10	8	25	23	
	8	26	10	5	24	22	
	9	29	10	4	24	22	
26	1	1	25	25	24	25	
	2	5	24	24	23	23	
	3	6	23	23	23	22	
	4	7	22	21	22	22	
	5	9	20	20	22	19	
	6	12	19	20	21	17	
	7	20	18	18	20	15	
	8	24	18	16	20	13	
	9	25	17	16	20	13	
27	1	6	14	20	24	27	
	2	7	14	19	21	24	
	3	9	13	19	18	21	
	4	10	12	19	15	21	
	5	11	12	18	14	18	
	6	13	11	18	11	16	
	7	19	10	17	9	16	
	8	22	9	17	6	13	
	9	25	9	17	5	11	
28	1	1	15	24	20	15	
	2	3	15	23	20	15	
	3	5	15	22	19	14	
	4	11	15	22	18	12	
	5	12	15	21	18	12	
	6	15	15	20	17	10	
	7	16	15	19	16	9	
	8	29	15	19	15	7	
	9	30	15	18	15	7	
29	1	4	27	4	23	22	
	2	11	27	4	22	22	
	3	14	23	4	19	19	
	4	20	20	4	16	18	
	5	22	20	4	16	14	
	6	24	18	4	13	12	
	7	25	14	4	11	11	
	8	26	11	4	8	8	
	9	28	10	4	8	6	
30	1	3	11	26	17	29	
	2	6	11	25	16	26	
	3	9	10	25	15	23	
	4	15	8	25	13	22	
	5	18	8	24	12	18	
	6	19	6	23	12	15	
	7	22	4	22	11	15	
	8	27	3	21	10	12	
	9	29	2	21	9	11	
31	1	8	22	27	18	13	
	2	15	19	23	16	12	
	3	16	17	21	14	12	
	4	17	16	20	13	10	
	5	19	15	18	13	10	
	6	22	12	16	11	9	
	7	25	12	15	9	8	
	8	28	9	13	7	8	
	9	29	8	9	6	7	
32	1	12	21	3	26	26	
	2	18	21	3	25	25	
	3	19	20	3	25	23	
	4	20	20	3	25	21	
	5	21	20	3	24	15	
	6	22	19	3	24	14	
	7	23	18	3	24	10	
	8	24	18	3	23	7	
	9	25	18	3	23	6	
33	1	1	26	29	20	7	
	2	2	25	29	18	7	
	3	5	23	29	18	7	
	4	13	23	29	17	7	
	5	16	21	28	15	6	
	6	17	19	28	15	6	
	7	21	19	28	14	6	
	8	26	18	27	13	5	
	9	27	16	27	12	5	
34	1	4	19	21	25	27	
	2	8	18	18	24	26	
	3	9	17	16	23	24	
	4	10	15	16	23	23	
	5	13	14	14	22	22	
	6	16	14	12	20	21	
	7	17	13	10	20	20	
	8	22	11	9	18	19	
	9	29	10	9	18	19	
35	1	1	23	11	4	5	
	2	2	21	11	4	4	
	3	4	21	10	3	4	
	4	5	19	8	3	4	
	5	11	19	8	3	3	
	6	21	17	7	2	3	
	7	22	17	7	1	3	
	8	25	16	5	1	3	
	9	26	14	5	1	3	
36	1	4	18	17	22	6	
	2	11	17	15	20	4	
	3	13	15	15	19	4	
	4	14	15	13	16	4	
	5	16	13	12	16	3	
	6	26	13	9	12	2	
	7	27	12	7	11	2	
	8	28	11	7	9	2	
	9	29	10	5	7	1	
37	1	6	30	21	21	25	
	2	12	30	21	20	24	
	3	14	30	19	20	22	
	4	15	30	18	19	22	
	5	18	30	17	19	21	
	6	20	30	14	18	21	
	7	23	30	12	18	19	
	8	25	30	12	18	18	
	9	27	30	11	17	18	
38	1	7	28	29	10	27	
	2	8	26	27	9	23	
	3	9	26	26	9	22	
	4	10	26	23	9	20	
	5	15	25	23	8	18	
	6	16	24	22	8	16	
	7	20	24	20	7	15	
	8	29	23	18	7	12	
	9	30	22	18	7	11	
39	1	4	12	19	24	29	
	2	5	12	19	23	26	
	3	12	12	17	23	25	
	4	14	12	16	22	22	
	5	17	12	15	22	22	
	6	18	12	14	21	20	
	7	20	12	14	21	17	
	8	25	12	13	20	17	
	9	27	12	12	19	15	
40	1	5	21	26	24	22	
	2	6	20	24	22	22	
	3	10	17	23	21	21	
	4	11	17	21	21	20	
	5	20	15	20	19	19	
	6	22	13	19	18	17	
	7	23	10	16	17	16	
	8	24	8	14	17	15	
	9	28	7	14	16	14	
41	1	9	27	12	20	23	
	2	10	25	10	20	21	
	3	13	24	9	20	20	
	4	15	22	8	20	17	
	5	16	22	6	20	15	
	6	20	20	6	20	14	
	7	21	19	4	20	11	
	8	22	18	4	20	9	
	9	26	17	3	20	8	
42	1	5	13	29	17	21	
	2	6	13	29	16	17	
	3	8	11	28	15	16	
	4	19	10	27	14	13	
	5	23	10	26	13	13	
	6	24	8	25	12	10	
	7	27	8	24	10	9	
	8	28	7	24	10	7	
	9	30	6	23	9	4	
43	1	13	26	30	21	29	
	2	14	25	26	20	26	
	3	15	25	26	18	26	
	4	16	23	23	18	23	
	5	17	23	21	16	23	
	6	18	22	18	15	21	
	7	21	21	17	12	20	
	8	26	21	16	10	18	
	9	28	20	13	9	17	
44	1	1	20	28	6	30	
	2	10	19	23	5	26	
	3	11	18	23	5	24	
	4	12	18	20	5	21	
	5	13	18	15	4	18	
	6	14	17	13	4	15	
	7	16	16	7	4	14	
	8	25	16	5	4	10	
	9	30	16	4	4	9	
45	1	1	22	21	26	25	
	2	4	22	18	24	22	
	3	6	21	16	23	21	
	4	13	20	15	21	21	
	5	14	20	12	20	19	
	6	15	20	11	19	18	
	7	18	19	7	18	17	
	8	20	19	7	18	15	
	9	30	18	5	16	14	
46	1	3	9	22	23	9	
	2	4	9	19	22	8	
	3	7	9	18	20	8	
	4	8	9	15	19	8	
	5	17	8	14	17	8	
	6	20	8	12	16	7	
	7	23	8	10	14	7	
	8	24	8	9	12	7	
	9	25	8	7	10	7	
47	1	3	22	21	28	17	
	2	6	19	21	26	15	
	3	10	19	20	25	14	
	4	11	18	20	25	13	
	5	12	16	20	23	10	
	6	14	13	19	23	7	
	7	18	13	19	21	5	
	8	24	10	18	21	3	
	9	29	10	18	19	2	
48	1	9	22	26	21	25	
	2	11	19	26	18	21	
	3	13	15	26	17	19	
	4	14	15	26	16	18	
	5	16	10	26	14	13	
	6	20	10	25	10	12	
	7	21	7	25	9	10	
	8	22	4	25	8	7	
	9	27	3	25	6	5	
49	1	1	8	16	12	27	
	2	3	6	15	11	25	
	3	4	5	15	11	21	
	4	5	4	15	9	20	
	5	10	4	14	7	17	
	6	12	3	13	7	17	
	7	22	2	13	5	13	
	8	26	1	13	4	13	
	9	28	1	12	4	10	
50	1	2	24	27	25	30	
	2	4	24	25	25	28	
	3	5	22	25	25	28	
	4	6	21	24	25	27	
	5	9	20	24	25	25	
	6	16	19	24	25	24	
	7	17	19	23	25	24	
	8	21	18	23	25	23	
	9	22	17	22	25	22	
51	1	1	5	7	28	17	
	2	3	5	7	27	15	
	3	4	4	7	25	14	
	4	7	4	7	25	12	
	5	11	4	6	22	10	
	6	17	3	6	22	9	
	7	20	3	6	19	9	
	8	24	2	6	19	8	
	9	29	2	6	17	6	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	79	77	931	926

************************************************************************
