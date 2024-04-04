#include <Python.h>

/**
 * File: PyFloatObject
 * Author: By Mugisha Alphonse
 */

// Function prototypes
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print info about Python list
 * @p: Pointer to PyObject list
 */
void print_python_list(PyObject *p)
{
    // Variables to store size and allocation of list
    Py_ssize_t size, alloc, u;
    const char *type;
    
    // Cast the PyObject to PyListObject
    PyListObject *list = (PyListObject *)p;
    // Cast the PyObject to PyVarObject
    PyVarObject *var = (PyVarObject *)p;

    // Extract size and allocation
    size = var->ob_size;
    alloc = list->allocated;

    // Flush standard output
    fflush(stdout);

    // Print Python list info
    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    // Print size and allocation information
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    // Loop through elements of the list
    for (u = 0; u < size; u++)
    {
        // Get the type of the current element
        type = Py_TYPE(list->ob_item[u])->tp_name;
        printf("Element %ld: %s\n", u, type);
        // Call appropriate function based on the type of element
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[u]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[u]);
    }
}
