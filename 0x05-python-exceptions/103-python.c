#include <Python.h>

/**
 * File: print PyFloatObject
 * Author: By Mugisha Alphonse
 */

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print info of basics in Python list
 * @p: pointer to PyObject list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, u;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (u = 0; u < size; u++)
    {
        type = list->ob_item[u]->ob_type->tp_name;
        printf("Element %ld: %s\n", u, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[u]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[u]);
    }
}
