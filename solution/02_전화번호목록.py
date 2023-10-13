def solution(phone_book):
    phone_book_set = set(phone_book)
    for phone_number in phone_book:
        for idx in range(1, len(phone_number)):
            if phone_number[:idx] in phone_book_set:
                return False
    return True