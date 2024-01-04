#ifndef BITSTREAM_H
#define BITSREAM_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unistd.h>
#include <sys/stat.h>

using namespace std;

template <typename T>
class Bitstream
{
public:
    Bitstream(T *data_, unsigned size__): size_(size__), 
        byteOffset(0), bit((sizeof(T) * 8) - 1), eof_(false), data(data_) {}
    
    // Randomly generated (read: uninitialized) data
    Bitstream(unsigned size__): size_(size__), byteOffset(0), 
        bit((sizeof(T) * 8) - 1), eof_(false), data(new T[size__]) {}

    Bitstream(string filename);

    ~Bitstream() { delete[] data; }
    T getNextVal(unsigned numBits);
    bool eof(void) const { return eof_; }
    unsigned size(void) const { return size_; }

private:
    unsigned size_;
    unsigned byteOffset;
    unsigned bit;
    bool eof_;
    T *data;
};

template <typename T>
Bitstream<T>::Bitstream(string filename): size_(0), byteOffset(0), 
    bit((sizeof(T) * 8) - 1), eof_(true), data(NULL)
{
    struct stat stats;
    if (stat(filename.c_str(), &stats))
    {
        perror(NULL);
        throw("Unable to stat file.");
    }

    size_ = stats.st_size;
    if (size_ > 0)
    {
        data = new T[size_ / sizeof(T)];

        ifstream infile(filename, ios::in | ios::binary);
        unsigned byteIndex = 0;
        while (!infile.eof())
        {
            data[byteIndex] = infile.get();

            // If T is more than one byte, scoot existing data to the left and add
            for (unsigned i = 0; i < sizeof(T) - 1; i++)
            {
                data[byteIndex] = data[byteIndex] << 8;
                data[byteIndex] += infile.get();
            }

            byteIndex++;
        }

        infile.close();
        size_ = byteIndex;
        eof_ = false;
    }
}

// Returns the requested number of bits from the bitstream
template <typename T>
T Bitstream<T>::getNextVal(unsigned numBits)
{
    if (numBits > sizeof(T) * 8)
    {
        throw("Requested too many bits from getNextVal.");
    }

    if (eof_)
        throw("Bitstream reached end of data.");

    T result = 0;
    for (unsigned i = 0; i < numBits; i++)
    {
        result *= 2;
        result += ((1 << bit) & data[byteOffset]) ? 1 : 0;
        if (bit == 0)
        {
            bit = (sizeof(T) * 8) - 1;
            byteOffset++;

            if (byteOffset == size_)
            {
                eof_ = true;
                break;
            }
        }
        else
            bit--;

    }

    return result;
}
#endif
