#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: a pointer to the head pointer of the linked list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	new_node->n = number;
	printf("================================\n");
	current = *head;
	while ((current->next != NULL) && (current->next->n < number))
	{
		printf("%d\n", current->n);
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	printf("================================\n");
	return (current);
}
