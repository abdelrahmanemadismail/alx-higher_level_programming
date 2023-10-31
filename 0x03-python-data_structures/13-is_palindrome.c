#include "lists.h"
/**
 * is_palindrome - function in C that checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *first;
	listint_t *last;

	first = *head;
	last = *head;

}
