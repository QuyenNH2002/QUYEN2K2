import tkinter as tk
import numpy as np


def solve_linear_system(a, b, method):
    pass


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Giải hệ phương trình tuyến tính n phương trình n ẩn")

        # Thêm menu để người dùng chọn phương pháp giải
        self.menubar = tk.Menu(self.root)
        self.method_menu = tk.Menu(self.menubar, tearoff=0)
        self.method_menu.add_command(label="Gauss", command=lambda: self.set_method("Gauss"))
        self.method_menu.add_command(label="Gauss-Seidel", command=lambda: self.set_method("Gauss-Seidel"))
        self.method_menu.add_command(label="Jacobi", command=lambda: self.set_method("Jacobi"))
        self.menubar.add_cascade(label="Phương pháp", menu=self.method_menu)

        # Khởi tạo các thành phần giao diện người dùng
        self.label_a = tk.Label(self.root, text="Ma trận hệ số:", font=("Arial", 8), bg="white", fg="black")
        self.entry_a = tk.Text(self.root, width=30, font=("Arial", 8), bg="pink", fg="black")
        self.label_b = tk.Label(self.root, text="Ma trận biên:", font=("Arial", 8), bg="white", fg="black")
        self.entry_b = tk.Text(self.root, width=30, font=("Arial", 8), bg="pink", fg="black")
        self.button_solve = tk.Button(self.root, text="Giải", command=self.solve, font=("Arial", 8), bg="white", fg="black")
        self.label_result = tk.Label(self.root, text="Kết quả:", font=("Arial", 8), bg="white", fg="black")
        self.text_result = tk.Text(self.root, width=60, font=("Arial", 8), bg="white", fg="black")

        # Sắp xếp các thành phần giao diện người dùng
        self.label_a.grid(row=0, column=0)
        self.entry_a.grid(row=0, column=1)
        self.label_b.grid(row=1, column=0)
        self.entry_b.grid(row=1, column=1)
        self.button_solve.grid(row=2, column=0)
        self.label_result.grid(row=3, column=0)
        self.text_result.grid(row=3, column=1)

        # Thiết lập giá trị mặc định cho phương pháp giải
        self.set_method("Gauss")

        # Bắt đầu vòng lặp sự kiện
        self.root.mainloop()

    def set_method(self, method):
        self.method = method

    def solve(self):
        # Lấy dữ liệu hệ phương trình từ các thành phần giao diện người dùng
        a = np.array(self.entry_a.get("1.0", "end-1c").split(",")).astype(float).reshape(-1, -1)
        b = np.array(self.entry_b.get("1.0", "end-1c").split(",")).astype(float)

        # Giải hệ phương trình
        x = solve_linear_system(a, b, self.method)

        # Hiển thị kết quả
        self.text_result.delete("1.0", "end")
        self.text_result.insert("1.0", str(x))


if __name__ == "__main__":
    app = App()
    app.mainloop()
