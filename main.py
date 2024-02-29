from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def high():
    return render_template('high.html')

@app.route('/efforts.html')
def render_efforts():
    project_name = request.args.get('projectName')
    # Your code to handle the project_name parameter
    return render_template('efforts.html', project_name=project_name)
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    rows_data = []
    row_count = int(request.form.get('row_count', 0))

    for i in range(row_count):
        expertise = request.form.get(f'expertise_{i}')
        name = request.form.get(f'name_{i}')
        internal_external = request.form.get(f'internal_external_{i}')
        organization = request.form.get(f'organization_{i}')
        onshore_offshore = request.form.get(f'onshore_offshore_{i}')
        resource_manager = request.form.get(f'resource_manager_{i}')
        rate = request.form.get(f'rate_{i}')
        start_date = request.form.get(f'start_date_{i}')
        end_date = request.form.get(f'end_date_{i}')
        total_hours = request.form.get(f'total_hours_{i}')
        total_amount = request.form.get(f'total_amount_{i}')

        # Extract month-wise data
        month_inputs = {}
        for key, value in request.form.items():
            if f'{i}_' in key and "'" in key:
                month_inputs[key.replace(f'{i}_', '')] = value

        # Create a dictionary for the row data
        row_data = {
            'Expertise': expertise,
            'Name': name,
            'Int/Ext': internal_external,
            'Organization': organization,
            'Onshore/Offshore': onshore_offshore,
            'Resource Manager': resource_manager,
            'Rate': rate,
            'Start Date': start_date,
            'End Date': end_date,
            **month_inputs,
            'Total Hours': total_hours,
            'Total Amount': total_amount
        }

        rows_data.append(row_data)

    # Create a DataFrame with the entered data for all rows
    df = pd.DataFrame(rows_data)

    # Save DataFrame to Excel file with a dynamic filename
    project_name = request.form.get('project_name')
    excel_filename = f'{project_name}_output.xlsx'
    df.to_excel(excel_filename, index=False)

    return send_file(excel_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)