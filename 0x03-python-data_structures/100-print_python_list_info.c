#include <python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - print basic python list
 * @p: some python object
 */
void print_python_list_info(PyObject *p);
{
	int element;
	
	print("[*] Size of the python List = %lu\n", Py_SIZE));
	printf("[*] Allocated = %lu\n", PyListObject *)p)->allocated);
	for (element = 0; element < Py_SIZE(p); element++)
		printf("element %d: %s\n", element, Py_TYPE(PyList_GetItem(p, element))->tp_name);
}
