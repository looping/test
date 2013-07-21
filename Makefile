#Top Makefile for desocode project

CC = gcc #gcc compiler
CFLAGS = -Wall #mean compile option ,here show warning info

VPATH = src libs debug
vpath %.h inc
SRCDIR = src
LIBDIR = libs
DEBUGDIR = debug
INCDIR = inc

target = $(DEBUGDIR)/desocode

LDFLAGS = $(LIBS)
RM = -rm -rf
OBJS := $(DEBUGDIR)/main.o $(DEBUGDIR)/world.o 


$(target) : $(OBJS) 
	$(CC) $(CFLAGS) -o $(target) $(OBJS) -lm


$(DEBUGDIR)/world.o : $(SRCDIR)/world.c
	$(CC) $(CFLAGS) -o $(DEBUGDIR)/world.o -c $(SRCDIR)/world.c -I ./$(INCDIR)/

$(DEBUGDIR)/main.o : $(SRCDIR)/main.c world.h
	$(CC) $(CFLAGS) -o $(DEBUGDIR)/main.o -c $(SRCDIR)/main.c -I ./$(INCDIR)/

clean :
	$(RM) $(OBJS) $(target)
.PHONY : all clean
