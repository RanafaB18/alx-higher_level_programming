#include "lists.h"
#include <stdio.h>
/**
* check_cycle - Check if the linked list is a circular linked list
* @list: linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *temp = list;
	
	if (!list)
	{
		return (0);
	}
	while (temp->next != NULL)
	{
		if (temp->next == head)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
