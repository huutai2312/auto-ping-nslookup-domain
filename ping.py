import subprocess
import time
import os

def main():
    domain = input("Nhập domain (https://domain | http://domain | domain): ").strip()
    
    # Xử lý để lấy domain (loại bỏ 'http://', 'https://', ...)
    if domain.startswith("https://"):
        domain = domain[8:]
    elif domain.startswith("http://"):
        domain = domain[7:]
    
    print("\nChọn lệnh:")
    print("1. Ping")
    print("2. Nslookup")
    option = input("Nhập lựa chọn của bạn (1 hoặc 2): ").strip()
    
    try:
        interval = float(input("Nhập khoảng thời gian giữa mỗi lần thực hiện lệnh (giây): ").strip())
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")
        return
    
    def run_command(command):
        try:
            # Thực hiện lệnh và lấy output
            result = subprocess.run(command, capture_output=True, text=True)
            return result.stdout.strip()  # Trả về kết quả
        except Exception as e:
            return f"Lỗi khi thực hiện lệnh: {e}"
    
    results = []
    count = 0

    if option == "1":
        print(f"\nPing tới {domain} mỗi {interval} giây...")
        while True:
            count += 1
            # Thực hiện lệnh ping (trên Windows: ping -n 1, trên Linux/Mac: ping -c 1)
            command = ["ping", "-n" if subprocess.os.name == "nt" else "-c", "1", domain]
            output = run_command(command)
            results.append([count, output])
            
            os.system('cls' if subprocess.os.name == 'nt' else 'clear')
        
            print(tabulate(results, headers=["Lần thực hiện", "Kết quả"], tablefmt="fancy_grid"))
            time.sleep(interval)  # Chờ khoảng thời gian đã nhập trước khi thực hiện lại

    elif option == "2":
        print(f"\nNslookup tới {domain} mỗi {interval} giây...")
        while True:
            count += 1
            command = ["nslookup", domain]
            output = run_command(command)
            results.append([count, output])
            
            os.system('cls' if subprocess.os.name == 'nt' else 'clear')
            
            print(tabulate(results, headers=["Lần thực hiện", "Kết quả"], tablefmt="fancy_grid"))
            time.sleep(interval)  # Chờ khoảng thời gian đã nhập trước khi thực hiện lại
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    # Kiểm tra xem thư viện tabulate đã được cài đặt hay chưa
    try:
        from tabulate import tabulate
    except ImportError:
        print("Thư viện 'tabulate' chưa được cài đặt. Hãy cài đặt bằng lệnh: pip install tabulate")
        exit()

    main()
