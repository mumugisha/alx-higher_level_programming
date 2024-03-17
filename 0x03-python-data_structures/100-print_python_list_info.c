#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print basic python list information
 * @p: a Python object (should be a list)
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyListObject *obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", obj->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
    }
}
