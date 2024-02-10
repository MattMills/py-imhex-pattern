%module patternlanguage
%{

#include "pl.hpp"
#include <cstring>
#include <string>
%}

%include "stdint.i"
%include "cpointer.i"

%typemap(in) (bytearray data) {
    $1 = PyByteArray_AsString($input);
}

%typemap(in) (std::string code) {
    $1 = PyString_AsString($input);
}

%typemap(out) std::string {
    $result = PyString_FromString($1.c_str());
}

class PatternLanguage {
public:
    PatternLanguage();
    ~PatternLanguage();
    void setDataSource(uint64_t address, size_t length, bool (*callback)(uint64_t, uint8_t *, size_t));
    bool executeString(std::string code);
    std::string getError();
};