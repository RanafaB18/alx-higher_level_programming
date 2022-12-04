#include "lists.h"
/**
 * is_palindrome - Checks if a linked list is palindromic
 * @head: head oflinkedlist
 * Return: 1 if palindromic else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int *var = NULL;
	int i = 1;
	int j;
	int arrayLength;
	var = malloc(sizeof(int));
	if (!head)
	{
		return 1;
	}
	while (temp)
	{
		var[i - 1] = temp->n;
		i++;
		realloc(var, sizeof(int) * i);
		temp = temp->next;
	}

	arrayLength = i - 1;
	i = 0;
	for (j = arrayLength - 1; j > 0; j--)
	{
		if (var[i] != var[j])
		{
			return 0;
		}
		i++;
	}
	return 1;
}

