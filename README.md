# Windows Endpoint Monitoring Agent (Research Prototype)

### ⚠️ Disclaimer
**This software is for EDUCATIONAL and RESEARCH purposes only.** It was developed to study **Windows API hooking**, **User Account Control (UAC) flow**, and **SMTP-based log aggregation**. The author is not responsible for any misuse of this code.

---

### 📝 Project Overview
This project demonstrates the internal mechanics of endpoint monitoring agents. It functions as a background process that captures input events and securely transmits them to a remote server for analysis.

**Key Technical Concepts Demonstrated:**
* **Input Hooking:** Utilizing the `pynput` library to intercept hardware interrupts.
* **Privilege Escalation:** analyzing the `runas` verb to request High Integrity context from standard users.
* **Data Exfiltration:** Automated log aggregation via SMTP (TLS encryption).
* **Persistence Mechanisms:** Threading implementation for non-blocking background execution.

### 🛠️ Usage
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configuration:**
    Update the `TARGET_EMAIL` in `src/agent.py` with your test credentials.

3.  **Execution:**
    ```bash
    python src/agent.py
    ```

### 🛡️ Mitigation
To defend against such agents, ensure **User Account Control (UAC)** is set to "Always Notify" and monitor network traffic for outbound SMTP connections on port 587.
