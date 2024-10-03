import tkinter as tk
import cv2
from PIL import Image, ImageTk

class AttendanceSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Facial Recognition Attendance System")
        self.root.geometry("800x600")

        # Title Label
        self.title_label = tk.Label(self.root, text="Facial Recognition Attendance System", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        # Start Webcam Button
        self.start_btn = tk.Button(self.root, text="Start Webcam", width=20, height=2, command=self.start_webcam)
        self.start_btn.pack(pady=20)

        # Video Display Area
        self.video_label = tk.Label(self.root)
        self.video_label.pack(pady=20)

        # Mark Attendance Button
        self.attendance_btn = tk.Button(self.root, text="Mark Attendance", width=20, height=2, command=self.mark_attendance)
        self.attendance_btn.pack(pady=10)

        # Show Attendance Log Button
        self.show_log_btn = tk.Button(self.root, text="Show Attendance Log", width=20, height=2, command=self.show_log)
        self.show_log_btn.pack(pady=10)

        # Exit Button
        self.exit_btn = tk.Button(self.root, text="Exit", width=20, height=2, command=self.root.quit)
        self.exit_btn.pack(pady=30)

        # Initialize the webcam variable
        self.cap = None
        self.webcam_running = False

    def start_webcam(self):
        if not self.webcam_running:
            self.webcam_running = True
            self.cap = cv2.VideoCapture(0)  # Start capturing from webcam
            self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()  # Capture frame-by-frame
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color from BGR to RGB
            img = Image.fromarray(frame)  # Convert frame to PIL image
            imgtk = ImageTk.PhotoImage(image=img)  # Convert PIL image to ImageTk format
            self.video_label.imgtk = imgtk  # Keep reference to avoid garbage collection
            self.video_label.configure(image=imgtk)  # Update the label with the new frame
        if self.webcam_running:
            self.root.after(10, self.update_frame)  # Call update_frame every 10 ms

    def mark_attendance(self):
        print("Marking attendance...")

    def show_log(self):
        print("Showing attendance log...")

    def on_close(self):
        self.webcam_running = False
        if self.cap is not None:
            self.cap.release()  # Release the camera when closing the app
        self.root.quit()

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSystemUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # Handle window close event
    root.mainloop()
