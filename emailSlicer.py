email = input("Enter your email address: ").strip()

email_username = email[0:email.index('@')]
email_domain = email[email.index('@') + 1:]

msg = 'Your email username is {}, and your email domain server is {}'.format(email_username,email_domain)

print(msg)
