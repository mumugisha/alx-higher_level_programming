


#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_Python_bytes(PyObject *p) {
    long int size;
    int i;
    char *trying_str = NULL;

    printf("[*] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Not a valid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &trying_str, &size);

    printf(" size: %li\n", size);
    printf(" trying string: %s\n", trying_str);

    printf(" first %li bytes:", (size > 10) ? 10 : size);
    for (i = 0; i < size && i < 10; i++)
        printf(" %02hhx", trying_str[i]);
    printf("\n");
}

void print_python_list(PyObject *p) {
    long int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;
    const char *type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python list = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);
    
    for (i = 0; i < size; i++) {
        type = Py_TYPE(list->ob_item[i])->tp_name;
        printf("Element %i; %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_Python_bytes(list->ob_item[i]);
    }
}
