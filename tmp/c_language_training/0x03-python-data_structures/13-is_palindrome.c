#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: a pointer to the head pointer of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, len, *ptr;

	current = *head;
	len = 0;
	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	ptr = malloc(len * sizeof(int));
	current = *head;
	i = 0;
	while (current != NULL)
	{
		ptr[i] = current->n;
		i++;
		current = current->next;
	}
	i = 0;
	while (i < len)
	{
		if (ptr[i] != ptr[len - i - 1])
			return (0);
		i++;
	}
	return (1);
}
