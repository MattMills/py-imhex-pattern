# distutils: language = c++
# distutils: include_dirs = ./external/PatternLanguage/lib/include/


from libc.stdint cimport uint8_t as u8, uint64_t as u64
from libc.string cimport memcpy
from libcpp.string cimport string
from libcpp cimport bool
from cpython.bytearray cimport PyByteArray_AsString, PyByteArray_GET_SIZE


cdef extern from "pattern_language.hpp" namespace "pl":
    cdef cppclass PatternLanguage:
        PatternLanguage() noexcept
        void setDataSource(u64 address, size_t size, bool (*callback)(u64, u8*, size_t)) noexcept
        bool executeString(const string& code) noexcept
        string getError() noexcept

cdef class PyPatternLanguage:
    cdef PatternLanguage* thisptr
    cdef bytearray _data_source  # Hold a reference to the data source

    def __cinit__(self):
        self.thisptr = new PatternLanguage()
        self._data_source = bytearray()  # Initialize with an empty bytearray

    def __dealloc__(self):
        del self.thisptr

    def set_data_source(self, data: bytearray):
        self._data_source = data
        cdef u8* buffer = <u8*> PyByteArray_AsString(self._data_source)
        cdef size_t length = PyByteArray_GET_SIZE(self._data_source)
        self.thisptr.setDataSource(0, length, &_data_source_callback)

    def execute(self, code: str):
        cdef string std_code = code.encode('utf-8')
        if not self.thisptr.executeString(std_code):
            raise ValueError("Execution failed: " + self.thisptr.getError().decode('utf-8'))
        # Implement result parsing if necessary
        return "Execution succeeded"

# Global reference to the current PyPatternLanguage instance being used
cdef PyPatternLanguage _current_instance = None

cdef bool _data_source_callback(u64 address, u8* buffer, size_t size) noexcept:
    global _current_instance
    if _current_instance is None or len(_current_instance._data_source) < address + size:
        return False
    memcpy(buffer, <u8*> PyByteArray_AsString(_current_instance._data_source) + address, size)
    return True

