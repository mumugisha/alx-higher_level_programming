#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>

/**
 * insert_node - Insert sorted number list
 * @head: head to list
 * @number: Number to insert
 * Return: 0 If fails or if pointed to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
