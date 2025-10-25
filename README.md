# File-Based-Password-Locker
The main Python script that implements the password and "forgot password" logic. It reads the password, hint, and security credentials from password.txt and handles user input, attempts, lockouts, and password changing .


A basic Python script that implements a simple password and "forgot password" protection mechanism using local text files for configuration and temporary data storage.

## 🚀 How It Works

This script provides multiple login attempts with a hint, a lockout period, and a simple mechanism to reset the password using pre-configured security credentials.

### Authentication Flow:
1.  **Initial Attempt:** User gets 2 tries.
2.  **Second Block:** If the first 2 attempts fail, the user is locked out for 2 seconds and prompted to try again.
3.  **Final Attempt:** User gets 2 more tries before access is permanently denied, and an "EMERGENCY" message is displayed.
4.  **Hint:** A hint is displayed after the 5th attempt.
5.  **Forgot Password:** If the user selects "yes," they must enter a predefined `name` and `text file name` to receive a temporary OTP in the `forgotpass.txt` file.

## ⚙️ Setup and Configuration


### Project Files

| File Name | Description |
| :--- | :--- |
| `password.py` | The main Python script containing the login and forgot password logic. |
| `password.txt` | **Configuration file.** Stores the actual password, the password hint, and security question data for the reset function. **DO NOT modify any lines other than the data itself.** |
| `forgotpass.txt` | **Temporary file.** Used to store the randomly generated OTP during the password reset process. |

### Configuration (`password.txt`)

You must edit `password.txt` to set the password and security credentials before running the script.

```text
Hint:(only change the data)(pls dont add any space btween the lines otherwise code error)
[Your Hint Here] 
Password:
[Your Password Here] 
Forgot password data:
name:[Your Security Name]
text: [Your Security Text/File Name]
