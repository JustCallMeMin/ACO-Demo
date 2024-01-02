
# Hướng Dẫn Sử Dụng Thuật Toán Tối ưu Hóa Đàn Kiến (Ant Colony Optimization - ACO)

## Giới Thiệu
Dự án này bao gồm một triển khai của thuật toán Tối ưu Hóa Đàn Kiến (ACO) trong Python. Thuật toán ACO là một phương pháp tìm kiếm lời giải tối ưu bằng cách mô phỏng hành vi tìm đường của kiến trong tự nhiên. Đặc biệt, dự án này tập trung vào việc tìm đường đi ngắn nhất giữa các điểm.

## Cấu Trúc File
- `AntColony.py`: Chứa lớp `AntColony`, triển khai cơ bản của thuật toán ACO.
- `ACOAnimation.py`: Chứa lớp `ACOAnimation`, dùng để tạo hoạt hình hiển thị quá trình của thuật toán.
- `Example.py`: Một ví dụ minh họa cách sử dụng lớp `AntColony` và `ACOAnimation`.

## Yêu Cầu Thư Viện
Để chạy được code, bạn cần cài đặt các thư viện sau:
- `numpy`: Dùng cho các tính toán ma trận và mảng.
- `matplotlib`: Dùng để tạo đồ thị và hoạt hình.
- `sklearn`: Chỉ cần cho phần Multi-Dimensional Scaling (MDS) trong `Example.py`.

Bạn có thể cài đặt các thư viện này thông qua pip:
```bash
pip install numpy matplotlib scikit-learn
```

## Cách Chạy Code
1. Mở Terminal hoặc Command Prompt.
2. Chuyển đến thư mục chứa các file Python.
3. Chạy script bằng cách sử dụng lệnh:
   ```bash
   python Example.py
   ```
   Điều này sẽ chạy script `Example.py`, mà sử dụng các lớp từ `AntColony.py` và `ACOAnimation.py`.

## Giải Thích về Thuật Toán
Thuật toán ACO trong dự án này mô phỏng hành vi của kiến khi tìm đường đi ngắn nhất giữa các điểm. Kiến sẽ để lại pheromone trên đường đi của chúng, và các kiến khác có xu hướng theo dõi đường đi có nhiều pheromone nhất. Trong quá trình lặp, đường đi ngắn nhất sẽ dần được tìm thấy thông qua sự tương tác này.

`AntColony.py` xử lý phần lớn logic của thuật toán, bao gồm việc tạo ra kiến, phân phối pheromone, và cập nhật đường đi ngắn nhất. `ACOAnimation.py` sau đó sử dụng dữ liệu này để tạo ra hình ảnh hoạt hình, cho phép người dùng nhìn thấy quá trình tìm kiếm đường đi ngắn nhất diễn ra như thế nào.
