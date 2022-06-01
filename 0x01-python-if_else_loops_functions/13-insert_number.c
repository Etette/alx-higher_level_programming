#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to head of the linked list
 * @number: integer to be inserted
 * Return: NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *tohead = *head;
	listint_t *last = tohead;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (!tohead)
	{
		new_node->next = tohead, *head = new_node;
		return (new_node);
	}

	while (tohead->next)
	{
		if (tohead->n < number)
			last = tohead, tohead = tohead->next;
		else
			break;
	}
	new_node->next = (tohead->next) ? tohead : NULL;
	if (last == tohead)
		*head = new_node;
	else
	{
		if (tohead->next)
			last->next = new_node;
		else
			tohead->next = new_node;
	}
	return (new_node);
}
