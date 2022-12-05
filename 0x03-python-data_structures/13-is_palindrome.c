#include "lists.h"
/**
  * insertAtHead - inserts nodes at head of linked list
  * @head: head of linked list
  * @value: value of new node
  * Return: new head if no error else NULL
  */

listint_t *insertAtHead(listint_t **head, int value)
{
	listint_t *newNode = malloc(sizeof(listint_t));

	if (!newNode)
	{
		return (NULL);
	}
	newNode->n = value;
	newNode->next = NULL;
	if (!*head)
	{
		*head = newNode;
		return (*head);
	}
	newNode->next = *head;
	*head = newNode;
	return (*head);
}
/**
  * is_palindrome - Checks if a linked list is palindromic
  * @head: head of linked list
  * Return: 0 if its not palindromic else 1
  */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *newHead = NULL;
	listint_t *tempHead;

	if (*head == NULL)
	{
		return (1);
	}
	while (temp)
	{
		insertAtHead(&newHead, temp->n);
		temp = temp->next;
	}
	temp = *head;
	tempHead = newHead;
	while (tempHead && temp)
	{
		if (tempHead->n != temp->n)
		{
			free_listint(newHead);
			return (0);
		}
		tempHead = tempHead->next;
		temp = temp->next;
	}
	free_listint(newHead);
	return (1);
}

