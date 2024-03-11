#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check singly linked lists in a cycle
 * list: linked list checks
 * 
 * Return: 1 if list has a cycle, 0 if not included
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
