#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of a list
 * Return: 0 if there is no cycle, otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *check;

	if (!list)
		return (0);

	while (list)
	{
		check = list;
		list = list->next;
		if (check <= list)
			return (1);
	}
	return (0);
}
