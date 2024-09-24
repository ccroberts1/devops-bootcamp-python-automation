def get_user_info(list_of_users):
    for user in list_of_users:
        print(f"User Name: {user['UserName']}\nLast Active:{user['PasswordLastUsed']}\n")

def get_most_active_user(list_of_users):
    latest_active_date = list_of_users[0]['PasswordLastUsed']
    latest_active_name = list_of_users[0]['UserName']
    latest_active_id = list_of_users[0]['UserId']
    for user in list_of_users:
        if user['PasswordLastUsed'] > latest_active_date:
            latest_active_date = user['PasswordLastUsed']
            latest_active_name = user['UserName']
            latest_active_id = user['UserId']
    print(f"Latest Active User\n User ID: {latest_active_id}\n User Name:{latest_active_name}")