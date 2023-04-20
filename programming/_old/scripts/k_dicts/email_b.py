# Email (B)
# https://dmoj.ca/problem/ecoo19r2p1

# REMEMBER! DMOJ doesn't give much feedback when testing
# Just copy the functions to Idle, then run those individually
# Much easier to test and check your work

def sanitize(email: str) -> str:
    sanitized = ''

    email = email.lower()

    end_email = email[email.find('@'):]

    email = email.replace('.', '')
    
    for c in email:        
        if c in ['@', '+']:
            break
        sanitized += c

    sanitized += end_email
    return sanitized


    
# there are ten datasets
# so we just write the entire solution in this for block
# to do it 10 times
for i in range(10):
    n_emails = int(input())
    emails = set()
    for j in range(n_emails):
        email = input()
        emails.add(sanitize(email))
    print(len(emails))
