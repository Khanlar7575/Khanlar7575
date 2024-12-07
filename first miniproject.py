import tkinter as tk
root = tk.Tk()

root.title("rengleri deyisme")
root.geometry("400x400")
def arxafonu_deyis(rengler):
    root.config(bg=rengler)
def texttu_deyis(reng):
    label1.config(text="Qirmizi")


label1=tk.Label(root,text="Pencerenin rengini deyis",font=("Arial",25),bg="white",padx=50)
label1.pack(pady=25)

tk.Button(root,text="texin rengini deyisdir",font=("Calibri",15),bg="purple",fg="white",padx=30,pady=30,width=20,height=1,borderwidth=5,command=lambda:texttu_deyis("red") ).pack(pady=5)
tk.Button(root,text="Qirmizi",font=("Calibri",15),bg="red",fg="white",padx=30,pady=30,width=20,height=1,borderwidth=5,command=lambda: arxafonu_deyis("red")).pack(pady=5)
tk.Button(root,text="Yasil",font=("Calibri",15),bg="green",fg="white",padx=30,pady=30,width=20,height=1,borderwidth=5,command=lambda: arxafonu_deyis("green")).pack(pady=5)
tk.Button(root,text="Mavi",font=("Calibri",15),bg="blue",fg="white",padx=30,pady=30,width=20,height=1,borderwidth=5,command=lambda: arxafonu_deyis("blue")).pack(pady=5)
tk.Button(root,text="Sari",font=("Calibri",15),bg="yellow",padx=30,pady=30,width=20,height=1,borderwidth=5,command=lambda: arxafonu_deyis("yellow")).pack(pady=5)

root.mainloop()  