#include "lists.h"
/**
 * insert_node - insert a node into a linked list
 * @head: head of linked list
 * @number: value of node
 * Return: linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *newNode = malloc(sizeof(listint_t));

	if (*head == NULL)
	{
		return (NULL);
	}
	if (newNode == NULL)
	{
		free(newNode);
		return (NULL);
	}
	if (number <= (*head)->n)
	{
		newNode->n = number;
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}
	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}
	printf("Temp: %d\n", temp->n);
	newNode->next = temp->next;
	newNode->n = number;
	temp->next = newNode;

	return (newNode);
}
