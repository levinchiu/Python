#python 3.4
#AES_ECBmode_GUI.py


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from Crypto.Cipher import AES
import binascii


class EncryptGUI(Frame):
    #初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.my_IV = 16 * '\x00'
        
        
    def createWidgets(self):
        """#########################################
        #        設置GUI - GUI下方狀態說明         #
        #########################################"""
        self.depictionText = Label(self)
        self.depictionText["text"] = "歡迎使用AES加密工具!!"
        self.depictionText.grid(row=6, column=0, columnspan=10)
        
        
        
        """#########################################
        #           設置GUI - Input標籤            #
        #########################################"""
        #Input文字
        self.input = Label(self)
        self.input["text"] = "Input:"
        self.input.grid(row=0, column=2)
        
        
        
        """#########################################
        #           設置GUI - Input欄位            #
        #########################################"""
        self.Value_Input = StringVar()
        self.Entry_Input = Entry(self)
        self.Value_Input.set("請輸入您要加密的文字")
        self.Entry_Input["textvariable"] = self.Value_Input
        self.Entry_Input["width"] = 55
        self.Entry_Input.grid(row=0, column=3, columnspan=6)
        
        
        
        """#########################################
        #       設置GUI - TextEncryption標籤       #
        #########################################"""
        #Label_TextEncryption
        self.Label_TextEncryption = Label(self)
        self.Label_TextEncryption["text"] = "密文:"
        self.Label_TextEncryption.grid(row=1, column=2)
        
        
        
        """#########################################
        #       設置GUI - TextEncryption欄位       #
        #########################################"""
        self.Value_TextEncryption = StringVar()
        self.Entry_TextEncryption = Entry(self)
        self.Entry_TextEncryption["textvariable"] = self.Value_TextEncryption
        self.Entry_TextEncryption["width"] = 55
        self.Entry_TextEncryption.grid(row=1, column=3, columnspan=6)
        
        
        
        """#########################################
        #       設置GUI - TextDecryption標籤       #
        #########################################"""
        #Label_TextDecryption
        self.Label_TextDecryption = Label(self)
        self.Label_TextDecryption["text"] = "明文:"
        self.Label_TextDecryption.grid(row=2, column=2)
        
        
        
        """#########################################
        #       設置GUI - TextDecryption欄位       #
        #########################################"""
        self.Value_TextDecryption = StringVar()
        self.Entry_TextDecryption = Entry(self)
        self.Entry_TextDecryption["textvariable"] = self.Value_TextDecryption
        self.Entry_TextDecryption["width"] = 55
        self.Entry_TextDecryption.grid(row=2, column=3, columnspan=6)
        
        
        
        """#########################################
        #          設置GUI - 讀取檔案標籤          #
        #########################################"""
        self.Label_FileName = Label(self)
        self.Label_FileName["text"] = "檔案名稱:"
        self.Label_FileName.grid(row=3, column=1)
        
        
        
        """#########################################
        #          設置GUI - 讀取檔案欄位          #
        #########################################"""
        self.Value_ReadFileName = StringVar()
        self.Entry_ReadFileName = Entry(self)
        self.Entry_ReadFileName['textvariable']= self.Value_ReadFileName
        self.Entry_ReadFileName["width"] = 60
        self.Entry_ReadFileName.grid(row=3, column=2, columnspan=6)
        
        
        
        """#########################################
        #            設置GUI - Key標籤             #
        #########################################"""
        #Label_Key
        self.Label_Key = Label(self)
        self.Label_Key["text"] = "key:"
        self.Label_Key.grid(row=4, column=1)
        
        
        
        """#########################################
        #            設置GUI - Key欄位             #
        #########################################"""
        self.Value_Key = StringVar()
        self.Entry_Key = Entry(self)
        self.Value_Key.set("請輸入密碼")
        self.Entry_Key['textvariable']= self.Value_Key
        self.Entry_Key["width"] = 60
        self.Entry_Key.grid(row=4, column=2, columnspan=6)
        
        
        
        """#########################################
        #         設置GUI - Encryption按鈕         #
        #########################################"""
        self.Button_Encryption = Button(self)
        self.Button_Encryption["text"] = "Encryption"
        self.Button_Encryption.grid(row=0, column=0)
        self.Button_Encryption["command"] = self.Event_Encryption
        
        
        
        """#########################################
        #         設置GUI - Decryption按鈕         #
        #########################################"""
        self.Button_Decryption = Button(self)
        self.Button_Decryption["text"] = "Decryption"
        self.Button_Decryption.grid(row=0, column=1)
        self.Button_Decryption["command"] = self.Event_Decryption
        
        
        
        """#########################################
        #            設置GUI - Load按鈕            #
        #########################################"""
        self.Button_Load = Button(self)
        self.Button_Load["text"] = "Load"
        self.Button_Load.grid(row=3, column=0)
        self.Button_Load["command"] = self.Event_Load
        
        
        
        """#########################################
        #      設置GUI - Ciphertext Save按鈕       #
        #########################################"""
        self.Button_CiphertextSave = Button(self)
        self.Button_CiphertextSave["text"] = "Save File"
        self.Button_CiphertextSave.grid(row=1, column=0)
        self.Button_CiphertextSave["command"] = self.Event_CiphertextSave
        
        
        
        """#########################################
        #      設置GUI - Ciphertext Copy按鈕       #
        #########################################"""
        self.Button_CiphertextCopy = Button(self)
        self.Button_CiphertextCopy["text"] = "CopyToInput"
        self.Button_CiphertextCopy.grid(row=1, column=1)
        self.Button_CiphertextCopy["command"] = self.Event_CiphertextCopy
        
        
        
        """#########################################
        #       設置GUI - Plaintext Save按鈕       #
        #########################################"""
        self.Button_PlaintextSave = Button(self)
        self.Button_PlaintextSave["text"] = "Save File"
        self.Button_PlaintextSave.grid(row=2, column=0)
        self.Button_PlaintextSave["command"] = self.Event_PlaintextSave
        
        
        
        """#########################################
        #       設置GUI - Plaintext Copy按鈕       #
        #########################################"""
        self.Button_PlaintextCopy = Button(self)
        self.Button_PlaintextCopy["text"] = "CopyToInput"
        self.Button_PlaintextCopy.grid(row=2, column=1)
        self.Button_PlaintextCopy["command"] = self.Event_PlaintextCopy
        
        
        
        """#########################################
        #         設置GUI - Clear All按鈕          #
        #########################################"""
        self.Button_ClearAll = Button(self)
        self.Button_ClearAll["text"] = "Clear All"
        self.Button_ClearAll.grid(row=4, column=0)
        self.Button_ClearAll["command"] = self.Event_ClearAll
        
        
        
    """#############################################
    #         GUI事件 - Load按鈕(存檔功能)         #
    #############################################""" 
    def Event_Load(self):
        self.depictionText["text"] = "請選擇檔案..."
        self.fileName = filedialog.askopenfilename(filetypes = (("All file", "*.*"), ("python code file", "*.py")))
        
        if self.fileName != "":
            #讀取檔案內文字並放置到變數self.fileString
            self.fileString = ""
            file = open(self.fileName, 'r')
            self.fileString = file.read()
            file.close()
            
            #將讀取到的檔案內文字放置到GUI中Input欄位
            self.Value_Input.set(self.fileString)
        
            #將讀取到的檔案名稱放置到GUI中檔案名稱欄位
            self.Value_ReadFileName.set(self.fileName)
            
            #在GUI下方顯示狀態列顯示讀取到了多少個字元
            self.depictionText["text"] = "檔案內容有" + str(len(self.fileString)) + "個字元"
            
        elif self.fileName == "":
            #在GUI下方顯示狀態列顯示未讀取到檔案
            self.depictionText["text"] = "未選擇檔案"
            
            
            
    """#############################################
    #         GUI事件 - Save按鈕(密文存檔)         #
    #############################################"""  
    def Event_CiphertextSave(self):
        #清空my_ErrorMsg
        self.my_ErrorMsg = ""
        
        
        #讀取檔案名稱
        self.fileName = self.Entry_ReadFileName.get()
        if self.fileName == "":
            self.ErrorMessage("未選擇欲存檔檔案!")
        
        
        #讀取GUI密文欄位中的值
        self.my_ciphertext = self.Entry_TextEncryption.get()
        if self.my_ciphertext == "":
            self.ErrorMessage("沒有密文!")
            
            
        #如沒有任何錯誤訊息則執行存檔
        if self.my_ErrorMsg != "":
           messagebox.showerror(title="Error Message", message=self.my_ErrorMsg)     
           
        elif self.my_ErrorMsg == "":
            self.depictionText["text"] = "執行密文存檔功能..."
            file = open(self.fileName, 'w')
            file.write(self.my_ciphertext)
            file.close()
            self.depictionText["text"] = "密文存檔完畢!!"
        
        
        
    """#############################################
    #         GUI事件 - Save按鈕(明文存檔)         #
    #############################################"""  
    def Event_PlaintextSave(self):
        #清空my_ErrorMsg
        self.my_ErrorMsg = ""
        
        
        #讀取檔案名稱
        self.fileName = self.Entry_ReadFileName.get()
        if self.fileName == "":
            self.ErrorMessage("未選擇欲存檔檔案!")
            
            
        #讀取GUI明文欄位中的值
        self.my_plaintext = self.Entry_TextDecryption.get()
        if self.my_plaintext == "":
            self.ErrorMessage("沒有明文!")
            
            
        #如沒有任何錯誤訊息則執行存檔
        if self.my_ErrorMsg != "":
           messagebox.showerror(title="Error Message", message=self.my_ErrorMsg)     
           
        elif self.my_ErrorMsg == "":
            self.depictionText["text"] = "執行明文存檔功能..."
            file = open(self.fileName, 'w')
            file.write(self.my_plaintext)
            file.close()
            self.depictionText["text"] = "明文存檔完畢!!"
        
        
        
    """#############################################
    #      GUI事件 - Encryption按鈕(加密功能)      #
    #############################################"""
    def Event_Encryption(self):
        #清空my_ErrorMsg
        self.my_ErrorMsg = ""
        
        
        #取得使用者輸入key以utf-8編碼後的長度
        self.my_key = self.Entry_Key.get()    #取得使用者輸入key
        self.my_keyLength = len(self.my_key.encode("utf-8"))    #計算編碼號的長度
        
        
        #判斷key長度，長度超過或為空會跳出提醒，長度不足補0
        if self.my_keyLength > 16:
            self.ErrorMessage("key長度不得超過16 bytes!")
            
        elif self.my_keyLength == 0:
            self.ErrorMessage("key不能為空!")
            
        else:
            #key長度少於16 bytes，用0補滿(0佔1 byte)
            if self.my_keyLength < 16:    
                self.my_key = self.my_key + (16 - self.my_keyLength)*'0'
                
                
        #AES以每區塊16 bytes進行加密，因此判斷GUI中Input欄位(欲加密)的值的長度，如長度不滿16 bytes的倍數以空格補滿
        self.my_text = self.Entry_Input.get()   #取得GUI中Input欄位的值
        if self.my_text == "":
            self.ErrorMessage("Input欄位的值為空無法進行加密!")
            
        elif len(self.my_text.encode("utf-8"))%16 != 0:
            self.my_text = self.my_text + (16-len(self.my_text.encode("utf-8"))%16)*' '
            
            
        #沒有ErrorMsg則執行AES加密
        if self.my_ErrorMsg != "":
            messagebox.showerror(title="Error Message", message=self.my_ErrorMsg)    
            
        else:        
            #更新GUI下方顯示狀態列顯示狀態
            self.depictionText["text"] = "進行AES加密...."
                        
            #以AES ECB mode進行加密，加密後密文(self.my_ciphertext)的型態為bytes
            self.my_ciphertext = AES.new(self.my_key, AES.MODE_ECB, self.my_IV).encrypt(self.my_text)
            
            #以binascii.hexlify()將self.my_ciphertext從binary data轉為16進位並填至GUI密文欄位
            self.Value_TextEncryption.set(binascii.hexlify(self.my_ciphertext))
            
            #更新GUI下方顯示狀態列顯示狀態
            self.depictionText["text"] = "AES加密完成!!!"
            
            
            
    """#############################################
    #      GUI事件 - Decryption按鈕(解密功能)      #
    #############################################"""
    def Event_Decryption(self):
        #清空my_ErrorMsg
        self.my_ErrorMsg = ""
        
        
        #取得使用者輸入key以utf-8編碼後的長度
        self.my_key = self.Entry_Key.get()    #取得使用者輸入key
        self.my_keyLength = len(self.my_key.encode("utf-8"))    #計算編碼號的長度
        
        
        #判斷key長度，長度超過或為空會跳出提醒，長度不足補0
        if self.my_keyLength > 16:
            self.ErrorMessage("key長度不得超過16 bytes!")
            
        elif self.my_keyLength == 0:
            self.ErrorMessage("key不能為空!")
            
        else:
            #key長度少於16 bytes，用0補滿(0佔1 byte)
            if self.my_keyLength < 16:    
                self.my_key = self.my_key + (16 - self.my_keyLength)*'0'
                
                
        #AES以每區塊16 bytes進行解密，因此判斷GUI中Input欄位(欲解密)的值的長度是否符合16 bytes的倍數
        try:
            #利用binascii.unhexlify()將Input欄位的值從16進位轉為binary data
            self.my_text = binascii.unhexlify(self.Entry_Input.get())
            
        except:
            #Input欄位的值如果有非16進位執行unhexlify()會Error，跳至此例外
            self.ErrorMessage("Please check your ciphertext!")
            
        else:
            #AES為區塊(1區塊16 bytes)解密，欲解密的字串須為16的倍數
            if len(self.my_text) == 0:
                self.ErrorMessage("Input欄位的值為空無法進行解密!")
            elif len(self.my_text)%16 != 0:
                self.ErrorMessage("欲解密密文的bytes長度須為16的倍數!")
                
                
        #沒有ErrorMsg則執行AES解密
        if self.my_ErrorMsg != "":
            messagebox.showerror(title="Error Message", message=self.my_ErrorMsg)
            
        else:        
            #更新狀況
            self.depictionText["text"] = "進行AES解密...."
                
            #以AES ECB mode進行解密，解密後明文(self.my_plaintext)的型態為bytes
            self.my_plaintext = AES.new(self.my_key, AES.MODE_ECB, self.my_IV).decrypt(self.my_text)
            
            #以decode("utf-8")進行解碼將bytes型態轉為str型態
            self.Value_TextDecryption.set(self.my_plaintext.decode("utf-8"))
            
            #更新狀況
            self.depictionText["text"] = "AES解密完成!!!"
            
            
            
    """#############################################
    #  GUI事件 - CopyToInput按鈕(CiphertextCopy)   #
    #############################################"""
    def Event_CiphertextCopy(self):
        self.Value_Input.set(self.Entry_TextEncryption.get())
        self.depictionText["text"] = "將密文欄位的值複製到Input欄位"
        
        
        
    """#############################################
    #   GUI事件 - CopyToInput按鈕(PlaintextCopy)   #
    #############################################""" 
    def Event_PlaintextCopy(self):
        self.Value_Input.set(self.Entry_TextDecryption.get())
        self.depictionText["text"] = "將明文欄位的值複製到Input欄位"
        
        
        
    """#############################################
    #      GUI事件 - Clear All按鈕(ClearAll)       #
    #############################################"""  
    def Event_ClearAll(self):
        self.Value_Input.set('')
        self.Value_TextEncryption.set('')
        self.Value_TextDecryption.set('')
        self.Value_ReadFileName.set('')
        self.Value_Key.set('')
        self.depictionText["text"] = "所有欄位的值已清除!!"
        
        
        
    """#############################################
    #                Error Message                 #
    #############################################"""  
    def ErrorMessage(self, errMessage):
        if self.my_ErrorMsg == "":
            self.my_ErrorMsg = errMessage
        else:
            self.my_ErrorMsg = self.my_ErrorMsg + "\n" + errMessage


        
if __name__ == "__main__":
    
    root = Tk()    #建立Tk物件
    app = EncryptGUI(master=root)
    app.mainloop()
    
    