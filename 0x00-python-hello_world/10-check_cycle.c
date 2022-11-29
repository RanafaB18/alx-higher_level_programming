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
	
	if (!list)
	{
		return (0);
	}
	while (next->next != NULL && prev != NULL)
	{
		prev = prev->next;
		next = (next->next)->next;
		if (next == prev)
		{
			return (1);
		}
	}
	return (0);
}
