#include <python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - print basic python list
 * @p: some python object
 */
void print_python_list_info(PyObject *p);
{
	long int size = pylist_size(p)
	int i;
	pyListobject *obj = (pyListobject *)p';

	print("[*] size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
		printf("element %s\n", i, py_type(obj->ob_item[i]->tp_name);
}
