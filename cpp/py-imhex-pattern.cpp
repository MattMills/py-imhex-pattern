#include <Python.h>
#include "pl.hpp"
#include <cstring>
#include <string>

// Function to set data source
static PyObject* setDataSource(PyObject* self, PyObject* args) {
    PyObject* py_callback;
    PatternLanguage* pl;
    uint64_t address;
    size_t length;

    if (!PyArg_ParseTuple(args, "OKK0", &pl, &address, &length, &py_callback)) {
        return NULL;
    }

    if (!PyCallable_Check(py_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }

    auto c_callback = [py_callback](uint64_t address, uint8_t *data, size_t length) -> bool {
        PyObject* arglist = Py_BuildValue("(OKK)", address, data, length);
        PyObject* result = PyObject_CallObject(py_callback, arglist);
        Py_DECREF(arglist);

        if (result == NULL) {
            return false;
        }

        bool bool_result = PyObject_IsTrue(result);
        Py_DECREF(result);

        return bool_result;
    };

    pl->setDataSource(address, length, c_callback);

    Py_RETURN_NONE;
}

// List of functions to expose to Python
static PyMethodDef PatternLanguageMethods[] = {
    {"setDataSource", setDataSource, METH_VARARGS, "Set data source"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef patternlanguagemodule = {
    PyModuleDef_HEAD_INIT,
    "patternlanguage",
    NULL,
    -1,
    PatternLanguageMethods
};

// Init function
PyMODINIT_FUNC PyInit_patternlanguage(void) {
    return PyModule_Create(&patternlanguagemodule);
}