# build a program from 2 files and one shared header
CC = gcc
CFLAGS = -g

source1.o: source1.c
	$(CC) $(CFLAGS) -c source1.c

source2.o: source2.c
	$(CC) $(CFLAGS) -c source2.c

program: source1.o source2.o
	$(CC) $(CFLAGS) -o program source1.o source2.o 
