# Email (A)
# https://dmoj.ca/problem/ecoo19r2p1

# REMEMBER! DMOJ doesn't give much feedback when testing
# Just copy the functions to Idle, then run those individually
# Much easier to test and check your work

def sanitize(email: str) -> str:
    sanitized = lowercase(email)
    sanitized = remove_periods(sanitized)
    sanitized = remove_plus_strings(sanitized)
    return sanitized
    
def lowercase(email: str) -> str:
    return email.lower()
    
def remove_periods(email: str) -> str:
    before, after = email.split('@')
    before = before.replace('.', '')
    return before + '@' + after
    
def remove_plus_strings(email: str) -> str:
    before, after = email.split('@')
    parts = before.split('+')
    up_to_plus = parts[0]
    return up_to_plus + '@' + after

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
