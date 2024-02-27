from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    expertise = request.form['expertise']
    name = request.form['name']
    internal_external = request.form['interal_external']
    organization = request.form['organization']
    onshore_offshore = request.form['onshore_offshore']
    resource_manager = request.form['resource_manager']
    rate = request.form['rate']
    feb_23 = request.form['feb_23']
    mar_23 = request.form['mar_23']
    apr_23 = request.form['apr_23']
    may_23 = request.form['may_23']
    jun_23 = request.form['jun_23']
    jul_23 = request.form['jul_23']
    aug_23 = request.form['aug_23']
    sept_23 = request.form['sept_23']
    oct_23 = request.form['oct_23']
    nov_23 = request.form['nov_23']
    dec_23 = request.form['dec_23']
    jan_24 = request.form['jan_24']
    feb_24 = request.form['feb_24']
    mar_24 = request.form['mar_24']
    total_hours = request.form['total_hours']
    total_amount = request.form['total_amount']

    # Create a DataFrame with the entered data
    data = {
        'Expertise': [expertise],
        'Name': [name],
        'Int/Ext': [internal_external],
        'Organization': [organization],
        'Onshore/Offshore': [onshore_offshore],
        'Resource Manager': [resource_manager],
        'Rate': [rate],
        'Feb\'23': [feb_23],
        'Mar\'23': [mar_23],
        'Apr\'23': [apr_23],
        'May\'23': [may_23],
        'Jun\'23': [jun_23],
        'Jul\'23': [jul_23],
        'Aug\'23': [aug_23],
        'Sept\'23': [sept_23],
        'Oct\'23': [oct_23],
        'Nov\'23': [nov_23],
        'Dec\'23': [dec_23],
        'Jan\'24': [jan_24],
        'Feb\'24': [feb_24],
        'Mar\'24': [mar_24],
        'Total Hours': [total_hours],
        'Total Amount': [total_amount]
    }

    df = pd.DataFrame(data)

    # Save DataFrame to Excel file
    excel_filename = 'output.xlsx'
    df.to_excel(excel_filename, index=False)

    return send_file(excel_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
