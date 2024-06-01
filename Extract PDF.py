#using os and win32com.client to access the pdfs in the outlook mailbox. 
#sourcecode: https://stackoverflow.com/questions/71615629/extract-attachments-from-email-and-email-them-as-attachments-using-win32com-clie
#https://www.youtube.com/watch?v=oyEMi8sDVOM, please note the two references were inspiration. Final code came together with help from Ørsted (as their code is confidential I can not share it here.)

import os
import win32com.client

#Path to save the pdfs once extracted.
save_path = r"C:\Users\MITTH\OneDrive - Ørsted\Desktop\speciale coding\PDF"

#Initialize Outlook and get the MAPI namespace. MAPI allows access to COM objects, such as Outlook, enabling automation of tasks.
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#acessing the specific mailbox in Outlook
mailbox = outlook.Folders("Ørsted - WIND - Technical Integrity")

#navigating to the 'Checklists' folder within the inbox
inbox = mailbox.Folders('Inbox')
checklists_folder = inbox.Folders('Checklists')

#further navigate to the 'Generator Debris Inspection' subfolder
inspection_folder = checklists_folder.Folders('Generator Debris Inspection')

#initialize a counter for the file names
file_counter = 1

#function to save and rename attachment
def save_and_rename_attachment(attachment, save_path, counter):
    #constructing the new file name using the counter
    new_file_name = f"{counter}.pdf"
    #saving the attachment with containing new_file
    attachment.SaveAsFile(os.path.join(save_path, new_file_name))
    print(f"Downloaded and renamed to: {new_file_name}")

#iterating through the messages in the 'Generator Debris Inspection' folder
for message in inspection_folder.Items:
    for attachment in message.Attachments:
        if attachment.FileName.lower().endswith('.pdf'):
            save_and_rename_attachment(attachment, save_path, file_counter)
            file_counter += 1

#navigating to the 'Reviewed' subfolder within the 'Generator Debris Inspection' folder
reviewed_folder = inspection_folder.Folders('Reviewed')

#iterating through the messages in the 'Reviewed' subfolder 
for message in reviewed_folder.Items:
    for attachment in message.Attachments:
        if attachment.FileName.lower().endswith('.pdf'):
            save_and_rename_attachment(attachment, save_path, file_counter)
            file_counter += 1

