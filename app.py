import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

logging.info("Starting application")

try:
    from flask import Flask, render_template, request
    logging.info("Flask imported successfully")
    from njattuvela_calendar import generate_njattuvela_calendar, format_malayalam_period_string
    logging.info("njattuvela_calendar imported successfully")
except Exception as e:
    logging.error(f"Error during import: {e}")


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Index function called")
    calendar_data = None
    year = None
    if request.method == 'POST':
        try:
            year = int(request.form['year'])
            logging.info(f"Year received: {year}")
            raw_calendar_data = generate_njattuvela_calendar(year)
            logging.info("Calendar data generated")
            # Format the malayalam period string for each entry
            calendar_data = []
            for period in raw_calendar_data:
                period['malayalam_period_str'] = format_malayalam_period_string(
                    period['malayalam_start_info'], period['malayalam_end_info']
                )
                calendar_data.append(period)
            logging.info("Calendar data formatted")
        except Exception as e:
            logging.error(f"Error processing request: {e}")

    return render_template('index.html', calendar_data=calendar_data, year=year)

if __name__ == '__main__':
    logging.info("Starting Flask server")
    app.run(debug=True)
