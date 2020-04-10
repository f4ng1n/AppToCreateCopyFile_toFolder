# AppToCreateCopyFile_toFolder

The User application has the following functionality: when launched, the user is prompted to enter information that will be saved as a test file in his directory (valuable object). Further, it is possible to create a copy of the recorded file in a public directory (public object).

This application addresses a threat to the security of information. The implementation of threats to the confidentiality of information often occurs using an adverse **information flow**. There are two main types of information flows: *memory* and *time*. In this app, an unfavorable information flow is simulated from *memory* (Fig. 1).
![image](https://user-images.githubusercontent.com/24553030/78949828-81a63e80-7ad5-11ea-913e-7d97dd9e7be0.png)
## Application: User: Creation and Copy file to folder  
Lauch the app, the “User app” asks you - real user, to enter text, select a directory (private folder) to save a text file as name, select a directory (public folder) to copy the file. The steps of saving and copying are accompanied by  message-boxes (successful or error!).  
              ![image](https://user-images.githubusercontent.com/24553030/78950357-33923a80-7ad7-11ea-98bc-6c2e5e2e50b8.png)

After entering the information, the path along which the file will be saved is selected. The save function is called up by pressing the “Save” key. If saved successfully, a message about this is displayed.

Figure below shows the interface of the copy file tab. The name of the file to be copied is entered, and the path where the copy will be saved is also indicated. If there is no such file, then an error message is displayed.
![image](https://user-images.githubusercontent.com/24553030/78950906-e9aa5400-7ad8-11ea-8271-43c4ce815eb6.png)
Press “Copy” button to copy file. If the operation is successful, a confirmation message is displayed (Figure below):
![image](https://user-images.githubusercontent.com/24553030/78951031-545b8f80-7ad9-11ea-9cd8-723319792754.png)
