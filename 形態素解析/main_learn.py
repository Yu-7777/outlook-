from outlook import choice_account
import win32com.client as win32
import MeCab
from outlook import load_all_folder_mails
from データ変換 import morphological, convert_to_list

mecabTagger = MeCab.Tagger()
outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")

print("実行中...")
account = choice_account(outlook, 'メアド')
mails = load_all_folder_mails(account, 10)
morphological_list = morphological(mails)
morphological_list = convert_to_list(morphological_list)
print(morphological_list)