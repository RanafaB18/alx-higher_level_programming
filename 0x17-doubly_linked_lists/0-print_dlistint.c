#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *temp = h;
	size_t nnodes = 0;

	while (temp)
	{
		printf("%d\n", temp->n);
		nnodes++;
		temp = temp->next;
	}
	return (nnodes);
}
