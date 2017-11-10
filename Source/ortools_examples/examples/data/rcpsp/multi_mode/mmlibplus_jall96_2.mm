jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	11		2 3 4 5 6 7 9 11 15 16 23 
2	3	9		32 28 27 24 22 17 14 13 12 
3	3	7		32 29 27 25 20 17 10 
4	3	9		32 28 27 24 22 20 17 14 12 
5	3	4		27 17 12 8 
6	3	5		32 25 17 14 12 
7	3	4		32 25 24 12 
8	3	7		36 32 29 25 24 18 14 
9	3	7		40 32 29 25 24 21 19 
10	3	6		28 26 24 21 19 18 
11	3	7		38 36 35 34 30 25 24 
12	3	5		39 36 34 29 18 
13	3	4		31 29 25 18 
14	3	8		45 40 39 35 33 31 30 26 
15	3	5		40 36 33 32 25 
16	3	6		45 36 35 33 30 26 
17	3	8		45 44 40 38 36 35 31 30 
18	3	8		51 44 40 38 37 35 33 30 
19	3	6		45 44 35 34 33 30 
20	3	4		35 33 30 26 
21	3	7		44 43 39 37 36 33 31 
22	3	7		51 41 40 38 37 35 30 
23	3	6		51 41 38 37 33 32 
24	3	6		45 44 43 39 33 31 
25	3	1		26 
26	3	7		51 50 47 44 42 41 37 
27	3	6		51 49 44 42 41 35 
28	3	3		45 33 31 
29	3	4		51 49 43 35 
30	3	6		50 49 48 47 43 42 
31	3	5		51 50 49 48 42 
32	3	2		42 35 
33	3	4		49 48 47 42 
34	3	3		51 42 41 
35	3	4		50 48 47 46 
36	3	4		51 49 48 47 
37	3	3		49 48 46 
38	3	3		49 48 47 
39	3	2		47 42 
40	3	2		47 46 
41	3	1		43 
42	3	1		46 
43	3	1		46 
44	3	1		46 
45	3	1		46 
46	3	1		52 
47	3	1		52 
48	3	1		52 
49	3	1		52 
50	3	1		52 
51	3	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	3	4	4	3	5	1	25	23	20	
	2	23	4	3	3	3	1	18	21	14	
	3	29	4	2	3	3	1	14	18	12	
3	1	2	4	3	4	1	29	23	24	12	
	2	20	4	1	3	1	29	21	17	11	
	3	30	3	1	3	1	29	15	13	9	
4	1	1	2	1	5	2	25	28	13	16	
	2	11	2	1	3	2	17	27	10	12	
	3	28	2	1	1	2	16	26	3	8	
5	1	15	3	2	3	1	23	13	4	16	
	2	21	2	2	3	1	15	11	3	9	
	3	28	1	2	3	1	11	10	3	4	
6	1	17	4	5	3	5	8	19	3	19	
	2	26	4	5	3	2	7	19	2	19	
	3	27	4	5	2	2	3	19	2	18	
7	1	2	5	3	4	5	26	14	13	29	
	2	29	4	2	3	3	26	13	11	27	
	3	30	4	2	3	2	24	13	10	26	
8	1	11	2	5	4	3	18	28	25	23	
	2	14	1	2	3	2	17	26	24	22	
	3	15	1	2	2	1	16	25	21	21	
9	1	4	5	4	4	3	23	24	27	16	
	2	7	5	3	3	3	20	23	27	16	
	3	12	5	3	2	3	18	19	27	15	
10	1	4	2	5	1	2	14	22	25	12	
	2	16	1	3	1	1	10	16	21	10	
	3	27	1	3	1	1	9	9	12	6	
11	1	2	3	2	3	5	25	21	15	28	
	2	17	2	2	2	3	22	18	11	27	
	3	25	2	1	2	3	21	7	5	24	
12	1	15	3	5	4	3	22	29	12	13	
	2	16	3	3	4	3	19	16	7	9	
	3	28	3	3	4	3	16	11	3	4	
13	1	7	2	3	3	5	18	20	6	16	
	2	8	1	2	3	5	18	12	6	12	
	3	27	1	2	3	5	17	6	4	5	
14	1	18	3	3	2	3	25	11	5	25	
	2	23	2	2	2	2	21	9	5	25	
	3	28	2	2	2	1	16	6	5	21	
15	1	11	2	1	4	3	21	18	23	12	
	2	12	2	1	3	2	20	15	17	11	
	3	27	1	1	2	2	15	14	13	9	
16	1	9	4	3	4	4	15	27	11	15	
	2	20	4	3	2	3	9	27	9	13	
	3	23	3	3	2	3	7	27	6	9	
17	1	10	3	1	4	3	8	27	17	7	
	2	26	3	1	3	3	7	24	15	7	
	3	29	3	1	1	3	6	18	15	7	
18	1	7	4	3	2	4	18	13	8	29	
	2	18	4	3	2	4	11	12	5	21	
	3	30	4	3	2	4	6	12	4	10	
19	1	4	2	1	1	5	18	26	18	23	
	2	11	2	1	1	3	17	23	15	16	
	3	17	2	1	1	3	17	20	5	12	
20	1	3	3	4	2	2	27	10	12	19	
	2	8	2	3	1	1	25	10	9	11	
	3	18	1	3	1	1	22	7	8	3	
21	1	5	3	4	4	4	28	24	29	9	
	2	28	2	4	3	4	27	24	27	9	
	3	30	2	4	3	3	27	24	27	7	
22	1	6	1	3	4	3	21	25	28	30	
	2	20	1	3	2	1	18	11	25	27	
	3	24	1	2	2	1	12	3	25	26	
23	1	23	3	4	3	3	11	15	22	24	
	2	26	3	3	3	3	10	11	20	20	
	3	29	2	1	1	3	3	6	18	20	
24	1	15	1	3	5	2	22	25	26	12	
	2	19	1	3	4	2	22	21	25	8	
	3	22	1	2	4	2	22	21	23	8	
25	1	2	2	4	3	4	14	24	7	16	
	2	10	2	3	2	2	10	20	3	13	
	3	14	2	2	2	1	6	16	1	12	
26	1	4	1	5	5	5	22	28	9	23	
	2	12	1	5	5	3	19	22	7	22	
	3	18	1	5	5	3	18	22	4	22	
27	1	6	5	5	3	3	8	20	3	21	
	2	16	2	3	3	1	6	8	2	15	
	3	24	1	3	1	1	3	2	2	6	
28	1	3	3	4	5	4	28	21	21	18	
	2	11	2	3	4	2	23	20	17	12	
	3	16	1	2	4	2	20	20	13	9	
29	1	3	4	2	4	5	27	14	23	15	
	2	23	3	2	3	5	27	13	19	15	
	3	28	2	2	1	5	26	12	10	12	
30	1	13	3	5	1	3	28	25	15	12	
	2	27	3	4	1	3	27	12	13	11	
	3	28	3	4	1	3	27	9	7	11	
31	1	12	3	5	4	4	17	23	23	24	
	2	14	2	5	4	3	13	17	22	23	
	3	25	1	5	3	1	10	16	21	22	
32	1	2	3	5	4	4	14	21	11	12	
	2	25	3	4	2	4	14	18	8	10	
	3	26	3	3	2	2	12	14	8	7	
33	1	18	3	5	3	2	2	7	19	18	
	2	23	1	3	3	1	2	7	16	14	
	3	28	1	3	3	1	2	4	12	9	
34	1	4	5	2	2	3	20	13	28	25	
	2	9	4	1	1	2	14	13	27	22	
	3	22	4	1	1	2	8	10	26	16	
35	1	5	5	5	5	1	25	18	10	11	
	2	21	2	3	4	1	22	17	10	8	
	3	24	2	3	4	1	21	17	10	6	
36	1	15	1	4	4	1	17	27	17	22	
	2	24	1	4	3	1	17	24	13	21	
	3	28	1	4	3	1	14	20	9	17	
37	1	3	4	4	2	1	7	11	14	25	
	2	6	4	2	2	1	6	6	10	23	
	3	14	4	2	2	1	4	5	6	19	
38	1	7	2	1	3	3	12	10	14	23	
	2	12	2	1	2	1	12	8	10	18	
	3	17	2	1	2	1	10	7	8	15	
39	1	1	4	3	5	2	21	27	11	15	
	2	7	4	3	3	2	14	14	9	14	
	3	13	4	3	2	2	8	9	8	9	
40	1	8	2	4	3	1	28	26	21	23	
	2	23	2	4	2	1	25	25	19	19	
	3	27	2	4	2	1	22	25	15	10	
41	1	1	3	2	3	3	6	13	19	20	
	2	5	2	2	2	2	6	8	18	16	
	3	18	1	2	1	2	4	5	17	14	
42	1	7	3	2	4	3	24	25	20	19	
	2	14	3	1	3	3	22	24	18	13	
	3	22	3	1	3	2	19	20	17	3	
43	1	3	1	5	5	2	27	27	20	28	
	2	4	1	4	4	2	22	21	13	26	
	3	9	1	3	3	1	21	16	7	23	
44	1	4	3	4	3	2	10	26	26	20	
	2	10	2	3	2	2	9	21	18	15	
	3	20	2	3	2	1	5	12	11	5	
45	1	4	2	2	4	5	19	16	28	28	
	2	19	2	2	4	3	18	14	26	22	
	3	28	2	2	4	3	18	14	26	18	
46	1	8	5	3	3	4	13	28	21	13	
	2	11	3	2	3	3	10	20	13	12	
	3	27	3	2	3	3	8	16	5	10	
47	1	7	4	3	4	5	23	22	20	29	
	2	16	3	3	3	2	17	17	13	15	
	3	26	2	3	3	1	11	5	8	11	
48	1	1	4	2	4	3	26	16	28	23	
	2	7	2	1	3	3	22	16	28	19	
	3	14	2	1	1	3	18	12	25	13	
49	1	4	4	1	2	1	19	19	20	25	
	2	9	2	1	1	1	16	19	16	24	
	3	24	2	1	1	1	7	18	10	24	
50	1	10	1	5	4	3	3	9	24	12	
	2	18	1	4	3	2	3	4	16	11	
	3	24	1	4	3	2	3	2	5	11	
51	1	8	4	2	2	4	23	14	18	27	
	2	20	3	2	2	2	15	10	13	25	
	3	29	2	1	2	2	9	5	8	23	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	132	141	137	138	863	929	801	889

************************************************************************
