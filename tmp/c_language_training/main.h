#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct node - single linked list node structure
 *
 * @data: integer data
 * @link: a pointer to the next node
 *
 * Description: single linked list node structure that contains
 * data of integer type and a pointer to a data of struct node type
*/
typedef struct node
{
	int data;
	struct node *link;
} node;

void add_at_end(node *head, int data);
void print_list(node *head);
node *add_at_beginning(node *head, int data);
void free_list(node *head);


#endif
