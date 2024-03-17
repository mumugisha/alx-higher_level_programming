#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast, *reverse, *temp1 = NULL, *temp2 = NULL;

 	if (!*head || !(*head)->next)
        	return (1);

    fast = *head;
    reverse = *head;

    while (reverse->next)
        reverse = reverse->next;

    while (reverse)
    {
        temp1 = reverse->next;
        reverse->next = temp2;
        temp2 = reverse;
        reverse = temp1;
    }

    reverse = temp2;

	 while (fast && reverse)
    	{
        	if (fast->n != reverse->n)
            		return (0);
        fast = fast->next;
        reverse = reverse->next;
    }

    return (1);
}
