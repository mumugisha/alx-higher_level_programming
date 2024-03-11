#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check linked lists in a cycle
 * list: linked list checks
 * 
 * Return: 1 if list has a cycle, 0 if not included
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	
	if (list == NULL || list ->next == NULL)
		return (0);
	slow = list ->next;
	fast = list ->next ->next;
	
	while (slow && fast && fast ->next)
	{
		if(slow == fast)
			return (1);
		slow = slow ->next;
		fast = fast ->next ->next;
	}
	return (0);
}
