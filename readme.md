
````markdown
# 🧩 ITEC ICT QR CODE GEN

## 📖 Overview
**ITEC ICT QR CODE GEN** is a desktop application developed by **ITEC ICT Solutions** to simplify and accelerate the process of generating large batches of QR codes.  
It was designed out of necessity during fieldwork projects for the **Centre for Social Research (CSR)** and **Catholic Relief Services (CRS)**, where hundreds of QR-coded identification cards had to be produced quickly and efficiently.

---
## 🏗️ Background & Motivation
During the development of digital survey tools for CSR and CRS, a key requirement was to print physical cards — each embedded with a unique QR code.  

- **CSR** required approximately **1000 cards**  
- **CRS** required approximately **350 cards**  

That meant **1350+ QR codes** had to be generated — each with its own data.  
Online QR code generators, however, demanded **manual entry for every single code**, which was impractical and time-consuming.  

This challenge inspired the creation of **ITEC ICT QR CODE GEN** — a fully automated QR code generator capable of producing **hundreds or thousands of QR codes** at the click of a button.

---
## ⚙️ Features

- ✅ **Batch QR Code Generation** — generate any number of QR codes automatically.  
- 🧠 **Custom Text Support** — create QR codes from custom text or structured input fields.  
- 🔢 **Controlled Numbering** — define your starting number for sequential QR generation.  
- 🎲 **Custom Random Number Range** — set your own range for random values.  
- 💾 **Automatic File Saving** — all QR codes are saved to your `Documents/qr_codes` folder.  
- 🧭 **Quick Folder Access** — open the output folder directly from the app.  
- 🎨 **Modern, Futuristic Interface** — clean red, black, and gray design matching ITEC’s branding.  
- 🪟 **Resizable GUI** — interface dynamically adjusts to window size.  
- 💻 **Standalone Executable (.exe)** — runs on all Windows computers without setup.

---
## 🧭 How to Use

1. **Launch** the app:  
   Double-click the file `ITEC_ICT_QR_CODE_GEN.exe`.

2. **Input the following details:**
   - **Title** (e.g., *CRS* or *CSR*)  
   - **District** (e.g., *Blantyre / BT*)  
   - **Code Prefix & Start Number** (e.g., *MW-BT00200*)  
   - **Number of QR Codes** to generate  
   - **Random Number Range** *(optional)*  

3. **Optional Custom Text:**  
   - Instead of using fields, type your own message or text in the “Custom Text” box.  
   - Each QR code will contain this text.

4. **Click Generate QR Codes:**  
   - Watch the progress bar update.  
   - Once done, all QR images are saved to:  
     ```
     C:\Users\<YourName>\Documents\qr_codes
     ```

5. **Open Folder:**  
   - Use the “Open Folder” option in the app to instantly view your QR codes.

---
## 🧩 Installation (EXE Installer)

### 📦 Option 1 — Using the Executable Directly
- The app comes as a **standalone `.exe` file** (`ITEC_ICT_QR_CODE_GEN.exe`).  
- No additional installation is needed.  
- Just **double-click** to run it on any Windows PC.

### 🧰 Option 2 — Manual Installation for Developers
If you’re running the Python source version:
1. Ensure you have **Python 3.10+** installed.  
2. Install dependencies:
   ```bash
   pip install qrcode[pil] pillow
````

3. Run the app:

   ```bash
   python qrcode.py
   ```

### 🏗️ Option 3 — Build Your Own EXE

If you want to rebuild the `.exe`:

```bash
pyinstaller --onefile --noconsole --icon=itec_logo.ico qrcode.py
```

Your executable will appear in:

```
dist\qrcode.exe
```

---
## 💡 Future Enhancements

Planned features include:

* 🌐 QR codes for **URLs and websites**
* 📶 QR codes for **Wi-Fi passwords**
* 🔐 **Password-protected** or **encrypted QR codes**
* 📋 **CSV data import/export**
* 🖨️ Built-in **printing and layout** options

---
## 🧑‍💻 Developer Information

**Developer:** Leonard J.J. Mhone
**Organization:** ITEC ICT Solutions
**Language:** Python
**Website:** [https://itecictesolutions.gt.tc](https://itecictesolutions.gt.tc)
**Year:** 2025

---
## 📜 License

© 2025 ITEC ICT Solutions. All rights reserved.
Unauthorized duplication, modification, or distribution of this software is prohibited.

---
**ITEC ICT QR CODE GEN** —
*“Automating QR creation, one code at a time.”*