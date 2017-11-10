jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	7		2 3 5 6 14 15 18 
2	9	3		10 7 4 
3	9	4		19 13 12 9 
4	9	3		13 12 8 
5	9	2		12 8 
6	9	2		12 8 
7	9	2		19 11 
8	9	4		29 24 17 16 
9	9	4		29 24 17 16 
10	9	4		29 24 17 16 
11	9	5		29 24 21 20 17 
12	9	3		24 17 16 
13	9	3		24 17 16 
14	9	5		29 24 22 21 20 
15	9	4		29 24 21 20 
16	9	3		22 21 20 
17	9	5		30 28 26 23 22 
18	9	5		30 28 26 23 22 
19	9	1		20 
20	9	6		35 30 28 27 26 23 
21	9	7		40 35 33 30 28 27 25 
22	9	7		40 37 36 35 33 31 27 
23	9	6		40 37 33 32 31 25 
24	9	6		36 35 34 33 32 30 
25	9	4		41 39 36 34 
26	9	4		39 38 37 32 
27	9	3		39 34 32 
28	9	3		36 32 31 
29	9	3		37 34 31 
30	9	4		42 39 38 37 
31	9	3		42 41 38 
32	9	4		46 43 42 41 
33	9	3		44 39 38 
34	9	2		42 38 
35	9	3		44 41 39 
36	9	2		44 38 
37	9	6		51 50 49 46 45 44 
38	9	4		50 46 45 43 
39	9	6		51 50 49 48 46 45 
40	9	3		46 45 43 
41	9	4		50 49 48 45 
42	9	3		50 45 44 
43	9	4		51 49 48 47 
44	9	2		48 47 
45	9	1		47 
46	9	1		47 
47	9	1		52 
48	9	1		52 
49	9	1		52 
50	9	1		52 
51	9	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	5	20	14	25	23	22	10	
	2	7	20	14	23	21	22	8	
	3	11	20	14	23	20	19	8	
	4	12	20	14	23	19	18	8	
	5	18	19	14	22	19	14	7	
	6	21	19	14	21	18	11	6	
	7	25	19	14	21	17	11	6	
	8	29	18	14	20	17	8	6	
	9	30	18	14	20	16	5	5	
3	1	1	19	27	25	16	26	26	
	2	4	18	25	25	15	22	23	
	3	6	16	25	25	13	20	21	
	4	12	16	23	25	12	17	19	
	5	13	15	22	25	12	16	15	
	6	16	13	22	25	11	15	13	
	7	17	13	20	25	10	11	13	
	8	18	12	19	25	9	10	10	
	9	25	10	19	25	8	9	6	
4	1	4	4	18	22	27	16	22	
	2	7	4	17	21	24	15	20	
	3	8	4	17	18	24	13	19	
	4	9	3	17	18	22	12	14	
	5	17	2	17	15	18	9	11	
	6	20	2	16	13	16	9	10	
	7	21	1	16	13	16	6	9	
	8	26	1	16	9	13	5	4	
	9	27	1	16	8	11	5	2	
5	1	3	22	24	15	28	29	25	
	2	5	21	21	14	26	23	25	
	3	8	17	18	14	21	23	24	
	4	9	17	17	14	17	21	24	
	5	10	14	12	14	16	16	23	
	6	14	11	10	13	12	14	23	
	7	19	10	7	13	12	13	22	
	8	23	9	6	13	7	9	21	
	9	30	7	2	13	5	6	21	
6	1	1	25	28	20	18	28	17	
	2	3	24	23	18	18	23	16	
	3	4	24	20	15	17	21	13	
	4	5	23	18	13	16	20	12	
	5	18	22	17	11	13	16	10	
	6	20	22	12	9	13	14	9	
	7	23	21	11	9	12	11	8	
	8	24	21	6	6	11	6	7	
	9	25	21	6	5	9	5	6	
7	1	3	23	23	27	20	19	26	
	2	5	23	19	27	18	18	23	
	3	8	21	17	27	16	18	23	
	4	11	21	16	27	16	16	21	
	5	12	20	15	26	13	15	18	
	6	13	19	12	26	12	15	18	
	7	14	18	10	25	8	13	16	
	8	15	18	8	25	6	13	13	
	9	24	17	7	25	6	12	11	
8	1	1	29	14	22	2	22	21	
	2	3	25	13	20	2	20	20	
	3	15	22	12	17	2	19	20	
	4	17	21	11	16	2	18	18	
	5	19	17	11	15	2	16	18	
	6	20	14	10	14	2	15	17	
	7	21	12	8	12	2	12	15	
	8	27	7	7	9	2	9	14	
	9	28	5	7	8	2	8	13	
9	1	1	29	15	8	24	25	10	
	2	2	29	13	6	23	25	10	
	3	7	29	13	5	23	24	10	
	4	12	28	12	5	22	22	10	
	5	17	27	8	4	21	21	10	
	6	20	27	8	3	19	21	10	
	7	24	27	5	2	18	20	10	
	8	25	26	3	2	16	19	10	
	9	27	26	2	1	16	18	10	
10	1	1	21	23	27	13	24	21	
	2	5	20	23	27	12	24	18	
	3	10	19	22	23	12	23	18	
	4	14	16	20	21	12	22	16	
	5	20	14	20	20	12	21	16	
	6	26	13	19	18	12	21	13	
	7	27	12	17	15	12	19	12	
	8	28	11	17	13	12	19	11	
	9	29	10	16	10	12	18	11	
11	1	4	25	23	21	10	27	15	
	2	5	24	22	21	9	26	14	
	3	6	22	20	20	8	21	13	
	4	9	21	19	17	7	19	12	
	5	18	21	18	16	6	15	12	
	6	23	21	17	15	6	12	12	
	7	25	19	17	13	4	11	10	
	8	26	18	15	12	3	8	10	
	9	29	18	15	11	3	4	9	
12	1	6	23	22	21	16	26	20	
	2	10	23	21	21	16	25	19	
	3	11	21	21	21	16	25	18	
	4	12	20	21	21	16	24	17	
	5	17	18	20	20	16	22	17	
	6	18	17	20	20	16	21	16	
	7	19	17	20	20	16	21	15	
	8	27	15	20	19	16	19	16	
	9	30	14	20	19	16	19	15	
13	1	3	19	18	17	11	29	29	
	2	7	19	17	14	9	28	29	
	3	18	15	16	13	7	26	29	
	4	19	14	15	11	6	25	29	
	5	20	13	15	9	5	25	29	
	6	22	11	13	6	4	23	29	
	7	27	9	12	6	3	21	29	
	8	29	7	11	3	3	20	29	
	9	30	3	11	2	2	20	29	
14	1	4	18	20	11	24	7	16	
	2	11	18	18	10	19	5	15	
	3	14	18	18	8	19	5	13	
	4	15	18	15	7	17	5	12	
	5	16	17	15	6	13	4	12	
	6	17	17	13	5	10	3	12	
	7	22	17	13	5	7	2	10	
	8	27	17	10	4	7	2	10	
	9	28	17	9	2	5	1	9	
15	1	5	22	21	26	4	17	29	
	2	8	19	19	23	4	15	28	
	3	10	19	19	22	4	13	28	
	4	13	16	19	20	4	12	28	
	5	14	14	18	17	4	11	27	
	6	18	9	18	15	4	9	27	
	7	23	7	17	13	4	8	26	
	8	27	6	17	10	4	5	26	
	9	28	4	16	8	4	4	25	
16	1	4	10	11	25	28	26	25	
	2	7	9	10	25	26	26	24	
	3	13	8	10	19	24	24	24	
	4	18	8	10	17	24	22	23	
	5	19	7	10	13	21	21	23	
	6	24	7	10	10	20	19	22	
	7	25	6	10	9	19	18	21	
	8	29	6	10	5	16	17	21	
	9	30	6	10	2	14	15	21	
17	1	4	17	13	30	21	20	4	
	2	5	15	13	29	21	18	4	
	3	8	13	11	28	18	17	4	
	4	12	12	10	27	16	17	4	
	5	19	10	9	26	14	14	3	
	6	21	9	9	26	13	13	3	
	7	22	6	8	24	10	12	3	
	8	28	4	6	24	7	11	2	
	9	29	3	5	23	6	10	2	
18	1	3	22	25	24	16	21	23	
	2	12	21	23	24	14	19	22	
	3	15	21	22	20	14	19	21	
	4	16	21	21	19	13	19	21	
	5	17	20	19	17	11	18	20	
	6	18	20	19	14	10	17	20	
	7	20	19	17	14	9	16	19	
	8	27	19	15	12	9	15	19	
	9	29	19	14	10	7	15	19	
19	1	1	7	25	23	29	7	9	
	2	2	5	24	21	27	6	8	
	3	6	5	21	20	27	6	7	
	4	7	4	19	18	26	5	7	
	5	8	3	18	15	26	5	6	
	6	16	3	16	13	25	4	6	
	7	17	2	12	11	25	3	5	
	8	21	1	10	10	25	3	3	
	9	23	1	10	7	24	3	3	
20	1	2	4	26	21	28	12	17	
	2	8	4	25	19	23	12	16	
	3	16	4	22	19	19	12	15	
	4	17	3	16	18	19	12	14	
	5	19	3	15	16	14	11	13	
	6	20	3	13	14	11	11	13	
	7	21	3	10	13	11	11	12	
	8	22	2	7	11	7	10	11	
	9	23	2	5	9	4	10	11	
21	1	3	15	18	27	12	24	26	
	2	13	15	18	27	12	23	23	
	3	17	15	18	25	11	22	20	
	4	22	15	18	25	10	21	19	
	5	23	15	18	24	10	21	15	
	6	24	15	17	23	9	20	13	
	7	25	15	17	21	9	20	11	
	8	26	15	17	20	9	19	7	
	9	30	15	17	19	8	18	6	
22	1	4	27	22	15	22	27	22	
	2	7	25	20	13	20	26	21	
	3	9	25	19	12	18	24	19	
	4	10	25	17	10	14	22	18	
	5	11	24	14	9	12	22	18	
	6	21	23	12	7	8	19	17	
	7	25	23	10	6	6	18	16	
	8	27	22	8	5	4	17	16	
	9	28	21	5	3	1	16	15	
23	1	1	22	14	8	20	27	30	
	2	2	22	12	8	19	24	27	
	3	3	22	12	8	19	22	22	
	4	6	22	10	7	18	22	18	
	5	11	22	10	7	17	19	15	
	6	15	22	10	6	17	18	12	
	7	16	22	9	6	17	18	11	
	8	22	22	8	5	16	15	6	
	9	24	22	7	5	16	14	4	
24	1	1	25	24	27	27	29	14	
	2	2	25	23	24	25	28	13	
	3	3	22	23	21	22	28	12	
	4	4	22	23	16	19	28	10	
	5	5	20	22	14	18	28	10	
	6	6	19	22	13	14	28	9	
	7	17	18	22	10	10	28	7	
	8	19	15	22	7	10	28	7	
	9	20	14	22	1	7	28	5	
25	1	4	16	28	30	18	5	18	
	2	8	14	28	30	17	4	17	
	3	13	13	27	30	17	4	17	
	4	15	13	26	30	17	4	16	
	5	20	10	26	30	17	4	15	
	6	21	10	26	30	16	4	14	
	7	22	7	25	30	16	4	14	
	8	28	6	24	30	16	4	12	
	9	29	5	24	30	16	4	12	
26	1	4	21	5	30	23	19	13	
	2	5	21	4	26	21	16	12	
	3	9	20	4	25	18	16	11	
	4	11	19	4	23	16	15	10	
	5	14	18	4	20	14	13	9	
	6	17	18	4	17	12	12	8	
	7	23	18	4	17	10	9	7	
	8	25	17	4	15	9	8	6	
	9	29	16	4	11	8	7	6	
27	1	1	15	22	21	18	28	9	
	2	2	15	22	21	17	26	9	
	3	5	15	21	19	15	24	9	
	4	6	15	20	18	13	20	9	
	5	15	15	19	18	13	17	8	
	6	17	15	17	17	11	17	8	
	7	21	15	17	15	9	14	8	
	8	24	15	15	14	7	10	8	
	9	29	15	15	14	6	8	8	
28	1	3	18	27	19	17	22	27	
	2	4	17	25	18	15	20	25	
	3	5	16	24	17	14	20	22	
	4	10	16	23	17	12	19	20	
	5	19	14	22	16	11	17	18	
	6	23	12	21	15	9	16	15	
	7	24	12	21	15	8	13	13	
	8	27	10	20	13	7	12	11	
	9	28	10	19	13	6	12	9	
29	1	1	9	26	26	22	7	27	
	2	7	8	26	26	20	5	27	
	3	11	8	21	26	18	5	24	
	4	18	7	18	26	18	4	23	
	5	22	6	16	26	16	3	19	
	6	23	6	15	26	16	3	17	
	7	24	5	13	26	14	3	15	
	8	25	5	7	26	14	1	13	
	9	26	4	7	26	12	1	11	
30	1	7	28	15	22	20	30	27	
	2	9	22	13	18	18	28	24	
	3	18	21	13	18	16	28	22	
	4	20	17	12	16	15	28	20	
	5	21	14	9	13	13	26	16	
	6	25	10	8	12	11	26	12	
	7	26	8	6	9	9	26	12	
	8	27	5	6	8	9	25	7	
	9	28	2	4	5	6	24	4	
31	1	1	29	6	20	24	23	24	
	2	7	26	5	20	21	23	22	
	3	8	21	5	20	21	23	21	
	4	11	17	4	20	19	23	20	
	5	14	15	3	20	19	23	15	
	6	25	12	3	20	16	23	14	
	7	27	11	2	20	16	23	11	
	8	28	6	2	20	15	23	9	
	9	30	4	2	20	14	23	6	
32	1	2	10	8	19	8	10	19	
	2	3	10	8	17	8	10	18	
	3	19	10	6	17	8	9	16	
	4	20	9	5	16	7	8	16	
	5	23	9	5	13	7	7	14	
	6	24	9	3	12	7	5	12	
	7	26	9	2	11	6	4	10	
	8	27	8	1	10	6	3	9	
	9	29	8	1	9	6	3	9	
33	1	2	28	20	5	17	9	23	
	2	3	24	20	5	15	8	22	
	3	4	22	20	4	13	7	18	
	4	5	19	20	4	11	5	17	
	5	17	17	19	3	10	5	14	
	6	18	15	19	3	8	5	13	
	7	19	14	18	3	6	4	8	
	8	20	13	18	2	3	2	7	
	9	25	9	18	2	1	2	5	
34	1	2	21	28	26	29	28	16	
	2	4	18	24	24	28	27	15	
	3	5	16	24	24	28	26	13	
	4	7	14	21	23	28	25	13	
	5	19	12	21	23	27	22	11	
	6	26	11	19	22	27	20	10	
	7	28	9	16	22	27	20	10	
	8	29	7	14	22	27	18	9	
	9	30	3	13	21	27	17	8	
35	1	4	5	12	27	18	25	19	
	2	14	5	11	25	18	25	19	
	3	15	5	9	24	17	25	19	
	4	18	5	9	23	17	25	19	
	5	19	5	8	20	17	25	19	
	6	24	5	7	18	16	25	19	
	7	25	5	6	16	15	25	19	
	8	26	5	5	11	15	25	19	
	9	29	5	4	9	15	25	19	
36	1	5	27	29	18	4	26	27	
	2	12	22	28	17	3	24	26	
	3	15	20	28	16	3	21	25	
	4	17	16	28	14	2	20	24	
	5	19	16	27	14	2	19	24	
	6	22	10	27	12	2	16	23	
	7	23	8	26	10	2	15	23	
	8	24	5	25	10	1	13	23	
	9	27	2	25	9	1	11	22	
37	1	2	26	22	17	12	24	17	
	2	3	23	20	15	11	22	17	
	3	4	23	19	14	11	22	14	
	4	10	20	17	12	9	18	13	
	5	17	18	13	10	9	17	9	
	6	22	15	10	8	7	15	8	
	7	23	14	9	5	5	14	7	
	8	25	12	8	3	4	13	4	
	9	27	9	6	2	4	10	3	
38	1	3	19	23	29	27	14	16	
	2	13	17	20	28	27	13	14	
	3	14	17	19	27	27	13	13	
	4	15	14	18	26	27	10	11	
	5	16	12	15	25	26	8	9	
	6	17	10	12	24	26	7	7	
	7	18	9	10	23	25	6	6	
	8	19	7	6	22	25	4	6	
	9	21	6	6	22	25	4	4	
39	1	2	23	11	25	18	27	27	
	2	8	23	11	24	15	26	26	
	3	9	23	10	23	15	26	22	
	4	14	23	8	23	11	26	20	
	5	15	22	8	22	11	24	19	
	6	17	22	8	22	8	24	17	
	7	19	22	7	21	6	24	15	
	8	20	21	5	19	3	22	11	
	9	28	21	5	19	2	22	10	
40	1	5	25	13	11	23	20	13	
	2	6	22	10	11	23	19	12	
	3	7	22	9	9	23	19	11	
	4	9	20	9	8	23	16	11	
	5	11	19	7	7	23	15	9	
	6	12	17	6	5	22	15	9	
	7	19	14	5	4	22	13	7	
	8	24	12	3	3	22	11	6	
	9	26	12	1	2	22	10	6	
41	1	1	19	15	26	16	21	22	
	2	4	19	15	24	15	19	21	
	3	8	17	13	24	15	16	19	
	4	12	15	13	22	13	15	19	
	5	13	13	12	19	13	12	16	
	6	20	13	9	18	12	10	16	
	7	21	11	8	18	10	5	15	
	8	22	10	7	14	9	5	13	
	9	24	9	6	13	9	1	13	
42	1	2	7	7	14	26	23	29	
	2	4	6	7	13	24	22	25	
	3	10	5	7	12	23	20	22	
	4	15	4	7	10	22	20	21	
	5	17	3	7	9	20	19	17	
	6	27	3	7	9	18	17	15	
	7	28	3	7	7	17	17	14	
	8	29	1	7	6	16	16	12	
	9	30	1	7	6	15	14	9	
43	1	5	2	8	16	30	7	27	
	2	6	2	7	15	25	6	27	
	3	7	2	7	13	24	6	27	
	4	8	2	6	12	18	5	27	
	5	9	2	5	8	18	5	27	
	6	10	2	5	7	12	4	27	
	7	12	2	4	7	11	4	27	
	8	17	2	4	5	7	3	27	
	9	22	2	4	3	3	3	27	
44	1	9	27	6	19	27	29	19	
	2	13	24	6	15	27	23	19	
	3	14	22	6	15	22	21	18	
	4	16	17	6	13	19	20	17	
	5	18	17	6	10	18	15	16	
	6	21	14	6	7	12	11	15	
	7	22	9	6	7	10	10	13	
	8	27	6	6	4	6	7	13	
	9	29	5	6	2	5	1	12	
45	1	4	26	27	18	19	25	13	
	2	8	24	27	17	19	23	12	
	3	10	24	25	16	15	23	11	
	4	14	23	24	16	14	22	11	
	5	15	22	24	15	12	22	10	
	6	16	21	23	15	10	22	10	
	7	17	21	22	14	8	21	10	
	8	27	19	21	14	6	20	9	
	9	30	19	20	14	5	20	9	
46	1	3	19	24	23	20	1	7	
	2	4	18	23	22	18	1	6	
	3	7	18	19	21	16	1	6	
	4	8	18	17	20	14	1	6	
	5	10	18	13	17	14	1	6	
	6	11	17	11	17	13	1	5	
	7	12	17	8	16	11	1	5	
	8	22	17	8	14	10	1	5	
	9	29	17	4	13	9	1	5	
47	1	4	20	25	26	22	27	5	
	2	5	19	25	25	21	25	5	
	3	6	17	25	21	20	25	5	
	4	8	14	25	17	19	23	5	
	5	11	13	24	14	17	21	4	
	6	12	10	24	14	16	18	4	
	7	14	8	24	8	15	15	4	
	8	20	5	24	8	14	14	3	
	9	26	4	24	3	14	12	3	
48	1	4	30	15	23	22	27	8	
	2	5	29	13	22	21	24	7	
	3	8	29	12	21	21	22	7	
	4	10	29	12	20	21	18	7	
	5	17	28	10	20	20	18	6	
	6	18	28	9	19	20	15	6	
	7	20	27	8	19	19	12	6	
	8	24	27	8	18	19	10	5	
	9	27	27	6	18	18	7	5	
49	1	1	25	14	12	9	18	26	
	2	3	22	13	12	8	15	26	
	3	5	22	12	12	8	15	22	
	4	12	19	12	11	8	11	20	
	5	15	19	11	10	8	11	18	
	6	18	16	11	10	7	9	18	
	7	20	16	10	9	7	8	15	
	8	23	14	10	9	7	4	13	
	9	26	13	10	9	7	4	12	
50	1	7	13	25	26	12	27	21	
	2	8	13	25	24	10	26	19	
	3	9	11	24	21	10	26	18	
	4	11	11	24	19	8	26	15	
	5	16	10	23	18	8	25	15	
	6	17	9	23	16	6	25	12	
	7	26	7	22	13	6	25	12	
	8	29	7	22	11	5	25	9	
	9	30	6	22	9	3	25	8	
51	1	1	26	21	17	19	26	9	
	2	2	21	19	16	17	24	9	
	3	5	21	19	15	17	23	8	
	4	10	19	17	14	15	22	6	
	5	17	17	15	12	14	21	6	
	6	18	14	15	10	11	20	4	
	7	19	11	12	7	11	18	3	
	8	26	8	11	7	10	17	3	
	9	28	8	11	4	8	16	2	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2
	61	61	63	61	677	620

************************************************************************
