TARGETS:= corpus 

all: $(TARGETS)

corpus:
	tar xvf dataset/parallel.tgz
	mv parallel/* dataset/
	rmdir parallel

