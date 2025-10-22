import qrcode
import os
import tkinter as tk
from tkinter import messagebox, ttk
import webbrowser
import subprocess
import platform

# ---------- QR Generation Logic ----------
def generate_qr_codes():
    custom_text = custom_entry.get("1.0", "end-1c").strip()
    title = title_entry.get().strip()
    district = district_entry.get().strip()
    start_code = mid_prefix_entry.get().strip()
    num_codes = num_entry.get().strip()
    random_input = random_entry.get().strip()

    if not custom_text and (not title or not district or not start_code or not num_codes):
        messagebox.showwarning("Missing Information", "Please fill in all required fields or provide custom text.")
        return

    if not custom_text:
        try:
            num_codes = int(num_codes)
            if num_codes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Number of QR codes must be a positive number.")
            return

        import re
        match = re.search(r'(\D*)(\d+)$', start_code)
        if match:
            prefix = match.group(1)
            start_num = int(match.group(2))
        else:
            prefix = start_code
            start_num = 1

        if random_input:
            try:
                random_numbers = [int(x.strip()) for x in random_input.split(',')]
                if len(random_numbers) < num_codes:
                    messagebox.showerror("Error", "Not enough random numbers provided.")
                    return
            except:
                messagebox.showerror("Error", "Invalid random numbers input. Use comma-separated integers.")
                return
        else:
            import random
            random_numbers = random.sample(range(10000, 100000), num_codes)

    try:
        output_dir = os.path.expanduser("~/Documents/qr_codes")
        os.makedirs(output_dir, exist_ok=True)

        total = num_codes if not custom_text else 1
        progress_bar['maximum'] = total
        progress_bar['value'] = 0
        root.update_idletasks()

        for i in range(total):
            if custom_text:
                qr_text = custom_text
                qr_code_label = f"CustomQR_{i+1}"
            else:
                incremental_num = f"{start_num + i:05d}"
                qr_code_label = f"{prefix}{incremental_num}"
                qr_text = f"{title}\n#{random_numbers[i]}\n{qr_code_label}\n{district}"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save(os.path.join(output_dir, f"{qr_code_label}.png"))

            progress_bar['value'] = i + 1
            progress_label.config(text=f"Generating QR Code {i+1} of {total}...")
            root.update_idletasks()

        progress_label.config(text="Generation Complete!")
        messagebox.showinfo("Success", f"{total} QR code(s) generated in:\n{output_dir}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
    
    # ---------- Other Functions ----------
def open_folder():
    output_dir = os.path.expanduser("~/Documents/qr_codes")
    if not os.path.exists(output_dir):
        messagebox.showinfo("Info", "No folder found yet. Generate QR codes first.")
        return
    if platform.system() == "Windows":
        subprocess.Popen(f'explorer "{output_dir}"')
    else:
        subprocess.Popen(["open", output_dir])


def open_link(url):
    webbrowser.open(url)