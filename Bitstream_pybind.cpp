#include <pybind11/pybind11.h>
#include <string>

#include "Bitstream.cpp"

template <typename T>
void declareBitstream(pybind11::module &m, std::string typestr)
{
    using Class = Bitstream<T>;
    std::string pyclass_name = std::string("Bitstream_") + typestr;
    pybind11::class_<Class>(m, pyclass_name.c_str())
        .def(pybind11::init<T *, unsigned>())
        .def(pybind11::init<unsigned>())
        .def(pybind11::init<std::string>())
        .def("getNextVal", &Class::getNextVal)
        .def("eof", &Class::eof)
        .def("size", &Class::size);
}

PYBIND11_MODULE(Bitstream, m)
{
    declareBitstream<unsigned>(m, "uint");
    declareBitstream<unsigned char>(m, "uchar");
    declareBitstream<unsigned long>(m, "ulong");
    declareBitstream<int>(m, "int");
    declareBitstream<char>(m, "char");
    declareBitstream<long>(m, "long");
}
