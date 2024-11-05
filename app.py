from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Thông tin kết nối cơ sở dữ liệu
connection = psycopg2.connect(
    host="34.30.165.154",          # Địa chỉ host của database (thường là localhost nếu chạy cục bộ)
    user="postgres",      # Tên người dùng PostgreSQL
    password="test-room",  # Mật khẩu PostgreSQL
    database="test-room",  # Tên cơ sở dữ liệu
    port="5432"                # Cổng PostgreSQL, mặc định là 5432
)

@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, age, department, hire_date FROM employees")
        rows = cursor.fetchall()
        
        # Chuyển dữ liệu thành danh sách các từ điển
        employees = []
        for row in rows:
            employee = {
                "id": row[0],
                "name": row[1],
                "age": row[2],
                "department": row[3],
                "hire_date": row[4].strftime('%Y-%m-%d')  # Định dạng ngày tháng
            }
            employees.append(employee)

        return jsonify(employees), 200  # Trả về dữ liệu dạng JSON
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Unable to fetch data"}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
