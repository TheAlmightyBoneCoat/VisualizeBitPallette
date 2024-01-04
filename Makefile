CC=g++
CFLAGS=-Wall -shared -std=c++11 -fPIC $(shell python3-config --includes) -Iextern/pybind11/include
CFLAGS1 = -Wall -g -shared -std=c++11 -fPIC $(shell python3 -m pybind11 --includes)
PRG=Bitstream
SUFFIX=$(shell python3-config --extension-suffix)
SRCFILES=$(PRG).cpp $(PRG)_pybind.cpp

$(PRG)$(SUFFIX): $(SRCFILES)
	$(CC) $(CFLAGS1) $(SRCFILES) -o $(PRG)$(SUFFIX)

Bitstream_test: Bitstream.cpp Bitstream_test.cpp
	$(CC) -Wall -g Bitstream.cpp Bitstream_test.cpp -o Bitstream_test

generateImages_test: generateImages_test.cpp
	$(CC) -Wall -g generateImages_test.cpp -o generateImages_test

generateImages: generateImages.cpp
	$(CC) -Wall -g generateImages.cpp -o generateImages

clean:
	rm $(PRG)$(SUFFIX) 
