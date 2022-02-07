struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{

    struct ListNode try;
    try.val = 0;
    try.next = NULL;
    struct ListNode *answer = &try;

    int carry = 0;
    // int len= 0 ;
    // int arr [15];
    do
    {
        int sum = l1->val + l2->val;
        // answer->val= sum%10+ carry;
        printf("%d\n", answer->val);
        // printf( "%d\n",arr[len] );
        answer->next = calloc(1, sizeof(struct ListNode));
        answer->next->next = NULL;
        answer->next->val = (sum % 10 + carry) % 10;
        answer = answer->next;

        if ((sum >= 10) || ((sum % 10 + carry) >= 10))
        {
            carry = 1;
        }
        else
        {
            carry = 0;
        }

        if (l2->next == NULL && l1->next != NULL)
        {
            printf("l2 no null \n");
            l2->next = calloc(1, sizeof(struct ListNode));
            l2 = l2->next;
            l1 = l1->next;
        }
        else if (l2->next != NULL && l1->next == NULL)
        {
            printf("l1 no null \n");
            l1->next = calloc(1, sizeof(struct ListNode));
            l2 = l2->next;
            l1 = l1->next;
        }
        else if (l2->next != NULL && l1->next != NULL)
        {
            printf("no null\n");
            l2 = l2->next;
            l1 = l1->next;
        }
        else if (l2->next == NULL && l1->next == NULL && carry == 1)
        {
            printf(" carry\n");
            l1->next = calloc(1, sizeof(struct ListNode));
            l2->next = calloc(1, sizeof(struct ListNode));
            l2 = l2->next;
            l1 = l1->next;
        }
        else
        {
            l2 = l2->next;
            l1 = l1->next;
        }

    } while (l1 != NULL && l2 != NULL);

    printf("here\n");

    // for ( int j = len; j>=0 ; j--){
    // answer->val= arr[len];
    // answer->next =calloc(1, sizeof(struct ListNode));
    // answer=answer->next;
    // printf("%d and %d\n", j, arr[len]);
    //}
    return try.next;
}
