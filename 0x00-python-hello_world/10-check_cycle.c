#include "lists.h"
#include <stdio.h>
/**
* check_cycle - Check if the linked list is a circular linked list
* @list: linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *prev = list;
	listint_t *next = list;
	
	printf("Entering check\n");
	if (!list)
	{
		return (0);
	}
	while (next != NULL && next->next != NULL && prev != NULL)
	{
		printf("Before change: prev: %d ==== next: %d\n", prev->n, next->n);
		prev = prev->next;
		next = (next->next)->next;
		if (next == prev)
		{
			printf("After change: prev: %d %p  ==== next: %p\n", prev->n, (void *) prev, (void     *) next);
			return (1);
		}
	}
	return (0);
}
