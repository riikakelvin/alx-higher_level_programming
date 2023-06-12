/**
 * is_palindrome - diagnose whether a linked list is a palindrome
 * @head: ** pointer to linked list
 * Return: 1 if True, 0 when False
 */
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && temp)
    {
      if (temp->n == dup->n)
	{
	  dup = dup->next;
	  temp = temp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}
