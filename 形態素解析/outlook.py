def load_all_folder_mails(account, cnt = 3, set_account = 'メアド'):
    print('load_all_folder_mail開始...')
    if set_account == str(account):
        print('対象アカウント')
    else:
        print('対象外アカウント')
        return
    all_folder_mails_list = []
    folders = account.Folders
    for folder in folders:
        mails = folder.items
        count = 0
        print('現在のフォルダ: ' + folder.Name + '...')
        for mail in mails:
            count += 1
            if count == cnt:
                break
            all_folder_mails_list.append(mail.body)

    return all_folder_mails_list

def choice_account(outlook, set_account):
    print('choice_account開始...')
    accounts = outlook.Folders
    for account in accounts:
        print('現在のアカウント: ' + str(account) + '...')
        print(type(account))
        if str(account) == set_account:
            return account