#include <Python.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

// The c++ string.substr method raise 'out of range exception' when the stop parameter
// exceeds the size of the string. But that is not we want in our case. We need empty string instead.
// This helper function will mimic this behaviour.
std::string _catch_exce_in_substr_if_any(std::string str, int start, int stop)
{
    std::string sub;
    try
    {
        sub = str.substr(start, stop);
    }
    catch (std::out_of_range &exception)
    {
    }
    return sub;
}

PyObject *longest_common_substring(PyObject *, PyObject *args)
{
    PyObject *o1, *o2;
    const char *str1, *str2;
    Py_ssize_t str1_len, str2_len;

    /* Parse arguments into Pyobjects*/
    if (!PyArg_ParseTuple(args, "OO", &o1, &o2))
        return NULL;

    /* Both arguments must be unicode instances.*/
    if (!PyUnicode_Check(o1) || !PyUnicode_Check(o2))
    {
        PyErr_Format(PyExc_TypeError, "Both arguments must be strings but got '%s' and '%s'",
                     Py_TYPE(o1)->tp_name, Py_TYPE(o2)->tp_name);
        return NULL;
    }

    /* Convert unicode string to char array */
    str1 = PyUnicode_AsUTF8AndSize(o1, &str1_len);
    if (str1 == NULL)
    {
        return NULL;
    }

    str2 = PyUnicode_AsUTF8AndSize(o2, &str2_len);
    if (str1 == NULL)
    {
        return NULL;
    }

    /* The original algorithm starts from here. See // See https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
    for more details. */
    std::string ss1(str1);
    std::string ss2(str2);

    int rowCount = 1 + ss1.size();
    int colCount = 1 + ss2.size();
    int longest = 0;
    int x_longest = 0;
    int start, stop;
    std::string longest_string;
    std::string left_s1;
    std::string left_s2;
    PyObject *out; // Our final result.
    std::string right_s1, right_s2;

    /* for 32bit systems if the strings are very long the vector allocation
    will raise MemoryError causing the function to crash. */
    std::vector<std::vector<int> > f;
    try {
        f.assign(rowCount, std::vector<int>(colCount));
    }
    catch(std::exception& e) {
        PyErr_NoMemory();
        return NULL;
    }

    for (int i = 1; i < rowCount; ++i)
    {
        for (int j = 1; j < colCount; ++j)
        {
            if (ss1[i - 1] == ss2[j - 1])
            {
                f[i][j] = f[i - 1][j - 1] + 1;
                if (f[i][j] > longest)
                {
                    longest = f[i][j];
                    x_longest = i;
                }
            }
            else
            {
                f[i][j] = 0;
            }
        }
    }

    start = x_longest - longest;
    stop = x_longest;

    longest_string = _catch_exce_in_substr_if_any(ss1, start, stop - (start));
    if (!longest_string.empty())
    {
        left_s1 = _catch_exce_in_substr_if_any(ss1, 0, start);
        left_s2 = _catch_exce_in_substr_if_any(ss2, 0, ss2.find(longest_string));
        right_s1 = _catch_exce_in_substr_if_any(ss1, stop, ss1.size());
        right_s2 = _catch_exce_in_substr_if_any(ss2, ss2.find(longest_string) + longest_string.size(), ss2.size());
    }

    out = PyTuple_New(5);
    if (!out)
        return NULL;

    PyTuple_SET_ITEM(out, 0, PyUnicode_FromString(longest_string.c_str()));
    PyTuple_SET_ITEM(out, 1, PyUnicode_FromString(left_s1.c_str()));
    PyTuple_SET_ITEM(out, 2, PyUnicode_FromString(left_s2.c_str()));
    PyTuple_SET_ITEM(out, 3, PyUnicode_FromString(right_s1.c_str()));
    PyTuple_SET_ITEM(out, 4, PyUnicode_FromString(right_s2.c_str()));

    if (PyErr_Occurred())
    {
        Py_DECREF(out);
        return NULL;
    }

    return out;
}

static PyMethodDef accel_methods[] = {
    // The first property is the name exposed to Python, longest_common_substring, the second is the C++
    // function name that contains the implementation.
    {"longest_common_substring", (PyCFunction)longest_common_substring, METH_VARARGS, 0},

    // Terminate the array with an object containing nulls.
    {0, 0, 0, 0}};

static PyModuleDef accel_module = {
    PyModuleDef_HEAD_INIT,
    "accel",                                        // Module name to use with Python import statements
    "Helper function to find the longest_common_substring", // Module description
    0,
    accel_methods // Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_accel()
{
    return PyModule_Create(&accel_module);
}