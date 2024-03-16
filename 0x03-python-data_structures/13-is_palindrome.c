#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - It checks a singly linked list if is a palindrome
 * @head: point to linked list
 * Return: checks, 1 if is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *renew, *eye1 = NULL, *eye2 = NULL;

	if(!*head || !(*head)->next)
		return (1);
	fast = *head;
	renew = *head;
	while (renew->next)
		renew = renew->next;
	while (renew)
	{
		eye1 = renew->next;
		renew->next = eye2;
		eye2 = renew;
		renew = eye1;
	}
	renew = eye2;
	while (fast && renew)
	{
		if (fast->n != renew->n)
			return (0);
		fast = fast->next;
		renew = renew->next;
	}
	return (1);
}
