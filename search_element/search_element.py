def search(head, k):
    cursor_one = head
    cursor_two = head
    i = 0
    while i < k - 1:
        if not cursor_two:
            return None
        else:
            cursor_two.next
            i += 1
    if not cursor_two:
        return None
    while cursor_two.next:
        cursor_one.next
        cursor_two.next
    return cursor_one
