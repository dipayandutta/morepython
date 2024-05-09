import paramiko
import tkinter as tk


class main_window():
    def __init__(self, root2, ip, user, pword):
        self.root2 = root2

        # Connection Label
        conn_label = tk.Label(root2, text=str('CONNECTED TO: ' + user + '    ' + 'ON: ' + ip))
        conn_label.grid(row=0, columnspan=6, sticky=tk.W)

        # Frequency Entery
        freq_label = tk.Label(root2, text='Tag Frequency:')
        freq_entry = tk.Entry(root2)
        self.freq_enter_button = tk.Button(root2, text='Enter')
        freq_label.grid(row=1, column=1, sticky=tk.E, padx=(5, 0))
        freq_entry.grid(row=1, column=2, sticky=tk.W)
        self.freq_enter_button.grid(row=1, column=3, padx=5)

        # Scroll Bar and Command Line Ouput
        self.scrollbar = tk.Scrollbar(root2)
        self.scrollbar.grid(row=3, column=5, rowspan=1, sticky=tk.N+tk.S)

        self.mylist = tk.Listbox(root2, yscrollcommand=self.scrollbar.set)
        self.mylist.grid(row=3, column=0, columnspan=5, sticky=tk.W+tk.E+tk.N+tk.S)

        # SSH Connection
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, port=22, username=user, password=pword)
        # stdin, stdout, stderr = ssh.exec_command('ls')
        # for line in stdout:
        #     mylist.insert(tk.END, str('... ' + line.strip('\n')))
        # ssh.close()

        # Start Script Button
        self.script_btn = tk.Button(root2, text="Start Script", command=self.toggle)
        self.script_btn.grid(row=2, column=1, columnspan=3, sticky=tk.W+tk.E, padx=(10, 8), pady=2)

        # Customize Grid Expansion
        root2.columnconfigure(0, weight=1)
        root2.columnconfigure(4, weight=1)
        root2.rowconfigure(3, weight=1)

        # Visual Touches
        root2.title("Terminal Connection")
        #root2.wm_iconbitmap('logo_blue.ico')

    def toggle(self):
        def_color = self.freq_enter_button.cget('bg')
        if self.script_btn.config('text')[-1] == 'Start Script':
            stdin, self.stdout, stderr = self.ssh.exec_command('bash memory.sh', get_pty=True)
            self.mylist.insert(tk.END, str('Starting Script\n'))
            self.script_btn.config(text='End Script', bg='red')
            self.update_window()
        else:
            stdin, self.stdout, stderr = self.ssh.exec_command(chr(3))
            self.mylist.insert(tk.END, str('Ending Script\n'))
            self.script_btn.config(text='Start Script', bg=def_color)

    def update_window(self):
        for line in iter(lambda: self.stdout.readline(), ""):
            self.mylist.insert(tk.END, str(line))
            self.scrollbar.config(command=self.mylist.yview)
        # self.root2.after(1000, self.update_window)


def main():
    root = tk.Tk()
    IP = '192.168.56.101'
    user = 'node'
    pswd = 'node'
    runGUI = main_window(root, IP, user, pswd)
    root.title("Connect to Drone")
   # root.wm_iconbitmap('logo_blue.ico')
    root.mainloop()


if __name__ == "__main__":
    main()