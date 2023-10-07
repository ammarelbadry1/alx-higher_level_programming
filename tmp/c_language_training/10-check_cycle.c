#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list: a pointer to the first node in the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current1, *current2;

	if (list == NULL)
		return (0);
	current1 = list;
	if (list->next == NULL)
		current2 = list->next;
	else
		current2 = list->next->next;
	while ((current1 != NULL) & (current2 != NULL))
	{
		if (current1 == current2)
			return (1);
		current1 = current1->next;
		if ((current2->next->next == NULL) | (current2->next == NULL))
			current2 = NULL;
		else
			current2 = current2->next->next;
	}
	return (0);
}
