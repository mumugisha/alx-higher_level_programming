#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - print basic lists info in python
 * @p: pointer pyObject lists
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, alloc, u;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    fflush(stdout);

    printf("[.] python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0) {
        printf(" [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] size of the python list = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (u = 0; u < size; u++) {
        type = list->ob_item[u]->ob_type->tp_name;
        printf("Element %ld: %s\n", u, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[u]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list->ob_item[u]);
    }
}

/**
 * print_python_bytes - print basic bytes info in python
 * @p: pointer pyObject bytese
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, u;
    PyBytesObject *bytes = (PyBytesObject *)p;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0) {
        printf(" [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf(" trying string: %s\n", bytes->ob_sval);

    if (((PyVarObject *)p)->ob_size >= 10)
        size = 10;
    else
        size = ((PyVarObject *)p)->ob_size + 1;

    printf(" first %ld bytes: ", size);
    for (u = 0; u < size; u++) {
        printf("%02hhx", bytes->ob_sval[u]);
        if (u == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - print basics floats info in python
 * @p: pointer pyObject floats
 */
void print_python_float(PyObject *p) {
    char *buffer = NULL;
    PyFloatObject *float_obj = (PyFloatObject *)p;

    fflush(stdout);

    printf("[.] Float object info\n");
    if (strcmp(p->ob_type->tp_name, "float") != 0) {
        printf(" [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
                                    Py_DTSF_ADD_DOT_0, NULL);
    printf(" value: %s\n", buffer);
    PyMem_Free(buffer);
}
