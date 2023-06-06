#include "lists.h"

/**
 * check_cycle - establishes whether a linked list has a cycle
 * @list: pointer of linked list to check from
 * Return: 1 when list has a cycle, otherwise 0 for absence
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
