# healthy-analysis
## How to Run the Project

### 1️⃣ Open the Project in VS Code
1. Launch **Visual Studio Code**  
2. Click **File → Open Folder**  
3. Select the project folder:

---

### 2️⃣ Open PowerShell in VS Code
- Press **Ctrl + `** (backtick) to open the terminal  
- Ensure you are in the project folder:

```powershell
cd "C:\Users\YourName\Documents\GitHub\healthy-analysis"
docker build -t healthy-analysis .
docker run -v "${PWD}/output:/app/output" healthy-analysis
